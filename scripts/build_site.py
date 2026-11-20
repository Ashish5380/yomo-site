#!/usr/bin/env python3
"""Build the Yomo marketing site (meetyomo.in) from one shared shell.

Every page gets the same head, header, footer and design tokens, so navigation,
branding and the legal disclosure cannot drift between pages. Run from anywhere:

    python3 scripts/build_site.py

Then serve the repo root (`python3 -m http.server 8109`) to preview, commit the
generated HTML, and push to main — GitHub Pages serves the repo root.

Design: "Serene Financial Flow" (Stitch export, 2026-11-21). Light architectural
surfaces, deep navy structure, hairline borders, prosperity green for money that
moved your way, magenta kept to micro-accents.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://meetyomo.in"
MAIL = "hello@prasthana.in"

TW_CONFIG = """
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        surface: "#f8f9fb",
        "surface-dim": "#d9dadc",
        "surface-bright": "#f8f9fb",
        "surface-container-lowest": "#ffffff",
        "surface-container-low": "#f3f4f6",
        "surface-container": "#edeef0",
        "surface-container-high": "#e7e8ea",
        "surface-container-highest": "#e1e2e4",
        "on-surface": "#191c1e",
        "on-surface-variant": "#46464d",
        "inverse-surface": "#2e3132",
        "inverse-on-surface": "#f0f1f3",
        hairline: "#e8eaef",
        outline: "#77767e",
        "outline-variant": "#c7c5ce",
        primary: "#050722",
        "on-primary": "#ffffff",
        "primary-container": "#1c1f3a",
        "on-primary-container": "#8486a7",
        secondary: "#595e72",
        "on-secondary": "#ffffff",
        "secondary-container": "#dde1fa",
        "on-secondary-container": "#5f6478",
        tertiary: "#000e05",
        "tertiary-container": "#002813",
        "on-tertiary-container": "#0f9d5d",
        error: "#ba1a1a",
        "error-container": "#ffdad6",
        "on-error-container": "#93000a",
        "primary-fixed": "#dfe0ff",
        "primary-fixed-dim": "#c2c4e7",
        "on-primary-fixed": "#161934",
        "secondary-fixed": "#dde1fa",
        "secondary-fixed-dim": "#c1c5dd",
        "tertiary-fixed": "#82fab0",
        "tertiary-fixed-dim": "#65dd96",
        magenta: "#e6007e",
        prosperity: "#1fa463"
      },
      borderRadius: {
        sm: "0.25rem",
        DEFAULT: "0.5rem",
        md: "0.75rem",
        lg: "1rem",
        xl: "1.5rem",
        full: "9999px"
      },
      spacing: {
        gutter: "1rem",
        "gutter-mobile": "0.75rem",
        margin: "1.25rem",
        "margin-mobile": "1rem",
        "space-xs": "0.25rem",
        "space-sm": "0.5rem",
        "space-md": "1rem",
        "space-lg": "1.5rem",
        "space-xl": "2rem"
      },
      fontFamily: {
        display: ["Plus Jakarta Sans", "system-ui", "sans-serif"],
        headline: ["Plus Jakarta Sans", "system-ui", "sans-serif"],
        body: ["Plus Jakarta Sans", "system-ui", "sans-serif"],
        label: ["Plus Jakarta Sans", "system-ui", "sans-serif"]
      },
      fontSize: {
        "display-lg": ["36px", { lineHeight: "44px", letterSpacing: "-0.03em", fontWeight: "700" }],
        "headline-lg": ["28px", { lineHeight: "36px", letterSpacing: "-0.02em", fontWeight: "600" }],
        "headline-md": ["22px", { lineHeight: "30px", letterSpacing: "-0.015em", fontWeight: "600" }],
        "headline-sm": ["18px", { lineHeight: "26px", letterSpacing: "-0.01em", fontWeight: "600" }],
        "body-lg": ["16px", { lineHeight: "24px", letterSpacing: "-0.005em", fontWeight: "400" }],
        "body-md": ["14px", { lineHeight: "20px", letterSpacing: "0em", fontWeight: "400" }],
        "body-sm": ["12px", { lineHeight: "18px", letterSpacing: "0.01em", fontWeight: "400" }],
        "label-lg": ["15px", { lineHeight: "20px", letterSpacing: "0em", fontWeight: "600" }],
        "label-md": ["13px", { lineHeight: "18px", letterSpacing: "0.01em", fontWeight: "500" }],
        "label-sm": ["11px", { lineHeight: "16px", letterSpacing: "0.04em", fontWeight: "600" }],
        "currency-hero": ["34px", { lineHeight: "40px", letterSpacing: "-0.02em", fontWeight: "700" }],
        "currency-card": ["20px", { lineHeight: "26px", letterSpacing: "-0.01em", fontWeight: "600" }]
      },
      boxShadow: {
        soft: "0 4px 20px rgba(5,7,34,0.04)",
        lift: "0 20px 36px -12px rgba(16,18,34,0.08), 0 1px 3px rgba(0,0,0,0.03)"
      }
    }
  }
};
"""

HEAD = """<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta name="theme-color" content="#f8f9fb"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{site}{path}"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="Yomo"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{site}{path}"/>
<meta property="og:image" content="{site}/assets/icon-180.png"/>
<meta name="twitter:card" content="summary"/>
<link rel="icon" href="assets/icon-64.png" type="image/png" sizes="64x64"/>
<link rel="apple-touch-icon" href="assets/icon-180.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="assets/site.css"/>
<script src="https://cdn.tailwindcss.com?plugins=forms"></script>
<script id="tailwind-config">{tw}</script>
<noscript><style>.rise{{opacity:1;transform:none}}</style></noscript>
</head>
<body class="bg-surface font-body text-body-md text-on-surface antialiased">
"""

NAV = [
    ("Home", "index.html", "home"),
    ("How it works", "index.html#how-it-works", "how"),
    ("Features", "index.html#features", "features"),
    ("Pricing", "pricing.html", "pricing"),
    ("Security", "security.html", "security"),
    ("About", "about.html", "about"),
]


def nav_links(active: str, mobile: bool = False) -> str:
    out = []
    for label, href, key in NAV:
        if mobile:
            cls = "px-3 py-3 rounded-lg font-label-md text-label-md text-primary font-semibold bg-surface-container" if key == active \
                else "px-3 py-3 rounded-lg font-label-md text-label-md text-on-surface hover:bg-surface-container transition-colors"
            out.append(f'<a class="{cls}" href="{href}">{label}</a>')
        else:
            cls = ("text-primary font-semibold relative after:content-[''] after:absolute after:-bottom-1.5 "
                   "after:left-0 after:w-full after:h-0.5 after:bg-primary after:rounded-full") if key == active \
                else "text-on-surface-variant hover:text-primary transition-colors duration-200"
            out.append(f'<a class="font-body-md text-body-md {cls}" href="{href}">{label}</a>')
    return "\n        ".join(out)


def header(active: str) -> str:
    return f"""<header class="fixed top-0 left-0 right-0 w-full z-50 bg-surface/85 backdrop-blur-xl border-b border-hairline">
  <div class="h-20 max-w-7xl mx-auto px-6 lg:px-12 flex items-center justify-between gap-6">
    <a class="flex items-center gap-3 group" href="index.html" aria-label="Yomo home">
      <span class="w-9 h-9 rounded-xl overflow-hidden bg-surface-container-low border border-hairline shadow-[0_2px_8px_rgba(5,7,34,0.06)] flex items-center justify-center shrink-0">
        <img src="assets/mascot.png" alt="Yomo mascot" class="w-full h-full object-cover"/>
      </span>
      <span class="flex flex-col">
        <span class="font-headline text-headline-sm text-primary tracking-tight font-bold leading-none">Yomo</span>
        <span class="font-label text-[10px] text-secondary uppercase tracking-widest font-semibold mt-0.5">Finance</span>
      </span>
    </a>
    <nav class="hidden lg:flex items-center gap-8">
        {nav_links(active)}
    </nav>
    <div class="flex items-center gap-3">
      <a class="inline-flex items-center gap-2 h-10 px-4 rounded-lg bg-primary-container text-on-primary font-label text-label-lg hover:bg-primary transition-colors" href="#request">
        Request invite
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M14 5l7 7m0 0l-7 7m7-7H3" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <button id="menu-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="mobile-menu" class="lg:hidden w-10 h-10 rounded-lg border border-hairline flex items-center justify-center text-primary hover:bg-surface-container transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
  <div id="mobile-menu" class="hidden lg:hidden bg-surface border-t border-hairline">
    <nav class="max-w-7xl mx-auto px-6 py-4 flex flex-col gap-1">
        {nav_links(active, mobile=True)}
    </nav>
  </div>
</header>
"""

FOOTER = f"""<footer class="w-full bg-surface-container-lowest border-t border-hairline mt-space-xl">
  <div class="max-w-7xl mx-auto px-6 lg:px-12 py-14">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12">
      <div class="lg:col-span-2 flex flex-col gap-4">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl overflow-hidden bg-surface-container-low border border-hairline flex items-center justify-center shrink-0">
            <img src="assets/mascot.png" alt="Yomo mascot" class="w-full h-full object-cover"/>
          </span>
          <span class="font-headline text-headline-sm text-primary font-bold tracking-tight">Yomo</span>
        </div>
        <p class="font-body text-body-md text-on-surface-variant max-w-sm leading-relaxed">
          A read-only money assistant for India. It reads the alerts and statements you already have, then answers what you can spend, what you owe and where it went — in plain rupees.
        </p>
        <div class="flex items-center gap-2 font-label text-label-sm text-on-surface-variant">
          <span class="w-1.5 h-1.5 rounded-full bg-prosperity"></span>
          <span>Read-only by design · no bank credentials</span>
        </div>
      </div>
      <div class="flex flex-col gap-4">
        <span class="font-label text-label-md text-primary font-bold">Product</span>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="index.html#features">Safe to spend</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="index.html#features">Portfolio &amp; net worth</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="index.html#features">Tax comparison</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="index.html#how-it-works">How it reads your data</a>
      </div>
      <div class="flex flex-col gap-4">
        <span class="font-label text-label-md text-primary font-bold">Company</span>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="about.html">About Yomo</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="pricing.html">Pricing</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="security.html">Security &amp; privacy</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="mailto:{MAIL}">Contact</a>
      </div>
      <div class="flex flex-col gap-4">
        <span class="font-label text-label-md text-primary font-bold">Trust</span>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="security.html#data-deletion">Delete my data</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="security.html#faq">Security FAQ</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="pricing.html#faq">Billing FAQ</a>
        <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="mailto:{MAIL}?subject=Yomo%20invite%20request">Request an invite</a>
      </div>
    </div>
    <div class="rounded-xl bg-surface-container-low border border-hairline p-6">
      <h2 class="font-label text-label-lg text-primary font-bold mb-2">What Yomo is, and is not</h2>
      <p class="font-body text-body-sm text-on-surface-variant leading-relaxed">
        Yomo is a read-only money analytics tool built by Prasthana. It cannot move money, place orders, hold funds or act on your accounts, and it never asks for a bank password or an OTP. Yomo is not a SEBI-registered investment adviser and does not sell investment products; its insights are informational, not personalised advice. Mutual fund investments are subject to market risks — read the scheme documents before investing.
      </p>
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mt-4 pt-4 border-t border-hairline">
        <p class="font-body text-body-sm text-on-surface-variant">© 2026 Yomo · a Prasthana product · made in India</p>
        <div class="flex items-center gap-4">
          <a class="font-body text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="mailto:{MAIL}">{MAIL}</a>
          <span class="w-px h-3 bg-hairline hidden sm:block"></span>
          <span class="font-label text-label-sm text-on-surface-variant">Read-only sync</span>
        </div>
      </div>
    </div>
  </div>
</footer>
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def page(path: str, title: str, desc: str, active: str, body: str) -> str:
    head = HEAD.format(title=title, desc=desc, site=SITE, path="/" + path if path != "index.html" else "/", tw=TW_CONFIG)
    return head + header(active) + "\n" + body.strip() + "\n" + FOOTER


# --------------------------------------------------------------------------- content
ICON = {
    "mail": '<path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>',
    "doc": '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>',
    "chat": '<path d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>',
    "rupee": '<path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>',
    "chart": '<path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>',
    "tax": '<path d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/>',
    "tag": '<path d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/>',
    "shield": '<path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>',
    "lock": '<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 118 0v3"/>',
    "eye": '<path d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/><path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>',
    "download": '<path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>',
    "check": '<path d="M5 13l4 4L19 7"/>',
    "x": '<path d="M6 18L18 6M6 6l12 12"/>',
    "chevron": '<path d="M19 9l-7 7-7-7"/>',
    "arrow": '<path d="M14 5l7 7m0 0l-7 7m7-7H3"/>',
    "phone": '<path d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/>',
}


def icon(name: str, cls: str = "w-5 h-5", stroke: str = "1.8") -> str:
    return (f'<svg class="{cls}" fill="none" stroke="currentColor" stroke-width="{stroke}" viewBox="0 0 24 24" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')
