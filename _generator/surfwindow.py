from icons import EXTERNAL
from chrome import EMAIL, hero, features, shots, feature_rows, build_pages
from surfwindow_ja import PRIVACY_JA, TERMS_JA

PRIVACY = f'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: November 5, 2026 · <a href="/surfwindow/privacy-ja.html" lang="ja" hreflang="ja">日本語</a></p>

<p>Surf Window is a surf forecast web app for breaks in Shonan and Chiba, at surfwindow.jp, made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what information Surf Window collects, why, who it is shared with, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> you can use Surf Window without an account. If you sign in with Google, we keep your saved breaks and the handle you choose. Surf reports you post are public under your handle. Your location stays on your device and is only used to show distances and to check you're at the beach before you report. We use PostHog analytics, including session recordings, to see how the app is used and fix problems. We don't show ads or sell your data.</p>
</div>

<h2>Information we collect</h2>

<h3>If you sign in</h3>
<ul>
  <li>Signing in is optional and uses <strong>Google Sign-In</strong>. We receive a <strong>user ID</strong> from Firebase Authentication. Your email address is shown to you in the app but is not saved in our database.</li>
  <li>We store the breaks you <strong>track</strong> and have <strong>checked</strong>, and your <strong>handle</strong>: a short public name that starts as the first word of your Google name and that you can change.</li>
</ul>

<h3>Surf reports</h3>
<ul>
  <li>When you post a report, we store your rating of the conditions, the wave size, up to four tags (such as glassy or crowded), an optional short note, the break and hour, your handle and your user ID.</li>
  <li><strong>Reports are public.</strong> Anyone using Surf Window can see your handle, rating and note. Your user ID is stored with the report. Your email address is never shown.</li>
  <li>You can post one report per break per hour, and you can delete your own reports in the app.</li>
</ul>

<h3>Suggestions</h3>
<p>If you send a suggestion or correction, we store what you wrote, which break it is about, your handle and your user ID. Only we can read it.</p>

<h3>Your location</h3>
<ul>
  <li>Surf Window asks for your location only when you tap to use it. It is used on your device to show how far each break is and to check that you are at the beach before you post a report.</li>
  <li>Your location is not saved and is not sent to us, to our analytics or to the forecast services. Reports don't include your location or distance; we only check, on your device, that you were near the beach.</li>
  <li>Tap the location button again to stop using it.</li>
</ul>

<h3>Analytics and session recordings</h3>
<ul>
  <li>We use <strong>PostHog</strong> to understand how Surf Window is used and to find errors. It records the pages you view, actions such as opening a break, signing in or posting a report (but not your handle or note), and errors the app hits.</li>
  <li>PostHog also makes <strong>session recordings</strong>: replays of how the app was used, built from what was on screen. Anything you type is hidden, and your email address, your position on the map, your distance from each break, and lists ordered by distance are left out of recordings. Other text on screen, such as forecasts and public reports, can appear in them.</li>
  <li>When you sign in, PostHog links your activity to your user ID, not your name or email. Without signing in, it uses a random identifier stored in your browser.</li>
  <li>Coordinates are removed from analytics events before they are sent.</li>
</ul>

<h3>Device and browser</h3>
<ul>
  <li>Your tracked and checked breaks are saved in your browser, so the app works without signing in and offline.</li>
  <li>The app stores itself and its fonts in your browser so it loads quickly and can be added to your home screen.</li>
  <li>Forecasts come straight from <strong>Open-Meteo</strong>, and the wind map is an embedded map from <strong>Windy</strong>. Fonts load from <strong>Google Fonts</strong>. Because your browser contacts these services directly, they receive your IP address. They are only told the location of the break, never yours.</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To run Surf Window: show forecasts, keep your saved breaks in sync across devices, and show surf reports.</li>
  <li>To check that reports come from people at the beach.</li>
  <li>To understand how the app is used, fix errors and improve it.</li>
  <li>To read and act on your suggestions.</li>
</ul>
<p>We don't use your information for advertising, and we don't sell it.</p>

<h2>Where it is stored</h2>
<p>Account data, reports and suggestions are stored in Google Firebase (Authentication and Cloud Firestore), and the app is hosted on Firebase Hosting. Analytics are stored by PostHog in the United States. These services may store and process data in the United States or other countries. Data is encrypted in transit and at rest.</p>

<h2>Who we share it with</h2>
<ul>
  <li><strong>Google Firebase</strong>, which hosts the app and stores account data, reports and suggestions. <a href="https://firebase.google.com/support/privacy">Firebase privacy</a></li>
  <li><strong>Google</strong>, for Google Sign-In and Google Fonts. <a href="https://policies.google.com/privacy">Google privacy</a></li>
  <li><strong>PostHog</strong>, for analytics and session recordings. <a href="https://posthog.com/privacy">PostHog privacy</a></li>
  <li><strong>Open-Meteo</strong> and <strong>Windy</strong>, which your browser contacts for forecasts and the wind map. <a href="https://open-meteo.com/en/terms">Open-Meteo terms</a> · <a href="https://account.windy.com/agreements/windy-privacy-policy">Windy privacy</a></li>
  <li>Everyone using Surf Window, who can see the reports you post under your handle.</li>
</ul>
<p>We may also disclose information if the law requires it.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Your saved breaks and handle are kept until you delete your account.</li>
  <li>Reports are shown in the app for three hours and kept until you or we delete them.</li>
  <li>Suggestions are kept until we have dealt with them or you delete your account.</li>
  <li>Analytics and session recordings are kept for the period PostHog's plan allows, then deleted.</li>
</ul>

<h2>Your choices and rights</h2>
<ul>
  <li>Use Surf Window without signing in, and without sharing your location.</li>
  <li>Change your handle, or delete any of your reports, in the app.</li>
  <li>Signing out clears your saved breaks and handle from that browser.</li>
  <li>Delete your account with <strong>アカウント削除 Delete account</strong> at the bottom of the app while signed in. This permanently deletes your account, saved breaks, handle, the reports you posted and the suggestions you sent. If you can't sign in, email us and we will delete them within 30 days.</li>
  <li>Depending on where you live, you may have further rights, such as to see, correct or object to how we use your information, or to complain to a data protection authority. Contact us and we will help.</li>
</ul>

<h2>Children</h2>
<p>Surf Window is not directed at children under 13, and we don't knowingly collect their information. If you believe a child has given us information, contact us and we will delete it.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top.</p>

<h2>Contact</h2>
<p>Questions or requests about your privacy: {EMAIL}</p>
'''

TERMS = f'''
<h1>Terms of Service</h1>
<p class="updated">Last updated: November 5, 2026 · <a href="/surfwindow/terms-ja.html" lang="ja" hreflang="ja">日本語</a></p>

<p>These terms apply to your use of Surf Window, a surf forecast web app made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). By using Surf Window, you agree to these terms. If you don't agree, please don't use it.</p>

<div class="card">
  <p><strong>The short version:</strong> Surf Window's scores are estimates from forecast data, not a promise that it's safe to surf. Check the conditions yourself, know your limits, and follow local rules and lifeguards. Reports you post are public under your handle, so keep them honest and kind. Surf Window is free.</p>
</div>

<h2>Forecasts are estimates, not safety advice</h2>
<p>Surf Window scores each break by comparing forecast data with a profile of that beach. Forecasts can be wrong, conditions change quickly, and break profiles and hazard notes may be incomplete. Surf reports come from other users and may be inaccurate.</p>
<p>Surfing is dangerous. Nothing in Surf Window, including a good score, a level label or a report, means it is safe for you to go in the water. Always look at the conditions yourself before you paddle out, surf within your ability, and follow lifeguards, warning flags and local rules. You are responsible for your own safety.</p>

<h2>Who can use Surf Window</h2>
<p>You must be at least 13 years old to sign in to Surf Window or post reports.</p>

<h2>Your account</h2>
<p>Signing in is optional and uses Google Sign-In. You are responsible for activity on your account. You can delete your account at any time with <strong>アカウント削除 Delete account</strong> at the bottom of the app.</p>

<h2>Reports and suggestions</h2>
<ul>
  <li>Reports are public and show your handle. Post only what you saw at the beach, and keep notes and handles respectful.</li>
  <li>Don't post anything unlawful, offensive or misleading, or personal information about anyone.</li>
  <li>You keep ownership of what you post. You give us permission to store and show your reports in Surf Window, and to use your suggestions to improve the app.</li>
  <li>We may remove reports or handles that break these terms.</li>
</ul>

<h2>Acceptable use</h2>
<p>Please don't:</p>
<ul>
  <li>use Surf Window for anything unlawful;</li>
  <li>post reports for a beach you aren't at, or try to get around the location check;</li>
  <li>interfere with the app or its servers, or scrape its data in bulk;</li>
  <li>copy or resell Surf Window, except where the law allows it.</li>
</ul>
<p>We may suspend an account that breaks these terms.</p>

<h2>Data sources</h2>
<p>Forecasts come from Open-Meteo, licensed under CC BY 4.0. The wind map is provided by Windy. Coastline data comes from Natural Earth. Break profiles are written by us.</p>

<h2>Changes and availability</h2>
<p>Surf Window is free. We work to keep it running, but we can't promise it will always be available, up to date or free of errors, and we may change or stop it at any time.</p>

<h2>Disclaimer and limit of liability</h2>
<p>To the extent the law allows, Surf Window is provided "as is", without any promise that its forecasts, scores or reports are accurate, and we are not liable for any injury, loss or damage that results from decisions you make using it. Nothing in these terms limits liability for our intentional misconduct or gross negligence, or any rights you have under consumer protection laws that can't be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Japan. If you are a consumer, you also keep the protection of any mandatory laws of the country where you live.</p>

<h2>Changes to these terms</h2>
<p>If we change these terms, we will update the date at the top. If you keep using Surf Window after a change, the new terms apply.</p>

<h2>Contact</h2>
<p>Questions about these terms: {EMAIL}</p>
'''

OVERVIEW = hero("surfwindow", "Web app · Free",
    "Is it worth going, and when?",
    "Surf Window scores live swell, wind and tide against the profile of each of 25 breaks in Shonan and Chiba. You get a number for every hour, and the reason behind it. In Japanese and English.",
    '<a class=\"button\" href=\"https://surfwindow.jp/\">Open Surf Window' + EXTERNAL + '</a><span class="label">No account needed</span>') + """

<section aria-label="Main features">
""" + feature_rows([
    ("/assets/screens/surfwindow-home.jpg", "Surf Window home screen listing saved breaks with scores.", "A score for every break", "Surf Window covers 25 surf spots in Shonan and Chiba. For each one, it checks the latest forecast for waves, wind and tide, and compares it with what that particular beach needs to be good. Every hour gets a score out of 100 and a short, plain sentence saying what's helping and what's holding the waves back."),
    ("/assets/screens/surfwindow-break.jpg", "A break page with a wind and swell map, the swell window and a tide curve.", "See the swell window", "Every beach faces its own direction. Waves from some directions reach it, while headlands and bays block the rest. Surf Window draws this swell window on a live map of wind and waves, so you can see why one beach is working today while the one next to it is flat."),
    ("/assets/screens/surfwindow-forecast.jpg", "Forecast tab with daily wave heights and a seven-day chart.", "Seven days, hour by hour", "The forecast tab lays out the next seven days hour by hour: wave size at the beach, the time between waves (the period), wind, tide and wave power, all on one timeline. Surf Window also picks out the best times of the week for you, so you don't have to work them out yourself."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([('Reports from the sand', "Surfers at the beach report what it's really doing in three taps, shown beside the forecast."),
    ('Honest about danger', 'Hours for experts only are flagged, and every break has notes on its hazards.'),
    ('Japanese and English', 'Every screen is in both languages. No account needed, and your location stays on your phone.')]) + f"""
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/surfwindow/privacy.html">Privacy Policy</a> · <a href="/surfwindow/privacy-ja.html" lang="ja">プライバシーポリシー</a></li>
    <li><a href="/surfwindow/terms.html">Terms of Service</a> · <a href="/surfwindow/terms-ja.html" lang="ja">利用規約</a>. Scores are estimates, not safety advice.</li>
    <li>Delete your account with アカウント削除 (Delete account) at the bottom of the app.</li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("Surf Window", "Go or no-go surf scores for 25 breaks in Shonan and Chiba. Free, in Japanese and English.", OVERVIEW, "en", "wrap app-page"),
    "privacy.html": ("Privacy Policy", "How Surf Window collects, uses and protects your information.", PRIVACY, "en", "wrap page"),
    "terms.html": ("Terms of Service", "The terms for using Surf Window.", TERMS, "en", "wrap page"),
    "privacy-ja.html": ("プライバシーポリシー", "Surf Window が取得する情報、その利用目的と提供先、お客様が選べること。", PRIVACY_JA, "ja", "wrap page"),
    "terms-ja.html": ("利用規約", "Surf Window の利用規約。予報は目安であり、安全の保証ではありません。", TERMS_JA, "ja", "wrap page"),
}

def build(root):
    build_pages(root, "surfwindow", PAGES)
