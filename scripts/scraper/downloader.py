"""
downloader.py — PDF download from government websites using Selenium.

Navigates to pages that require JavaScript rendering, finds PDF links,
and downloads them directly through the browser to bypass anti-bot
protections.
"""

import logging
import os
import shutil
import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .browser import create_driver, kill_driver
from .cloudflare_bypass import get_page_with_retry, is_cloudflare_challenge, is_waf_blocked
from .state_manager import StateManager

logger = logging.getLogger(__name__)

PDF_LINK_SELECTORS = [
    "a[href$='.pdf']",
    "a[href*='.pdf']",
    "a[href*='pdf']",
]

GOV_DOMAINS = {
    ".go.jp": "Japan government",
    ".go.kr": "Korea government",
    ".gov": "US government",
    ".gouv.fr": "France government",
    ".gob": "Spain/LATAM government",
    ".gov.uk": "UK government",
    ".gc.ca": "Canada government",
    ".gov.au": "Australia government",
    ".gov.nz": "New Zealand government",
    ".gov.sg": "Singapore government",
    ".fi": "Finland (finlex.fi)",
}


def download_pdfs(
    urls,
    output_dir,
    manifest_csv=None,
    bypass_cloudflare=False,
    headless=True,
    timeout=30,
    wait_after_load=5,
    max_retries=3,
    pdf_selectors=None,
):
    """
    Download PDFs from government websites using Selenium.

    Args:
        urls: List of URLs to visit (pages containing PDF links)
        output_dir: Directory to save downloaded PDFs
        manifest_csv: Path to manifest.csv for incremental checks (None to skip)
        bypass_cloudflare: Use undetected-chromedriver for WAF bypass
        headless: Run browser in headless mode
        timeout: Page load timeout in seconds
        wait_after_load: Seconds to wait after page load for JS rendering
        max_retries: Number of retry attempts per URL
        pdf_selectors: Custom CSS selectors for PDF links

    Returns:
        List of dicts with download results:
        [{filename, url, source_page, status, size_bytes, sha256, error}]
    """
    results = []
    driver = None

    os.makedirs(output_dir, exist_ok=True)

    # Initialize state manager if manifest provided
    state_mgr = None
    if manifest_csv:
        state_mgr = StateManager(Path(output_dir))
    else:
        state_mgr = StateManager(output_dir)

    try:
        driver = create_driver(
            headless=headless,
            bypass_cloudflare=bypass_cloudflare,
            download_dir=output_dir,
            timeout=timeout,
        )

        for url in urls:
            result = _process_url(
                driver=driver,
                url=url,
                output_dir=output_dir,
                state_mgr=state_mgr,
                wait_after_load=wait_after_load,
                max_retries=max_retries,
                pdf_selectors=pdf_selectors or PDF_LINK_SELECTORS,
            )
            results.extend(result)

    except Exception as e:
        logger.error("[downloader] Fatal error: %s", e)
    finally:
        kill_driver(driver)

    return results


def _process_url(
    driver, url, output_dir, state_mgr, wait_after_load, max_retries, pdf_selectors
):
    """Process a single URL: navigate, find PDFs, download them."""
    results = []

    logger.info("[downloader] Processing: %s", url)

    # Navigate with retry and Cloudflare bypass
    success = get_page_with_retry(driver, url, max_retries=max_retries, bypass=True)

    if not success:
        results.append({
            "filename": "",
            "url": url,
            "source_page": url,
            "status": "blocked",
            "size_bytes": 0,
            "sha256": "",
            "error": "Could not load page (WAF/Cloudflare blocked)",
        })
        return results

    # Wait for JS to render
    time.sleep(wait_after_load)

    # Find PDF links on the page
    pdf_links = _find_pdf_links(driver, pdf_selectors)

    if not pdf_links:
        logger.info("[downloader] No PDF links found on page: %s", url)
        results.append({
            "filename": "",
            "url": url,
            "source_page": url,
            "status": "no_pdfs_found",
            "size_bytes": 0,
            "sha256": "",
            "error": "",
        })
        return results

    # Download each PDF
    for pdf_url, pdf_text in pdf_links:
        # Generate filename from URL
        filename = _url_to_filename(pdf_url, pdf_text)

        # Check if already downloaded
        if state_mgr and not state_mgr.should_download(filename, pdf_url):
            results.append({
                "filename": filename,
                "url": pdf_url,
                "source_page": url,
                "status": "skipped_existing",
                "size_bytes": 0,
                "sha256": "",
                "error": "",
            })
            continue

        # Download the PDF
        result = _download_single_pdf(driver, pdf_url, filename, output_dir)
        results.append(result)

    return results


def _find_pdf_links(driver, selectors):
    """Find PDF links on the current page using CSS selectors."""
    pdf_links = []
    seen_urls = set()

    for selector in selectors:
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            for elem in elements:
                href = elem.get_attribute("href")
                if href and href not in seen_urls:
                    text = elem.text.strip()
                    pdf_links.append((href, text))
                    seen_urls.add(href)
        except Exception:
            continue

    logger.info("[downloader] Found %d PDF links on page", len(pdf_links))
    return pdf_links


def _download_single_pdf(driver, pdf_url, filename, output_dir):
    """Download a single PDF file through the browser."""
    filepath = Path(output_dir) / filename

    try:
        # Try direct browser download
        logger.info("[downloader] Downloading: %s -> %s", pdf_url, filename)

        # Navigate to the PDF URL
        driver.get(pdf_url)

        # Wait for download
        time.sleep(5)

        # Check if file was downloaded to the default download directory
        # (Chrome auto-downloads because of prefs)
        # Look for .crdownload (partial) files first
        download_dir = Path(output_dir)

        # Wait for download to complete
        _wait_for_download(download_dir, filename, timeout=30)

        if filepath.exists():
            size_bytes = filepath.stat().st_size

            # Validate it's a real PDF
            with open(filepath, "rb") as f:
                header = f.read(8)

            if header.startswith(b"%PDF"):
                sha256 = StateManager._compute_sha256(filepath)
                logger.info("[downloader] Downloaded: %s (%d bytes, SHA-256: %s...)",
                            filename, size_bytes, sha256[:12])
                return {
                    "filename": filename,
                    "url": pdf_url,
                    "source_page": driver.current_url,
                    "status": "downloaded",
                    "size_bytes": size_bytes,
                    "sha256": sha256,
                    "error": "",
                }
            else:
                logger.warning("[downloader] Downloaded file is not a PDF: %s", filename)
                # Try to move invalid file
                invalid_path = filepath.with_suffix(".invalid")
                shutil.move(str(filepath), str(invalid_path))
                return {
                    "filename": filename,
                    "url": pdf_url,
                    "source_page": "",
                    "status": "invalid_pdf",
                    "size_bytes": size_bytes,
                    "sha256": "",
                    "error": "Downloaded file is not a valid PDF",
                }

        logger.warning("[downloader] File not found after download: %s", filename)
        return {
            "filename": filename,
            "url": pdf_url,
            "source_page": "",
            "status": "download_failed",
            "size_bytes": 0,
            "sha256": "",
            "error": "File not found after download",
        }

    except Exception as e:
        logger.error("[downloader] Error downloading %s: %s", pdf_url, e)
        return {
            "filename": filename,
            "url": pdf_url,
            "source_page": "",
            "status": "error",
            "size_bytes": 0,
            "sha256": "",
            "error": str(e),
        }


def _wait_for_download(download_dir, filename, timeout=30):
    """Wait for a Chrome download to complete."""
    start_time = time.time()
    filepath = download_dir / filename
    crdownload = download_dir / (filename + ".crdownload")

    while time.time() - start_time < timeout:
        if filepath.exists() and not crdownload.exists():
            # File exists and no partial download file
            time.sleep(1)  # Small buffer for file system
            return True
        time.sleep(1)

    return False


def _url_to_filename(url, link_text=""):
    """Generate a clean filename from a PDF URL."""
    from urllib.parse import urlparse, unquote

    parsed = urlparse(url)
    path = unquote(parsed.path)

    # Get the last part of the path
    basename = Path(path).name

    # If it ends with .pdf, use it
    if basename.lower().endswith(".pdf"):
        # Clean up the filename
        basename = basename.replace(" ", "_")
        basename = "".join(c for c in basename if c.isalnum() or c in "._-")
        return basename

    # If no .pdf extension, try to construct from link text
    if link_text:
        clean = "".join(c if c.isalnum() else "_" for c in link_text)
        clean = clean[:80]  # Limit length
        return f"{clean}.pdf"

    # Fallback: use URL hash
    import hashlib
    url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
    return f"document_{url_hash}.pdf"