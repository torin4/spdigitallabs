from chrome import EMAIL, hero, features, feature_rows_wide, build_pages
from tuck_ja import PAGES_JA

SUPPORT_EMAIL = EMAIL.replace('class="email"', 'class="email" data-subject="Tuck support"')

PRIVACY = f'''
<h1>Privacy Policy</h1>
<p class="updated">Last updated: November 11, 2026</p>

<p>Tuck is a clipboard manager for Mac made by SP Digital Labs, the name under which Joseph Suzuki-Parker, an independent developer based in Japan, publishes apps ("we", "us"). This policy explains what Tuck keeps, where it keeps it, and the choices you have.</p>

<div class="card">
  <p><strong>The short version:</strong> Tuck collects nothing. It has no account, no sync, no analytics and no ads, and it never connects to the internet. Your clipboard history is stored only on your Mac, and you can delete it at any time.</p>
</div>

<h2>Information we collect</h2>
<p>None. Tuck does not send anything to us or to anyone else. We cannot see what you copy, how you use the app, or that you use it at all.</p>

<h2>What Tuck keeps on your Mac</h2>
<ul>
  <li><strong>Your clipboard history:</strong> the text, file paths and images you copy, with the name of the app each came from and the time.</li>
  <li><strong>Screenshots:</strong> if you choose a screenshot folder in Settings, new screenshots saved there are added to the history. Tuck can only read the folder you choose, and only reads it.</li>
  <li><strong>Text in images:</strong> Tuck recognizes the text in images so you can search for them. This is done on your Mac by macOS. The image is not sent anywhere.</li>
  <li><strong>Your settings:</strong> your shortcut, layout, history limits and the list of apps Tuck should never record from.</li>
</ul>
<p>All of this is stored in Tuck's own folder on your Mac. It is not uploaded, backed up to us, or shared between your devices. If you back up your Mac, for example with Time Machine, the history is included in that backup like your other files.</p>

<h2>Passwords and other secrets</h2>
<ul>
  <li>Anything a password manager marks as hidden is skipped and never recorded.</li>
  <li>Copies made in the apps listed under Settings &gt; Privacy are not recorded. Common password managers are on that list from the start, and you can add any app.</li>
  <li>Text that looks like a password, API key or access token is held in memory only. It is shown masked, is never written to disk, and is forgotten after 10 minutes or when Tuck quits.</li>
  <li>Text recognized in an image is not kept if it looks like a secret.</li>
</ul>
<p>This detection is a safeguard, not a guarantee. A secret in an unusual form may be recorded like any other text, so add the apps you copy sensitive things from to the list.</p>

<h2>Permissions Tuck asks for</h2>
<ul>
  <li><strong>Accessibility:</strong> used only to press Cmd+V for you, so the clip you pick is pasted into the app you were in. Tuck does not read your screen or what you type. Without this permission, Tuck puts the clip on the clipboard and you paste it yourself.</li>
  <li><strong>A folder you choose:</strong> used only to notice new screenshots.</li>
</ul>

<h2>How long it is kept</h2>
<p>Tuck keeps the most recent clips up to the limits in Settings &gt; History (1,000 clips and 200 images unless you change them) and drops older ones. Clips you pin are kept until you unpin or delete them.</p>

<h2>Deleting your data</h2>
<ul>
  <li>Delete one clip by selecting it and pressing Cmd+Delete.</li>
  <li>Delete the history with Settings &gt; History &gt; Clear History. Pinned clips are kept; delete those one by one.</li>
  <li>Deleting Tuck and its data from your Mac removes everything. There is nothing for us to delete, because we never had it.</li>
</ul>

<h2>Who we share it with</h2>
<p>No one. We don't have your data, we don't sell data, and Tuck contains no third-party analytics or advertising code.</p>
<p>If you have chosen to share diagnostics with app developers in macOS, Apple may give us crash reports and usage statistics that do not identify you. You can turn this off in System Settings &gt; Privacy &amp; Security &gt; Analytics &amp; Improvements.</p>

<h2>Children</h2>
<p>Tuck collects no information from anyone, including children.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we will update the date at the top.</p>

<h2>Contact</h2>
<p>Questions about your privacy: {EMAIL}</p>
<p>This policy is also available in <a href="/ja/tuck/privacy.html" lang="ja" hreflang="ja">Japanese</a>. If the two versions differ, the English version applies.</p>
'''

SUPPORT = f'''
<h1>Support</h1>
<p class="updated">We're happy to help.</p>

<div class="card">
  <h3>Contact us</h3>
  <p>Email {SUPPORT_EMAIL}. We usually reply within two business days. Please include your macOS version and what you were doing when the problem happened. Never send anything you copied that is private.</p>
</div>

<h2>Getting started</h2>

<h3>How do I open Tuck?</h3>
<p>Press Cmd+Shift+V. Type a few letters to find a clip, then press Return to paste it into the app you were in. You can also open Tuck from its icon in the menu bar. Change the shortcut in Settings &gt; General.</p>

<h3>Tuck opens, but nothing is pasted</h3>
<p>Tuck needs Accessibility access to press Cmd+V for you. Open System Settings &gt; Privacy &amp; Security &gt; Accessibility and turn on Tuck. If it is already on, turn it off and on again. Until then, the clip you pick is placed on the clipboard and you can paste it yourself with Cmd+V.</p>

<h3>The shortcut doesn't open Tuck</h3>
<p>Another app may be using the same shortcut. Open Settings from the menu bar icon and choose a different one under General.</p>

<h3>I hid the menu bar icon. How do I open Settings?</h3>
<p>Open Tuck with the shortcut and press Cmd+, (comma).</p>

<h2>Screenshots</h2>

<h3>My screenshots don't appear</h3>
<p>Open Settings &gt; General &gt; Screenshots and choose the folder macOS saves screenshots to, usually the Desktop. New screenshots saved there are then added to your history.</p>
<p>To skip the files altogether, press Cmd+Shift+5, open Options, and set "Save to" to Clipboard. Every screenshot then goes straight into Tuck.</p>

<h3>How do I find an image?</h3>
<p>Type words that appear in it. Tuck reads the text in images on your Mac, which can take a minute or two for the first image after it starts. Type <code>is:image</code> to list only images.</p>

<h2>Finding and pasting</h2>

<h3>How do I narrow the list?</h3>
<p>Every word you type must appear in the clip. Add <code>app:safari</code> to show clips from one app, or <code>is:text</code>, <code>is:file</code>, <code>is:image</code> or <code>is:pinned</code> to show one kind.</p>

<h3>What are the ways to paste?</h3>
<ul>
  <li><strong>Return:</strong> paste cleaned, without terminal color codes, trailing spaces or shared indentation</li>
  <li><strong>Option+Return:</strong> paste exactly as copied</li>
  <li><strong>Cmd+Return:</strong> paste wrapped in a code fence</li>
  <li><strong>Shift+Return:</strong> paste the text recognized in an image</li>
  <li><strong>Tab:</strong> mark several clips, then Return pastes them as one block</li>
</ul>
<p>Turn the cleaning off under Settings &gt; Panel.</p>

<h3>How do I keep a clip?</h3>
<p>Select it and press Cmd+P to pin it. Pinned clips are never dropped. A pinned clip containing <code>{{clipboard}}</code> is a template: pasting it fills in whatever is on the clipboard at that spot.</p>

<h2>Your data</h2>

<h3>Does Tuck record my passwords?</h3>
<p>Copies from password managers are skipped, and text that looks like a password or key is held in memory only and forgotten after 10 minutes. Add any other app Tuck should never record from under Settings &gt; Privacy.</p>

<h3>How do I delete my history?</h3>
<p>Press Cmd+Delete to delete the selected clip, or use Settings &gt; History &gt; Clear History to delete everything except pinned clips.</p>

<h3>Is my history synced or uploaded?</h3>
<p>No. Tuck never connects to the internet. Your history stays on your Mac.</p>

<p>For the details, read our <a href="/tuck/privacy.html">Privacy Policy</a>.</p>
'''

OVERVIEW = hero("tuck", "Mac app",
    "Everything you copied, one shortcut away.",
    "Tuck is a clipboard manager for Mac that stays out of sight. It remembers the text, files, images and screenshots you copy, and shows them only when you press the shortcut. Type a few letters, press Return, and it's pasted.",
    '<span class="label">Coming soon to the Mac App Store</span>') + """

<section aria-label="Main features">
""" + feature_rows_wide([
    ("/assets/screens/tuck-history.jpg", "The Tuck panel listing recent clips: text, code, a file and an image, with the selected clip shown in full below.", "Your history, one shortcut away", "Press Cmd+Shift+V and everything you copied is there: text, code, files and images, newest first. The pane under the list shows the selected clip in full. Press Return and it's pasted into the app you were in, then Tuck gets out of the way."),
    ("/assets/screens/tuck-search.jpg", "Searching for the word git finds a git command and an image whose text contains the word.", "Find it by typing, even inside a screenshot", "Type a few letters and the list narrows as you go. Tuck reads the text in images on your Mac, so a screenshot turns up when you type a word that appears in it. Narrow further by the app a clip came from, or by kind: text, file, image or pinned."),
    ("/assets/screens/tuck-settings.jpg", "Tuck settings for the panel: floating or docked layout, keep open, the strip, and paste cleaning.", "Set it up your way", "Keep Tuck as a floating panel that appears where you left it, or dock it to the edge of the screen as a sidebar. Add a small strip that shows the newest clip, choose your own shortcut, and decide how pasted text is cleaned up."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([
    ('Paste it clean', 'Strip terminal color codes, trailing spaces and extra indentation, wrap code in a fence, or paste exactly as copied.'),
    ('Pins and templates', 'Pin what you reuse. A pinned clip can have a blank that Tuck fills with whatever is on the clipboard.'),
    ('Private by design', 'Password managers are skipped and secrets are never written to disk. No account, no sync, and nothing leaves your Mac.'),
]) + f"""
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/tuck/support.html">Support</a></li>
    <li><a href="/tuck/privacy.html">Privacy Policy</a></li>
    <li>Requires macOS 13 or later.</li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("Tuck", "A clipboard manager for Mac that stays out of sight until you press the shortcut. Nothing leaves your Mac.", OVERVIEW, "en", "wrap app-page"),
    "support.html": ("Support", "Help with Tuck: opening it, pasting, screenshots and your history.", SUPPORT, "en", "wrap page"),
    "privacy.html": ("Privacy Policy", "Tuck collects nothing. Your clipboard history stays on your Mac.", PRIVACY, "en", "wrap page"),
}


def build(root):
    build_pages(root, "tuck", PAGES, PAGES_JA)
