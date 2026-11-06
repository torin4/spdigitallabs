"""The blog: /blog/ and /blog/<slug>.html. Posts live in blog_posts.py."""
import html
import json
import os
import re
from datetime import date

from chrome import head_tags
from icons import ARROW_RIGHT, EXTERNAL
from blog_posts import POSTS

SITE = "https://spdigitallabs.app"
AUTHOR = {"@type": "Person", "name": "Joseph Suzuki-Parker", "url": SITE + "/"}
BLOG_TITLE = "Blog"
BLOG_DESCRIPTION = "Guides from every SP Digital Labs app: everyday money, reading Genesis in its history, journaling, and surf in Shonan and Chiba."

# The hub lists every app's posts. Daily Allowance posts live here; the others
# live on their app's own site and are listed from external_posts.json
# (refresh it with fetch_blog_posts.py).
APP_GROUPS = [
    ("dailyallowance", "Daily Allowance", "/dailyallowance/", "Budgeting by the day", None),
    ("strata", "Strata", "/strata/", "Reading Genesis with its history", "stratabible.app"),
    ("understory", "Understory", "/understory/", "Journaling, privately", "understoryjournal.app"),
    ("surfwindow", "Surf Window", "/surfwindow/", "Surf guides for Shonan and Chiba, in Japanese", "surfwindow.jp"),
]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "external_posts.json")) as _f:
    EXTERNAL_POSTS = json.load(_f)


def nice_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def minutes(body):
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return max(1, round(words / 230))


def ld(data):
    return '<script type="application/ld+json">\n%s\n</script>\n' % json.dumps(data, ensure_ascii=False, indent=1)


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": name, "item": SITE + path}
        for i, (name, path) in enumerate(items, 1)]}


def header():
    return '''<header class="site-header">
  <div class="wrap bar">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a class="brand" href="/"><img src="/assets/logo.svg" alt="" width="32" height="32"><span class="brand-text">SP Digital Labs</span></a>
      <span class="crumb-sep" aria-hidden="true"><svg class="icon" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></span>
      <a class="crumb-app" href="/blog/">Blog</a>
    </nav>
  </div>
</header>'''


FOOTER = '''<footer class="site-footer">
  <div class="wrap foot-simple">
    <p>&copy; 2026 SP Digital Labs, the name under which Joseph Suzuki-Parker publishes apps. Japan.</p>
    <nav aria-label="Apps">
      <a href="/dailyallowance/">Daily Allowance</a>
      <a href="/strata/">Strata</a>
      <a href="/understory/">Understory</a>
      <a href="/surfwindow/">Surf Window</a>
      <a href="/blog/">Blog</a>
    </nav>
  </div>
</footer>'''


def document(title, description, path, body, og_type="website", extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
{head_tags(title, description, path, og_type, extra)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

{header()}

<main id="main" class="wrap">
{body.strip()}
</main>

{FOOTER}
<script src="/email.js"></script>
<script src="/motion.js"></script>
</body>
</html>
'''


def meta_line(post):
    return (f'<p class="post-meta"><time datetime="{post["date"]}">{nice_date(post["date"])}</time>'
            f'<span aria-hidden="true"> · </span>{minutes(post["body"])} min read</p>')


CTA = f'''<aside class="post-cta" aria-labelledby="cta-title">
  <div class="post-cta-text">
    <div class="post-cta-id"><img src="/assets/apps/dailyallowance.png" alt="" width="56" height="56"><span class="label">iPhone app</span></div>
    <h2 id="cta-title">Daily Allowance</h2>
    <p>Add your income and bills once. Daily Allowance turns them into one number for today and carries whatever you don't spend into tomorrow.</p>
    <a class="button" href="/dailyallowance/">See Daily Allowance{ARROW_RIGHT}</a>
  </div>
  <img class="post-cta-shot" src="/assets/screens/dailyallowance-home.jpg?v=2" alt="The Daily Allowance home screen with a Daily Balance of $96.33." width="390" height="844" loading="lazy">
</aside>'''


def post_page(post, others):
    path = f"/blog/{post['slug']}.html"
    title = f"{post['title']} - SP Digital Labs"
    article_ld = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": post["title"], "description": post["description"],
        "datePublished": post["date"], "dateModified": post.get("updated", post["date"]),
        "inLanguage": "en", "author": AUTHOR, "publisher": AUTHOR,
        "image": SITE + "/assets/og.png",
        "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + path},
        "about": {"@type": "SoftwareApplication", "name": "Daily Allowance", "operatingSystem": "iOS",
                  "applicationCategory": "FinanceApplication", "url": SITE + "/dailyallowance/"},
    }
    extra = (f'<meta property="article:published_time" content="{post["date"]}">\n'
             + ld(article_ld) + ld(crumbs_ld([("Home", "/"), ("Blog", "/blog/"), (post["title"], path)])))
    more = "\n".join(f'    <li><a href="/blog/{p["slug"]}.html">{p["title"]}</a></li>' for p in others)
    body = f'''<article class="post">
  <header class="post-head">
    <p class="label"><a href="/blog/">Blog</a></p>
    <h1>{post["title"]}</h1>
    {meta_line(post)}
  </header>
  {CTA}
  <div class="post-body">
{post["body"].strip()}
  </div>
  <nav class="post-more" aria-labelledby="more-title">
    <h2 id="more-title" class="label">More from the blog</h2>
    <ul>
{more}
    </ul>
  </nav>
</article>'''
    return path, document(title, html.escape(post["description"]), path, body, "article", extra)


def local_card(p):
    return f'''  <li>
    <a class="post-card" href="/blog/{p["slug"]}.html">
      <span class="post-card-meta"><time datetime="{p["date"]}">{nice_date(p["date"])}</time> · {minutes(p["body"])} min read</span>
      <span class="post-card-title">{p["title"]}</span>
      <span class="post-card-desc">{p["description"]}</span>
      <span class="post-card-go">Read{ARROW_RIGHT}</span>
    </a>
  </li>'''


def external_card(p, site):
    lang = f' lang="{p["lang"]}"' if p.get("lang", "en") != "en" else ""
    read = "Read in Japanese on" if p.get("lang") == "ja" else "Read on"
    return f'''  <li>
    <a class="post-card" href="{html.escape(p["url"])}" target="_blank" rel="noopener">
      <span class="post-card-meta">{site}</span>
      <span class="post-card-title"{lang}>{html.escape(p["title"])}</span>
      <span class="post-card-desc"{lang}>{html.escape(p["description"])}</span>
      <span class="post-card-go">{read} {site}{EXTERNAL}</span>
    </a>
  </li>'''


def index_page(posts):
    path = "/blog/"
    jump = []
    groups = []
    for slug, name, page, line, site in APP_GROUPS:
        cards = ([local_card(p) for p in posts] if site is None else
                 [external_card(p, site) for p in EXTERNAL_POSTS if p["app"] == slug])
        if not cards:
            continue
        jump.append(f'<a href="#{slug}">{name}</a>')
        groups.append(f'''<section class="blog-group" id="{slug}" aria-labelledby="{slug}-title">
  <header class="blog-group-head">
    <img src="/assets/apps/{slug}.png" alt="" width="48" height="48">
    <div>
      <h2 id="{slug}-title"><a href="{page}">{name}</a></h2>
      <p>{line}</p>
    </div>
  </header>
  <ul class="post-list">
{chr(10).join(cards)}
  </ul>
</section>''')
    blog_ld = {
        "@context": "https://schema.org", "@type": "Blog", "name": "SP Digital Labs Blog",
        "description": BLOG_DESCRIPTION, "url": SITE + path, "inLanguage": "en", "author": AUTHOR,
        "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "datePublished": p["date"],
                      "url": f"{SITE}/blog/{p['slug']}.html"} for p in posts]
                    + [{"@type": "BlogPosting", "headline": p["title"], "url": p["url"],
                        **({"datePublished": p["date"]} if p["date"] else {})} for p in EXTERNAL_POSTS],
    }
    extra = ld(blog_ld) + ld(crumbs_ld([("Home", "/"), ("Blog", path)]))
    body = f'''<section class="blog-intro" aria-labelledby="blog-title">
  <h1 id="blog-title">Blog</h1>
  <p class="lede">Guides and notes from every app: everyday money, reading Genesis with its history, journaling, and surfing in Shonan and Chiba. Written by Joseph Suzuki&#8209;Parker.</p>
  <nav class="blog-jump" aria-label="Jump to an app">{"".join(jump)}</nav>
</section>

<div class="blog-list">
{(chr(10)+chr(10)).join(groups)}
</div>'''
    return path, document("Blog - SP Digital Labs", BLOG_DESCRIPTION, path, body, "website", extra)


def build(root):
    os.makedirs(f"{root}/blog", exist_ok=True)
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    _, page = index_page(posts)
    open(f"{root}/blog/index.html", "w").write(page)
    for post in posts:
        others = [p for p in posts if p is not post]
        _, page = post_page(post, others)
        open(f"{root}/blog/{post['slug']}.html", "w").write(page)
