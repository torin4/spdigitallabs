from icons import EXTERNAL
from chrome import EMAIL, hero, features, feature_rows, build_pages
from lift_ja import PAGES_JA

APP = "https://liftjp.web.app"
UPDATED = "November 14, 2026"
SUPPORT_EMAIL = EMAIL.replace('class="email"', 'class="email" data-subject="Lift support"')

PRIVACY = f'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: {UPDATED}</p>

<p>Lift is a workout log web app at liftjp.web.app, made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what information Lift collects, why, who it is shared with, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> Lift works without an account, and then nothing you enter leaves your device. If you choose to sign in with Google, your log is also stored in Google Firebase so it can be backed up and kept in step across your devices. Lift Pro, an optional paid plan, builds workouts with AI: what you pick is sent to Anthropic to write the routine, and payment is handled by Stripe. Lift has no analytics, advertising or tracking, and we don't sell data. You can export everything, and you can delete your account and everything synced with it from Settings.</p>
</div>

<h2>Information we collect</h2>

<h3>If you don't sign in</h3>
<p>Everything you enter is stored only in your browser, on your device. We can't see it. That covers:</p>
<ul>
  <li><strong>Your routines:</strong> the exercises you add, with their sets, target reps, rest times and weight steps.</li>
  <li><strong>Your sessions:</strong> the date and length of each workout, the weight and reps of each set, sets you skipped, machine setup notes and any other notes you write.</li>
  <li><strong>Your body measurements:</strong> bodyweight, and any other values you enter from an InBody result sheet, such as body fat and muscle mass. If you choose to enter them, also your height and sex, which are used only to show the normal ranges for those values.</li>
  <li><strong>Your settings:</strong> language, rest time and your weekly set targets.</li>
</ul>
<p>Like any website, the service that hosts Lift (Google Firebase Hosting) receives your IP address and basic details of the request when the app loads, and keeps them in logs for a limited time for security and reliability.</p>

<h3>If you sign in</h3>
<ul>
  <li><strong>Your account:</strong> Firebase Authentication receives your email address, name and profile picture from Google and creates a user ID. Lift itself shows only your email address, in Settings. We never see your Google password.</li>
  <li><strong>Your log:</strong> the routines, sessions, body measurements and settings listed above are stored in Cloud Firestore under your user ID. Access rules allow only your own signed-in account to read or change them.</li>
  <li><strong>If you subscribe to Lift Pro:</strong> whether your subscription is active and a Stripe customer ID are stored with your user ID, along with a count of the workouts you have generated this month. Your card details go straight to Stripe; we never see or store them.</li>
  <li><strong>If you generate a workout:</strong> the choices you tap (goal, focus, time, equipment, experience), anything you type in the optional note, and the names of the exercises in your library, including ones you added yourself, are sent to Anthropic so its AI model can write the routine. Your sessions, weights, body measurements, name and email address are not sent. We don't keep a copy of what you send or of the routine, other than the routine you choose to save in your log.</li>
</ul>

<h2>Body measurements</h2>
<p>Body measurements are information about your body. Lift stores them only because you enter them, and uses them only to show them back to you. They are synced only if you sign in. If you would rather they stay on your device, use Lift without signing in, or don't enter them.</p>

<h2>Device and browser</h2>
<ul>
  <li><strong>Stored in your browser:</strong> your log, a copy of the app so it works offline, and, once you sign in, your sign-in and Firebase's own offline copy of your synced data.</li>
  <li>Lift doesn't use your camera, microphone, location or contacts. If you leave "Keep screen awake" on, it asks your browser not to lock the screen during a workout.</li>
  <li>Lift has no analytics, advertising or tracking tools, and it loads no outside fonts or scripts, with one exception: Google's Firebase code for signing in and syncing, which is loaded only once you choose to sign in.</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To run Lift: show your log, suggest weights from it, back it up and keep your devices in step.</li>
  <li>To provide Lift Pro: build the workouts you ask for, and manage your subscription.</li>
  <li>To keep your account secure.</li>
  <li>To answer your messages and requests.</li>
</ul>
<p>We don't use your information for advertising, and we don't sell it. We can technically open data stored in Firebase in order to run the service. We do that only to fix a problem you have asked us to fix, or if the law requires it.</p>

<h2>Where it is stored, and transfers abroad</h2>
<p>If you sign in, your data is stored in Google Firebase (Authentication and Cloud Firestore), and the app is served by Firebase Hosting. Google may store and process data in the United States or other countries. The United States has no comprehensive federal privacy law equivalent to Japan's. Google commits to protecting data under its own policies and contracts, linked below. Data is encrypted in transit and at rest. By signing in, you consent to this transfer.</p>
<p>If you use Lift Pro, Stripe processes your payment and Anthropic processes the request for each workout you generate. Both are based in the United States and may process data there or in other countries, under their own policies linked below. By subscribing and by generating a workout, you consent to these transfers.</p>

<h2>Who we share it with</h2>
<p>We share information only with the services that run Lift:</p>
<ul>
  <li><strong>Google</strong>, which provides Firebase for hosting, sign-in and storage. <a href="https://firebase.google.com/support/privacy">Firebase privacy</a> · <a href="https://cloud.google.com/terms/data-processing-addendum">Google Cloud data processing terms</a></li>
  <li><strong>Anthropic</strong>, whose AI model writes generated workouts (Lift Pro only). It receives the choices, note and exercise names described above. <a href="https://www.anthropic.com/legal/privacy">Anthropic privacy policy</a></li>
  <li><strong>Stripe</strong>, which takes payment for Lift Pro. It receives your email address and your card details. <a href="https://stripe.com/privacy">Stripe privacy policy</a></li>
</ul>
<p>We may also disclose information if the law requires it.</p>

<h2>How long we keep it</h2>
<ul>
  <li>On your device: until you delete it, clear your browser's data for the site, or remove the app.</li>
  <li>Synced data: until you delete it or your account. When you delete a session or a measurement it is removed from the cloud, and a note that it was deleted is kept for 90 days so that your other devices remove it too.</li>
  <li>Hosting and sign-in logs: kept by Google for a limited time.</li>
  <li>Subscription status and Stripe customer ID: for as long as you have an account. Stripe keeps payment records for as long as the law requires.</li>
</ul>

<h2>Your choices and rights</h2>
<ul>
  <li>Use Lift without an account. Nothing you enter then leaves your device.</li>
  <li>Save a copy of everything with Settings &gt; Export everything.</li>
  <li>Delete a session or a measurement in the app.</li>
  <li>Delete every routine, session and measurement with Settings &gt; Reset all data. If you are signed in, this deletes the synced copy too.</li>
  <li>Sign out in Settings, and choose whether your log stays on that device.</li>
  <li>Delete your account with Settings &gt; Delete account. This permanently deletes everything synced for your account, and the sign-in itself. If you can't sign in, email us from the address on your account and we will delete it for you.</li>
  <li>Depending on where you live, you may have further rights, such as to see, correct or object to how we use your information, or to complain to a data protection authority. Contact us and we will help.</li>
</ul>

<h2>Children</h2>
<p>Lift is not directed at children under 13, and we don't knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top.</p>

<h2>Contact</h2>
<p>Questions or requests about your privacy: {EMAIL}</p>
<p>This policy is also available in <a href="/ja/lift/privacy.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

TERMS = f'''
<h1>Terms of Service</h1>
<p class="updated">Last updated: {UPDATED}</p>

<p>These terms apply to your use of Lift, a workout log web app made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). By using Lift, you agree to these terms. If you don't agree, please don't use it.</p>

<div class="card">
  <p><strong>The short version:</strong> Lift is a training log, not medical advice or coaching. Its suggested weights are worked out from your own log by fixed rules, and you decide what to lift. Your log is yours: you can export it or delete it at any time. Lift is free. Lift Pro is an optional paid plan that builds workouts for you.</p>
</div>

<h2>Suggestions are not medical advice or coaching</h2>
<p>Lift records what you tell it and suggests a next weight from those records. It does not know your health, your injuries, your technique or how a set felt. A suggested weight, a set target or a body measurement range is information, not medical, fitness or nutrition advice.</p>
<p>Training with weights can cause injury. Talk to a doctor before starting or changing a training programme if you have any health concern. Use equipment the way your gym instructs, stop if something hurts, and lift within your ability. You are responsible for your own training and safety.</p>
<p>The same applies to workouts generated with Lift Pro. They are written by an AI model from the choices you make and the exercises in the app. The model can be wrong, and it does not know your body. Read a generated routine before you save it, change anything that doesn't suit you, and don't rely on it to work around an injury.</p>

<h2>Who can use Lift</h2>
<p>You must be at least 13 years old to use Lift. If you are under the age of majority where you live, you need a parent or guardian's permission.</p>

<h2>Your account</h2>
<ul>
  <li>Signing in is optional and uses Google Sign-In. Lift works without an account.</li>
  <li>Keep your sign-in secure. You are responsible for activity on your account.</li>
  <li>You can delete your account at any time with Settings &gt; Delete account. This can't be undone.</li>
</ul>

<h2>Your log</h2>
<p>Everything you record in Lift belongs to you. You give us permission to store and sync it only as needed to run the app for you, as described in our <a href="/lift/privacy.html">Privacy Policy</a>.</p>
<p>If you don't sign in, your log exists only on your device. Clearing your browser's data, removing the app or losing the device will lose it. Sign in, or save a copy with Settings &gt; Export everything, if it matters to you.</p>

<h2>Acceptable use</h2>
<p>Please don't:</p>
<ul>
  <li>use Lift for anything unlawful;</li>
  <li>access other people's data without permission, or interfere with the app or its servers;</li>
  <li>use automated tools to store data in bulk or otherwise overload the service;</li>
  <li>copy or resell Lift, except where the law allows it.</li>
</ul>
<p>We may suspend or close an account that breaks these terms. Where reasonable, we will tell you first and give you a chance to fix the problem.</p>

<h2>Lift Pro</h2>
<ul>
  <li><strong>What it is:</strong> an optional subscription that lets you generate workouts from the exercise library, up to 40 a month. Everything else in Lift stays free.</li>
  <li><strong>Price:</strong> ¥480 a month, including consumption tax. Payment is by card through Stripe.</li>
  <li><strong>Renewal:</strong> it starts as soon as payment completes and renews every month until you cancel.</li>
  <li><strong>Cancelling:</strong> cancel at any time in Settings &gt; Manage subscription. You keep Lift Pro until the end of the period you have paid for, and you are not charged again.</li>
  <li><strong>Refunds:</strong> payments aren't refunded for partly used periods, except where the law requires it or the service was unavailable because of a fault on our side.</li>
  <li><strong>Seller details:</strong> see the <a href="/lift/tokushoho.html">notice under the Act on Specified Commercial Transactions</a>.</li>
  <li><strong>Changes:</strong> if the price changes, we will tell you before your next renewal, and you can cancel before it applies.</li>
</ul>

<h2>Changes and availability</h2>
<p>Lift is free to use, and Lift Pro is optional. We work to keep it running, but we can't promise it will always be available or free of errors, and we may change or stop it. If we stop offering Lift, we will give reasonable notice where we can, so you can export your log.</p>

<h2>Disclaimer and limit of liability</h2>
<p>To the extent the law allows, Lift is provided "as is", without any promise that its suggestions are right for you, and we are not liable for any injury, loss or damage that results from how you train, or for a log that is lost. Nothing in these terms limits liability for our intentional misconduct or gross negligence, or any rights you have under consumer protection laws that can't be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Japan. If you are a consumer, you also keep the protection of any mandatory laws of the country where you live.</p>

<h2>Changes to these terms</h2>
<p>If we change these terms, we will update the date at the top. If you keep using Lift after a change, the new terms apply.</p>

<h2>Contact</h2>
<p>Questions about these terms: {EMAIL}</p>
<p>These terms are also available in <a href="/ja/lift/terms.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

SUPPORT = f'''
<h1>Support</h1>
<p class="updated">We're happy to help.</p>

<div class="card">
  <h3>Contact us</h3>
  <p>Email {SUPPORT_EMAIL}. We usually reply within two business days. Please tell us which phone and browser you use, and what you were doing when the problem happened.</p>
</div>

<h2>Getting started</h2>

<h3>How do I start?</h3>
<p>Open Lift. Sign in with Google, or tap "Continue without an account"; you can sign in later from Settings. Then tap New routine and add your machines in the order you use them. Or tap "Start from a sample machine circuit" for a ten-station routine you can edit. Then tap Start workout.</p>

<h3>How do I put Lift on my home screen?</h3>
<p>On iPhone, open Lift in Safari, tap the Share button, then Add to Home Screen. On Android, open it in Chrome, tap the menu, then Add to Home screen or Install app. Lift then opens full screen like any other app.</p>

<h3>Do I need an account?</h3>
<p>No. Lift works fully without one, and everything is saved on your device. Signing in is only for backing up your log and using it on more than one device.</p>

<h3>Does it work without a connection?</h3>
<p>Yes. After the first visit Lift opens and saves with no signal. If you are signed in, anything you log offline is synced when you are back online.</p>

<h2>Logging a workout</h2>

<h3>How do I log a set?</h3>
<p>The weight and reps from last time are already filled in. Tap the check to log the set and start the rest timer. To change a number, tap it first.</p>

<h3>How do I skip a set or a station?</h3>
<p>Tap the set number to mark that set as skipped, or tap Skip at the top of a station to skip all of it. Skipped sets are recorded as skipped. They are left out of your averages and out of the next suggestion.</p>

<h3>I closed the app in the middle of a workout</h3>
<p>Open it again. Lift returns to the station you were on, with your sets, the clock and the rest timer as you left them.</p>

<h3>How do I fix a past workout, or add one I forgot to log?</h3>
<p>Open History, tap the session, then tap Edit this session. To add an old workout, tap "Log a past workout" in History and choose its date.</p>

<h3>My exercise isn't in the list</h3>
<p>Type its name in the search box when you add an exercise. If nothing matches, Lift offers to create it.</p>

<h2>Suggested weights</h2>

<h3>Where does the suggested weight come from?</h3>
<p>From your own log for that machine: what you lifted last time, whether every set reached the target, and whether you have been stuck at the same weight. Tap Why on the suggestion to see the sessions and the rule it used.</p>

<h3>The suggestion isn't right for me today</h3>
<p>Type the weight you want. A suggestion never locks you in, and next time Lift works from what you actually did.</p>

<h3>The weight goes up by the wrong amount</h3>
<p>Machines differ. Tap Edit on the routine and change Step for that exercise to match its weight stack.</p>

<h2>Sync and accounts</h2>

<h3>How do I back up my log, or use it on two devices?</h3>
<p>Open Settings and tap "Sign in with Google". Your log is backed up, and kept in step on every device where you sign in with the same account.</p>

<h3>What happens when I sign out?</h3>
<p>Lift asks whether to keep your log on that device or remove it from the device. Nothing is deleted from your account either way.</p>

<h3>Someone else signed in on my device</h3>
<p>If a different Google account signs in on a device that already holds a log, Lift asks before it does anything. It never mixes two people's logs.</p>

<h3>Settings says "Not syncing"</h3>
<p>Your log is still saved on the device. Check your connection, then open Settings and tap Sync to try again.</p>

<h3>How do I delete my account?</h3>
<p>Open Settings and tap Delete account. This deletes everything synced for your account, and the sign-in itself. For your security it only works shortly after signing in, so you may be asked to sign out and sign in again first. The copy on your device is kept; use "Reset all data" to remove that too. If you can't sign in, email us from the address on your account and we will delete it for you.</p>

<h2>Lift Pro</h2>

<h3>What is Lift Pro?</h3>
<p>An optional subscription, ¥480 a month. It adds "Generate with AI": pick a goal, a time and your equipment, add a note if you like, and Lift builds a routine from the exercise library. Each exercise comes with the reason it was chosen. Nothing is saved until you tap Save, and you can change anything first. Logging, suggested weights and sync stay free.</p>

<h3>How do I subscribe?</h3>
<p>Sign in, then tap "Generate with AI" on the home screen, or "Get Lift Pro" in Settings. Payment is by card on a page run by Stripe.</p>

<h3>How do I cancel, or change my card?</h3>
<p>Open Settings and tap "Manage subscription". You keep Lift Pro until the end of the period you have paid for.</p>

<h3>I've used all my workouts for the month</h3>
<p>Lift Pro includes 40 generated workouts a month. The count starts again on the 1st. Routines you have already saved are yours to keep and use.</p>

<h2>Your data</h2>

<h3>How do I save a copy of my data?</h3>
<p>Settings &gt; Export everything saves your routines, sessions, measurements and settings as one file. "Import a backup" puts a saved file back.</p>

<h3>How do I erase everything?</h3>
<p>Settings &gt; Reset all data deletes every routine, session and measurement on the device, and in your account too if you are signed in.</p>

<p>For the details, read our <a href="/lift/privacy.html">Privacy Policy</a>.</p>
'''

TOKUSHOHO = f'''
<h1>Notice under the Act on Specified Commercial Transactions</h1>
<p class="updated">Last updated: {UPDATED}</p>

<p>This notice covers Lift Pro, the paid subscription in Lift. The Japanese version, <a href="/ja/lift/tokushoho.html" lang="ja" hreflang="ja">特定商取引法に基づく表記</a>, is the legal notice; this page is a translation.</p>

<h2>Seller</h2>
<p>Joseph Torin Suzuki-Parker (trading as SP Digital Labs)</p>

<h2>Person responsible</h2>
<p>Joseph Torin Suzuki-Parker</p>

<h2>Address</h2>
<p>Chiba, Japan. The full address is disclosed without delay on request.</p>

<h2>Phone number</h2>
<p>Disclosed without delay on request. Please contact us by email.</p>

<h2>Email</h2>
<p>{SUPPORT_EMAIL}</p>

<h2>Price</h2>
<p>Lift Pro monthly plan: ¥480 (tax included)</p>

<h2>Other charges</h2>
<p>You pay your own internet connection costs.</p>

<h2>Payment method</h2>
<p>Credit or debit card, processed by Stripe.</p>

<h2>When you are charged</h2>
<p>The first month is charged when you subscribe. After that it renews and is charged automatically every month.</p>

<h2>When the service starts</h2>
<p>As soon as payment completes.</p>

<h2>Cancelling</h2>
<p>Cancel at any time in the app under Settings &gt; Manage subscription. You keep Lift Pro until the end of the period you have paid for, and you are not charged from the next renewal date.</p>

<h2>Returns and refunds</h2>
<p>Because this is a digital service, payments aren't refunded once you have subscribed, except where the law requires it or the service could not be provided because of a fault on our side.</p>

<h2>Supported environment</h2>
<p>A current version of Chrome, Safari, Edge or Firefox, on iPhone, Android or a computer.</p>

<p>See also the <a href="/lift/terms.html">Terms of Service</a> and <a href="/lift/privacy.html">Privacy Policy</a>.</p>
'''

OVERVIEW = hero("lift", "Web app",
    "Log the set in one tap. Know the next weight.",
    "Lift is a workout log for people who train on machines, one station after another. Your numbers from last time are already filled in, so logging a set is a single tap, and that same tap starts the rest timer. Before each station it suggests a weight from your own history and shows you why.",
    f'<a class="button" href="{APP}/">Open Lift' + EXTERNAL + '</a><span class="label">Free · No account needed</span>') + """

<section aria-label="Main features">
""" + feature_rows([
    ("/assets/screens/lift-log.jpg", "A workout on station 5 of 10, the chest press. Two of three sets are ticked and a rest timer is counting down.", "One tap logs the set", "Last session's weights and reps are filled in before you sit down. Tap the check and the set is logged and the rest timer starts. Change a number only when it changed. You can skip a set or a whole station, and Lift records it as skipped, not as a zero."),
    ("/assets/screens/lift-why.jpg", "A suggested weight of 47.5 kg for the pec deck, opened to show why: last time the final set dropped to 37.5 kg, so keep the weight and finish the last set.", "A suggestion that shows its reasoning", "Before each station Lift suggests a weight from what you actually did. Reach the target on every set and it adds one step. Fall short on the last set and it holds. Stay stuck for several sessions and it eases off. Tap Why to see the sessions and the rule it used. It is only a suggestion: type another number and Lift goes with yours."),
    ("/assets/screens/lift-history.jpg", "The history of the chest press: working weight rising from 45 kg to 52.5 kg over five weeks, with each session's sets listed below.", "Every machine, over time", "Pick a machine and see its working weight session by session, with every set underneath. Stats counts your hard sets for each muscle over the last seven days against a range you set, which says more about a week of training than a total of kilograms does."),
    ("/assets/screens/lift-ja.jpg", "The same workout screen in Japanese, with the English name of the exercise shown under the Japanese one.", "English and Japanese", "Switch the whole app between English and Japanese, coaching notes included. Lift can also show both at once, with the second language under each exercise name. That helps when the label on the machine is in the other one."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([
    ('It remembers the seat', 'Note the seat and pad positions once. They are waiting at the same machine next session, like the setup column on a paper record sheet.'),
    ('Works with no signal', 'Everything is saved on your phone first, so it works in a basement gym. A workout in progress survives the app being closed.'),
    ('Opens like an app', 'Add Lift to your home screen from your browser and it opens full screen, with nothing to install from a store.'),
    ('Sync if you want it', 'Sign in with Google to back up your log and use it on your other devices. Without an account, nothing leaves your phone.'),
    ('Body measurements', 'Enter the numbers from an InBody result sheet, or just your bodyweight, and follow weight, body fat and muscle over time.'),
    ('Your data is yours', 'Export everything as a file whenever you like. Delete your account, and everything synced with it, from Settings.'),
    ('Lift Pro, if you want it', 'An optional ¥480 a month. Pick a goal, a time and your equipment and get a routine built from the exercise library, with the reason for every exercise.'),
]) + f"""
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/lift/support.html">Support</a></li>
    <li><a href="/lift/privacy.html">Privacy Policy</a></li>
    <li><a href="/lift/terms.html">Terms of Service</a></li>
    <li><a href="/lift/tokushoho.html">Notice under the Act on Specified Commercial Transactions</a></li>
    <li>Lift is a training log, not medical advice or coaching.</li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("Lift", "A workout log for machine training: one tap logs the set and starts the rest timer, and it suggests your next weight and shows why. English and Japanese. Free.", OVERVIEW, "en", "wrap app-page"),
    "support.html": ("Support", "Help with Lift: getting started, logging a workout, suggested weights, sync and your data.", SUPPORT, "en", "wrap page"),
    "privacy.html": ("Privacy Policy", "Lift works without an account and keeps your log on your device. If you sign in, it is synced through Google Firebase. No analytics or ads.", PRIVACY, "en", "wrap page"),
    "tokushoho.html": ("Specified Commercial Transactions notice", "Seller, price, payment, cancellation and refund details for Lift Pro, as required by Japan's Act on Specified Commercial Transactions.", TOKUSHOHO, "en", "wrap page"),
    "terms.html": ("Terms of Service", "The terms for using Lift, a free workout log. Its suggestions are not medical advice or coaching.", TERMS, "en", "wrap page"),
}


def build(root):
    build_pages(root, "lift", PAGES, PAGES_JA)
