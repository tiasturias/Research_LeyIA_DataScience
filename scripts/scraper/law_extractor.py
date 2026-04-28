"""
law_extractor.py — Extract structured law text from government websites.

Uses Selenium to render JavaScript-heavy pages and inject custom JavaScript
to extract law articles, sections, and content from government portals like
e-gov.go.jp, finlex.fi, and similar sites.

Inspired by scrape_ley_selenium.py's EXTRACT_SCRIPT approach.
"""

import json
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .browser import create_driver, kill_driver
from .cloudflare_bypass import get_page_with_retry

logger = logging.getLogger(__name__)

# Site-specific extraction scripts
# Each script returns a JSON-serializable dict with law content

E_GOV_GO_JP_SCRIPT = """
return (() => {
    const data = {
        title: "",
        law_number: "",
        promulgation_date: "",
        effective_date: "",
        articles: [],
        raw_text: "",
        url: window.location.href
    };

    // Try to extract title
    const titleEl = document.querySelector('h2, .lawTitle, .title, h1');
    if (titleEl) data.title = titleEl.textContent.trim();

    // Try to extract all text content from law body
    const lawBody = document.querySelector('.lawBody, .law-body, #lawBody, main, article, .content');
    if (lawBody) {
        data.raw_text = lawBody.innerText.trim();
    } else {
        // Fallback: get body text
        data.raw_text = document.body.innerText.trim();
    }

    // Try to extract articles (Japanese law format)
    const articleElements = document.querySelectorAll('[id^="a"], .Article, .article');
    articleElements.forEach(el => {
        const text = el.textContent.trim();
        if (text.length > 10) {
            data.articles.push({
                content: text.substring(0, 500),
                full_content: text
            });
        }
    });

    // If no articles found, split raw text into paragraphs
    if (data.articles.length === 0 && data.raw_text) {
        const paragraphs = data.raw_text.split(/\\n{2,}/);
        paragraphs.forEach(p => {
            p = p.trim();
            if (p.length > 20) {
                data.articles.push({ content: p.substring(0, 500), full_content: p });
            }
        });
    }

    return data;
})();
"""

FINLEX_FI_SCRIPT = """
return (() => {
    const data = {
        title: "",
        law_number: "",
        promulgation_date: "",
        articles: [],
        raw_text: "",
        url: window.location.href
    };

    const titleEl = document.querySelector('h1, .law-title, .document-title');
    if (titleEl) data.title = titleEl.textContent.trim();

    const contentEl = document.querySelector('.law-text, .document-content, main, article');
    if (contentEl) {
        data.raw_text = contentEl.innerText.trim();
    } else {
        data.raw_text = document.body.innerText.trim();
    }

    return data;
})();
"""

GENERIC_LAW_SCRIPT = """
return (() => {
    const data = {
        title: "",
        articles: [],
        raw_text: "",
        url: window.location.href
    };

    // Try multiple selectors for title
    const titleSelectors = ['h1', 'h2.law-title', '.document-title', '.law-title',
                              'title', '.page-title', '.entry-title'];
    for (const sel of titleSelectors) {
        const el = document.querySelector(sel);
        if (el && el.textContent.trim()) {
            data.title = el.textContent.trim();
            break;
        }
    }

    // Extract main content
    const contentSelectors = ['main', 'article', '.content', '.law-text',
                               '.document-content', '.law-body', '#content',
                               '.entry-content', '.page-content'];
    let mainContent = null;
    for (const sel of contentSelectors) {
        const el = document.querySelector(sel);
        if (el && el.innerText.trim().length > 100) {
            mainContent = el;
            break;
        }
    }

    if (mainContent) {
        data.raw_text = mainContent.innerText.trim();
    } else {
        data.raw_text = document.body.innerText.trim();
    }

    // Try to find article-like sections
    const sectionPatterns = [
        { selector: '.article, .Article, [class*="article"]', name_attr: 'class' },
        { selector: 'section, .section, [class*="section"]', name_attr: 'class' },
        { selector: '.paragraph, .Paragraph, p', name_attr: 'class' },
    ];

    for (const pattern of sectionPatterns) {
        const elements = document.querySelectorAll(pattern.selector);
        if (elements.length > 0) {
            elements.forEach(el => {
                data.articles.push({
                    content: el.textContent.trim().substring(0, 500),
                    full_content: el.textContent.trim()
                });
            });
            break;
        }
    }

    // If still no articles, split raw text
    if (data.articles.length === 0) {
        const paragraphs = data.raw_text.split(/\\n{2,}/);
        paragraphs.forEach(p => {
            p = p.trim();
            if (p.length > 20) {
                data.articles.push({ content: p.substring(0, 500), full_content: p });
            }
        });
    }

    return data;
})();
"""

SITE_SCRIPTS = {
    "e-gov.go.jp": E_GOV_GO_JP_SCRIPT,
    "laws.e-gov.go.jp": E_GOV_GO_JP_SCRIPT,
    "finlex.fi": FINLEX_FI_SCRIPT,
}

DEFAULT_SCRIPT = GENERIC_LAW_SCRIPT


def extract_law_text(
    url,
    site_type=None,
    headless=True,
    bypass_cloudflare=False,
    timeout=30,
    wait_after_load=10,
    output_file=None,
    max_retries=3,
):
    """
    Extract structured law text from a government website.

    Args:
        url: URL of the law page
        site_type: Site identifier for custom extraction script.
            Options: 'e-gov.go.jp', 'finlex.fi', or None for generic.
            Auto-detected from URL if not provided.
        headless: Run browser in headless mode
        bypass_cloudflare: Use undetected-chromedriver
        timeout: Page load timeout
        wait_after_load: Seconds to wait for JS rendering
        output_file: Path to save extracted text (JSON format)
        max_retries: Number of retry attempts

    Returns:
        Dict with extracted law data:
        {title, articles: [{content, full_content}], raw_text, url, source}
    """
    driver = None
    result = {
        "title": "",
        "articles": [],
        "raw_text": "",
        "url": url,
        "source": "selenium_extraction",
        "extraction_status": "unknown",
    }

    # Auto-detect site type from URL
    if site_type is None:
        site_type = _detect_site_type(url)

    # Select appropriate extraction script
    script = SITE_SCRIPTS.get(site_type, DEFAULT_SCRIPT)

    try:
        driver = create_driver(
            headless=headless,
            bypass_cloudflare=bypass_cloudflare,
            timeout=timeout,
        )

        # Navigate with retry
        success = get_page_with_retry(driver, url, max_retries=max_retries, bypass=True)

        if not success:
            result["extraction_status"] = "blocked"
            result["raw_text"] = f"Could not load page: {url}"
            return result

        # Wait for JS rendering
        logger.info("[extractor] Waiting %d seconds for JS rendering...", wait_after_load)
        time.sleep(wait_after_load)

        # Wait for body to be present
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except Exception:
            logger.warning("[extractor] Timeout waiting for body element")

        # Execute extraction script
        logger.info("[extractor] Executing extraction script for site type: %s", site_type)
        data = driver.execute_script(script)

        if data:
            result.update(data)
            result["extraction_status"] = "success"
            logger.info("[extractor] Extracted: title='%s', %d articles, %d chars",
                        result.get("title", "")[:50],
                        len(result.get("articles", [])),
                        len(result.get("raw_text", "")))
        else:
            result["extraction_status"] = "extraction_failed"
            result["raw_text"] = driver.page_source if driver else ""

    except Exception as e:
        logger.error("[extractor] Error extracting from %s: %s", url, e)
        result["extraction_status"] = "error"
        result["raw_text"] = str(e)

    finally:
        kill_driver(driver)

    # Save to file if requested
    if output_file:
        os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        logger.info("[extractor] Saved to: %s", output_file)

    return result


def _detect_site_type(url):
    """Auto-detect site type from URL domain."""
    url_lower = url.lower()

    for site_key in SITE_SCRIPTS:
        if site_key in url_lower:
            return site_key

    return "generic"


def extract_law_text_from_multiple(urls, **kwargs):
    """
    Extract law text from multiple URLs.

    Args:
        urls: List of URLs to extract from
        **kwargs: Passed to extract_law_text()

    Returns:
        List of extraction result dicts
    """
    results = []
    for url in urls:
        result = extract_law_text(url, **kwargs)
        results.append(result)

    return results