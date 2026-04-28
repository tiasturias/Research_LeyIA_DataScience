"""
corpus-legal-ia scraper package.

Download PDFs and extract law text from government websites
that require JavaScript rendering or have anti-bot protections.

Usage:
    from scraper import download_pdfs, extract_law_text
    # or via CLI:
    python3 scripts/run_scraper.py --country FIN --urls "https://..."
"""

from .downloader import download_pdfs
from .law_extractor import extract_law_text
from .state_manager import StateManager
from .browser import create_driver, kill_driver

__all__ = [
    "download_pdfs",
    "extract_law_text",
    "StateManager",
    "create_driver",
    "kill_driver",
]