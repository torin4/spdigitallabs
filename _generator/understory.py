from icons import EXTERNAL
from chrome import EMAIL, hero, features, shots, feature_rows, build_pages

PRIVACY = f'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: November 5, 2026</p>

<p>Understory is a private journaling web app at understoryjournal.app, made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what information Understory collects, why, who it is shared with, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> your journal entries are encrypted in your browser with a key only you hold, so we can't read them. If you use Premium and keep the companion on, the text of an entry is sent, unencrypted and only for that moment, to Google's Gemini AI service to write the companion's replies; our server doesn't keep a copy, and Google doesn't use it to train its models. A few results, such as an entry's mood and themes, are stored without that encryption so your growth rings can be drawn. We don't show ads, don't use analytics, and don't sell your data. Payments go through Stripe, and we never see your card.</p>
</div>

<h2>Information we collect</h2>

<h3>Your account</h3>
<ul>
  <li><strong>Email address</strong> and a <strong>user ID</strong> from Firebase Authentication, whether you sign up with an email and password or with Google.</li>
  <li>Your <strong>preferences</strong>, such as the companion's voice and where its words are drawn from, and when you finished setting up.</li>
  <li>We never see your sign-in password; Google Firebase handles it. If you sign up with email and password, that same password also unlocks your journal on your device (see below).</li>
</ul>

<h3>Your journal</h3>
<ul>
  <li><strong>Entries, notes ("spores") and the companion's memory ("heartwood")</strong> are encrypted in your browser before they are saved, with a key made from your passphrase. The key is also protected by a recovery code shown to you once. We only store the encrypted text and the protected key, so we can't read your writing, and we can't recover it if you lose both your passphrase and your recovery code.</li>
  <li>Some details about each entry are stored <strong>without</strong> that encryption so the app can work: when it was written and changed, its word count, whether it was typed or spoken, its season, and whether it is finished or archived.</li>
  <li>With Premium, each finished entry's <strong>mood reading</strong> is also stored without that encryption: its main mood and scores, up to five themes, and the reflection shown to you (a quotation and a short note). These draw your growth rings and stats.</li>
</ul>

<h3>The companion and other AI features (Premium)</h3>
<p>Premium's AI features use Google's Gemini models. <strong>Nothing is sent until you agree.</strong> The first time a Premium AI feature would run, the app explains what is sent and where, and asks for your consent; we record when you agreed. When they run, the text needed is decrypted in your browser and sent through our server to Google over an encrypted connection:</p>
<ul>
  <li><strong>When you finish an entry</strong>, its full text is sent to read its mood and, if the companion remembers is on, to update the companion's memory. This happens automatically when the companion is on.</li>
  <li><strong>When you ask the companion</strong> to reflect, tend, glean, seek or chat, the text you're working on is sent, with the conversation so far, the companion's memory, and up to three short passages from your earlier entries that your device picks as related.</li>
  <li><strong>Spelling check</strong> sends the text being checked.</li>
  <li><strong>Voice-to-text</strong> records audio in your browser and sends it to be transcribed. The audio is not saved.</li>
</ul>
<p>We use Gemini through Google Cloud's Vertex AI service. Under Google Cloud's terms, Google does not use what we send to train its models; it may process it briefly to detect abuse, as its terms describe. Our server passes these requests on and returns the answers to you. It does not store your text or audio. Entries you mark as windthrow are never added to the companion's memory. If you turn the companion off in Preferences, nothing about your entries is sent to the AI service, and your consent is withdrawn; turning it back on asks again.</p>
<p>We also keep a count of how many AI requests you make each month, to apply the monthly limit.</p>

<h3>Sharing links</h3>
<p>If you create a link to share entries, for example with a therapist, the entries you choose are encrypted with a new key that is part of the link itself. We store only the encrypted copy and when it expires. Anyone who has the link can read what you shared, so share it only with people you trust. You can set links to expire, and you can revoke a link at any time, which deletes our copy.</p>

<h3>Payments</h3>
<ul>
  <li>Premium is paid through <strong>Stripe</strong>. We send Stripe your email address and user ID so it can link the subscription to your account.</li>
  <li>We store your subscription's status, plan, renewal and trial dates, and Stripe's customer and subscription IDs.</li>
  <li>We never receive your card or payment details; Stripe handles them.</li>
</ul>

<h3>Safety check</h3>
<p>When you use the companion, our server checks the text for words that may suggest you are in crisis, and if it finds them, the app shows links to crisis helplines. This check isn't saved, and it isn't reported to anyone.</p>

<h3>Device and browser</h3>
<ul>
  <li><strong>Microphone:</strong> used only when you choose voice-to-text. Understory doesn't use your camera or location.</li>
  <li><strong>Stored in your browser:</strong> an offline copy of your journal data so the app works without a connection, encrypted drafts you haven't saved yet, and, if you set a device PIN, your journal key protected by that PIN.</li>
  <li>Understory has no analytics, advertising or tracking tools.</li>
  <li>The app loads its fonts from Google Fonts, so Google receives your IP address when the page loads.</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To run Understory: keep your journal in sync, draw your growth rings and stats, and keep your account secure.</li>
  <li>To produce the companion's replies, mood readings, transcriptions and spelling suggestions when Premium features run.</li>
  <li>To process your subscription and apply its limits.</li>
  <li>To answer your messages and requests.</li>
</ul>
<p>We don't use your information for advertising, and we don't sell it.</p>

<h2>Sensitive information and transfers abroad</h2>
<p>What you write may include sensitive personal information, such as your health or your religious beliefs, and your settings may show the tradition you'd like the companion to draw from. Under Japan's Act on the Protection of Personal Information, we only send this to the AI service, and only store mood readings, with your explicit consent, which you give in the app and can withdraw at any time.</p>
<p>Your data is processed by service providers in the United States (Google, Vercel and Stripe). The United States has no comprehensive federal privacy law equivalent to Japan's. These providers commit to protecting data under their own policies and contracts, linked below. By agreeing in the app, you consent to this transfer.</p>

<h2>Where it is stored</h2>
<p>Your data is stored in Google Firebase (Authentication and Cloud Firestore). The app and its server run on Vercel. These services may store and process data in the United States or other countries. Data is encrypted in transit and at rest, and your journal text is also encrypted with your own key as described above.</p>

<h2>Who we share it with</h2>
<p>We share information only with the services that run Understory:</p>
<ul>
  <li><strong>Google</strong>: Firebase stores your account and data, and Google Cloud's Vertex AI runs the Gemini models behind Premium's AI features. <a href="https://firebase.google.com/support/privacy">Firebase privacy</a> · <a href="https://cloud.google.com/terms/data-processing-addendum">Google Cloud data processing terms</a></li>
  <li><strong>Vercel</strong>, which hosts the app and runs its server. <a href="https://vercel.com/legal/privacy-policy">Vercel privacy</a></li>
  <li><strong>Stripe</strong>, which handles payments for Premium. <a href="https://stripe.com/privacy">Stripe privacy</a></li>
  <li>Anyone you give a sharing link to can read the entries in it.</li>
</ul>
<p>We may also disclose information if the law requires it.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Your account, journal and mood readings are kept until you delete them or your account.</li>
  <li>Sharing links are kept until they expire or you revoke them.</li>
  <li>Monthly AI usage counts are kept until you delete your account.</li>
  <li>Stripe keeps payment records as the law requires.</li>
</ul>

<h2>Your choices and rights</h2>
<ul>
  <li>Turn the companion, its memory, and voice-to-text on or off in Preferences. Turning the companion off withdraws your consent to the AI service.</li>
  <li>Delete an entry from your journal; this also deletes its mood reading.</li>
  <li>Read, edit or clear the companion's memory in Preferences.</li>
  <li>Save entries as a PDF from the app.</li>
  <li>Revoke any sharing link.</li>
  <li>Delete your account in Preferences &gt; Account &gt; Delete account. This permanently deletes your account, your journal, notes, mood readings, the companion's memory, your sharing links and your AI usage counts, cancels any Premium subscription, and clears Understory's data from that browser. If you can't sign in, email us from the address on your account and we will delete it within 30 days.</li>
  <li>Depending on where you live, you may have further rights, such as to see, correct or object to how we use your information, or to complain to a data protection authority. Contact us and we will help.</li>
</ul>

<h2>Children</h2>
<p>Understory is not directed at children under 13, and we don't knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top. For significant changes, we will also tell you in the app.</p>

<h2>Contact</h2>
<p>Questions or requests about your privacy: {EMAIL}</p>
'''

TERMS = f'''
<h1>Terms of Service</h1>
<p class="updated">Last updated: November 5, 2026</p>

<p>These terms apply to your use of Understory, a journaling web app made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). By creating an account or using Understory, you agree to these terms. If you don't agree, please don't use it.</p>

<div class="card">
  <p><strong>The short version:</strong> Understory is a journal, not therapy or medical care. Your entries are encrypted with a key only you hold, so keep your passphrase and recovery code safe; we can't recover them. Journaling is free. Premium is a subscription billed by Stripe that renews until you cancel, and you can ask us for a refund. Its AI replies can be wrong. Your writing belongs to you, and you can delete your account at any time.</p>
</div>

<h2>Who can use Understory</h2>
<p>You must be at least 13 years old to use Understory. If you are under the age of majority where you live, you need a parent or guardian's permission, including to buy Premium.</p>

<h2>Your account and your key</h2>
<ul>
  <li>You sign in with an email address and password, or with Google. Keep your sign-in details secure; you are responsible for activity on your account.</li>
  <li>Your journal is encrypted with a key protected by your passphrase and by a recovery code shown to you once. Keep both safe. If you lose both, your encrypted entries can't be recovered, by you or by us.</li>
  <li>Tell us right away if you think someone else has used your account.</li>
  <li>You can delete your account at any time in Preferences &gt; Account &gt; Delete account. This can't be undone and cancels any Premium subscription.</li>
</ul>

<h2>Not therapy or medical care</h2>
<p>Understory is a place to write and reflect. The companion, mood readings and reflections are not therapy, counselling, or medical or mental health advice, and they are not a substitute for care from a qualified professional. If you are in crisis or thinking about harming yourself, contact local emergency services or a crisis line straight away; the app links to <a href="https://findahelpline.com">findahelpline.com</a>.</p>

<h2>Premium</h2>
<ul>
  <li>Journaling is free. Premium is an optional subscription that adds the companion and its memory, mood readings and growth rings, voice-to-text and spelling check.</li>
  <li>Premium costs US$9.99 a month or US$89 a year. Prices are shown in the app before you buy, and your card issuer may convert them to your currency. Any taxes are shown at checkout.</li>
  <li>New subscribers get a 14-day free trial. You won't be charged if you cancel before it ends.</li>
  <li>Payment is handled by Stripe. Your subscription renews automatically at the end of each period until you cancel. Cancel any time in Preferences &gt; Account; you keep Premium until the end of the period you've paid for.</li>
  <li>To ask for a refund, email us from the address on your account. Refunds are paid through Stripe to the card you paid with and usually appear within 5 to 10 business days, depending on your bank.</li>
  <li>We may change Premium's features or prices. A price change won't affect a period you have already paid for, and we will tell you before a higher price applies to your renewal.</li>
</ul>

<h2>AI features</h2>
<ul>
  <li>Premium's AI features are produced by Google's Gemini models from the text sent to them, as described in our <a href="/understory/privacy.html">Privacy Policy</a>.</li>
  <li>AI replies can be incomplete, inaccurate or unsuitable. Use your own judgement about them.</li>
  <li>AI features have a monthly limit, currently 300 requests a month, or 100 during the free trial. Spelling check and voice-to-text don't count toward it. We may change these limits to keep the service sustainable.</li>
</ul>

<h2>Sharing links</h2>
<p>If you share entries with a link, anyone who has the link can read them until it expires or you revoke it. You are responsible for who you share it with and for what you share.</p>

<h2>Your writing</h2>
<p>Everything you write in Understory belongs to you. You give us permission to store, sync and process it only as needed to run the app for you, as described in our Privacy Policy.</p>

<h2>Acceptable use</h2>
<p>Please don't:</p>
<ul>
  <li>use Understory for anything unlawful;</li>
  <li>try to get around Premium checks, AI limits or other restrictions;</li>
  <li>access other people's data without permission, or interfere with the app or its servers;</li>
  <li>copy, resell or reverse engineer Understory, except where the law allows it.</li>
</ul>
<p>We may suspend or close an account that breaks these terms. Where reasonable, we will tell you first and give you a chance to fix the problem.</p>

<h2>Changes and availability</h2>
<p>We work to keep Understory running, but we can't promise it will always be available or free of errors. We may update, change or stop parts of it. If we stop offering Understory or Premium, we will give reasonable notice where we can, so you can save your entries.</p>

<h2>Disclaimer and limit of liability</h2>
<p>To the extent the law allows, Understory is provided "as is", and we are not liable for indirect or consequential losses, or for lost entries you can no longer decrypt. Our total liability to you is limited to the amount you paid for Premium in the 12 months before the claim. Nothing in these terms limits liability for our intentional misconduct or gross negligence, or any rights you have under consumer protection laws that can't be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Japan. If you are a consumer, you also keep the protection of any mandatory laws of the country where you live.</p>

<h2>Changes to these terms</h2>
<p>If we change these terms, we will update the date at the top. For significant changes, we will also tell you in the app. If you keep using Understory after a change, the new terms apply.</p>

<h2>Contact</h2>
<p>Questions about these terms: {EMAIL}</p>
'''


OVERVIEW = hero("understory", "Web app",
    "A quiet journal for the slow work beneath the surface.",
    "Understory is a private journal for grief, change, ordinary days, and everything that doesn't resolve on a schedule. Your entries are encrypted in your browser with a key only you hold. With Premium, a gentle companion helps you reflect, and every entry you keep grows a ring.",
    '<a class=\"button\" href=\"https://understoryjournal.app/\">Open Understory' + EXTERNAL + '</a><span class="label">Free to start · Works in any browser</span>') + f"""

<section aria-label="Main features">
""" + feature_rows([
    ("/assets/screens/understory-dashboard.jpg", "Understory dashboard with a button to lay down a ring, spores and recent entries.", "Private by design", "Every entry is encrypted in your browser before it's saved. Your passphrase and a one-time recovery code are the only keys, so no one else can read your journal, including us."),
    ("/assets/screens/understory-companion.jpg", "An entry with the companion's Root question below it and the writer's reply.", "A companion that waits to be asked", "With Premium, the companion answers only when you ask. Root asks you one question, Tend walks through a thought in four steps, Glean offers a short passage, and Seek answers briefly."),
    ("/assets/screens/understory-reflection.jpg", "A reflection card with a short Emily Dickinson passage and a gentle note.", "A word to sit with", "When you keep an entry, Understory reads its mood and offers a short passage and a few words for you, from secular or Christian sources, or both."),
    ("/assets/screens/understory-rings.jpg", "Growth rings drawn like a tree's cross-section, with frequent moods and themes.", "Every entry grows a ring", "Your entries become rings, drawn like a tree's cross-section, oldest at the heart. With Premium each ring takes its entry's mood, and your most frequent moods and themes appear beside it."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([('Seasons for hard stretches', "Mark an entry fallow, a nurse log for a loss, or windthrow for venting you don't want to keep."),
    ('Heartwood, its memory', 'The companion can keep one encrypted remembering of your journal. Read it, edit it or clear it.'),
    ('Share with someone you trust', 'Send chosen entries to a therapist or friend with an encrypted link that can expire.'),
    ('Speak instead of typing', 'With Premium, dictate an entry and check its spelling without changing your words.')]) + f"""
</section>

<section aria-labelledby="plans-title">
  <h2 id="plans-title" class="section-title">Plans</h2>
  <div class="plans">
    <div class="plan"><h3>Journal</h3><span class="price">Free</span><p>Encrypted entries, growth rings, seasons, spores, sharing links and PDF export.</p></div>
    <div class="plan"><h3>Premium</h3><span class="price">US$9.99<small> / month</small></span><p>Or US$89 a year. Adds the companion and its memory, mood colors, voice-to-text and spelling check. 14 days free, cancel anytime.</p></div>
  </div>
  <p class="plans-note">Understory is a journal, not therapy. If you're in crisis, contact local emergency services or a crisis line.</p>
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/understory/privacy.html">Privacy Policy</a></li>
    <li><a href="/understory/terms.html">Terms of Service</a></li>
    <li><a href="/understory/legal-notice.html">特定商取引法に基づく表記</a> (legal notice for purchases)</li>
    <li>Delete your account in Preferences &gt; Account &gt; Delete account.</li>
    <li>Questions or refunds: {EMAIL}</li>
  </ul>
</section>
"""

LEGAL_ROWS = [
    ("販売業者", "Seller", "Joseph Suzuki-Parker（屋号：SP Digital Labs）", "Joseph Suzuki-Parker, trading as SP Digital Labs"),
    ("運営責任者", "Person responsible", "Joseph Suzuki-Parker", "Joseph Suzuki-Parker"),
    ("所在地", "Address", "請求があった場合には、遅滞なく開示いたします。", "Provided without delay on request."),
    ("電話番号", "Phone", "請求があった場合には、遅滞なく開示いたします。お問い合わせはメールでお願いいたします。", "Provided without delay on request. Please contact us by email."),
    ("メールアドレス", "Email", '<a class="email" href="/#contact">support [at] spdigitallabs [dot] app</a>', '<a class="email" href="/#contact">support [at] spdigitallabs [dot] app</a>'),
    ("サービス名", "Service", "Understory Premium（ウェブアプリ「Understory」の有料サブスクリプション）", "Understory Premium, a subscription for the Understory web app"),
    ("販売価格", "Price", "月額プラン：US$9.99／月<br>年額プラン：US$89／年<br>お申し込み前に購入画面に表示されます。", "Monthly: US$9.99 a month<br>Yearly: US$89 a year<br>Shown on the checkout screen before you buy."),
    ("商品代金以外の必要料金", "Other charges", "インターネット接続にかかる通信料金はお客様のご負担となります。日本円以外の通貨でお支払いの場合、カード会社所定の為替レート・手数料が適用されることがあります。", "Internet connection charges are yours. If your card is in another currency, your card issuer's exchange rate and fees may apply."),
    ("支払方法", "Payment method", "クレジットカード・デビットカード（決済代行：Stripe）", "Credit or debit card, processed by Stripe"),
    ("支払時期", "When you pay", "無料体験期間（14日間）の終了時に初回のお支払いが発生し、以降は各契約期間の開始時に自動で請求されます。", "The first charge is made when the 14-day free trial ends, then automatically at the start of each billing period."),
    ("提供時期", "When the service starts", "お申し込み手続きの完了後、直ちにご利用いただけます。", "Immediately after you complete checkout."),
    ("自動更新・解約", "Renewal and cancellation", "契約は解約されるまで自動で更新されます。アプリの「設定 &gt; アカウント」からいつでも解約でき、解約後も支払済みの期間の終了まではご利用いただけます。無料体験期間中に解約された場合、料金は発生しません。", "Your subscription renews automatically until you cancel. Cancel any time in Preferences &gt; Account; you keep Premium until the end of the period you've paid for. Cancelling during the free trial means you aren't charged."),
    ("返金", "Refunds", "返金をご希望の場合は、アカウントのメールアドレスから上記メールアドレスまでご連絡ください。返金はStripeを通じて、お支払いに使用されたカードへ行います。", "To ask for a refund, email us from the address on your account. Refunds are paid through Stripe to the card you paid with."),
    ("動作環境", "Requirements", "最新版のChrome、Safari、Edge、Firefoxなど、主要なウェブブラウザ。インターネット接続が必要です。", "A current version of a major web browser, such as Chrome, Safari, Edge or Firefox, and an internet connection."),
]

def legal_body():
    ja = "\n".join(f"    <tr><th scope=\"row\">{a}</th><td>{c}</td></tr>" for a, _, c, _ in LEGAL_ROWS)
    en = "\n".join(f"    <tr><th scope=\"row\">{b}</th><td>{d}</td></tr>" for _, b, _, d in LEGAL_ROWS)
    return f'''
<h1>特定商取引法に基づく表記</h1>
<p class="updated">最終更新日：2026年11月5日</p>
<p>Understory Premium の販売に関する、特定商取引法に基づく表記です。</p>
<div class="table-scroll">
<table>
  <tbody>
{ja}
  </tbody>
</table>
</div>

<h2 lang="en">Legal notice (English)</h2>
<p lang="en">The seller details for Understory Premium required by Japan's Act on Specified Commercial Transactions. The Japanese version above is the official one.</p>
<div class="table-scroll" lang="en">
<table>
  <tbody>
{en}
  </tbody>
</table>
</div>
'''


PAGES = {
    "index.html": ("Understory", "A private, encrypted journal with an optional reflective companion. Free to start.", OVERVIEW, "en", "wrap app-page"),
    "privacy.html": ("Privacy Policy", "How Understory collects, uses and protects your information.", PRIVACY, "en", "wrap page"),
    "terms.html": ("Terms of Service", "The terms for using Understory and Understory Premium.", TERMS, "en", "wrap page"),
    "legal-notice.html": ("特定商取引法に基づく表記", "Understory Premium の特定商取引法に基づく表記。", legal_body(), "ja", "wrap page"),
}

def build(root):
    build_pages(root, "understory", PAGES)
