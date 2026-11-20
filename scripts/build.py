#!/usr/bin/env python3
"""Render the Yomo marketing site. Usage: python3 scripts/build.py

Shared head/header/footer/tokens live in build_site.py; page bodies in
pages_index.py / pages_other.py. Output is committed and served by GitHub Pages.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build_site import page  # noqa: E402
from pages_index import INDEX  # noqa: E402
from pages_other import ABOUT, PRICING, SECURITY  # noqa: E402

PAGES = {
    "index.html": dict(
        title="Yomo — the read-only money assistant for India",
        desc=("Yomo reads the bank alerts in your Gmail, the statements you forward and, on Android, the bank SMS "
              "on your phone — then answers what you can spend, what you owe and where it went. No bank logins. "
              "Free to start."),
        active="home",
        body=INDEX,
    ),
    "pricing.html": dict(
        title="Pricing — Free, Plus ₹399/mo, Pro ₹899/mo | Yomo",
        desc=("Yomo pricing: start free, then Plus at ₹399/month (₹3,990/year) for the full picture, or Pro at "
              "₹899/month (₹7,999/year) for tax and what-if planning. Exporting and deleting your data stay free."),
        active="pricing",
        body=PRICING,
    ),
    "security.html": dict(
        title="Security & privacy — read-only by construction | Yomo",
        desc=("How Yomo reads Indian bank alerts, statements and broker holdings without a bank password: read-only "
              "feeds, encrypted storage, no OTPs kept, and in-app export and deletion."),
        active="security",
        body=SECURITY,
    ),
    "about.html": dict(
        title="About Yomo — a money app that counts like an accountant",
        desc=("Yomo is a chat-first, read-only money assistant built in India by Prasthana. Every rupee figure is "
              "computed in code; the model never does arithmetic. Meet Roast, Pro and Zen."),
        active="about",
        body=ABOUT,
    ),
}

root = HERE.parent
for filename, spec in PAGES.items():
    html = page(filename, spec["title"], spec["desc"], spec["active"], spec["body"])
    (root / filename).write_text(html, encoding="utf-8")
    print(f"wrote {filename:16} {len(html):>7,} bytes")
