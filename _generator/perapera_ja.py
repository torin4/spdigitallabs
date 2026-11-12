"""PeraPera page in Japanese: /ja/perapera/. Translated from perapera.py; keep the two saying the same."""
from icons import EXTERNAL
from chrome import EMAIL_JA, hero, features, feature_rows

APP = "https://japanese-app-kappa.vercel.app"

OVERVIEW_JA = hero("perapera", "ウェブアプリ",
    "すでに日本語ができる人のための、日本語練習。",
    "PeraPera は、中上級からネイティブに近いレベル（CEFR B1〜C2）の大人の学習者に向けたアプリです。答えが表示される前に、すべての単語の読みを自分で入力します。さらに、AIのツールが使えます。自分のレベルに合わせて書かれる文章、声に出して話せる会話の相手、そして話した内容への詳しいフィードバックです。",
    f'<a class="button" href="{APP}/">PeraPera を開く' + EXTERNAL + '</a><span class="label">単語の復習は無料 · アカウント不要 · アプリは英語です</span>') + """

<section aria-label="主な機能">
""" + feature_rows([
    ("/assets/screens/perapera-review.jpg", "「田舎」という単語が例文とともに表示され、読みを入力する欄がある復習カード。", "まず、読みを入力する", "多くの単語アプリでは、選択肢から答えを選びます。PeraPera では自分で答えを出します。例文の中の単語を見て、意味が表示される前に、読みをひらがなで入力します。同じ単語が穴埋め問題や聞き取り問題としても出題されるので、ひとつの単語を複数の面から身につけられます。"),
    ("/assets/screens/perapera-level.jpg", "レベルチェックの結果画面。推定の読解レベルは C1+（上級の上）で、B1〜C1 は定着、C1+ が現在の境目、C2 はこれからと表示されています。", "2分で自分のレベルがわかる", "短いレベルチェックでは、単語がひとつずつ表示され、その読みを入力します。正解すると次はより難しい単語に、間違えるとよりやさしい単語になります。こうして、単語が難しくなり始めるレベルを見つけて CEFR の目安（B1〜C2）で示します。どのレベルが定着していて、どこがまだこれからなのかもわかります。復習は、その境目に集中します。いつでも受け直せます。"),
    ("/assets/screens/perapera-reader.jpg", "トピック、レベル、長さを指定する、多読の設定画面。", "AIが書く、自分のレベルの文章", "ニュース記事、昔話、ビジネスメールなど、読みたいものを伝えて、レベルと長さを選びます。AIがその場で文章を書くので、ちょうどよい難しさの新しい読み物がいつでもあります。単語をタップすると読みと意味が表示され、最後にいくつかの読解問題に答えます。"),
    ("/assets/screens/perapera-conversation.jpg", "連休の旅行について、AIが演じる同僚と日本語で話している会話画面。使った目標の単語に印が付き、文法の間違いを直すメモが表示されています。", "AIの会話パートナー", "好きな話題について、AIのパートナーと日本語で声に出して話します。ガイド付きの練習に取り組んだり、スピーキングテストを受けたりもできます。終わったあとには、AIがそのセッションを振り返ります。よくできた点、足りなかった点、見直したい文法、覚えておきたい単語がわかります。誰かとの実際の会話を録音すると、AIが文字に起こして、どうだったかを振り返ります。"),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">その他の機能</h2>
""" + features([('AIで調べる', '単語、文、字幕の一行を貼り付けると、AIが翻訳し、単語ごとに分解して説明します。単語をタップすれば復習に追加でき、自分で単語を入力して残りをAIに埋めてもらうこともできます。'),
    ('正直な数字', 'PeraPera が表示するのは、読みの正答率の推移です。連続記録はありません。'),
    ('すべての端末で', 'ログインすると、単語と進み具合がスマートフォンとパソコンで同期されます。')]) + f"""
</section>

<section aria-labelledby="plans-title">
  <h2 id="plans-title" class="section-title">プラン</h2>
  <div class="plans">
    <div class="plan"><h3>無料</h3><span class="price">無料</span><p>単語の復習とレベルチェックは、アカウントなしで使えます。無料のアカウントを作ると、読解と会話に使えるAIリクエストが1日5回付きます。</p></div>
    <div class="plan"><h3>PeraPera Pro</h3><span class="price">1,980円<small>／月</small></span><p>年額 19,800円もあります。フルサイズのAIモデルに加えて、毎月、AIリクエスト400回、音声150,000文字、文字起こし150分が含まれます。</p></div>
  </div>
  <p class="plans-note">料金は税込です。日本円で、Stripe を通じて請求されます。Pro は解約するまで自動で更新されます。いつでも解約でき、支払済みの期間の終了まではご利用いただけます。アプリの画面は英語です。</p>
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">ヘルプとポリシー</h2>
  <ul class="help-list">
    <li><a href="{APP}/privacy.html" hreflang="en">プライバシーポリシー（英語）</a></li>
    <li><a href="{APP}/terms.html" hreflang="en">利用規約（英語）</a></li>
    <li><a href="{APP}/tokushoho.html">特定商取引法に基づく表記</a></li>
    <li>お問い合わせ：{EMAIL_JA}</li>
  </ul>
</section>
"""

PAGES_JA = {
    "index.html": ("PeraPera", "上級者のための日本語練習。すべての単語の読みを入力し、AIが書く自分のレベルの文章を読み、フィードバックをくれるAIのパートナーと会話を練習できます。", OVERVIEW_JA, "ja", "wrap app-page"),
}
