"""Calorie Count page in Japanese: /ja/caloriecount/. Translated from caloriecount.py; keep the two saying the same."""
from chrome import EMAIL_JA, hero, features

SITE = "https://calorie-count-hw.web.app"

OVERVIEW_JA = hero("caloriecount", "近日公開",
    "カロリー計算を、ひとつの数字で。",
    "Calorie Count は、食べたカロリーと消費するカロリーを比べて、その差を表示します。食事の写真を撮ると、AIがカロリーを見積もります。表示するのは、その数字だけです。",
    '<span class="label">App Store と Google Play で近日公開</span>') + """

<section aria-labelledby="what-title">
  <h2 id="what-title" class="section-title">できること</h2>
""" + features([
    ('写真からAIが見積もる', '食事の写真を撮るか、食べたものを短い言葉で入力すると、AIがカロリーを見積もります。数字を自分で入力することもできます。'),
    ('消費カロリーは自動で計算', '最初に一度、自分のことを入力します。体格、歩数、運動から、1日に消費するカロリーを計算します。歩数と体重は、Apple ヘルスケアやヘルスコネクトから取り込めます。'),
    ('自分の体重で確かめる', '食事と体重を2週間記録すると、計算した数字を自分の記録と照らし合わせます。'),
    ('画面には数字がひとつ', 'メインの画面には、今日どれだけ下回っているか、上回っているかが表示されます。2週間の画面では、日ごとの差の合計を体重と並べて見られます。'),
    ('記録はスマートフォンの中に', '記録はすべてスマートフォンに保存され、オフラインでも使えます。バックアップしたいときや、別のスマートフォンで使いたいときだけログインします。広告はありません。'),
    ('無料で使える', 'カロリーを自分で入力するのは、いつでも無料で回数の制限もありません。AIの見積もりは1日1回使えます。Premium にすると、1日の回数の制限がなくなります。'),
]) + f"""
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">ヘルプとポリシー</h2>
  <ul class="help-list">
    <li><a href="{SITE}/privacy" hreflang="en">プライバシーポリシー（英語）</a></li>
    <li><a href="{SITE}/terms" hreflang="en">利用規約（英語）</a></li>
    <li>表示される数字は目安であり、医療上の助言ではありません。</li>
    <li>お問い合わせ：{EMAIL_JA}</li>
  </ul>
</section>
"""

PAGES_JA = {
    "index.html": ("Calorie Count", "カロリー計算を、ひとつの数字で。食べた分と消費する分の差を表示します。食事の写真からAIがカロリーを見積もります。iPhone と Android で近日公開。", OVERVIEW_JA, "ja", "wrap app-page"),
}
