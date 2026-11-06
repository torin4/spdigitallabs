"""Shared page chrome for spdigitallabs.app app pages."""

CSS_VERSION = "20261106f"

APPS = {
    "understory": {
        "name": "Understory",
        "icon": "/assets/apps/understory.png",
        "tabs": [("/understory/privacy.html", "Privacy"), ("/understory/terms.html", "Terms")],
        "foot": [("/understory/privacy.html", "Privacy Policy"), ("/understory/terms.html", "Terms of Service"),
                 ("/understory/legal-notice.html", "特定商取引法に基づく表記")],
    },
    "surfwindow": {
        "name": "Surf Window",
        "icon": "/assets/apps/surfwindow.png",
        "tabs": [("/surfwindow/privacy.html", "Privacy"), ("/surfwindow/terms.html", "Terms")],
        "foot": [("/surfwindow/privacy.html", "Privacy Policy"), ("/surfwindow/privacy-ja.html", "プライバシーポリシー"),
                 ("/surfwindow/terms.html", "Terms of Service"), ("/surfwindow/terms-ja.html", "利用規約")],
    },
    "dailyallowance": {
        "name": "Daily Allowance",
        "icon": "/assets/apps/dailyallowance.png",
        "tabs": [("/dailyallowance/support.html", "Support"), ("/dailyallowance/privacy.html", "Privacy"),
                 ("/dailyallowance/terms.html", "Terms")],
        "foot": [("/dailyallowance/support.html", "Support"), ("/dailyallowance/privacy.html", "Privacy Policy"),
                 ("/dailyallowance/terms.html", "Terms of Service"), ("/dailyallowance/delete-account.html", "Delete your account")],
    },
    "strata": {
        "name": "Strata",
        "icon": "/assets/apps/strata.png",
        "tabs": [("https://stratabible.app/privacy", "Privacy"), ("https://stratabible.app/terms", "Terms")],
        "foot": [("https://stratabible.app/privacy", "Privacy Policy"), ("https://stratabible.app/terms", "Terms of Service")],
    },
}


def app_header(slug, name, icon, tabs, current):
    """One header: breadcrumb (studio / app) on the left, the app's links on the right."""
    links = "\n".join(
        '        <li><a href="%s"%s>%s</a></li>' % (href, ' aria-current="page"' if href == current else "", label)
        for href, label in tabs)
    here = ' aria-current="page"' if current == "/%s/" % slug else ""
    return (
        '<header class="site-header">\n'
        '  <div class="wrap bar">\n'
        '    <nav class="crumbs" aria-label="Breadcrumb">\n'
        '      <a class="brand" href="/"><img src="/assets/logo.svg" alt="" width="32" height="32">'
        '<span class="brand-text">SP Digital Labs</span></a>\n'
        '      <span class="crumb-sep" aria-hidden="true"><svg class="icon" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></span>\n'
        '      <a class="crumb-app" href="/%s/"%s><img src="%s" alt="" width="28" height="28">%s</a>\n'
        '    </nav>\n'
        '    <nav class="nav" aria-label="%s">\n'
        '      <ul>\n%s\n'
        '      </ul>\n'
        '    </nav>\n'
        '  </div>\n'
        '</header>' % (slug, here, icon, name, name, links))


def app_footer(name, foot):
    links = "\n".join('      <a href="%s">%s</a>' % (href, label) for href, label in foot)
    return (
        '<footer class="site-footer">\n'
        '  <div class="wrap foot-simple">\n'
        '    <p>&copy; 2026 SP Digital Labs, the name under which Joseph Suzuki-Parker publishes apps. Japan.</p>\n'
        '    <nav aria-label="%s links">\n%s\n'
        '      <a href="/#contact">Contact</a>\n'
        '    </nav>\n'
        '  </div>\n'
        '</footer>' % (name, links))


def head_tags(title, description, path, og_type="website", extra=""):
    """The shared <head> contents, from charset to stylesheet. extra goes before the stylesheet."""
    return f'''<meta charset="utf-8">
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


def page(slug, current, title, description, body, lang="en", main_class="wrap page"):
    """current is this page's path, e.g. "/understory/privacy.html"."""
    app = APPS[slug]
    name = app["name"]
    full_title = name if current == "/%s/" % slug else "%s - %s" % (title, name)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_tags(full_title, description, current)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

{app_header(slug, name, app["icon"], app["tabs"], current)}

<main id="main" class="{main_class}">
{body.strip()}
</main>

{app_footer(name, app["foot"])}
<script src="/email.js"></script>
</body>
</html>
'''


EMAIL = '<a class="email" href="/#contact">support [at] spdigitallabs [dot] app</a>'


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


def build_pages(root, slug, pages):
    """pages: {filename: (title, description, body, lang, main_class)}"""
    import os
    os.makedirs(f"{root}/{slug}", exist_ok=True)
    for fn, (title, desc, body, lang, main_class) in pages.items():
        current = f"/{slug}/" if fn == "index.html" else f"/{slug}/{fn}"
        open(f"{root}/{slug}/{fn}", "w").write(page(slug, current, title, desc, body, lang, main_class))


def feature_rows(items):
    """items: (img src, alt, heading, text). Each main feature beside its screenshot."""
    rows = "\n".join(
        f'''  <li class="feature-row">
    <div class="feature-shot"><img src="{src}" alt="{alt}" width="390" height="844" loading="lazy"></div>
    <div class="feature-copy"><h2>{h}</h2><p>{p}</p></div>
  </li>''' for src, alt, h, p in items)
    return f'<ul class="feature-rows">\n{rows}\n</ul>'
