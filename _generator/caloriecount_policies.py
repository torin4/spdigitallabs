"""Calorie Count policy and help pages (English). Japanese twins are in caloriecount_ja.py."""

PRIVACY = '''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: November 25, 2026</p>

<p>Calorie Count is a calorie counting app for iPhone and Android, made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what information the app collects, why, who it is shared with, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> your log lives on your phone, and you can use the app without an account. If you sign in, we keep a backup of your log so it is safe and can appear on another phone. A photo or description is sent to an AI provider only when you ask for an estimate, and we don't keep it. Steps and weight from your health app are only read, never written, and are never used for advertising. We don't show ads, sell your data, or track you across other apps and websites. You can delete your account and its data from inside the app at any time.</p>
</div>

<h2>Information we collect</h2>

<h3>Your log, kept on your phone</h3>
<ul>
  <li>The <strong>food entries you add</strong>: calories, an optional name, how it was added, and the time.</li>
  <li>Your <strong>weigh-ins</strong>.</li>
  <li>Your <strong>profile</strong>: sex, age, height, weight, typical steps a day and workouts a week. The app uses these to work out how many calories you burn.</li>
</ul>
<p>If you never sign in, your log stays on your phone and is not sent to us.</p>

<h3>Your account (optional)</h3>
<ul>
  <li><strong>Email address and name</strong> from the sign-in method you choose: Sign in with Apple, Google Sign-In, or email and password. If you use Sign in with Apple and hide your email, we only receive Apple's private relay address.</li>
  <li>A <strong>user ID</strong> created by Firebase Authentication. We never see or store your password; Firebase handles it.</li>
  <li>A <strong>backup of your log</strong>: your food entries, weigh-ins and profile, so your log is safe and can appear on another phone.</li>
</ul>

<h3>Health data</h3>
<ul>
  <li>If you connect your health app, Calorie Count reads your <strong>step counts</strong> and <strong>weight</strong> from Apple Health (iPhone) or Health Connect (Android). It never writes to them.</li>
  <li>It uses them only to work out how many calories you burn and to draw your weight trend.</li>
  <li>Your average daily steps and your weigh-ins are stored with the rest of your log, and are included in your backup if you are signed in.</li>
  <li>Health data is never used for advertising or marketing, and is never sold or shared with anyone else.</li>
</ul>

<h3>AI estimates</h3>
<ul>
  <li>When you ask for an estimate, the <strong>photo or description</strong> you provide is sent to our server and on to an AI provider, which returns the calories. Your name, email and log are not sent with it.</li>
  <li>We do not store the photo or the description.</li>
  <li>To count the free estimates each day, the app gives each phone a <strong>random user ID</strong> the first time you ask for an estimate, even if you have not signed in. It holds no personal information. We record <strong>how many estimates you have used today</strong>.</li>
</ul>

<h3>Subscriptions</h3>
<ul>
  <li>If you buy Premium, your <strong>subscription status</strong>: which plan, when it expires, whether it renews, and the transaction ID from the App Store or Google Play.</li>
  <li>A <strong>one-way coded version of your user ID</strong> attached to the purchase, so a subscription can only unlock the account that bought it.</li>
  <li>We never receive your card or payment details. Apple and Google handle payment.</li>
</ul>

<h3>Usage and device information</h3>
<ul>
  <li>The app does not collect analytics, advertising identifiers or device identifiers.</li>
  <li><strong>Camera and photos:</strong> used only when you choose to estimate a meal from a photo.</li>
  <li><strong>Home screen widget:</strong> shows your calories from data stored on your device.</li>
  <li>If you send feedback from the app, the email includes the app version and your phone model, which you can see and remove before sending.</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To run the app: work out what you burn, show how far under or over you are, and draw your trend.</li>
  <li>To back up your log and bring it to another phone, if you sign in.</li>
  <li>To produce an estimate when you ask for one, and to apply the daily limit.</li>
  <li>To check purchases with Apple or Google and unlock Premium.</li>
  <li>To answer your support requests and keep the service secure.</li>
</ul>
<p>We don't use your information for advertising, we don't sell it, and we don't use it to train AI models.</p>

<h2>Where it is stored</h2>
<p>Your log is stored on your device. If you sign in, a backup is kept in Google Firebase (Cloud Firestore) in Tokyo, Japan. Data is encrypted in transit and at rest. Only you can read your backup.</p>

<h2>Who we share it with</h2>
<p>We share information only with the services that run the app:</p>
<ul>
  <li><strong>Google Firebase</strong> (Authentication, Cloud Firestore), which stores and processes data for us. <a href="https://firebase.google.com/support/privacy">Firebase privacy</a></li>
  <li><strong>Vercel</strong>, which hosts the server that handles estimates and checks purchases. <a href="https://vercel.com/legal/privacy-policy">Vercel privacy</a></li>
  <li><strong>AI providers</strong>, reached through Vercel, only for the estimates you request: Google (Gemini) for photos and Anthropic (Claude) for descriptions. They receive the photo or description and nothing else. <a href="https://policies.google.com/privacy">Google privacy</a> · <a href="https://www.anthropic.com/legal/privacy">Anthropic privacy</a></li>
  <li><strong>Apple</strong>, for Sign in with Apple and App Store purchases. <a href="https://www.apple.com/legal/privacy/">Apple privacy</a></li>
  <li><strong>Google</strong>, for Google Sign-In and Google Play purchases. <a href="https://policies.google.com/privacy">Google privacy</a></li>
</ul>
<p>We may also disclose information if the law requires it.</p>

<h2>How long we keep it</h2>
<ul>
  <li>The log on your phone stays until you delete it or remove the app.</li>
  <li>Your account and backup are kept until you delete them.</li>
  <li>The count of estimates used is replaced each day.</li>
  <li>Photos and descriptions sent for estimates are not kept.</li>
</ul>

<h2>Your choices and rights</h2>
<ul>
  <li><strong>See and change your data</strong> at any time in the app.</li>
  <li><strong>Use the app without an account.</strong> Signing in is only needed for backup and for Premium.</li>
  <li><strong>Disconnect your health app</strong> on the Profile screen, or in Apple Health or Health Connect settings.</li>
  <li><strong>Delete your account</strong> in Account &gt; Delete account. This deletes your account, your backup, your estimate count and your subscription record from our servers. The log on your phone stays until you remove the app. Deleting your account doesn't cancel an App Store or Google Play subscription; cancel that in your store account settings.</li>
  <li>If you can't use the app, follow the steps on our <a href="delete-account.html">account deletion page</a>.</li>
  <li>Depending on where you live, you may have further rights, such as to object to processing or complain to a data protection authority. Contact us and we will help.</li>
</ul>

<h2>Children</h2>
<p>Calorie Count is intended for adults. It is not directed at children, and we don't knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.</p>

<h2>Not medical advice</h2>
<p>The numbers in Calorie Count are estimates. They are not medical advice. Talk to a doctor before making significant changes to how you eat, especially if you have a health condition.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top. For significant changes, we will also tell you in the app.</p>

<h2>Contact</h2>
<p>Questions or requests about your privacy: <a class="email" href="support.html">support [at] spdigitallabs [dot] app</a></p>
<p>This policy is also available in <a href="/ja/caloriecount/privacy.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

TERMS = '''
<h1>Terms of Service</h1>
<p class="updated">Last updated: November 25, 2026</p>

<p>These terms apply to your use of Calorie Count, a calorie counting app for iPhone and Android made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). By using the app, you agree to these terms. If you don't agree, please don't use the app.</p>

<div class="card">
  <p><strong>The short version:</strong> Calorie Count compares what you eat with what you burn, but every number it shows is an estimate, and it isn't medical advice. Premium is a subscription billed by Apple or Google, which renews until you cancel it in your store account. AI estimates can be wrong, so check them. Your log belongs to you, and you can delete your account at any time.</p>
</div>

<h2>Who can use the app</h2>
<p>You must be at least 18 years old to use Calorie Count. The app is not suitable for anyone who is pregnant, has or has had an eating disorder, or has a medical condition affected by diet, unless a doctor has advised them to use it.</p>

<h2>Not medical advice</h2>
<p>Calorie Count works out how many calories you burn from the details you give it, and estimates the calories in food from photos and descriptions. These figures are estimates for your own information. They can be wrong, sometimes by a lot. They are not medical, nutritional or dietary advice, and the app is not a medical device. Talk to a doctor before making significant changes to how you eat or exercise. You are responsible for your own decisions about your health.</p>

<h2>Your account</h2>
<ul>
  <li>You can use the app without an account. If you create one, you sign in with Sign in with Apple, Google Sign-In, or an email address and password. Keep your sign-in details secure; you are responsible for activity on your account.</li>
  <li>Tell us right away if you think someone else has used your account.</li>
  <li>You can delete your account at any time in Account &gt; Delete account, or by following our <a href="delete-account.html">account deletion page</a>.</li>
</ul>

<h2>AI estimates</h2>
<ul>
  <li>Estimates from photos and descriptions are produced by AI models. What is sent is described in our <a href="privacy.html">Privacy Policy</a>.</li>
  <li>AI output can be incomplete or wrong. Check it, and change the number if you know better.</li>
  <li>Without Premium there is a daily limit on estimates, shown in the app. We may change this limit to keep the service sustainable.</li>
</ul>

<h2>Premium subscription</h2>
<ul>
  <li>Premium is an optional subscription that removes the daily limit on AI estimates. Prices and plans are shown in the app before you buy.</li>
  <li>You need an account to subscribe, so that your subscription can follow you to a new phone.</li>
  <li>Payment is handled by the App Store or Google Play, under their terms. We never receive your payment details.</li>
  <li>Subscriptions renew automatically at the end of each period unless you cancel at least 24 hours before it ends. Cancel in your App Store or Google Play account settings. Deleting your Calorie Count account does not cancel your subscription.</li>
  <li>Refunds are handled by Apple or Google under their refund policies. We can't issue refunds directly.</li>
  <li>A subscription belongs to the Calorie Count account that bought it.</li>
  <li>We may change Premium features or prices. A price change won't affect a period you have already paid for, and Apple or Google will tell you before a higher price applies to your renewal.</li>
</ul>

<h2>Your data</h2>
<p>The entries and other content you add belong to you. You give us permission to store, back up and process them only as needed to run the app for you, as described in our <a href="privacy.html">Privacy Policy</a>.</p>

<h2>Acceptable use</h2>
<p>Please don't:</p>
<ul>
  <li>use the app for anything unlawful;</li>
  <li>try to get around purchase checks, estimate limits or other restrictions;</li>
  <li>send anything other than food to the estimate feature;</li>
  <li>access other people's data without permission, or interfere with the app or its servers;</li>
  <li>copy, resell or reverse engineer the app, except where the law allows it.</li>
</ul>
<p>We may suspend or close an account that breaks these terms. Where reasonable, we will tell you first and give you a chance to fix the problem.</p>

<h2>The app</h2>
<p>We own the app, its design and its content. We give you a personal, non-transferable license to use it on devices you own or control. If you got the app from the App Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard End User License Agreement</a> also applies. Apple is not responsible for the app or for support, and these terms are between you and us, not Apple.</p>

<h2>Changes and availability</h2>
<p>We work to keep Calorie Count running, but we can't promise it will always be available or free of errors. We may update, change or stop parts of the app. If we stop offering the app or Premium, we will give reasonable notice where we can.</p>

<h2>Disclaimer and limit of liability</h2>
<p>To the extent the law allows, the app is provided "as is", and we are not liable for indirect or consequential losses, or for losses resulting from decisions you make using the app or relying on its estimates. Our total liability to you is limited to the amount you paid for Premium in the 12 months before the claim. Nothing in these terms limits liability for our intentional misconduct or gross negligence, or any rights you have under consumer protection laws that can't be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Japan. If you are a consumer, you also keep the protection of any mandatory laws of the country where you live.</p>

<h2>Changes to these terms</h2>
<p>If we change these terms, we will update the date at the top. For significant changes, we will also tell you in the app. If you keep using the app after a change, the new terms apply.</p>

<h2>Contact</h2>
<p>Questions about these terms: <a class="email" href="support.html">support [at] spdigitallabs [dot] app</a></p>
<p>These terms are also available in <a href="/ja/caloriecount/terms.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

SUPPORT = '''
<h1>Support</h1>
<p class="updated">We're happy to help.</p>

<div class="card">
  <h3>Contact us</h3>
  <p>Email <a class="email" data-subject="Calorie Count support" href="support.html">support [at] spdigitallabs [dot] app</a>, or use Account &gt; Send feedback in the app. We usually reply within two business days. Please include your phone model and what you were doing when the problem happened. Never send your password.</p>
</div>

<h2>Getting started</h2>

<h3>What is the big number?</h3>
<p>It is how far under or over you are today: the calories you have eaten, against the calories you burn in a day. "Under" means you have eaten less than you burn. Stay under, day after day, and you lose weight.</p>

<h3>How is what I burn worked out?</h3>
<p>From what you enter on the Profile screen: your sex, age, height and weight give the calories your body uses at rest, and your steps and workouts are added on top. It is an estimate. After two weeks of logging food and weighing in, the app compares it with what your own numbers show and lets you choose which to use.</p>

<h3>How do I add food?</h3>
<p>Tap the plus button. Type the calories if you know them, describe what you ate and tap Estimate, or take a photo. Foods you have eaten before appear underneath so you can add them again with one tap. Tap any entry in today's list to change or remove it.</p>

<h3>How accurate are the estimates?</h3>
<p>They are a reasonable guess, not a measurement. A photo can't show what is hidden or how much oil was used. If you know the real number, type it in.</p>

<h3>How do I connect my health app?</h3>
<p>On the Profile screen, tap "Use my health app" and allow access to steps and weight. On Android this uses Health Connect, so the app that counts your steps (such as Google Health, Fitbit, Samsung Health or Garmin) needs to be sharing with Health Connect in its own settings. If more than one app has recorded steps, you can choose which to use.</p>

<h3>How do I add the widget?</h3>
<p>Touch and hold your home screen, choose Widgets, and find Calorie Count. It shows your calories for today and a button to add.</p>

<h2>Premium and subscriptions</h2>

<h3>What does Premium include?</h3>
<p>Unlimited AI estimates from photos and descriptions. Without Premium you get one a day. Typing in calories yourself is always free and unlimited.</p>

<h3>Why do I need to sign in to subscribe?</h3>
<p>So that your subscription belongs to your account and follows you to a new phone.</p>

<h3>How do I cancel or change my subscription?</h3>
<p><strong>iPhone:</strong> open the Settings app, tap your name, then Subscriptions, and choose Calorie Count. You can also reach it from the Premium screen in the app.<br>
<strong>Android:</strong> open Google Play, tap your profile, then Payments &amp; subscriptions &gt; Subscriptions.</p>
<p>You keep Premium until the end of the period you've paid for. Deleting the app or your account does not cancel a subscription.</p>

<h3>I paid, but I don't have Premium</h3>
<p>Make sure you're signed in to the same Calorie Count account you used to buy it, then open the Premium screen and tap Restore purchase. A subscription can only be linked to one Calorie Count account. If it still doesn't work, email us with the date of the purchase.</p>

<h3>How do I get a refund?</h3>
<p>Refunds are handled by Apple or Google, not by us. On iPhone, go to <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. On Android, see Google Play's refund help.</p>

<h2>Your data</h2>

<h3>Does it work offline?</h3>
<p>Yes. Your log is kept on your phone. Only AI estimates and backup need a connection.</p>

<h3>How do I move to a new phone?</h3>
<p>On the old phone, open Account, sign in, and wait until it says "Backed up". On the new phone, sign in with the same account and your log appears.</p>

<h3>How do I delete my account?</h3>
<p>Account &gt; Delete account. See <a href="delete-account.html">deleting your account</a> for what's removed, or if you can't open the app.</p>

<p>For how we handle your information, read our <a href="privacy.html">Privacy Policy</a>. Calorie Count gives estimates, not medical advice.</p>
'''

DELETE_ACCOUNT = '''
<h1>Delete your account</h1>
<p class="updated">Last updated: November 25, 2026</p>

<div class="card">
  <p>Deleting your Calorie Count account permanently removes the account and its backup from our servers and can't be undone.</p>
</div>

<h2>Delete in the app</h2>
<ol>
  <li>Open Calorie Count and go to Profile, then <strong>Account</strong>.</li>
  <li>Tap <strong>Delete account</strong> and confirm.</li>
  <li>If it asks you to sign in again, sign out, sign back in, and delete within a few minutes. This proves it's you.</li>
</ol>
<p>Your account is deleted right away, along with everything listed below.</p>

<h2>Can't open the app?</h2>
<p>Email <a class="email" data-subject="Delete my Calorie Count account" href="support.html">support [at] spdigitallabs [dot] app</a> from the email address on your account, and say you want your account deleted. If you used Sign in with Apple with a hidden email, tell us the date you signed up instead. We will confirm and delete it within 30 days.</p>

<h2>What gets deleted</h2>
<ul>
  <li>Your account and sign-in details</li>
  <li>Your backup: food entries, weigh-ins and profile</li>
  <li>Your count of estimates used</li>
  <li>Your subscription record and the link between your account and your purchases</li>
</ul>

<h2>What stays</h2>
<p>The log on your phone is not removed, so you can keep using the app without an account. To remove it too, delete the app from your phone.</p>

<h2>Subscriptions</h2>
<p>Deleting your account doesn't cancel an App Store or Google Play subscription. Cancel it in your store account settings; see <a href="support.html">Support</a> for how.</p>
'''

META = {
    'privacy': ('Privacy Policy', 'How Calorie Count collects, uses and protects your information.'),
    'terms': ('Terms of Service', 'The terms for using the Calorie Count app and Premium subscription.'),
    'support': ('Support', 'Help with Calorie Count: how it works, health apps, subscriptions, and contacting us.'),
    'delete-account': ('Delete Your Account', 'How to delete your Calorie Count account and data.'),
}
