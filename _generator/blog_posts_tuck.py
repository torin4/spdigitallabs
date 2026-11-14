"""Tuck blog posts. Every statement about how Tuck works is checked against the app's code (../tuck)."""

POSTS = [
{
"app": "tuck",
"slug": "what-is-a-clipboard-manager-mac",
"date": "2026-11-14",
"title": "What a clipboard manager is, and who needs one on a Mac",
"description": "The Mac clipboard holds one thing at a time. What a clipboard history adds, who it suits, who it suits less, and how Tuck does it.",
"body": """
<p class="lede">The Mac clipboard holds one thing. Copy something new and whatever was there before is gone. A clipboard manager keeps a list of what you copied, so you can get an earlier item back.</p>

<h2>What the Mac clipboard keeps</h2>
<p>When you press Cmd+C, macOS puts your selection on the clipboard. Cmd+V pastes it, as many times as you like, until you copy something else. To see what's on it right now, switch to the Finder and choose Edit &gt; Show Clipboard.</p>
<p>That's all it does. In particular:</p>
<ul>
  <li><strong>It has one slot.</strong> The second thing you copy replaces the first. There's no way to ask for the one before.</li>
  <li><strong>It doesn't last.</strong> Whatever is on the clipboard is lost when you restart your Mac.</li>
  <li><strong>You can't search it.</strong> There's only one item, so there's nothing to search.</li>
</ul>
<p>Universal Clipboard lets you copy on an iPhone and paste on a Mac signed in to the same Apple Account, but it's still one item. macOS 26 added a basic clipboard history to Spotlight. It's off until you turn it on, and it keeps items for a limited time before dropping them. On earlier versions of macOS there is no history at all.</p>

<h2>What a history adds</h2>
<h3>You can get back what you overwrote</h3>
<p>The common accident is copying an address, then copying something else on the way to pasting it. With a history, the address is one line down the list. You don't have to go back and find it again.</p>
<h3>You can copy first and paste afterwards</h3>
<p>Moving five things from one document to another normally means ten trips: copy, switch, paste, switch back. With a history you copy all five, switch once, and paste them one after another.</p>
<h3>You can find things by typing</h3>
<p>A list of a thousand clips is only useful if you can find one. A clipboard manager lets you type a few letters and narrows the list to the clips that contain them: the tracking number from this morning, the command you ran last week.</p>
<h3>You can keep the things you reuse</h3>
<p>Some text gets pasted again and again: your address, a standard reply, a long command. Most clipboard managers let you mark those to keep, so they don't drop off the end of the history.</p>

<h2>Who it suits</h2>
<ul>
  <li><strong>People who move text between apps all day.</strong> Support replies, data entry, filling in forms from a spreadsheet, quoting sources into a document.</li>
  <li><strong>Developers.</strong> Commands, error messages, IDs and snippets get copied constantly, and the one you need is often three copies back.</li>
  <li><strong>People who take a lot of screenshots.</strong> A history that keeps images can replace the pile of files on the Desktop. <a href="/blog/mac-screenshots-to-clipboard.html">How to copy Mac screenshots to the clipboard</a> covers that.</li>
  <li><strong>Anyone who has lost a copied paragraph</strong> by copying something else before pasting it.</li>
</ul>

<h2>Who it suits less</h2>
<ul>
  <li><strong>People who copy and paste straight away.</strong> If you rarely need anything but the last thing you copied, one slot is enough.</li>
  <li><strong>People on macOS 26 or later who only need the last few hours.</strong> Try the history in Spotlight first. It may be all you need.</li>
  <li><strong>People who share one Mac user account with someone else.</strong> A history is a record of what you copied, and anyone using that account can open it.</li>
  <li><strong>People who mostly copy sensitive things.</strong> Passwords, keys and other people's personal details are exactly what you don't want kept. A good clipboard manager skips much of this, but none can catch everything. <a href="/blog/is-clipboard-history-safe.html">Is clipboard history safe?</a> goes through what to check.</li>
</ul>

<h2>How Tuck does it</h2>
<p>Tuck is a clipboard manager for Mac from SP Digital Labs. It isn't released yet; it's coming to the Mac App Store and will need macOS 13 or later. This is how it works.</p>
<p>Tuck records the text, files and images you copy while it's running. Nothing appears on screen until you press Cmd+Shift+V, apart from an icon in the menu bar that you can hide in Settings &gt; General. The panel lists your clips newest first, with the selected one shown in full underneath. Type to narrow the list: every word you type must appear in the clip. Press Return and the clip is pasted into the app you were in.</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Keys in the Tuck panel</caption>
  <thead><tr><th scope="col">To do this</th><th scope="col">Press</th></tr></thead>
  <tbody>
    <tr><th scope="row">Paste the selected clip</th><td>Return</td></tr>
    <tr><th scope="row">Paste one of the first nine rows</th><td>Cmd+1 to Cmd+9</td></tr>
    <tr><th scope="row">Paste exactly as copied</th><td>Option+Return</td></tr>
    <tr><th scope="row">Mark several clips to paste together</th><td>Tab</td></tr>
    <tr><th scope="row">Pin or unpin a clip</th><td>Cmd+P</td></tr>
    <tr><th scope="row">Switch between history and pinned clips</th><td>Cmd+/</td></tr>
    <tr><th scope="row">Delete the selected clip</th><td>Cmd+Delete</td></tr>
    <tr><th scope="row">Close the panel</th><td>Esc</td></tr>
  </tbody>
</table>
</div>

<p>A few details that matter in daily use:</p>
<ul>
  <li><strong>Search terms.</strong> Add <code>app:safari</code> to show clips copied in one app, or <code>is:text</code>, <code>is:file</code>, <code>is:image</code> or <code>is:pinned</code> to show one kind. Images are found by the text in them.</li>
  <li><strong>Pasting several at once.</strong> Mark clips with Tab, then press Return. They're pasted as one block, in the order you marked them, with a blank line between each.</li>
  <li><strong>Pins and templates.</strong> Pinned clips are never dropped. A pinned clip containing <code>{clipboard}</code> is a template: pasting it puts whatever text is on the clipboard at that spot.</li>
  <li><strong>Clean pasting.</strong> By default, Return removes terminal color codes, trailing spaces and indentation shared by every line. Option+Return pastes the clip untouched, and you can turn the cleaning off in Settings &gt; Panel.</li>
  <li><strong>No duplicates.</strong> Copy the same thing twice and Tuck keeps one entry and moves it to the top.</li>
</ul>

<h3>Limits worth knowing</h3>
<ul>
  <li><strong>The history has a size.</strong> Tuck keeps the newest 1,000 clips and 200 images unless you change the numbers in Settings &gt; History. Older ones are dropped, except pins.</li>
  <li><strong>Very large copies are skipped.</strong> Text over 1 MB and images over 60 MB are not recorded.</li>
  <li><strong>Files are recorded by location.</strong> When you copy a file in the Finder, Tuck keeps the path to it, not a copy of the file.</li>
  <li><strong>It only records while it's running.</strong> Turn on Launch at login in Settings &gt; General if you want it there every day.</li>
  <li><strong>Pasting for you needs permission.</strong> Tuck needs Accessibility access to press Cmd+V in the app you were in. Without it, the clip you pick is placed on the clipboard and you paste it yourself.</li>
  <li><strong>The shortcut may already be taken.</strong> Some apps use Cmd+Shift+V for pasting without formatting. If you rely on that, choose a different shortcut in Settings &gt; General.</li>
  <li><strong>There is no sync.</strong> Tuck has no account and never connects to the internet, so the history exists on one Mac only.</li>
</ul>
<p>There's more on the <a href="/tuck/">Tuck page</a>, and the <a href="/tuck/support.html">support page</a> lists every way to paste.</p>
""",
},
{
"app": "tuck",
"slug": "mac-screenshots-to-clipboard",
"date": "2026-11-14",
"title": "How to copy Mac screenshots to the clipboard, and find one later by the text in it",
"description": "Send Mac screenshots to the clipboard instead of the Desktop, make that the default, and find an old one by typing words that appear in it.",
"body": """
<p class="lede">Most screenshots are used once: pasted into a message or a document and never opened again. macOS still saves each one as a file on the Desktop. You can send them to the clipboard instead, and with a clipboard history you can still find one later.</p>

<h2>Where screenshots go by default</h2>
<p>Unless you've changed it, every screenshot is saved to the Desktop as a file named with the date and time. That's right for a screenshot you want to keep. For one you only want to paste somewhere, it means an extra step now, dragging the file in, and a file to delete later.</p>

<h2>Copy one screenshot to the clipboard</h2>
<p>Add the Control key to any screenshot shortcut and the picture goes to the clipboard instead of a file. Then press Cmd+V wherever you want it.</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Screenshot shortcuts that copy to the clipboard</caption>
  <thead><tr><th scope="col">Capture</th><th scope="col">Press</th></tr></thead>
  <tbody>
    <tr><th scope="row">The whole screen</th><td>Cmd+Ctrl+Shift+3</td></tr>
    <tr><th scope="row">An area you drag over</th><td>Cmd+Ctrl+Shift+4</td></tr>
    <tr><th scope="row">One window</th><td>Cmd+Ctrl+Shift+4, Space</td></tr>
  </tbody>
</table>
</div>

<p>Without Control, the same shortcuts save a file as usual.</p>
<p>For a window, press the shortcut, then Space, then click the window you want.</p>

<h2>Make the clipboard the default</h2>
<p>If you paste most of your screenshots, you can stop macOS creating files at all:</p>
<ul>
  <li>Press Cmd+Shift+5 to open the screenshot toolbar.</li>
  <li>Click Options.</li>
  <li>Under "Save to", choose Clipboard.</li>
</ul>
<p>From then on, the ordinary shortcuts, Cmd+Shift+3 and Cmd+Shift+4, copy to the clipboard and nothing lands on the Desktop. The setting stays until you change it back in the same menu.</p>
<p>If you'd rather keep files but not on the Desktop, the same menu has Other Location, where you can pick a folder for screenshots.</p>

<h2>The catch: the clipboard holds one thing</h2>
<p>A screenshot on the clipboard is not saved anywhere. Copy anything else, even a single word, and the screenshot is gone. So is the one you took just before it, if you took two in a row.</p>
<p>That's fine for a screenshot you paste within the next few seconds. For anything you might want again, either save it as a file or use a clipboard history, which keeps each copy in a list. <a href="/blog/what-is-a-clipboard-manager-mac.html">What a clipboard manager is, and who needs one on a Mac</a> explains how a history works.</p>

<h2>Finding a screenshot later</h2>
<p>Screenshot files are named by date, so the Finder can show you the one from Tuesday afternoon, if you remember it was Tuesday afternoon. What you usually remember is what was in it: an error message, an order number, a name.</p>
<p>macOS can read text in pictures. Open a screenshot in Preview and you can select and copy the words in it, like text in a document. That helps once you've found the right file. It doesn't help you find it among two hundred others.</p>
<p>A clipboard history that reads the text in each image as it arrives does. You type a word that was on screen, and the screenshots containing it come up.</p>

<h2>Doing it in Tuck</h2>
<p>Tuck is a clipboard manager for Mac that isn't released yet; it's coming to the Mac App Store. It keeps images as well as text, and it reads the text in them.</p>
<h3>Getting screenshots into Tuck</h3>
<p>Tuck records any image that reaches the clipboard. So the Control shortcuts above, and the "Save to: Clipboard" setting, work with no setup: every screenshot you copy is added to your history.</p>
<p>If you prefer to keep saving files, Tuck can pick those up too. In Settings &gt; General, under Screenshots, click Choose Folder and select the folder macOS saves screenshots to, usually the Desktop. New screenshots saved there are then added to the history. The file stays where it is, and Tuck only reads the folder; it has no permission to change it. Screenshots that were already in the folder are not imported, and screen recordings are not added.</p>
<h3>Finding one</h3>
<p>Press Cmd+Shift+V to open Tuck and type words that appear in the screenshot. Every word you type must be in the image's text. Type <code>is:image</code> to list only images, on its own or with other words. The selected image is shown under the list, next to the text Tuck found in it.</p>
<p>The reading is done on your Mac by macOS. The image is not sent anywhere; Tuck never connects to the internet.</p>
<h3>Using it</h3>
<ul>
  <li><strong>Return</strong> pastes the image into the app you were in. In Terminal and several other terminal apps, which only accept text, it pastes the path to the image file.</li>
  <li><strong>Shift+Return</strong> pastes the text found in the image, which saves retyping an error message or a code.</li>
  <li><strong>Cmd+P</strong> pins the image so it's never dropped.</li>
  <li><strong>Cmd+Delete</strong> deletes it.</li>
</ul>

<h3>Limits worth knowing</h3>
<ul>
  <li><strong>An image is found only by its text.</strong> A screenshot of a photo or an unlabeled chart has no words to search for. You'll find it by scrolling, or by listing images with <code>is:image</code>.</li>
  <li><strong>Reading takes a moment.</strong> A new image appears in the list straight away, but it can't be found by its words until the text has been read. Tuck reads images in the background, one at a time.</li>
  <li><strong>Text recognition makes mistakes.</strong> Very small or decorative text can be misread, and search matches the letters as they were read.</li>
  <li><strong>Images are dropped sooner than text.</strong> Tuck keeps the newest 200 images unless you change the number in Settings &gt; History. Pin the ones you need to keep, or save those as files.</li>
  <li><strong>Very large images are skipped.</strong> An image over 60 MB is not recorded.</li>
  <li><strong>Screenshots of secrets are not searchable.</strong> If the text in an image looks like a password or key, Tuck doesn't keep that text. The image itself stays in your history until you delete it. <a href="/blog/is-clipboard-history-safe.html">Is clipboard history safe?</a> has more on this.</li>
</ul>
<p>The <a href="/tuck/support.html">support page</a> covers what to do if screenshots don't appear.</p>
""",
},
{
"app": "tuck",
"slug": "is-clipboard-history-safe",
"date": "2026-11-14",
"title": "Is clipboard history safe? Passwords, API keys and what to check first",
"description": "A clipboard history records what you copy, passwords included unless it's built not to. What to check in any clipboard manager, and what Tuck does.",
"body": """
<p class="lede">A clipboard history is a record of what you copied, and some of what you copy is secret. Whether that's safe depends on what the clipboard manager records, where it keeps it, and what you do with the rest.</p>

<h2>What changes when you keep a history</h2>
<p>The clipboard is shared on purpose. It exists so that one app can read what another put there. Without a history, a password you copy sits on the clipboard until your next copy and is then gone.</p>
<p>A history changes how long things last. The same password is now in a list, and usually in a file, for as long as the history keeps it. That could be weeks. The ways it can then reach someone else are ordinary ones:</p>
<ul>
  <li><strong>Someone uses your Mac</strong> while you're logged in and opens the history.</li>
  <li><strong>You open the history while sharing your screen</strong> or with someone looking over your shoulder.</li>
  <li><strong>The history leaves your Mac,</strong> through a sync feature or in a backup.</li>
  <li><strong>Other software running under your account reads the file</strong> the history is stored in.</li>
</ul>

<h2>What you copy that shouldn't be kept</h2>
<ul>
  <li>Passwords, when you copy them instead of using autofill.</li>
  <li>One-time login codes from a text message or an authenticator app.</li>
  <li>API keys, access tokens and private keys, if you write software.</li>
  <li>Card numbers and bank details.</li>
  <li>Other people's personal information, such as a customer's address copied from one system into another.</li>
</ul>

<h2>What to check before trusting a clipboard manager</h2>
<h3>Does it connect to the internet?</h3>
<p>Sync between devices is convenient, and it means your clipboard is stored on someone's server. An app with no sync and no account has nowhere to send your history. Read the privacy policy for what is collected, and check whether the app works with no network connection.</p>
<h3>Where is the history stored?</h3>
<p>Find out which folder it's in, whether other user accounts on the Mac can read it, and whether it's included in your backups. A history file is protected by the same things as your other files: your login password and, if you've turned it on, FileVault.</p>
<h3>Does it skip what password managers mark as hidden?</h3>
<p>Many password managers mark what they copy with a flag that asks clipboard managers not to record it. It's a convention, not something macOS enforces, so it only works if the clipboard manager respects it. Many password managers can also clear the clipboard after a short time. That doesn't remove a copy a history has already made.</p>
<h3>Can you exclude apps?</h3>
<p>A list of apps to never record from covers the cases the flag misses: a banking app, a remote desktop window, a database tool.</p>
<h3>Can you pause it?</h3>
<p>If you know you're about to handle something sensitive, the simplest protection is to stop recording for a few minutes.</p>
<h3>How long is it kept, and can you delete it?</h3>
<p>Look for a limit on the size or age of the history, a way to delete a single item, and a way to clear everything.</p>

<h2>Habits that help with any clipboard manager</h2>
<ul>
  <li><strong>Use autofill instead of copying passwords.</strong> A password that never touches the clipboard can't be recorded from it.</li>
  <li><strong>Delete what slipped through.</strong> If you see a secret in your history, delete that item then, not later.</li>
  <li><strong>Lock your Mac when you step away,</strong> and turn on FileVault.</li>
</ul>

<h2>How Tuck handles it</h2>
<p>Tuck is a clipboard manager for Mac that isn't released yet; it's coming to the Mac App Store. Here is what it does with sensitive copies.</p>
<ul>
  <li><strong>Nothing leaves your Mac.</strong> Tuck has no account, no sync and no analytics, and it never connects to the internet. The Mac App Store version runs in Apple's App Sandbox without the permission an app needs to make network connections.</li>
  <li><strong>Hidden copies are skipped.</strong> Anything a password manager marks as hidden is never recorded.</li>
  <li><strong>Listed apps are skipped.</strong> Copies made while an app listed under Settings &gt; Privacy is in front are not recorded. 1Password, Bitwarden, Keychain Access and Apple's Passwords app are on the list from the start, and you can add any app.</li>
  <li><strong>Text that looks like a credential is held in memory only.</strong> It appears in the panel masked and labeled "secret, not saved". It's never written to disk, and it's forgotten after 10 minutes or when Tuck quits. Until then you can still paste it. It can't be pinned.</li>
  <li><strong>The same check applies to images.</strong> Tuck reads the text in images so you can search for them. If that text looks like a credential, it isn't kept.</li>
  <li><strong>You can pause.</strong> Pause Capture in the menu bar icon's menu stops recording until you turn it off again.</li>
  <li><strong>You can delete.</strong> Cmd+Delete removes the selected clip, and Settings &gt; History &gt; Clear History removes everything except pinned clips. Tuck also keeps only the newest 1,000 clips and 200 images unless you change those limits.</li>
  <li><strong>The history is private to your account.</strong> It's stored in Tuck's own folder on your Mac, and Tuck sets that folder so that only your macOS user account can read it.</li>
</ul>

<h3>What Tuck recognizes as a credential</h3>
<p>The check looks for shapes. It recognizes API keys and tokens in the formats used by a number of common services, JSON web tokens, private key blocks, lines such as <code>API_KEY=...</code> or <code>PASSWORD=...</code> from an environment file, web addresses with a password in them, <code>Bearer</code> authorization headers, and a copy that is nothing but a six to eight digit code.</p>

<h3>What it doesn't do</h3>
<ul>
  <li><strong>It can't recognize a plain password.</strong> A password on its own has no shape to detect. If you copy one from a note, a web page or an app that doesn't mark it as hidden, Tuck records it like any other text.</li>
  <li><strong>It doesn't remove an image that shows a secret.</strong> The text isn't kept, so the image can't be found by searching, but the picture stays in your history until you delete it.</li>
  <li><strong>It doesn't encrypt the history itself.</strong> The file is protected by your macOS account and by FileVault if you use it. If you back up your Mac, the history is in the backup.</li>
  <li><strong>Clear History keeps pinned clips.</strong> Don't pin anything secret.</li>
  <li><strong>Pausing needs the menu bar icon.</strong> If you've hidden the icon in Settings &gt; General, show it again to reach Pause Capture.</li>
</ul>
<p>As Tuck's <a href="/tuck/privacy.html">privacy policy</a> puts it, the detection is a safeguard, not a guarantee. Add the apps you copy sensitive things from to the list, and pause when you know what's coming.</p>
<p>For what a history is good for, see <a href="/blog/what-is-a-clipboard-manager-mac.html">What a clipboard manager is, and who needs one on a Mac</a>. For images, see <a href="/blog/mac-screenshots-to-clipboard.html">How to copy Mac screenshots to the clipboard</a>.</p>
""",
},
]
