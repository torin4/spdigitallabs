"""Rebuild the generated app and policy pages.

    python3 _generator/build.py

Writes into the site folder (the parent of _generator/). Generated:
  dailyallowance/{index,support,privacy,terms,delete-account}.html
  strata/index.html
  understory/{index,privacy,terms,legal-notice}.html
  hanjo/{index,privacy,terms,legal-notice}.html
  surfwindow/{index,privacy,terms}.html, plus redirects at privacy-ja.html
    and terms-ja.html (the Surf Window app links them)
  tuck/{index,support,privacy}.html
  ja/<app>/... : the Japanese twin of each of those pages, except the
    legal notices, which are already in Japanese. Japanese text is in
    <app>_ja.py; keep it saying the same as the English. On privacy
    policies and terms, the English version governs.
  blog/index.html and blog/<slug>.html (posts are in blog_posts.py; English only)
  about/index.html and ja/about/index.html
The homepages (index.html, ja/index.html) and 404.html are written by hand. When style.css changes, bump
CSS_VERSION in chrome.py and the ?v= on the hand-written pages to match.
Jekyll skips folders starting with "_", so this folder is never published.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import about, blog, dailyallowance, hanjo, strata, surfwindow, tuck, understory  # noqa: E402

for module in (dailyallowance, hanjo, strata, surfwindow, tuck, understory, blog, about):
    module.build(ROOT)
print("Rebuilt app pages in", ROOT)
