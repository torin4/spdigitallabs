"""Daily Allowance policy and help pages (English). Moved here from hand-written HTML."""

PRIVACY = '''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: November 11, 2026</p>

<p>Daily Allowance is a budgeting app for iPhone and Android, made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what information the app collects, why, who it is shared with, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> we collect what the app needs to work: your account, the budget you enter, and your subscription status. We don't show ads, sell your data, or track you across other apps and websites. Your spending is only sent to an AI provider when you ask for an AI report or question, and only after you agree. You can delete your account and data from inside the app at any time.</p>
</div>

<h2>Information we collect</h2>

<h3>Your account</h3>
<ul>
  <li><strong>Email address and name</strong> from the sign-in method you choose: Sign in with Apple, Google Sign-In, or email and password. If you use Sign in with Apple and hide your email, we only receive Apple's private relay address.</li>
  <li>A <strong>user ID</strong> created by Firebase Authentication. We never see or store your password; Firebase handles it.</li>
</ul>

<h3>Your budget</h3>
<ul>
  <li>The <strong>entries you add</strong>: amounts, dates, labels, categories and notes.</li>
  <li><strong>Recurring income and bills</strong>, wallets (such as Cash and Kitty Bank), categories, your savings goal and currency.</li>
  <li>If you <strong>share a budget</strong>, the email addresses of the people you invite.</li>
</ul>

<h3>Subscriptions</h3>
<ul>
  <li>If you buy Premium, your <strong>subscription status</strong>: which plan, when it expires, whether it renews, and the transaction ID from the App Store or Google Play.</li>
  <li>A <strong>one-way coded version of your user ID</strong> attached to the purchase, so a subscription can only unlock the account that bought it.</li>
  <li>We never receive your card or payment details. Apple and Google handle payment.</li>
</ul>

<h3>AI reports and questions (Premium)</h3>
<ul>
  <li>When you ask for an AI spending report or ask a question about your spending, the app sends your spending totals by category and month, your recurring entries, and the transactions needed to answer, including their labels. Your name and email are not sent.</li>
  <li>We keep your <strong>saved reports</strong> so you can see them again. Questions and answers are not stored on our servers.</li>
  <li>We record <strong>how many reports and questions you use each month</strong>, and their processing size and cost, to apply the monthly limits.</li>
</ul>

<h3>Usage and device information</h3>
<ul>
  <li><strong>iPhone:</strong> the app does not collect analytics, advertising identifiers or device identifiers.</li>
  <li><strong>Android:</strong> the app includes Firebase Analytics, which collects anonymous usage statistics such as which screens are used. It is not used for advertising.</li>
  <li><strong>Camera:</strong> used only to scan a budget invite QR code. Images are processed on your device and never saved or sent.</li>
  <li><strong>Home screen widget:</strong> shows your Daily Balance from data stored on your device.</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To run the app: work out your daily allowance, show your balance and analytics, and keep your data in sync across your devices.</li>
  <li>To let you share a budget with the people you invite.</li>
  <li>To check purchases with Apple or Google and unlock Premium.</li>
  <li>To create AI reports and answers when you ask for them.</li>
  <li>To answer your support requests and keep the service secure.</li>
</ul>
<p>We don't use your information for advertising, and we don't sell it.</p>

<h2>Where it is stored</h2>
<p>Your budget is stored on your device and synced to Google Firebase (Cloud Firestore), which keeps it in Google's data centers, which may be in the United States or other countries. Data is encrypted in transit and at rest. Only you, and anyone you share a budget with, can read your budget data.</p>

<h2>Who we share it with</h2>
<p>We share information only with the services that run the app:</p>
<ul>
  <li><strong>Google Firebase</strong> (Authentication, Cloud Firestore, Cloud Functions; Analytics on Android only), which stores and processes data for us. <a href="https://firebase.google.com/support/privacy">Firebase privacy</a></li>
  <li><strong>Apple</strong>, for Sign in with Apple and App Store purchases. <a href="https://www.apple.com/legal/privacy/">Apple privacy</a></li>
  <li><strong>Google</strong>, for Google Sign-In and Google Play purchases. <a href="https://policies.google.com/privacy">Google privacy</a></li>
  <li><strong>Anthropic</strong> (Claude), only for AI reports and questions you request, after you agree. Anthropic does not use this data to train its models. <a href="https://www.anthropic.com/legal/privacy">Anthropic privacy</a></li>
  <li><strong>People you share a budget with</strong> can see that budget's entries and your email address.</li>
</ul>
<p>We may also disclose information if the law requires it.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Your account and budget are kept until you delete them.</li>
  <li>Saved AI reports are kept until you delete your account.</li>
  <li>Monthly AI usage records are kept until you delete your account.</li>
</ul>

<h2>Your choices and rights</h2>
<ul>
  <li><strong>See and change your data</strong> at any time in the app.</li>
  <li><strong>Export it</strong> as a CSV file from the app (the current month on the free plan, your full history with Premium). Email us if you want a full copy without Premium.</li>
  <li><strong>Delete entries or reset your data</strong> in Settings &gt; Delete Data.</li>
  <li><strong>Delete your account</strong> in Settings &gt; Delete Account. This deletes your account, your budget, your saved AI reports, your AI usage records and your subscription record from our servers, and clears the app's data on your device. If you joined someone else's shared budget, you are removed from it; their budget stays. Deleting your account doesn't cancel an App Store or Google Play subscription; cancel that in your store account settings.</li>
  <li>If you can't use the app, follow the steps on our <a href="delete-account.html">account deletion page</a>.</li>
  <li>Depending on where you live, you may have further rights, such as to object to processing or complain to a data protection authority. Contact us and we will help.</li>
</ul>

<h2>Children</h2>
<p>Daily Allowance is not directed at children under 13, and we don't knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top. For significant changes, we will also tell you in the app.</p>

<h2>Contact</h2>
<p>Questions or requests about your privacy: <a class="email" href="support.html">support [at] spdigitallabs [dot] app</a></p>
<p>This policy is also available in <a href="/ja/dailyallowance/privacy.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

TERMS = '''
<h1>Terms of Service</h1>
<p class="updated">Last updated: November 11, 2026</p>

<p>These terms apply to your use of Daily Allowance, a budgeting app for iPhone and Android made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). By creating an account or using the app, you agree to these terms. If you don't agree, please don't use the app.</p>

<div class="card">
  <p><strong>The short version:</strong> Daily Allowance helps you plan your spending, but it isn't financial advice, and its numbers are only as accurate as what you enter. Premium is a subscription billed by Apple or Google, which renews until you cancel it in your store account. AI reports and answers can be wrong, so check them before you act on them. Your budget belongs to you, and you can delete your account at any time.</p>
</div>

<h2>Who can use the app</h2>
<p>You must be at least 13 years old to use Daily Allowance. If you are under the age of majority where you live, you need a parent or guardian's permission, including to buy Premium.</p>

<h2>Your account</h2>
<ul>
  <li>You sign in with Sign in with Apple, Google Sign-In, or an email address and password. Keep your sign-in details secure; you are responsible for activity on your account.</li>
  <li>Tell us right away if you think someone else has used your account.</li>
  <li>You can delete your account at any time in Settings &gt; Delete Account, or by following our <a href="delete-account.html">account deletion page</a>.</li>
</ul>

<h2>Not financial advice</h2>
<p>Daily Allowance works out a daily spending amount and other figures from the income, bills and entries you give it. These figures are estimates for your own planning. They are not financial, tax, investment or legal advice, and they don't take account of anything you haven't entered. You are responsible for your own financial decisions.</p>

<h2>Premium subscription</h2>
<ul>
  <li>Premium is an optional subscription that unlocks extra features, such as AI reports and questions and full CSV export. Prices and plans are shown in the app before you buy.</li>
  <li>Payment is handled by the App Store or Google Play, under their terms. We never receive your payment details.</li>
  <li>Subscriptions renew automatically at the end of each period unless you cancel at least 24 hours before it ends. Cancel in your App Store or Google Play account settings. Deleting your Daily Allowance account does not cancel your subscription.</li>
  <li>Refunds are handled by Apple or Google under their refund policies. We can't issue refunds directly.</li>
  <li>A subscription belongs to the Daily Allowance account that bought it. People who join that account's shared budget can use Premium features within it while the subscription is active.</li>
  <li>We may change Premium features or prices. A price change won't affect a period you have already paid for, and Apple or Google will tell you before a higher price applies to your renewal.</li>
</ul>

<h2>AI reports and questions</h2>
<ul>
  <li>Premium includes AI spending reports and answers to questions about your spending, produced by Claude, an AI model from Anthropic. The data sent is described in our <a href="privacy.html">Privacy Policy</a>.</li>
  <li>AI output can be incomplete or wrong. Check it before relying on it, and don't treat it as professional advice.</li>
  <li>AI features have monthly limits, shown in the app. We may change these limits to keep the service sustainable.</li>
</ul>

<h2>Shared budgets</h2>
<p>If you share a budget, the people you invite can see and change its entries and see your email address. Only invite people you trust. If you join someone else's budget, its owner can remove you, and the budget stays with them when you leave.</p>

<h2>Your data</h2>
<p>The budget entries and other content you add belong to you. You give us permission to store, sync and process them only as needed to run the app for you, as described in our <a href="privacy.html">Privacy Policy</a>. You can export or delete your data in the app.</p>

<h2>Acceptable use</h2>
<p>Please don't:</p>
<ul>
  <li>use the app for anything unlawful;</li>
  <li>try to get around purchase checks, AI limits or other restrictions;</li>
  <li>access other people's data without permission, or interfere with the app or its servers;</li>
  <li>copy, resell or reverse engineer the app, except where the law allows it.</li>
</ul>
<p>We may suspend or close an account that breaks these terms. Where reasonable, we will tell you first and give you a chance to fix the problem.</p>

<h2>The app</h2>
<p>We own the app, its design and its content. We give you a personal, non-transferable license to use it on devices you own or control. If you got the app from the App Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard End User License Agreement</a> also applies. Apple is not responsible for the app or for support, and these terms are between you and us, not Apple.</p>

<h2>Changes and availability</h2>
<p>We work to keep Daily Allowance running, but we can't promise it will always be available or free of errors. We may update, change or stop parts of the app. If we stop offering the app or Premium, we will give reasonable notice where we can, so you can export your data.</p>

<h2>Disclaimer and limit of liability</h2>
<p>To the extent the law allows, the app is provided "as is", and we are not liable for indirect or consequential losses, or for losses resulting from financial decisions you make using the app. Our total liability to you is limited to the amount you paid for Premium in the 12 months before the claim. Nothing in these terms limits liability for our intentional misconduct or gross negligence, or any rights you have under consumer protection laws that can't be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Japan. If you are a consumer, you also keep the protection of any mandatory laws of the country where you live.</p>

<h2>Changes to these terms</h2>
<p>If we change these terms, we will update the date at the top. For significant changes, we will also tell you in the app. If you keep using the app after a change, the new terms apply.</p>

<h2>Contact</h2>
<p>Questions about these terms: <a class="email" href="support.html">support [at] spdigitallabs [dot] app</a></p>
<p>These terms are also available in <a href="/ja/dailyallowance/terms.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

SUPPORT = '''
<h1>Support</h1>
<p class="updated">We're happy to help.</p>

<div class="card">
  <h3>Contact us</h3>
  <p>Email <a class="email" data-subject="Daily Allowance support" href="support.html">support [at] spdigitallabs [dot] app</a>. We usually reply within two business days. Please include your phone model and what you were doing when the problem happened. Never send your password.</p>
</div>

<h2>Getting started</h2>

<h3>How is my daily allowance worked out?</h3>
<p>Add your regular income and bills under Settings &gt; Daily Allowance. The app spreads them across the month: whatever is left after your bills, divided by the days, is your daily allowance. Each day, the allowance is added to your Daily Balance and what you spend is taken off.</p>

<h3>Why is my Daily Balance negative?</h3>
<p>You've spent more than your allowance so far. It recovers as each new day's allowance is added. If it looks wrong, check that your income is set up as a recurring entry and that one-off income or bills are added on the right dates.</p>

<h3>How do I change the currency or language?</h3>
<p>Settings &gt; Currency, and Settings &gt; Language. The language can follow your phone or be set just for the app.</p>

<h3>How do I add the widget?</h3>
<p>On iPhone, touch and hold your Home Screen, tap Edit &gt; Add Widget, and choose Daily Allowance. Tapping the widget opens a new entry.</p>

<h2>Sharing a budget</h2>
<p>Go to Settings &gt; Budget &amp; Sharing to invite someone by email or show a QR code. They join from the same screen on their phone. Everyone in a shared budget sees and edits the same entries. Sharing is a Premium feature for the budget owner, for up to 5 people.</p>

<h2>Premium and subscriptions</h2>

<h3>What does Premium include?</h3>
<ul>
  <li>Budget sharing with up to 5 people</li>
  <li>Unlimited recurring entries (the free plan includes 5)</li>
  <li>Spreading large purchases over several months</li>
  <li>Analytics for every month</li>
  <li>Full CSV export</li>
  <li>AI reports and questions: up to 5 spending reports and 40 questions a month, resetting on the 1st</li>
</ul>

<h3>How do I cancel or change my subscription?</h3>
<p><strong>iPhone:</strong> open the Settings app, tap your name, then Subscriptions, and choose Daily Allowance. You can also reach it from the Premium screen in the app.<br>
<strong>Android:</strong> open Google Play, tap your profile, then Payments &amp; subscriptions &gt; Subscriptions.</p>
<p>You keep Premium until the end of the period you've paid for. Deleting the app or your account does not cancel a subscription.</p>

<h3>I paid, but I don't have Premium</h3>
<p>Make sure you're signed in to the same Daily Allowance account you used to buy it, then open the Premium screen and tap Restore Purchases. A subscription can only be linked to one Daily Allowance account. If it still doesn't work, email us with the date of the purchase.</p>

<h3>How do I get a refund?</h3>
<p>Refunds are handled by Apple or Google, not by us. On iPhone, go to <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. On Android, see Google Play's refund help.</p>

<h2>Your data</h2>

<h3>Does it work offline?</h3>
<p>Yes. Entries are saved on your phone and sync when you're back online.</p>

<h3>How do I export my data?</h3>
<p>Use Settings &gt; Backup to CSV. The free plan exports the current month; Premium exports your full history.</p>

<h3>How do I delete my account?</h3>
<p>Settings &gt; Delete Account. See <a href="delete-account.html">deleting your account</a> for what's removed, or if you can't open the app.</p>

<p>For how we handle your information, read our <a href="privacy.html">Privacy Policy</a>.</p>
'''

DELETE_ACCOUNT = '''
<h1>Delete your account</h1>
<p class="updated">Last updated: November 2, 2026</p>

<div class="card">
  <p>Deleting your account permanently removes your data and can't be undone. If you want a copy first, use Settings &gt; Backup to CSV.</p>
</div>

<h2>Delete in the app</h2>
<ol>
  <li>Open Daily Allowance and sign in.</li>
  <li>Go to Settings and tap <strong>Delete Account</strong>.</li>
  <li>Confirm. You may be asked to sign in again to prove it's you.</li>
</ol>
<p>Your account is deleted right away, along with everything listed below.</p>

<h3>Just want a fresh start?</h3>
<p>Settings &gt; Delete Data clears your entries (and optionally your categories) but keeps your account.</p>

<h2>Can't open the app?</h2>
<p>Email <a class="email" data-subject="Delete my Daily Allowance account" href="support.html">support [at] spdigitallabs [dot] app</a> from the email address on your account, and say you want your account deleted. If you used Sign in with Apple with a hidden email, tell us the date you signed up instead. We will confirm and delete it within 30 days.</p>

<h2>What gets deleted</h2>
<ul>
  <li>Your account and sign-in details</li>
  <li>Your budget: entries, recurring income and bills, wallets, categories and settings</li>
  <li>Your saved AI reports and AI usage records</li>
  <li>Your subscription record and the link between your account and your purchases</li>
  <li>The app's data on the device you delete from</li>
</ul>
<p>If you joined someone else's shared budget, you are removed from it, but their budget stays. If you own a shared budget, it is deleted for everyone.</p>

<h2>Subscriptions</h2>
<p>Deleting your account doesn't cancel an App Store or Google Play subscription. Cancel it in your store account settings; see <a href="support.html">Support</a> for how.</p>
'''

META = {'privacy': ('Privacy Policy', 'How Daily Allowance collects, uses and protects your information.'), 'terms': ('Terms of Service', 'The terms for using the Daily Allowance app and Premium subscription.'), 'support': ('Support', 'Help with Daily Allowance: how it works, subscriptions, sharing, and contacting us.'), 'delete-account': ('Delete Your Account', 'How to delete your Daily Allowance account and data.')}
