#!/usr/bin/env python3
"""Create a lightweight HTML-text snapshot for an arXiv paper.

This helper is for theorem-extraction audits. It intentionally does not certify
any theorem. Its purpose is to give future agents a reproducible way to capture
section headings and nearby prose from arXiv HTML.

Example:
  python scripts/arxiv_html_section_snapshot.py 2602.15797 \
    --out data/theorem_extraction/pham_sauermann_2026_html_snapshot.txt

Notes:
  - arXiv HTML often strips or degrades displayed mathematics.
  - Use the snapshot only for theorem maps and prose dependencies.
  - Use PDF/TeX source for exact constants and displayed inequalities.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path


def strip_tags(html: str) -> str:
    # Preserve block-ish boundaries before stripping tags.
    html = re.sub(r"</(p|div|section|h[1-6]|li|tr)>", "\n", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    text = re.sub(r"<[^>]+>", "", html)
    text = unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("arxiv_id", help="arXiv id, e.g. 2602.15797")
    ap.add_argument("--out", required=True, help="Output text snapshot path")
    args = ap.parse_args()

    url = f"https://arxiv.org/html/{args.arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "erdos-475-theorem-extraction/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="replace")

    text = strip_tags(html)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"# arXiv HTML snapshot\n"
        f"# arxiv_id={args.arxiv_id}\n"
        f"# url={url}\n"
        f"# WARNING: displayed mathematics may be stripped; use PDF/TeX for constants.\n\n"
        f"{text}\n",
        encoding="utf-8",
    )
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
