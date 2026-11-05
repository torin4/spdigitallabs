"""Rebuild the generated app and policy pages.

    python3 _generator/build.py

Writes into the site folder (the parent of _generator/). Generated:
  dailyallowance/index.html
  strata/index.html
  understory/{index,privacy,terms,legal-notice}.html
  surfwindow/{index,privacy,terms,privacy-ja,terms-ja}.html
The Daily Allowance policy pages (privacy, terms, support, delete-account)
and the homepage are written by hand. When style.css changes, bump
CSS_VERSION in chrome.py and the ?v= on the hand-written pages to match.
Jekyll skips folders starting with "_", so this folder is never published.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import dailyallowance, strata, surfwindow, understory  # noqa: E402

for module in (dailyallowance, strata, surfwindow, understory):
    module.build(ROOT)
print("Rebuilt app pages in", ROOT)
