"""
cloudflare_bypass.py — Handle Cloudflare challenges and WAF protections.

Detects Cloudflare challenge pages, waits for resolution, and provides
fallback strategies for government websites with anti-bot protections.
"""

import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

CLOUDFLARE_INDICATORS = [
    "cloudflare",
    "cf-browser-verification",
    "challenge-platform",
    "Just a moment...",
    "Checking your browser",
    "Please Wait...",
    "Attention Required",
    "ray id",
]

WAF_INDICATORS = [
    "access denied",
    "forbidden",
    "403",
    "bot detected",
    "automated access",
    "rate limit",
    "security check",
]


def is_cloudflare_challenge(driver):
    """Detect if the current page is a Cloudflare challenge page."""
    try:
        page_source = driver.page_source.lower()
        title = driver.title.lower()

        for indicator in CLOUDFLARE_INDICATORS:
            if indicator in page_source or indicator in title:
                return True
    except Exception:
        pass
    return False


def is_waf_blocked(driver):
    """Detect if the page shows a WAF block message."""
    try:
        page_source = driver.page_source.lower()
        title = driver.title.lower()

        for indicator in WAF_INDICATORS:
            if indicator in page_source or indicator in title:
                return True
    except Exception:
        pass
    return False


def wait_for_cloudflare_resolution(driver, max_wait=20, poll_interval=2):
    """
    Wait for a Cloudflare challenge to resolve.

    On some sites, Cloudflare shows a "Checking your browser" page
    that auto-resolves in 4-10 seconds. This function polls until
    the challenge resolves or timeout is reached.

    Args:
        driver: Selenium WebDriver instance
        max_wait: Maximum seconds to wait for resolution
        poll_interval: Seconds between checks

    Returns:
        True if challenge resolved, False if still blocked
    """
    start = time.time()
    initial_url = driver.current_url

    logger.info("[cloudflare] Detected challenge page, waiting for resolution...")

    while time.time() - start < max_wait:
        time.sleep(poll_interval)

        if not is_cloudflare_challenge(driver):
            logger.info("[cloudflare] Challenge resolved after %.1f seconds",
                        time.time() - start)
            return True

        # Check if URL changed (redirect after challenge)
        current_url = driver.current_url
        if current_url != initial_url and "challenge" not in current_url.lower():
            logger.info("[cloudflare] Redirected after challenge to: %s", current_url)
            return True

    logger.warning("[cloudflare] Challenge not resolved after %d seconds", max_wait)
    return False


def bypass_cloudflare(driver, url, max_wait=20):
    """
    Navigate to a URL and attempt to bypass Cloudflare protection.

    Args:
        driver: Selenium WebDriver instance
        url: Target URL
        max_wait: Maximum seconds to wait for challenge resolution

    Returns:
        True if page loaded successfully (no Cloudflare challenge),
        False if still blocked
    """
    logger.info("[cloudflare] Navigating to: %s", url)
    driver.get(url)

    if is_cloudflare_challenge(driver):
        resolved = wait_for_cloudflare_resolution(driver, max_wait=max_wait)
        if resolved:
            logger.info("[cloudflare] Successfully bypassed Cloudflare")
            return True
        else:
            logger.warning("[cloudflare] Failed to bypass Cloudflare for %s", url)
            return False

    if is_waf_blocked(driver):
        logger.warning("[cloudflare] WAF block detected (not Cloudflare) for %s", url)
        return False

    logger.info("[cloudflare] No challenge detected, page loaded directly")
    return True


def get_page_with_retry(driver, url, max_retries=3, wait_between=5, bypass=True):
    """
    Navigate to a URL with retry logic and optional Cloudflare bypass.

    Args:
        driver: Selenium WebDriver instance
        url: Target URL
        max_retries: Number of retry attempts
        wait_between: Seconds to wait between retries
        bypass: Whether to attempt Cloudflare bypass

    Returns:
        True if page loaded successfully, False otherwise
    """
    for attempt in range(1, max_retries + 1):
        try:
            logger.info("[retry] Attempt %d/%d: %s", attempt, max_retries, url)

            if bypass:
                success = bypass_cloudflare(driver, url)
            else:
                driver.get(url)
                success = not is_waf_blocked(driver)

            if success:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                return True

            logger.warning("[retry] Blocked on attempt %d, retrying in %ds",
                           attempt, wait_between)

        except Exception as e:
            logger.warning("[retry] Error on attempt %d: %s", attempt, str(e))

        if attempt < max_retries:
            time.sleep(wait_between)

    logger.error("[retry] All %d attempts failed for %s", max_retries, url)
    return False