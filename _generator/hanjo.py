from icons import EXTERNAL
from chrome import EMAIL, hero, features, feature_rows_wide, build_pages

UPDATED = "November 11, 2026"
UPDATED_JA = "2026年11月11日"

PRIVACY = f'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: {UPDATED}</p>

<p>Hanjo is a house design web app at hanjo.app, made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what information Hanjo collects, why, who it is shared with, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> your designs are saved in your browser and, when you're signed in, to your account so you can open them on other devices. If you use the AI designer, the design you're working on and what you ask are sent to Anthropic's Claude AI service to produce its changes; Anthropic doesn't use it to train its models. Designs you share can be seen by the people you share them with. We don't show ads, don't use analytics, and don't sell your data. The AI plan is sold through Stripe, and we never see your card.</p>
</div>

<h2>Information we collect</h2>

<h3>Your account</h3>
<ul>
  <li><strong>Email address</strong> and a <strong>user ID</strong>, whether you sign in with Google or with an email address and password.</li>
  <li>If you sign in with Google, Google also gives us your <strong>name</strong> and <strong>profile picture</strong>. We don't show them to anyone.</li>
  <li>We never see your password; our sign-in provider, Supabase, stores only a secure hash of it.</li>
</ul>

<h3>Your designs</h3>
<ul>
  <li><strong>Your workspace:</strong> your house design (site, floors, walls, rooms, doors and windows, stairs, roof, finishes, furniture and landscaping), the history of edits that produced it, saved versions and proposals.</li>
  <li><strong>Traced drawings:</strong> images or PDF pages you import to trace over.</li>
  <li>These are stored in your browser. When you're signed in, a copy is also saved to your account so it can be opened on your other devices.</li>
  <li>A design may show your plot's size, shape and orientation. It doesn't need your address, and we don't ask for it.</li>
</ul>

<h3>Sharing and comments</h3>
<ul>
  <li>When you share a design, we store a copy of it, the email addresses of the people you invite and their roles, and the comments people leave, each with the commenter's email address.</li>
  <li>For view-only links, we store only a scrambled (hashed) form of the link's code, its expiry date, and whether you revoked it.</li>
</ul>

<h3>The AI designer</h3>
<p>When you send a request to the AI designer, our server sends Anthropic's Claude AI service, over an encrypted connection:</p>
<ul>
  <li>the design you're working on, as it stands;</li>
  <li>your request, the earlier messages in that conversation, and what you have selected or marked on the plan;</li>
  <li>which language you use.</li>
</ul>
<p>Claude's changes come back as ordinary edits to your design. Under Anthropic's commercial terms, Anthropic does not use what we send to train its models; it may keep it for a limited time to detect misuse, as its terms describe. Our server passes the request on and doesn't keep the conversation. For each request we record which model was used, how many tokens it used, what it cost and when, to apply your plan's allowance.</p>

<h3>Payments</h3>
<ul>
  <li>The AI plan is sold through Stripe's Managed Payments, with Link, part of the Stripe group, as the seller of record. Stripe and Link receive your payment details directly; we never do.</li>
  <li>We send Stripe your email address and user ID so the subscription is linked to your account, and we store Stripe's customer and subscription IDs, the subscription's status, and its billing period.</li>
</ul>

<h3>Device and browser</h3>
<ul>
  <li><strong>Stored in your browser:</strong> your designs and traced drawings, view settings such as the 3D options and the time of day, and your sign-in session.</li>
  <li>Hanjo has no analytics, advertising or tracking tools, and its fonts are served from hanjo.app itself.</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To run Hanjo: save your designs, open them on your devices, and keep your account secure.</li>
  <li>To share designs and comments with the people you choose.</li>
  <li>To produce the AI designer's changes when you ask for them, and to apply your plan's allowance.</li>
  <li>To process your subscription.</li>
  <li>To answer your messages and requests.</li>
</ul>
<p>We don't use your information for advertising, and we don't sell it.</p>

<h2>Where it is stored, and transfers abroad</h2>
<p>Your account, designs, shared copies and comments are stored with Supabase in its Tokyo region. The app and its server run on Vercel, whose servers may be in the United States or other countries. AI requests are processed by Anthropic in the United States. Payments are processed by Stripe, which may process data in the United States and other countries. The United States has no comprehensive federal privacy law equivalent to Japan's; these providers commit to protecting data under their own policies and contracts, linked below. Data is encrypted in transit and at rest.</p>

<h2>Who we share it with</h2>
<p>We share information only with the services that run Hanjo:</p>
<ul>
  <li><strong>Supabase</strong>, which stores your account and designs and handles sign-in. <a href="https://supabase.com/privacy">Supabase privacy</a></li>
  <li><strong>Vercel</strong>, which hosts the app and runs its server. <a href="https://vercel.com/legal/privacy-policy">Vercel privacy</a></li>
  <li><strong>Anthropic</strong>, which runs the Claude models behind the AI designer. <a href="https://www.anthropic.com/legal/privacy">Anthropic privacy</a></li>
  <li><strong>Stripe and Link</strong>, which sell and bill the AI plan. <a href="https://stripe.com/privacy">Stripe privacy</a> · <a href="https://link.com/privacy">Link privacy</a></li>
  <li><strong>Google</strong>, if you choose to sign in with it. <a href="https://policies.google.com/privacy">Google privacy</a></li>
  <li>The people you share a design with, or give a view-only link to, can see that design, and members can see each other's comments and email addresses.</li>
</ul>
<p>We may also disclose information if the law requires it.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Your account and designs are kept until you delete them or your account.</li>
  <li>Shared copies, comments and invitations are kept until you stop sharing the design; view-only links until they expire or you revoke them.</li>
  <li>AI usage records are kept until you delete your account.</li>
  <li>Stripe and Link keep payment records as the law requires.</li>
</ul>

<h2>Your choices and rights</h2>
<ul>
  <li>Stop sharing a design at any time; this deletes the shared copy, its comments and its links.</li>
  <li>Use Hanjo without the AI designer; nothing is sent to Anthropic unless you send a request.</li>
  <li>To delete your account and everything stored with it, email us from the address on your account and we will delete it within 30 days. Any AI plan is cancelled at the same time.</li>
  <li>Depending on where you live, you may have further rights, such as to see, correct or object to how we use your information, or to complain to a data protection authority. Contact us and we will help.</li>
</ul>

<h2>Children</h2>
<p>Hanjo is not directed at children under 13, and we don't knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top. For significant changes, we will also tell you in the app.</p>

<h2>Contact</h2>
<p>Questions or requests about your privacy: {EMAIL}</p>
'''

TERMS = f'''
<h1>Terms of Service</h1>
<p class="updated">Last updated: {UPDATED}</p>

<p>These terms apply to your use of Hanjo, a house design web app made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). By creating an account or using Hanjo, you agree to these terms. If you don't agree, please don't use it.</p>

<div class="card">
  <p><strong>The short version:</strong> Hanjo helps you plan a house; it is not an architect, and its plans, checks and cost estimates are not professional advice. Have a licensed architect (建築士) or builder check any design before you rely on it. Designing, 3D and sharing are free. The AI plan is a monthly subscription sold through Stripe that renews until you cancel. Its AI can make mistakes. Your designs belong to you.</p>
</div>

<h2>Who can use Hanjo</h2>
<p>You must be at least 13 years old to use Hanjo. If you are under the age of majority where you live, you need a parent or guardian's permission, including to buy the AI plan.</p>

<h2>Your account</h2>
<ul>
  <li>You sign in with Google, or with an email address and password. Keep your sign-in details secure; you are responsible for activity on your account.</li>
  <li>Tell us right away if you think someone else has used your account.</li>
  <li>To delete your account, email us from the address on your account.</li>
</ul>

<h2>Not professional advice</h2>
<p>Hanjo is a planning and visualisation tool. Its drawings, areas, building-regulation checks (such as coverage ratio, floor area ratio, setbacks and slant-line limits), sunlight study, door-clearance checks and rough cost estimates are simplified, may be incomplete or wrong, and don't account for every rule, local ordinance or site condition. They are not architectural, structural, legal or financial advice, and they don't replace a licensed architect (建築士), a builder, or a building confirmation application (確認申請). Check everything with qualified professionals before you buy land, sign a contract or build.</p>

<h2>The AI plan</h2>
<ul>
  <li>Designing, 3D views, the walk-through, printing and sharing are free. Every account gets a small amount of free AI designer use, once.</li>
  <li>The AI plan costs 1,980 yen a month, including tax, and is shown at checkout before you pay. If you pay in another currency, Stripe or your card issuer may convert the price.</li>
  <li>The plan includes a monthly allowance of AI designer use, measured by what the AI requests cost us to run, currently up to the equivalent of US$8 per billing month. The app shows how much is left. Unused allowance doesn't carry over. If the allowance runs out during a request, the AI stops and keeps what it has drawn so far. To keep the service available to everyone, we may also limit how much the AI designer is used across all accounts in a day.</li>
  <li>The plan is sold through Stripe's Managed Payments, with Link, part of the Stripe group, as the seller of record. Your receipts and card statement will show Link.</li>
  <li>Your subscription renews automatically each month until you cancel. Cancel any time from Manage plan in the app or from your Link account; you keep the plan until the end of the period you've paid for.</li>
  <li>To ask for a refund, email us from the address on your account, or contact Link support. Refunds are paid to the payment method you used.</li>
  <li>We may change the plan's features, allowance or price. A change won't affect a period you have already paid for, and we will tell you before a higher price applies to your renewal.</li>
</ul>

<h2>The AI designer</h2>
<ul>
  <li>The AI designer is run by Anthropic's Claude models, using the design and requests sent to it, as described in our <a href="/hanjo/privacy.html">Privacy Policy</a>.</li>
  <li>It makes ordinary edits you can review, accept, reject or change. Its layouts and answers can be unsuitable, inaccurate or against regulations; use your own judgement and check them with a professional.</li>
</ul>

<h2>Sharing</h2>
<p>If you share a design, the people you invite, and anyone with a view-only link, can see it until you stop sharing or revoke the link. You are responsible for who you share it with and for what you share.</p>

<h2>Your designs</h2>
<p>Your designs and the drawings you import belong to you. You give us permission to store, sync and process them only as needed to run Hanjo for you, as described in our Privacy Policy. Only import drawings you have the right to use.</p>

<h2>Acceptable use</h2>
<p>Please don't:</p>
<ul>
  <li>use Hanjo for anything unlawful;</li>
  <li>try to get around the AI plan, its allowance or other limits;</li>
  <li>access other people's designs without permission, or interfere with the app or its servers;</li>
  <li>copy, resell or reverse engineer Hanjo, except where the law allows it.</li>
</ul>
<p>We may suspend or close an account that breaks these terms. Where reasonable, we will tell you first and give you a chance to fix the problem.</p>

<h2>Changes and availability</h2>
<p>We work to keep Hanjo running, but we can't promise it will always be available or free of errors. We may update, change or stop parts of it. If we stop offering Hanjo or the AI plan, we will give reasonable notice where we can, so you can save your designs.</p>

<h2>Disclaimer and limit of liability</h2>
<p>To the extent the law allows, Hanjo is provided "as is", and we are not liable for indirect or consequential losses, including losses from relying on a design, check or estimate without professional review. Our total liability to you is limited to the amount you paid for the AI plan in the 12 months before the claim. Nothing in these terms limits liability for our intentional misconduct or gross negligence, or any rights you have under consumer protection laws that can't be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Japan. If you are a consumer, you also keep the protection of any mandatory laws of the country where you live.</p>

<h2>Changes to these terms</h2>
<p>If we change these terms, we will update the date at the top. For significant changes, we will also tell you in the app. If you keep using Hanjo after a change, the new terms apply.</p>

<h2>Contact</h2>
<p>Questions about these terms: {EMAIL}</p>
'''


OVERVIEW = hero("hanjo", "Web app",
    "Design your house in Japan, room by room, then walk through it.",
    "Hanjo (半畳, half a tatami mat) is a house planner for people building in Japan. Draw on the 910 mm module and see jo and tsubo as you go, check the plan against your plot's limits, then look around it in 3D, in real sunlight, and share it with your builder for comments. An AI designer can lay out a first plan or rework one corner.",
    '<a class="button" href="https://hanjo.app/">Open Hanjo' + EXTERNAL + '</a><span class="label">Free to design · Works in your browser</span>') + f"""

<section aria-label="Main features">
""" + feature_rows_wide([
    ("/assets/screens/hanjo-plan.jpg", "A single-storey 3LDK plan in Hanjo with an LDK, washitsu, bedroom, bath and genkan, a driveway and a garden.", "Plans the way Japanese houses are built", "Draw walls and rooms on the 910 mm module, with half-module snapping and free placement when you need it. Each room shows its size in jo, tsubo and square metres as you draw. Add doors, windows, stairs, a roof, finishes, furniture and the garden, and Hanjo works out the total floor area, coverage ratio and floor area ratio for your plot."),
    ("/assets/screens/hanjo-dollhouse.jpg", "The same house in 3D with the roof lifted off, showing furnished rooms from above.", "Every plan is already in 3D", "Switch to 3D and the house is there, built from your plan: walls, roof, doors, windows, furniture and the garden. Lift the roof off to look down into every room like a dollhouse, move the sun through the day on the solstices and equinox, and walk through the rooms at eye height."),
    ("/assets/screens/hanjo-hide-tools.jpg", "The house in 3D with the roof lifted off, the inside walls cut to half height and the near outside walls hidden, showing how the rooms connect.", "See inside without taking it apart", "Hide tools let you see the parts that matter. Hide near walls lifts away whichever walls face you as you turn the house, so you can look into the rooms with the roof on. Half-height inside walls cuts the partitions down to show how rooms connect, Hide floors above shows one storey at a time, and Hide furniture clears the plan back to its walls."),
    ("/assets/screens/hanjo-ai.jpg", "The AI designer panel open beside the plan, with example requests.", "An AI designer that edits like you do", "Describe the house you want and the AI designer draws a first layout, or mark one area of the plan and ask it to rework just that. Its changes arrive as a proposal you can compare, accept, reject or keep editing by hand, made with the same tools you use."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([('Your plot and its limits', 'Set the lot, north and use zone to check coverage, floor area ratio, setbacks and slant lines.'),
    ('A rough budget', 'See an estimate from average building costs in your prefecture, with garage, deck and garden.'),
    ('Share with your builder', 'Invite your builder or architect to view the design and pin comments to it.'),
    ('Print to scale', 'Print each floor on A3 at true scale, with dimensions, areas and a title block.')]) + f"""
</section>

<section aria-labelledby="plans-title">
  <h2 id="plans-title" class="section-title">Plans</h2>
  <div class="plans">
    <div class="plan"><h3>Design</h3><span class="price">Free</span><p>The plan editor, 3D, sunlight and walk-through, regulation checks, cost estimate, printing and sharing, plus a taste of the AI designer.</p></div>
    <div class="plan"><h3>AI plan</h3><span class="price">1,980 yen<small> / month</small></span><p>Tax included. A monthly allowance of AI designer use for first layouts and reworks. Cancel anytime.</p></div>
  </div>
  <p class="plans-note">Hanjo is a planning tool, not an architect. Have a licensed architect or builder check your design before you build.</p>
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/hanjo/privacy.html">Privacy Policy</a></li>
    <li><a href="/hanjo/terms.html">Terms of Service</a></li>
    <li><a href="/hanjo/legal-notice.html">特定商取引法に基づく表記</a> (legal notice for purchases)</li>
    <li>Questions, refunds or account deletion: {EMAIL}</li>
  </ul>
</section>
"""

LEGAL_ROWS = [
    ("販売業者", "Seller of record", "Link（Stripe グループ）。本サービスの有料プランは、Stripe の Managed Payments を通じて Link が販売事業者として販売・決済を行います。", "Link, part of the Stripe group. The plan is sold and billed by Link as seller of record, through Stripe's Managed Payments."),
    ("サービス提供者", "Service provider", "Joseph Suzuki-Parker（屋号：SP Digital Labs）", "Joseph Suzuki-Parker, trading as SP Digital Labs"),
    ("運営責任者", "Person responsible", "Joseph Suzuki-Parker", "Joseph Suzuki-Parker"),
    ("所在地", "Address", "請求があった場合には、遅滞なく開示いたします。", "Provided without delay on request."),
    ("電話番号", "Phone", "請求があった場合には、遅滞なく開示いたします。お問い合わせはメールでお願いいたします。", "Provided without delay on request. Please contact us by email."),
    ("メールアドレス", "Email", '<a class="email" href="/#contact">support [at] spdigitallabs [dot] app</a>', '<a class="email" href="/#contact">support [at] spdigitallabs [dot] app</a>'),
    ("サービス名", "Service", "Hanjo AIプラン（ウェブアプリ「Hanjo」のAIデザイナーの月額サブスクリプション）", "Hanjo AI plan, a monthly subscription for the AI designer in the Hanjo web app"),
    ("販売価格", "Price", "月額1,980円（税込）<br>お申し込み前に決済画面に表示されます。", "1,980 yen a month, tax included<br>Shown on the checkout screen before you pay."),
    ("商品代金以外の必要料金", "Other charges", "インターネット接続にかかる通信料金はお客様のご負担となります。日本円以外の通貨でお支払いの場合、所定の為替レート・手数料が適用されることがあります。", "Internet connection charges are yours. If you pay in another currency, an exchange rate and fees may apply."),
    ("支払方法", "Payment method", "クレジットカード、デビットカード、Apple Pay、Google Pay、Link など、決済画面に表示される方法", "Credit or debit card, Apple Pay, Google Pay, Link and the other methods shown at checkout"),
    ("支払時期", "When you pay", "お申し込み時に初回のお支払いが発生し、以降は毎月の更新日に自動で請求されます。", "The first payment is taken when you subscribe, then automatically on each monthly renewal date."),
    ("提供時期", "When the service starts", "お申し込み手続きの完了後、直ちにご利用いただけます。", "Immediately after you complete checkout."),
    ("利用範囲", "What the plan includes", "AIデザイナーの月間利用枠（AIの処理に要する費用で計算し、現在は1請求期間あたり最大8米ドル相当）。残りはアプリ内に表示されます。未使用分は翌月に繰り越されません。", "A monthly allowance of AI designer use, measured by what the AI requests cost to run, currently up to the equivalent of US$8 per billing period. The app shows what is left. Unused allowance doesn't carry over."),
    ("自動更新・解約", "Renewal and cancellation", "契約は解約されるまで毎月自動で更新されます。アプリの「プランを管理」またはLinkのアカウントからいつでも解約でき、解約後も支払済みの期間の終了まではご利用いただけます。", "The plan renews automatically every month until you cancel. Cancel any time from Manage plan in the app or from your Link account; you keep the plan until the end of the period you've paid for."),
    ("返金", "Refunds", "返金をご希望の場合は、アカウントのメールアドレスから上記メールアドレスまで、またはLinkのサポートまでご連絡ください。返金はお支払いに使用された方法で行います。", "To ask for a refund, email us from the address on your account, or contact Link support. Refunds are paid to the payment method you used."),
    ("動作環境", "Requirements", "最新版のChrome、Safari、Edge、Firefoxなど、3D表示（WebGL）に対応した主要なウェブブラウザ。パソコンでのご利用を推奨します。インターネット接続が必要です。", "A current version of a major web browser with 3D (WebGL) support, such as Chrome, Safari, Edge or Firefox; a computer is recommended. An internet connection is needed."),
]

def legal_body():
    ja = "\n".join(f"    <tr><th scope=\"row\">{a}</th><td>{c}</td></tr>" for a, _, c, _ in LEGAL_ROWS)
    en = "\n".join(f"    <tr><th scope=\"row\">{b}</th><td>{d}</td></tr>" for _, b, _, d in LEGAL_ROWS)
    return f'''
<h1>特定商取引法に基づく表記</h1>
<p class="updated">最終更新日：{UPDATED_JA}</p>
<p>Hanjo AIプランの販売に関する、特定商取引法に基づく表記です。</p>
<div class="table-scroll">
<table>
  <tbody>
{ja}
  </tbody>
</table>
</div>

<h2 lang="en">Legal notice (English)</h2>
<p lang="en">The seller details for the Hanjo AI plan required by Japan's Act on Specified Commercial Transactions. The Japanese version above is the official one.</p>
<div class="table-scroll" lang="en">
<table>
  <tbody>
{en}
  </tbody>
</table>
</div>
'''


PAGES = {
    "index.html": ("Hanjo", "Design your house in Japan on the 910 mm module, see it in 3D and sunlight, and share it with your builder. Free to design.", OVERVIEW, "en", "wrap app-page"),
    "privacy.html": ("Privacy Policy", "How Hanjo collects, uses and protects your information.", PRIVACY, "en", "wrap page"),
    "terms.html": ("Terms of Service", "The terms for using Hanjo and the Hanjo AI plan.", TERMS, "en", "wrap page"),
    "legal-notice.html": ("特定商取引法に基づく表記", "Hanjo AIプランの特定商取引法に基づく表記。", legal_body(), "ja", "wrap page"),
}

def build(root):
    build_pages(root, "hanjo", PAGES)
