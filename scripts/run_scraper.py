#!/usr/bin/env python3
"""
run_scraper.py — CLI wrapper for the corpus-legal-ia scraper.

Usage:
    # Download PDFs from government pages
    python3 scripts/run_scraper.py download \\
        --country JPN \\
        --urls "https://www8.cao.go.jp/cstp/ai/" \\
        --output-dir data/raw/legal_corpus/JPN

    # Download a single PDF directly
    python3 scripts/run_scraper.py download \\
        --country JPN \\
        --urls "https://www8.cao.go.jp/cstp/ai/ai_hou_gaiyou_en.pdf" \\
        --output-dir data/raw/legal_corpus/JPN \\
        --direct-pdf

    # Extract law text from a page
    python3 scripts/run_scraper.py extract \\
        --url "https://laws.e-gov.go.jp/law/507AC0000000053" \\
        --output data/raw/legal_corpus/JPN/JPN_AI_Act_text.json

    # Extract with Cloudflare bypass
    python3 scripts/run_scraper.py download \\
        --country FIN \\
        --urls "https://www.finlex.fi/fi/laki/alkup/2025/20251377" \\
        --output-dir data/raw/legal_corpus/FIN \\
        --bypass-cloudflare

    # Check state (what's already downloaded)
    python3 scripts/run_scraper.py state \\
        --country-dir data/raw/legal_corpus/JPN
"""

import argparse
import json
import logging
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scraper.downloader import download_pdfs
from scraper.law_extractor import extract_law_text
from scraper.state_manager import StateManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("run_scraper")


def cmd_download(args):
    """Download PDFs from government pages."""
    urls = args.urls
    output_dir = args.output_dir
    bypass_cloudflare = args.bypass_cloudflare
    headless = not args.visible
    direct_pdf = args.direct_pdf

    logger.info("="*60)
    logger.info("CORPUS-LEGAL-IA SCRAPER — DOWNLOAD MODE")
    logger.info("="*60)
    logger.info("Country: %s", args.country)
    logger.info("URLs: %s", urls)
    logger.info("Output: %s", output_dir)
    logger.info("Bypass Cloudflare: %s", bypass_cloudflare)
    logger.info("Headless: %s", headless)
    logger.info("Direct PDF: %s", direct_pdf)

    if direct_pdf:
        # Direct PDF download mode — treat URLs as direct PDF links
        from scraper.browser import create_driver, kill_driver
        import time

        driver = create_driver(
            headless=headless,
            bypass_cloudflare=bypass_cloudflare,
            download_dir=output_dir,
        )

        results = []
        for url in urls:
            from urllib.parse import urlparse
            filename = Path(urlparse(url).path).name
            if not filename.endswith(".pdf"):
                filename += ".pdf"

            try:
                logger.info("Navigating to: %s", url)
                driver.get(url)
                time.sleep(5)

                # Check if file downloaded
                filepath = Path(output_dir) / filename
                if filepath.exists():
                    sha256 = StateManager._compute_sha256(filepath)
                    results.append({
                        "filename": filename,
                        "url": url,
                        "status": "downloaded",
                        "size_bytes": filepath.stat().st_size,
                        "sha256": sha256,
                        "error": "",
                    })
                    logger.info("Downloaded: %s (%d bytes)", filename, filepath.stat().st_size)
                else:
                    results.append({
                        "filename": filename,
                        "url": url,
                        "status": "not_found",
                        "size_bytes": 0,
                        "sha256": "",
                        "error": "File not found after download",
                    })
            except Exception as e:
                results.append({
                    "filename": filename,
                    "url": url,
                    "status": "error",
                    "size_bytes": 0,
                    "sha256": "",
                    "error": str(e),
                })

        kill_driver(driver)
    else:
        # Page scraping mode — find PDFs on pages
        results = download_pdfs(
            urls=urls,
            output_dir=output_dir,
            manifest_csv=args.manifest,
            bypass_cloudflare=bypass_cloudflare,
            headless=headless,
            wait_after_load=args.wait,
            max_retries=args.retries,
        )

    # Print summary
    logger.info("="*60)
    logger.info("DOWNLOAD SUMMARY")
    logger.info("="*60)
    for r in results:
        status = r.get("status", "unknown")
        filename = r.get("filename", "")
        size = r.get("size_bytes", 0)
        error = r.get("error", "")
        if status == "downloaded":
            logger.info("  OK  %s (%d bytes, SHA-256: %s...)", filename, size, r.get("sha256", "")[:12])
        elif status == "skipped_existing":
            logger.info("  SKIP %s (already downloaded)", filename)
        else:
            logger.info("  FAIL %s — %s", filename or r.get("url", ""), error or status)

    logger.info("Total: %d files processed", len(results))

    return results


def cmd_extract(args):
    """Extract law text from a government page."""
    url = args.url
    output_file = args.output
    site_type = args.site_type
    bypass_cloudflare = args.bypass_cloudflare
    headless = not args.visible

    logger.info("="*60)
    logger.info("CORPUS-LEGAL-IA SCRAPER — EXTRACT MODE")
    logger.info("="*60)
    logger.info("URL: %s", url)
    logger.info("Site type: %s", site_type or "auto-detect")
    logger.info("Output: %s", output_file or "stdout")

    result = extract_law_text(
        url=url,
        site_type=site_type,
        headless=headless,
        bypass_cloudflare=bypass_cloudflare,
        wait_after_load=args.wait,
        output_file=output_file,
    )

    if not output_file:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    status = result.get("extraction_status", "unknown")
    title = result.get("title", "")[:60]
    n_articles = len(result.get("articles", []))
    n_chars = len(result.get("raw_text", ""))

    logger.info("Extraction status: %s", status)
    logger.info("Title: %s", title)
    logger.info("Articles: %d", n_articles)
    logger.info("Characters: %d", n_chars)

    return result


def cmd_state(args):
    """Show download state for a country."""
    country_dir = args.country_dir

    sm = StateManager(country_dir)
    summary = sm.summary()

    logger.info("="*60)
    logger.info("DOWNLOAD STATE — %s", country_dir)
    logger.info("="*60)
    logger.info("Manifest exists: %s", summary["manifest_exists"])
    logger.info("Total entries: %d", summary["total_entries"])

    if summary["filenames"]:
        logger.info("Downloaded files:")
        for fn in summary["filenames"]:
            logger.info("  - %s", fn)

    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Corpus Legal-IA Scraper — Download PDFs and extract law text from government websites"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Download command
    dl_parser = subparsers.add_parser("download", help="Download PDFs from government pages")
    dl_parser.add_argument("--country", required=True, help="ISO3 country code (e.g., JPN, FIN)")
    dl_parser.add_argument("--urls", nargs="+", required=True, help="URLs to scrape for PDFs")
    dl_parser.add_argument("--output-dir", required=True, help="Output directory for downloaded files")
    dl_parser.add_argument("--manifest", default=None, help="Path to manifest.csv for incremental checks")
    dl_parser.add_argument("--bypass-cloudflare", action="store_true", help="Use undetected-chromedriver")
    dl_parser.add_argument("--visible", action="store_true", help="Run browser in visible mode (not headless)")
    dl_parser.add_argument("--direct-pdf", action="store_true", help="Treat URLs as direct PDF links")
    dl_parser.add_argument("--wait", type=int, default=5, help="Seconds to wait after page load")
    dl_parser.add_argument("--retries", type=int, default=3, help="Number of retry attempts")

    # Extract command
    ex_parser = subparsers.add_parser("extract", help="Extract law text from a government page")
    ex_parser.add_argument("--url", required=True, help="URL of the law page")
    ex_parser.add_argument("--output", default=None, help="Output file path (JSON)")
    ex_parser.add_argument("--site-type", default=None, help="Site type for custom extraction (e-gov.go.jp, finlex.fi)")
    ex_parser.add_argument("--bypass-cloudflare", action="store_true", help="Use undetected-chromedriver")
    ex_parser.add_argument("--visible", action="store_true", help="Run browser in visible mode")
    ex_parser.add_argument("--wait", type=int, default=10, help="Seconds to wait for JS rendering")

    # State command
    st_parser = subparsers.add_parser("state", help="Show download state for a country")
    st_parser.add_argument("--country-dir", required=True, help="Path to country corpus directory")

    args = parser.parse_args()

    if args.command == "download":
        cmd_download(args)
    elif args.command == "extract":
        cmd_extract(args)
    elif args.command == "state":
        cmd_state(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()