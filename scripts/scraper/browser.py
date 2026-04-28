"""
browser.py — Selenium Chrome driver setup with anti-detection options.

Provides headless Chrome configuration for navigating government websites
that block automated curl requests. Inspired by scrape_ley_selenium.py
but enhanced with anti-bot evasion tactics.
"""

import logging
import os
import random
import sys

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger(__name__)

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
]

CHROME_WINDOW_SIZES = [
    (1920, 1080),
    (1440, 900),
    (1536, 864),
    (1280, 720),
]


def _use_undetected():
    """Check if undetected-chromedriver is available."""
    try:
        import undetected_chromedriver
        return True
    except ImportError:
        return False


def create_driver(
    headless=True,
    bypass_cloudflare=False,
    window_size=None,
    user_agent=None,
    download_dir=None,
    timeout=30,
    implicit_wait=10,
):
    """
    Create a Selenium Chrome WebDriver with anti-detection options.

    If bypass_cloudflare=True and undetected-chromedriver is installed,
    uses uc.Chrome instead of regular Chrome to bypass Cloudflare and
    similar WAF protections.

    Args:
        headless: Run in headless mode (default True)
        bypass_cloudflare: Use undetected-chromedriver for WAF bypass
        window_size: Tuple (width, height) or None for random
        user_agent: UA string or None for random selection
        download_dir: Directory for PDF downloads (enables PDF download in browser)
        timeout: Page load timeout in seconds
        implicit_wait: Implicit wait timeout in seconds

    Returns:
        selenium.webdriver.Chrome instance
    """
    if bypass_cloudflare and _use_undetected():
        return _create_undetected_driver(
            headless=headless,
            window_size=window_size,
            user_agent=user_agent,
            download_dir=download_dir,
            timeout=timeout,
            implicit_wait=implicit_wait,
        )

    return _create_standard_driver(
        headless=headless,
        window_size=window_size,
        user_agent=user_agent,
        download_dir=download_dir,
        timeout=timeout,
        implicit_wait=implicit_wait,
    )


def _create_standard_driver(
    headless, window_size, user_agent, download_dir, timeout, implicit_wait
):
    """Create a standard Chrome webdriver with anti-detection options."""
    from selenium import webdriver

    options = ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")

    # Anti-detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Window size
    if window_size is None:
        window_size = random.choice(CHROME_WINDOW_SIZES)
    options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

    # User agent
    if user_agent is None:
        user_agent = random.choice(USER_AGENTS)
    options.add_argument(f"--user-agent={user_agent}")

    # Language
    options.add_argument("--lang=en-US,en;q=0.9")
    options.add_argument("--accept-lang=en-US,en;q=0.9")

    # Download directory configuration for PDF auto-download
    if download_dir:
        os.makedirs(download_dir, exist_ok=True)
        prefs = {
            "download.default_directory": os.path.abspath(download_dir),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "pdfjs.disabled": True,
        }
        options.add_experimental_option("prefs", prefs)

    # Logging preferences
    options.set_capability("goog:loggingPrefs", {"browser": "SEVERE"})

    # Use webdriver_manager to auto-install chromedriver
    try:
        from webdriver_manager.chrome import ChromeDriverManager

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except ImportError:
        logger.warning("webdriver_manager not installed, using system chromedriver")
        driver = webdriver.Chrome(options=options)

    # Anti-detection JavaScript
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": _stealth_js()},
    )

    # Timeouts
    driver.set_page_load_timeout(timeout)
    driver.implicitly_wait(implicit_wait)

    return driver


def _create_undetected_driver(
    headless, window_size, user_agent, download_dir, timeout, implicit_wait
):
    """Create an undetected Chrome driver for Cloudflare/WAF bypass."""
    import undetected_chromedriver as uc

    options = uc.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    if window_size is None:
        window_size = random.choice(CHROME_WINDOW_SIZES)
    options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

    if user_agent:
        options.add_argument(f"--user-agent={user_agent}")

    options.add_argument("--lang=en-US,en;q=0.9")

    if download_dir:
        os.makedirs(download_dir, exist_ok=True)
        prefs = {
            "download.default_directory": os.path.abspath(download_dir),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "pdfjs.disabled": True,
        }
        options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(options=options)

    driver.set_page_load_timeout(timeout)
    driver.implicitly_wait(implicit_wait)

    return driver


def kill_driver(driver):
    """Safely quit a Selenium driver, ignoring errors."""
    if driver is None:
        return
    try:
        driver.quit()
    except Exception:
        pass


def _stealth_js():
    """Return JavaScript string for anti-detection overrides."""
    return """
    Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
    Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
    Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
    window.chrome = {runtime: {}};
    """