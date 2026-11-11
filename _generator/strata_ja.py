from icons import EXTERNAL
from chrome import EMAIL_JA, hero, features, feature_rows

OVERVIEW_JA = hero("strata", "ウェブアプリ",
    "聖書を、それが生まれた歴史とともに読む。",
    "Strata は、すべての箇所を4つの層で開く聖書通読アプリです。当時それが何を意味していたか、いつの時代にも伝えていること、いまのあなたにどう語りかけるか、そしてあなたが答える問い。まずは創世記から、「ムーブメント」と日々の通読に分けて読み進めます。",
    '<a class="button" href="https://stratabible.app/">Strata を開く' + EXTERNAL + '</a><span class="label">創世記1〜11章は無料 · アカウント不要 · アプリは英語です</span>') + """

<section aria-label="主な機能">
""" + feature_rows([
    ("/assets/screens/strata-home.jpg", "創世記と出エジプト記が並ぶ Strata のホーム画面。", "ムーブメントごとに読むライブラリ", "Strata では、聖書の各書を短い日々の通読で読み進めます。通読は「ムーブメント」と呼ぶ大きなまとまりに分かれています。各ムーブメントは場面を示す導入で始まり、全体をまとめる締めくくりで終わるので、物語のどこにいるのかをいつでも把握できます。まずは創世記から始まり、ほかの書も公開され次第追加されます。"),
    ("/assets/screens/strata-history.jpg", "バビロン捕囚についての歴史の層から始まる、創世記1章の通読。", "すべての箇所の背景にある歴史", "どの通読も、まず歴史から始まります。誰がその箇所を書いたのか、いつ書かれたのか、最初にそれを聞いた人々に何が起きていたのか。捕囚や戦争のさなかに語られた物語だと知ると、読み方が変わります。Strata は出典を示し、研究者の見解を、長い引用ではなく平易な言葉でまとめます。"),
    ("/assets/screens/strata-turn.jpg", "通読の「意味」と「転換」の層。最後に答える問いがあります。", "意味、転換、そしてあなたの応答", "歴史のあとに、さらに3つの段階があります。まず、その箇所がどの時代の読者にとっても持ってきた意味。次に「転換」として、いまのあなたの生活にどう語りかけるか。最後に、あなた自身の言葉で答える問い。聖書の中に異なる声や解決されない緊張があるところでは、Strata はそれを整った教訓にまとめず、そのまま誠実に示します。"),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">その他の機能</h2>
""" + features([('すべての通読にコンパニオン', 'Strata Plus では、AIのコンパニオンが通読ごとに意味と転換、そして問いを、あなたに合わせて引き出します。'),
    ('メモを同期', 'ログインすると、ハイライト、メモ、応答をすべての端末で使えます。'),
    ('パブリックドメインの本文', '聖書本文は、パブリックドメインの Berean Standard Bible（英語）です。')]) + f"""
</section>

<section aria-labelledby="plans-title">
  <h2 id="plans-title" class="section-title">プラン</h2>
  <div class="plans">
    <div class="plan"><h3>無料</h3><span class="price">無料</span><p>原初史（創世記1〜11章）はどなたでも読めます。ログインすると、コンパニオンを1回無料で使えます。</p></div>
    <div class="plan"><h3>Strata Plus</h3><span class="price">US$6.99<small>／月</small></span><p>年額 US$49 もあります。創世記のすべて、今後公開されるすべての書、すべての通読でのコンパニオン、メモの同期が含まれます。</p></div>
  </div>
  <p class="plans-note">1冊ずつ買い切りで購入することもできます（例：創世記 US$14.99）。料金は米ドルで、Stripe を通じて請求されます。Plus はいつでも解約でき、支払済みの期間の終了まではご利用いただけます。</p>
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">ヘルプとポリシー</h2>
  <ul class="help-list">
    <li><a href="https://stratabible.app/privacy" hreflang="en">プライバシーポリシー（英語）</a></li>
    <li><a href="https://stratabible.app/terms" hreflang="en">利用規約（英語）</a></li>
    <li><a href="https://stratabible.app/pricing" hreflang="en">料金（英語）</a></li>
    <li>お問い合わせ：{EMAIL_JA}</li>
  </ul>
</section>
"""

PAGES_JA = {
    "index.html": ("Strata", "すべての箇所を、その歴史、意味、そしていまあなたに問いかけることとともに読む聖書通読アプリ。", OVERVIEW_JA, "ja", "wrap app-page"),
}
