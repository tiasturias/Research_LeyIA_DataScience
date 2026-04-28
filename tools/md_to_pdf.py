"""Convierte un .md a PDF via markdown -> HTML -> Chrome headless."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import markdown

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 2cm 1.8cm 2cm 1.8cm; }
html { font-size: 10.5pt; }
body {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  color: #1a1a1a; line-height: 1.45; max-width: 100%;
}
h1 { font-size: 1.8rem; border-bottom: 2px solid #333; padding-bottom: .3rem;
     margin-top: 1.4rem; page-break-after: avoid; }
h2 { font-size: 1.35rem; border-bottom: 1px solid #bbb; padding-bottom: .2rem;
     margin-top: 1.2rem; page-break-after: avoid; }
h3 { font-size: 1.12rem; margin-top: 1rem; page-break-after: avoid; }
h4 { font-size: 1rem; margin-top: .8rem; page-break-after: avoid; }
p, li { orphans: 2; widows: 2; }
code { background: #f2f2f2; padding: 1px 4px; border-radius: 3px;
       font-family: "SF Mono", Menlo, Consolas, monospace; font-size: .88em; }
pre { background: #f6f6f6; padding: .7rem; border-radius: 4px;
      overflow-x: auto; font-size: .82em; page-break-inside: avoid; }
pre code { background: transparent; padding: 0; }
blockquote { border-left: 3px solid #bbb; padding: .2rem .8rem;
             color: #555; margin: .6rem 0; }
table { border-collapse: collapse; width: 100%; margin: .8rem 0;
        font-size: .88em; page-break-inside: avoid; }
th, td { border: 1px solid #ccc; padding: 4px 8px; text-align: left;
         vertical-align: top; }
th { background: #eee; }
hr { border: 0; border-top: 1px solid #ccc; margin: 1rem 0; }
a { color: #0b5fff; text-decoration: none; }
strong { color: #111; }
ul, ol { padding-left: 1.3rem; }
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>{body}</body></html>
"""


def md_to_pdf(md_path: Path, pdf_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
    )
    html = HTML_TEMPLATE.format(title=md_path.stem, css=CSS, body=html_body)

    html_tmp = pdf_path.with_suffix(".tmp.html")
    html_tmp.write_text(html, encoding="utf-8")

    cmd = [
        CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}", html_tmp.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    html_tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
    md_to_pdf(src, dst)
    print(f"[OK] {dst} ({dst.stat().st_size/1024:.1f} KB)")
