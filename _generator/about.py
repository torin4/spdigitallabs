"""The About page: /about/ (English) and /ja/about/ (Japanese).

Facts come from Joe's LinkedIn and Google Scholar profiles (checked 2026-11-06).
Keep the two languages saying the same things.
"""
import json
import os

from chrome import head_tags
from icons import EXTERNAL

SITE = "https://spdigitallabs.app"
SCHOLAR = "https://scholar.google.com/citations?user=CvWOL-0AAAAJ"
LINKEDIN = "https://www.linkedin.com/in/joseph-suzuki-parker-01a66a23/"

PERSON = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Joseph Suzuki-Parker",
    "alternateName": ["Joe Suzuki-Parker", "Joseph Torin Suzuki-Parker"],
    "url": SITE + "/about/",
    "image": SITE + "/assets/joe.jpg",
    "jobTitle": "English instructor and app developer",
    "worksFor": {"@type": "CollegeOrUniversity", "name": "Rissho University"},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "University of Birmingham"},
        {"@type": "CollegeOrUniversity", "name": "University of Colorado Boulder"},
    ],
    "knowsLanguage": ["en", "ja"],
    "sameAs": [SCHOLAR, LINKEDIN],
}

PAGES = {
    "en": {
        "path": "/about/",
        "alt_path": "/ja/about/",
        "title": "About Joseph Suzuki-Parker - SP Digital Labs",
        "description": "Joseph Suzuki-Parker is an English teacher and applied linguist in Japan who builds apps as SP Digital Labs. MA Applied Linguistics, University of Birmingham.",
        "home": "/",
        "crumb": "About",
        "skip": "Skip to content",
        "photo_alt": "Joseph Suzuki-Parker at sunset, in a cap and dark jacket.",
        "foot": "&copy; 2026 SP Digital Labs, the name under which Joseph Suzuki-Parker publishes apps. Japan.",
        "foot_links": [("/", "Apps"), ("/blog/", "Blog"), ("https://tevo.jp/", "Tevo")],
        "body": f'''
<h1>About</h1>
<p class="lede">SP Digital Labs is the name under which Joseph Suzuki-Parker publishes apps. Joe is an English teacher and applied linguist who builds software, based in Chiba, Japan.</p>

<h2>From music to languages</h2>
<p>Joe started out as a musician. He trained at the Military School of Music and served as a percussionist with the 3rd Infantry Division Band of the U.S. Army, including a deployment to Iraq. After the Army he studied Japanese at the University of Colorado Boulder, graduating with distinction in 2010, and soon after moved to Japan.</p>

<h2>Teaching and research</h2>
<p>He has taught English in Japan since 2011, from children's classes in Tsukuba to universities. He has taught at Rissho University since 2018, and before that at Dokkyo University, Tsukuba University of Technology and Nippon Institute of Technology. Along the way he worked as a translator and interpreter, and taught drums to children and adults.</p>
<p>In 2021 he completed an MA in Applied Linguistics at the University of Birmingham, with distinction. His research looks at how Japanese students learn vocabulary and how they use technology to study:</p>
<ul>
  <li>Independent use of Quizlet among Japanese EFL students: adoption rates, usage, and predictors. <i>CALL-EJ</i>, 2024 (with A. Duarte).</li>
  <li>Multimedia communications: Active English for medical science through short research-introduction videos. <i>Journal of Medical English Education</i>, 2023 (with T. Mayers).</li>
  <li>Does method of administration influence word association test responses? <i>Vocabulary Education Research Bulletin</i>, 2019 (with G. Higginbotham).</li>
</ul>

<h2>Building tools</h2>
<p>That classroom work led to <a href="https://tevo.jp/">Tevo</a>, an AI speaking-practice platform that turns English textbooks into conversations students can practise out loud. Joe co-founded it in 2023 with his brother Micah Parker and fellow teacher Hiro Iwama.</p>
<p>The apps here come from the same habit of building the tool he wishes already existed: <a href="/dailyallowance/">Daily Allowance</a> for knowing what you can spend today, <a href="/strata/">Strata</a> for reading the Bible with its history, <a href="/understory/">Understory</a> for private journaling, and <a href="/surfwindow/">Surf Window</a> for deciding when it's worth going surfing.</p>

<p class="about-links"><a href="{SCHOLAR}">Google Scholar{EXTERNAL}</a><a href="{LINKEDIN}">LinkedIn{EXTERNAL}</a><a href="/#contact">Get in touch</a></p>
''',
    },
    "ja": {
        "path": "/ja/about/",
        "alt_path": "/about/",
        "title": "Joseph Suzuki-Parker について - SP Digital Labs",
        "description": "Joseph Suzuki-Parker（ジョセフ・スズキ・パーカー）は、日本で英語を教える応用言語学の教員で、SP Digital Labs の名前でアプリを作っています。バーミンガム大学 応用言語学修士。",
        "home": "/ja/",
        "crumb": "紹介",
        "skip": "本文へ移動",
        "photo_alt": "夕日の中に立つ Joseph Suzuki-Parker。",
        "foot": "&copy; 2026 SP Digital Labs（Joseph Suzuki-Parker がアプリを公開する際の屋号）。日本。",
        "foot_links": [("/ja/", "アプリ"), ("/blog/", "ブログ"), ("https://tevo.jp/", "Tevo")],
        "body": f'''
<h1>紹介</h1>
<p class="lede">SP Digital Labs は、Joseph Suzuki-Parker がアプリを公開する際の屋号です。ジョーは千葉県在住の英語教員・応用言語学者で、ソフトウェアも作っています。</p>

<h2>音楽から言葉へ</h2>
<p>ジョーの出発点は音楽でした。米陸軍の軍楽学校で学び、第3歩兵師団軍楽隊の打楽器奏者としてイラクへの派遣も経験しました。除隊後はコロラド大学ボルダー校で日本語を専攻し、2010年に優秀な成績で卒業。その後まもなく日本に移りました。</p>

<h2>教育と研究</h2>
<p>2011年から日本で英語を教えています。つくばの子ども向けの教室から始まり、大学でも教えるようになりました。2018年からは立正大学で教え、これまでに獨協大学、筑波技術大学、日本工業大学でも教えてきました。その間、翻訳・通訳の仕事や、子どもから大人までのドラム指導もしてきました。</p>
<p>2021年にバーミンガム大学で応用言語学の修士号を取得しました（Distinction）。研究のテーマは、日本の学生の語彙学習と、学習へのテクノロジーの使い方です。</p>
<ul>
  <li lang="en">Independent use of Quizlet among Japanese EFL students: adoption rates, usage, and predictors. <i>CALL-EJ</i>, 2024 (with A. Duarte).</li>
  <li lang="en">Multimedia communications: Active English for medical science through short research-introduction videos. <i>Journal of Medical English Education</i>, 2023 (with T. Mayers).</li>
  <li lang="en">Does method of administration influence word association test responses? <i>Vocabulary Education Research Bulletin</i>, 2019 (with G. Higginbotham).</li>
</ul>

<h2>道具を作る</h2>
<p>教室での経験から生まれたのが <a href="https://tevo.jp/">Tevo</a> です。英語の教科書を、声に出して練習できる AI との会話に変えるスピーキング練習のプラットフォームで、2023年に兄弟の Micah Parker、同じく英語教員の Hiro Iwama と共同で立ち上げました。</p>
<p>ここにあるアプリも同じ発想から生まれています。あったらいいのに、と思った道具を自分で作る。今日使えるお金がわかる <a href="/dailyallowance/">Daily Allowance</a>、歴史を背景に聖書を読む <a href="/strata/">Strata</a>、プライベートな日記の <a href="/understory/">Understory</a>、そして海に行くべきかを判断する <a href="/surfwindow/">Surf Window</a> です。</p>

<p class="about-links"><a href="{SCHOLAR}">Google Scholar{EXTERNAL}</a><a href="{LINKEDIN}">LinkedIn{EXTERNAL}</a><a href="/ja/#contact">お問い合わせ</a></p>
''',
    },
}


def document(lang, p):
    alternates = (f'<link rel="alternate" hreflang="en" href="{SITE}/about/">\n'
                  f'<link rel="alternate" hreflang="ja" href="{SITE}/ja/about/">\n'
                  f'<link rel="alternate" hreflang="x-default" href="{SITE}/about/">\n')
    person = dict(PERSON, url=SITE + p["path"])
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "SP Digital Labs", "item": SITE + p["home"]},
        {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": SITE + p["path"]}]}
    ld = "".join('<script type="application/ld+json">\n%s\n</script>\n' % json.dumps(d, ensure_ascii=False, indent=1)
                 for d in (person, crumbs))
    other = "English" if lang == "ja" else "日本語"
    other_lang = "en" if lang == "ja" else "ja"
    foot_links = "\n      ".join(f'<a href="{href}">{label}</a>' for href, label in p["foot_links"])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_tags(p["title"], p["description"], p["path"], "profile", alternates)}
{ld}</head>
<body>
<a class="skip" href="#main">{p["skip"]}</a>

<header class="site-header">
  <div class="wrap bar">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a class="brand" href="{p["home"]}"><img src="/assets/logo.svg" alt="" width="32" height="32"><span class="brand-text">SP Digital Labs</span></a>
      <span class="crumb-sep" aria-hidden="true"><svg class="icon" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></span>
      <a class="crumb-app" href="{p["path"]}" aria-current="page">{p["crumb"]}</a>
    </nav>
    <nav class="nav" aria-label="Language">
      <ul><li><a href="{p["alt_path"]}" lang="{other_lang}" hreflang="{other_lang}">{other}</a></li></ul>
    </nav>
  </div>
</header>

<main id="main" class="wrap">
<article class="post about">
<img class="about-photo" src="/assets/joe.jpg" alt="{p["photo_alt"]}" width="540" height="720">
<div class="post-body">
{p["body"].strip()}
</div>
</article>
</main>

<footer class="site-footer">
  <div class="wrap foot-simple">
    <p>{p["foot"]}</p>
    <nav aria-label="Links">
      {foot_links}
    </nav>
  </div>
</footer>
<script src="/email.js"></script>
</body>
</html>
'''


def build(root):
    for lang, p in PAGES.items():
        out = os.path.join(root, p["path"].strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(document(lang, p))
