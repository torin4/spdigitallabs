"""Shared page chrome for spdigitallabs.app app pages."""

CSS_VERSION = "20261111a"

APPS = {
    "hanjo": {
        "name": "Hanjo",
        "icon": "/assets/apps/hanjo.png",
        "tabs": [("/hanjo/privacy.html", "Privacy"), ("/hanjo/terms.html", "Terms")],
        "foot": [("/hanjo/privacy.html", "Privacy Policy"), ("/hanjo/terms.html", "Terms of Service"),
                 ("/hanjo/legal-notice.html", "特定商取引法に基づく表記")],
        "tabs_ja": [("/ja/hanjo/privacy.html", "プライバシー"), ("/ja/hanjo/terms.html", "利用規約")],
        "foot_ja": [("/ja/hanjo/privacy.html", "プライバシーポリシー"), ("/ja/hanjo/terms.html", "利用規約"),
                 ("/hanjo/legal-notice.html", "特定商取引法に基づく表記")],
    },
    "understory": {
        "name": "Understory",
        "icon": "/assets/apps/understory.png",
        "tabs": [("/understory/privacy.html", "Privacy"), ("/understory/terms.html", "Terms")],
        "foot": [("/understory/privacy.html", "Privacy Policy"), ("/understory/terms.html", "Terms of Service"),
                 ("/understory/legal-notice.html", "特定商取引法に基づく表記")],
        "tabs_ja": [("/ja/understory/privacy.html", "プライバシー"), ("/ja/understory/terms.html", "利用規約")],
        "foot_ja": [("/ja/understory/privacy.html", "プライバシーポリシー"), ("/ja/understory/terms.html", "利用規約"),
                 ("/understory/legal-notice.html", "特定商取引法に基づく表記")],
    },
    "surfwindow": {
        "name": "Surf Window",
        "icon": "/assets/apps/surfwindow.png",
        "tabs": [("/surfwindow/privacy.html", "Privacy"), ("/surfwindow/terms.html", "Terms")],
        "foot": [("/surfwindow/privacy.html", "Privacy Policy"), ("/surfwindow/terms.html", "Terms of Service")],
        "tabs_ja": [("/ja/surfwindow/privacy.html", "プライバシー"), ("/ja/surfwindow/terms.html", "利用規約")],
        "foot_ja": [("/ja/surfwindow/privacy.html", "プライバシーポリシー"), ("/ja/surfwindow/terms.html", "利用規約")],
    },
    "dailyallowance": {
        "name": "Daily Allowance",
        "icon": "/assets/apps/dailyallowance.png",
        "tabs": [("/dailyallowance/support.html", "Support"), ("/dailyallowance/privacy.html", "Privacy"),
                 ("/dailyallowance/terms.html", "Terms")],
        "foot": [("/dailyallowance/support.html", "Support"), ("/dailyallowance/privacy.html", "Privacy Policy"),
                 ("/dailyallowance/terms.html", "Terms of Service"), ("/dailyallowance/delete-account.html", "Delete your account")],
        "tabs_ja": [("/ja/dailyallowance/support.html", "サポート"), ("/ja/dailyallowance/privacy.html", "プライバシー"),
                     ("/ja/dailyallowance/terms.html", "利用規約")],
        "foot_ja": [("/ja/dailyallowance/support.html", "サポート"), ("/ja/dailyallowance/privacy.html", "プライバシーポリシー"),
                    ("/ja/dailyallowance/terms.html", "利用規約"), ("/ja/dailyallowance/delete-account.html", "アカウントの削除")],
    },
    "tuck": {
        "name": "Tuck",
        "icon": "/assets/apps/tuck.png",
        "tabs": [("/tuck/support.html", "Support"), ("/tuck/privacy.html", "Privacy")],
        "foot": [("/tuck/support.html", "Support"), ("/tuck/privacy.html", "Privacy Policy")],
        "tabs_ja": [("/ja/tuck/support.html", "サポート"), ("/ja/tuck/privacy.html", "プライバシー")],
        "foot_ja": [("/ja/tuck/support.html", "サポート"), ("/ja/tuck/privacy.html", "プライバシーポリシー")],
    },
    "strata": {
        "name": "Strata",
        "icon": "/assets/apps/strata.png",
        "tabs": [("https://stratabible.app/privacy", "Privacy"), ("https://stratabible.app/terms", "Terms")],
        "foot": [("https://stratabible.app/privacy", "Privacy Policy"), ("https://stratabible.app/terms", "Terms of Service")],
        "tabs_ja": [("https://stratabible.app/privacy", "プライバシー"), ("https://stratabible.app/terms", "利用規約")],
        "foot_ja": [("https://stratabible.app/privacy", "プライバシーポリシー（英語）"), ("https://stratabible.app/terms", "利用規約（英語）")],
    },
    "perapera": {
        "name": "PeraPera",
        "icon": "/assets/apps/perapera.png",
        "tabs": [("https://japanese-app-kappa.vercel.app/privacy.html", "Privacy"), ("https://japanese-app-kappa.vercel.app/terms.html", "Terms")],
        "foot": [("https://japanese-app-kappa.vercel.app/privacy.html", "Privacy Policy"), ("https://japanese-app-kappa.vercel.app/terms.html", "Terms of Use"),
                 ("https://japanese-app-kappa.vercel.app/tokushoho.html", "特定商取引法に基づく表記")],
        "tabs_ja": [("https://japanese-app-kappa.vercel.app/privacy.html", "プライバシー"), ("https://japanese-app-kappa.vercel.app/terms.html", "利用規約")],
        "foot_ja": [("https://japanese-app-kappa.vercel.app/privacy.html", "プライバシーポリシー（英語）"), ("https://japanese-app-kappa.vercel.app/terms.html", "利用規約（英語）"),
                 ("https://japanese-app-kappa.vercel.app/tokushoho.html", "特定商取引法に基づく表記")],
    },
}


SITE = "https://spdigitallabs.app"
CHEVRON = '<svg class="icon" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>'


def ja_path(path):
    """The Japanese twin of an English path: /hanjo/privacy.html -> /ja/hanjo/privacy.html."""
    return "/ja" + path


def lang_link(lang, alt):
    """The header link to this page in the other language, or "" if there is no twin."""
    if not alt:
        return ""
    other, label = ("en", "English") if lang == "ja" else ("ja", "日本語")
    return '\n        <li><a href="%s" lang="%s" hreflang="%s">%s</a></li>' % (alt, other, other, label)


def alternates(en_path, ja_path_):
    """hreflang links for a page that exists in both languages."""
    return (f'<link rel="alternate" hreflang="en" href="{SITE}{en_path}">\n'
            f'<link rel="alternate" hreflang="ja" href="{SITE}{ja_path_}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{SITE}{en_path}">\n')


def app_header(slug, name, icon, tabs, current, lang="en", alt=None):
    """One header: breadcrumb (studio / app) on the left, the app's links and language switch on the right."""
    prefix = "/ja" if lang == "ja" else ""
    links = "\n".join(
        '        <li><a href="%s"%s>%s</a></li>' % (href, ' aria-current="page"' if href == current else "", label)
        for href, label in tabs)
    app_home = "%s/%s/" % (prefix, slug)
    here = ' aria-current="page"' if current == app_home else ""
    crumbs_label = "パンくずリスト" if lang == "ja" else "Breadcrumb"
    return (
        '<header class="site-header">\n'
        '  <div class="wrap bar">\n'
        '    <nav class="crumbs" aria-label="%s">\n'
        '      <a class="brand" href="%s/"><img src="/assets/logo.svg" alt="" width="32" height="32">'
        '<span class="brand-text">SP Digital Labs</span></a>\n'
        '      <span class="crumb-sep" aria-hidden="true">%s</span>\n'
        '      <a class="crumb-app" href="%s"%s><img src="%s" alt="" width="28" height="28">%s</a>\n'
        '    </nav>\n'
        '    <nav class="nav" aria-label="%s">\n'
        '      <ul>\n%s%s\n'
        '      </ul>\n'
        '    </nav>\n'
        '  </div>\n'
        '</header>' % (crumbs_label, prefix, CHEVRON, app_home, here, icon, name, name, links, lang_link(lang, alt)))


def app_footer(name, foot, lang="en"):
    links = "\n".join('      <a href="%s">%s</a>' % (href, label) for href, label in foot)
    if lang == "ja":
        legal = "&copy; 2026 SP Digital Labs（Joseph Suzuki-Parker がアプリを公開する際の屋号）。日本。"
        contact = '      <a href="/ja/#contact">お問い合わせ</a>'
        label = "%sのリンク" % name
    else:
        legal = "&copy; 2026 SP Digital Labs, the name under which Joseph Suzuki-Parker publishes apps. Japan."
        contact = '      <a href="/#contact">Contact</a>'
        label = "%s links" % name
    return (
        '<footer class="site-footer">\n'
        '  <div class="wrap foot-simple">\n'
        '    <p>%s</p>\n'
        '    <nav aria-label="%s">\n%s\n%s\n'
        '    </nav>\n'
        '  </div>\n'
        '</footer>' % (legal, label, links, contact))


def head_tags(title, description, path, og_type="website", extra=""):
    """The shared <head> contents, from charset to stylesheet. extra goes before the stylesheet."""
    return f'''<meta charset="utf-8">
<script>(function(d){{if(window.matchMedia&&matchMedia("(prefers-reduced-motion: no-preference)").matches&&"IntersectionObserver"in window){{d.classList.add("motion");setTimeout(function(){{if(!window.__spMotion)d.classList.remove("motion")}},2500)}}}})(document.documentElement)</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#f7f8fa" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0e1117" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="SP Digital Labs">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://spdigitallabs.app{path}">
<meta property="og:image" content="https://spdigitallabs.app/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="SP Digital Labs: Everyday tools, done right.">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://spdigitallabs.app{path}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/favicon-192.png" type="image/png" sizes="192x192">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/mplus-rounded-1c-800-latin.woff2" as="font" type="font/woff2" crossorigin>
{extra}<link rel="stylesheet" href="/style.css?v={CSS_VERSION}">'''


def page(slug, current, title, description, body, lang="en", main_class="wrap page", chrome_lang=None, alt=None):
    """current is this page's path, e.g. "/understory/privacy.html".

    lang is the content language (<html lang>). chrome_lang picks the header and
    footer language; it defaults to the folder the page is in (/ja/... is Japanese).
    alt is the path of the same page in the other language, if there is one."""
    app = APPS[slug]
    name = app["name"]
    chrome_lang = chrome_lang or ("ja" if current.startswith("/ja/") else "en")
    tabs = app["tabs_ja"] if chrome_lang == "ja" else app["tabs"]
    foot = app["foot_ja"] if chrome_lang == "ja" else app["foot"]
    app_home = ("/ja/%s/" if chrome_lang == "ja" else "/%s/") % slug
    full_title = name if current == app_home else "%s - %s" % (title, name)
    extra = ""
    if alt:
        en_path, ja_path_ = (alt, current) if chrome_lang == "ja" else (current, alt)
        extra = alternates(en_path, ja_path_)
    skip = "本文へスキップ" if chrome_lang == "ja" else "Skip to content"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_tags(full_title, description, current, extra=extra)}
</head>
<body>
<a class="skip" href="#main">{skip}</a>

{app_header(slug, name, app["icon"], tabs, current, chrome_lang, alt)}

<main id="main" class="{main_class}">
{body.strip()}
</main>

{app_footer(name, foot, chrome_lang)}
<script src="/email.js"></script>
<script src="/motion.js"></script>
</body>
</html>
'''


EMAIL = '<a class="email" href="/#contact">support [at] spdigitallabs [dot] app</a>'
EMAIL_JA = '<a class="email" href="/ja/#contact">support [at] spdigitallabs [dot] app</a>'


def shots(items):
    """items: (src, alt, caption)."""
    lis = "\n".join(
        f'''  <li><figure><img src="{src}" alt="{alt}" width="390" height="844" loading="lazy"><figcaption>{cap}</figcaption></figure></li>'''
        for src, alt, cap in items)
    return f'<ul class="shots" aria-label="Screenshots">\n{lis}\n</ul>'


def features(items):
    lis = "\n".join(f'  <li><h3>{h}</h3><p>{p}</p></li>' for h, p in items)
    return f'<ul class="features">\n{lis}\n</ul>'


def hero(slug, status, headline, lede, actions):
    app = APPS[slug]
    return f'''
<section class="app-hero" aria-labelledby="app-title">
  <div class="app-hero-id">
    <img src="{app["icon"]}" alt="" width="64" height="64">
    <div><span class="app-hero-name">{app["name"]}</span><span class="label live">{status}</span></div>
  </div>
  <h1 id="app-title">{headline}</h1>
  <p class="lede">{lede}</p>
  <div class="app-actions">{actions}</div>
</section>'''


def build_pages(root, slug, pages, pages_ja=None):
    """pages: {filename: (title, description, body, lang, main_class)} for /<slug>/.
    pages_ja: the same for the Japanese twins at /ja/<slug>/. A page and its twin
    share a filename, and each links to the other."""
    import os
    pages_ja = pages_ja or {}

    def path(prefix, fn):
        return f"{prefix}/{slug}/" if fn == "index.html" else f"{prefix}/{slug}/{fn}"

    for prefix, own, other in (("", pages, pages_ja), ("/ja", pages_ja, pages)):
        if not own:
            continue
        os.makedirs(f"{root}{prefix}/{slug}", exist_ok=True)
        other_prefix = "" if prefix else "/ja"
        for fn, (title, desc, body, lang, main_class) in own.items():
            alt = path(other_prefix, fn) if fn in other else None
            html = page(slug, path(prefix, fn), title, desc, body, lang, main_class, alt=alt)
            open(f"{root}{prefix}/{slug}/{fn}", "w").write(html)


def feature_rows(items):
    """items: (img src, alt, heading, text). Each main feature beside its screenshot."""
    rows = "\n".join(
        f'''  <li class="feature-row">
    <div class="feature-shot"><img src="{src}" alt="{alt}" width="390" height="844" loading="lazy"></div>
    <div class="feature-copy"><h2>{h}</h2><p>{p}</p></div>
  </li>''' for src, alt, h, p in items)
    return f'<ul class="feature-rows">\n{rows}\n</ul>'


def feature_rows_wide(items):
    """items: (img src, alt, heading, text). Like feature_rows, for landscape desktop screenshots."""
    rows = "\n".join(
        f'''  <li class="feature-row">
    <div class="feature-shot"><img src="{src}" alt="{alt}" width="1440" height="900" loading="lazy"></div>
    <div class="feature-copy"><h2>{h}</h2><p>{p}</p></div>
  </li>''' for src, alt, h, p in items)
    return f'<ul class="feature-rows wide">\n{rows}\n</ul>'


def redirect_stub(target):
    """A page that sends visitors on to target, for URLs that have moved. GitHub Pages has no redirects."""
    return f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>移動しました</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{SITE}{target}">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
<p>このページは移動しました：<a href="{target}">{SITE}{target}</a></p>
</body>
</html>
'''
