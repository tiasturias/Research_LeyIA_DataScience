"""
state_manager.py — Incremental download verification against manifest.csv.

Inspired by twitter_incremental.py's get_existing_tweet_ids() and
get_last_tweet_date(). Prevents re-downloading files that already exist
in the corpus with matching SHA-256 hashes.
"""

import csv
import hashlib
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


class StateManager:
    """
    Manages download state by checking manifest.csv for existing files.

    Prevents redundant downloads by verifying:
    1. File already exists on disk
    2. SHA-256 hash matches manifest entry
    3. File is a valid PDF (not an HTML error page)

    Usage:
        sm = StateManager("data/raw/legal_corpus/JPN")
        if sm.should_download("JPN_AI_Act_2025.pdf", "https://example.com/law.pdf"):
            # proceed with download
            sm.record_download("JPN_AI_Act_2025.pdf", metadata)
    """

    MANIFEST_FIELDS = [
        "iso3", "filename", "document_title", "doc_type", "issuer",
        "publication_date", "status", "language", "source_url_primary",
        "source_url_mirror", "source_domain", "retrieved_date",
        "retrieval_http_status", "retrieval_method", "sha256",
        "size_bytes", "pages", "notes",
    ]

    def __init__(self, country_dir):
        """
        Args:
            country_dir: Path to the country corpus directory
                (e.g., 'data/raw/legal_corpus/JPN')
        """
        self.country_dir = Path(country_dir)
        self.manifest_path = self.country_dir / "manifest.csv"
        self._existing_entries = {}
        self._loaded = False

    def _load_manifest(self):
        """Load existing manifest.csv entries into memory."""
        self._existing_entries = {}

        if not self.manifest_path.exists():
            self._loaded = True
            return

        try:
            with open(self.manifest_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    filename = row.get("filename", "").strip()
                    if filename:
                        source_url = row.get("source_url_primary", "").strip()
                        sha256 = row.get("sha256", "").strip()
                        self._existing_entries[filename] = {
                            "source_url": source_url,
                            "sha256": sha256,
                            "row": row,
                        }
        except Exception as e:
            logger.warning("[state] Error loading manifest: %s", e)

        self._loaded = True

    def should_download(self, filename, url=None):
        """
        Check whether a file should be downloaded.

        Returns True if:
        - File does not exist on disk, OR
        - File exists but is invalid (HTML instead of PDF), OR
        - File exists but has no matching manifest entry

        Returns False (skip) if:
        - File exists on disk AND
        - SHA-256 matches manifest entry AND
        - File is a valid PDF
        """
        if not self._loaded:
            self._load_manifest()

        filepath = self.country_dir / filename

        # Check if file exists on disk
        if not filepath.exists():
            logger.info("[state] File not on disk, will download: %s", filename)
            return True

        # Check if file is valid (not an HTML error page)
        if not self._is_valid_file(filepath):
            logger.warning("[state] File exists but invalid (likely HTML error), re-downloading: %s",
                          filename)
            return True

        # Check manifest entry
        entry = self._existing_entries.get(filename)
        if entry is None:
            logger.info("[state] File on disk but not in manifest, will keep: %s", filename)
            return False

        # Verify SHA-256 matches
        current_hash = self._compute_sha256(filepath)
        manifest_hash = entry.get("sha256", "")

        if manifest_hash and current_hash == manifest_hash:
            logger.info("[state] File already downloaded with matching hash, skipping: %s", filename)
            return False

        if manifest_hash and current_hash != manifest_hash:
            logger.warning("[state] File exists but hash mismatch, re-downloading: %s", filename)
            return True

        # No hash in manifest but file exists and is valid
        logger.info("[state] File exists and valid, skipping: %s", filename)
        return False

    def should_download_url(self, url):
        """
        Check if a URL has already been downloaded (by matching source_url_primary
        in manifest).

        Args:
            url: The source URL to check

        Returns:
            True if URL not found in manifest (should download)
            False if URL already in manifest (skip)
        """
        if not self._loaded:
            self._load_manifest()

        for filename, entry in self._existing_entries.items():
            if entry.get("source_url", "") == url:
                filepath = self.country_dir / filename
                if filepath.exists() and self._is_valid_file(filepath):
                    logger.info("[state] URL already downloaded as %s, skipping", filename)
                    return False

        logger.info("[state] URL not in manifest, will download: %s", url)
        return True

    def record_download(self, filename, metadata):
        """
        Append a download record to manifest.csv.

        Args:
            filename: Name of the downloaded file
            metadata: Dict with manifest fields
        """
        if not self._loaded:
            self._load_manifest()

        filepath = self.country_dir / filename

        # Compute file properties
        sha256 = self._compute_sha256(filepath) if filepath.exists() else ""
        size_bytes = filepath.stat().st_size if filepath.exists() else 0

        # Build row
        row = {
            "iso3": metadata.get("iso3", ""),
            "filename": filename,
            "document_title": metadata.get("document_title", ""),
            "doc_type": metadata.get("doc_type", ""),
            "issuer": metadata.get("issuer", ""),
            "publication_date": metadata.get("publication_date", ""),
            "status": metadata.get("status", ""),
            "language": metadata.get("language", ""),
            "source_url_primary": metadata.get("source_url_primary", ""),
            "source_url_mirror": metadata.get("source_url_mirror", ""),
            "source_domain": metadata.get("source_domain", ""),
            "retrieved_date": metadata.get("retrieved_date", ""),
            "retrieval_http_status": metadata.get("retrieval_http_status", ""),
            "retrieval_method": metadata.get("retrieval_method", "selenium"),
            "sha256": sha256,
            "size_bytes": str(size_bytes),
            "pages": metadata.get("pages", ""),
            "notes": metadata.get("notes", ""),
        }

        # Update in-memory cache
        self._existing_entries[filename] = {
            "source_url": row["source_url_primary"],
            "sha256": sha256,
            "row": row,
        }

        # Write to manifest.csv
        write_header = not self.manifest_path.exists()
        with open(self.manifest_path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.MANIFEST_FIELDS)
            if write_header:
                writer.writeheader()
            writer.writerow(row)

        logger.info("[state] Recorded download: %s (SHA-256: %s...)", filename, sha256[:12])

    @staticmethod
    def _compute_sha256(filepath):
        """Compute SHA-256 hash of a file."""
        sha256 = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception:
            return ""

    @staticmethod
    def _is_valid_file(filepath):
        """
        Check if a file is a valid PDF (not an HTML error page).

        Uses magic bytes: PDF files start with %PDF.
        """
        try:
            with open(filepath, "rb") as f:
                header = f.read(8)
                if header.startswith(b"%PDF"):
                    return True
                # Check if it's a text file (for .txt extractions)
                if filepath.suffix == ".txt":
                    return True
                # HTML error pages
                if header.strip().startswith(b"<!DOCTYPE") or header.strip().startswith(b"<html"):
                    return False
                if b"<html" in header.lower() or b"<!doctype" in header.lower():
                    return False
            return True
        except Exception:
            return False

    def get_downloaded_urls(self):
        """Return set of URLs already in the manifest."""
        if not self._loaded:
            self._load_manifest()
        return {e["source_url"] for e in self._existing_entries.values() if e.get("source_url")}

    def get_downloaded_filenames(self):
        """Return set of filenames already in the manifest."""
        if not self._loaded:
            self._load_manifest()
        return set(self._existing_entries.keys())

    def summary(self):
        """Return a summary of current state."""
        if not self._loaded:
            self._load_manifest()
        return {
            "total_entries": len(self._existing_entries),
            "manifest_exists": self.manifest_path.exists(),
            "country_dir": str(self.country_dir),
            "filenames": list(self._existing_entries.keys()),
        }