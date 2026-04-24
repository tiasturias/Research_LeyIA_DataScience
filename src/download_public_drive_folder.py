from __future__ import annotations

import argparse
import csv
import html
import re
import sys
import time
from contextlib import closing
from pathlib import Path
from typing import Iterator
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ENTRY_PATTERN = re.compile(
    r'<div class="flip-entry" id="entry-(?P<id>[^"]+)".*?'
    r'<a href="(?P<href>[^"]+)" target="_blank">.*?'
    r'<div class="flip-entry-title">(?P<title>.*?)</div>',
    re.DOTALL,
)


def sanitize_component(name: str) -> str:
    sanitized = name.strip().replace("/", "-")
    sanitized = sanitized.replace(":", " -")
    sanitized = sanitized.replace("\n", " ")
    return sanitized or "untitled"


def fetch_folder_html(folder_id: str, retries: int = 3) -> str:
    url = f"https://drive.google.com/embeddedfolderview?id={folder_id}#list"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    for attempt in range(1, retries + 1):
        try:
            request = Request(url, headers=headers)
            with urlopen(request) as response:
                return response.read().decode("utf-8")
        except (HTTPError, URLError) as error:
            if attempt == retries:
                raise RuntimeError(f"Unable to fetch folder {folder_id}: {error}") from error
            time.sleep(1.5 * attempt)

    raise RuntimeError(f"Unable to fetch folder {folder_id}")


def build_request(url: str) -> Request:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }
    return Request(url, headers=headers)


def parse_entries(folder_html: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []

    for match in ENTRY_PATTERN.finditer(folder_html):
        href = html.unescape(match.group("href"))
        title = html.unescape(match.group("title")).strip()
        entry_id = match.group("id")
        kind = "folder" if "/drive/folders/" in href else "file"
        entries.append({"id": entry_id, "href": href, "title": title, "kind": kind})

    return entries


def walk_public_drive(folder_id: str, relative_path: Path = Path()) -> Iterator[dict[str, str]]:
    folder_html = fetch_folder_html(folder_id)

    for entry in parse_entries(folder_html):
        entry_path = relative_path / sanitize_component(entry["title"])
        if entry["kind"] == "folder":
            yield {
                "type": "folder",
                "id": entry["id"],
                "title": entry["title"],
                "path": str(entry_path),
                "href": entry["href"],
            }
            yield from walk_public_drive(entry["id"], entry_path)
        else:
            yield {
                "type": "file",
                "id": entry["id"],
                "title": entry["title"],
                "path": str(entry_path),
                "href": entry["href"],
            }


def download_file(file_id: str, output_path: Path, retries: int = 3) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"Skipping existing file: {output_path}")
        return

    file_url = f"https://drive.google.com/uc?id={file_id}"
    temp_path = output_path.with_suffix(output_path.suffix + ".part")

    for attempt in range(1, retries + 1):
        try:
            print(f"Downloading {output_path}")
            with closing(urlopen(build_request(file_url))) as response, temp_path.open("wb") as target:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    target.write(chunk)
            temp_path.replace(output_path)
            return
        except (HTTPError, URLError) as error:
            if temp_path.exists():
                temp_path.unlink()
            if attempt == retries:
                raise RuntimeError(f"Failed to download file {file_id}: {error}") from error
            time.sleep(1.5 * attempt)


def write_manifest(destination: Path, records: list[dict[str, str]]) -> None:
    manifest_path = destination / "download_manifest.csv"
    with manifest_path.open("w", newline="", encoding="utf-8") as manifest_file:
        writer = csv.DictWriter(manifest_file, fieldnames=["type", "path", "title", "id", "href"])
        writer.writeheader()
        writer.writerows(records)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download a public Google Drive folder recursively.")
    parser.add_argument("folder_id", help="Public Google Drive folder ID")
    parser.add_argument("destination", help="Destination directory")
    args = parser.parse_args()

    destination = Path(args.destination).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    records = list(walk_public_drive(args.folder_id))
    folders = [record for record in records if record["type"] == "folder"]
    files = [record for record in records if record["type"] == "file"]

    for folder in folders:
        (destination / folder["path"]).mkdir(parents=True, exist_ok=True)

    for file_record in files:
        download_file(file_record["id"], destination / file_record["path"])

    write_manifest(destination, records)
    print(
        f"Completed download: {len(files)} files across {len(folders)} folders into {destination}",
        file=sys.stdout,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())