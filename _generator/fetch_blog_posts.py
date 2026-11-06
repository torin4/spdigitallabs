"""Refresh the list of posts that live on each app's own site.

    python3 _generator/fetch_blog_posts.py

The blog hub at /blog/ lists every app's posts. Daily Allowance posts live here
(blog_posts.py); the others live on their app's site and are read from its live
sitemap, then saved to external_posts.json so the build itself never needs the
network. Run this after publishing new posts on any app's site, then rebuild.
"""
import html
import json
import os
import re
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCES = [
    ("strata", "https://stratabible.app/sitemap.xml", r"/blog/[^/]+/?$"),
    ("understory", "https://understoryjournal.app/sitemap.xml", r"/blog/[^/]+/?$"),
    ("surfwindow", "https://surfwindow.jp/sitemap.xml", r"/guide/[^/]+/$"),
]
# Each site appends its own name to page titles; the hub shows the bare title.
SUFFIX = re.compile(r"\s*(?:\||｜)\s*(?:STRATA|Understory|Surf Window)\s*$")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "spdigitallabs-build"})
    return urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")


def meta(page, pattern):
    m = re.search(pattern, page)
    return html.unescape(m.group(1)).strip() if m else ""


def main():
    posts = []
    for app, sitemap, pattern in SOURCES:
        for url in re.findall(r"<loc>([^<]+)</loc>", get(sitemap)):
            if not re.search(pattern, url):
                continue
            page = get(url)
            title = meta(page, r'<meta property="og:title" content="([^"]*)"') or meta(page, r"<title>([^<]*)</title>")
            posts.append({
                "app": app,
                "url": url,
                "title": SUFFIX.sub("", title),
                "description": meta(page, r'<meta name="description" content="([^"]*)"'),
                "date": meta(page, r'"datePublished":\s*"([^"]+)"')[:10],
                "lang": meta(page, r'<html lang="([^"]+)"') or "en",
            })
    with open(os.path.join(HERE, "external_posts.json"), "w") as f:
        json.dump(posts, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Saved {len(posts)} posts to external_posts.json")


if __name__ == "__main__":
    main()
