"""PeraPera blog posts. Every statement about how PeraPera works is checked against the app's code (../japanese-app)."""

POSTS = [
{
"app": "perapera",
"slug": "japanese-intermediate-plateau",
"date": "2026-11-14",
"title": "Getting past the intermediate plateau in Japanese",
"description": "Why Japanese stops improving at upper-intermediate, and three kinds of practice that move it: producing, reading at the right level, speaking with feedback.",
"body": """
<p class="lede">Somewhere around upper-intermediate, roughly B1 to B2 on the CEFR scale, Japanese stops getting visibly better. You can read most things and hold a conversation, and another year of the same habits changes very little. Here is why that happens, and what kinds of practice tend to move it.</p>

<h2>Why progress stalls</h2>
<h3>The words you still need are rarer</h3>
<p>The most common words turn up everywhere, so each one you learn pays off the same day. By upper-intermediate, a word you don't know might appear once in an article, or once a month. Learning it changes nothing you can feel. You're still improving, but the improvement is spread so thinly that it's hard to see.</p>
<h3>You can get by with what you have</h3>
<p>A beginner who lacks a word is stuck. You aren't. You understand <span lang="ja">懸念</span> (<span lang="ja">けねん</span>) when you read it, but when you speak you say <span lang="ja">心配</span> every time, and everyone understands. Nothing forces the newer word out of you, so it stays a word you recognise and never one you use.</p>
<h3>Understanding hides the gaps</h3>
<p>Recognising something is easier than recalling it. Reading and listening only ask you to recognise, so they can feel fluent long after your own output has stopped growing. Kanji make this worse, because you can get the meaning of a word from its characters without knowing how it's said. <a href="/blog/read-kanji-but-not-say-it.html">Why you can read a kanji word but not say it</a> goes into that.</p>
<h3>Nobody corrects you any more</h3>
<p>Once you're easy to understand, people answer what you said and ignore how you said it. Mistakes that don't block communication, a particle here, a slightly wrong register there, can stay for years.</p>

<h2>What moves it</h2>
<h3>Produce, don't only recognise</h3>
<p>Pulling an answer out of your memory strengthens it more than looking at the answer again. So make the practice ask for something: type the reading before you see it, say the sentence before you hear it, summarise the article before you reread it. Rereading and picking from a list feel smooth because they ask for less, and they teach less for the same reason.</p>
<h3>Read at the right difficulty</h3>
<p>Text that's too easy has nothing new in it. Text that's too hard turns into decoding, with a dictionary open for every line. The useful range is text you can mostly follow, with a few words on each page you have to work out or look up.</p>
<p>Vary the kind of text too. News, fiction and business email each have their own vocabulary.</p>
<h3>Speak, and find out what was wrong</h3>
<p>Speaking practice without feedback mostly repeats what you can already do. You need to say something slightly beyond your comfortable range, and then learn which parts a native speaker would have said differently. <a href="/blog/practise-speaking-japanese-alone.html">How to practise speaking Japanese when you have nobody to practise with</a> covers how to do that alone.</p>
<h3>Measure something honest</h3>
<p>A count of days studied in a row measures attendance. At this level, better questions are: of the words I met this month, how many can I read aloud correctly? Can I explain an article I just read without looking at it? These go up slowly, but they reflect what you can do.</p>

<h2>Doing it in PeraPera</h2>
<p><a href="/perapera/">PeraPera</a> is a web app built around these three kinds of practice.</p>
<ul>
  <li><strong>Find where words start to get hard.</strong> Find my level is a 16-word reading test. You see one word at a time and type its reading, or skip it. It starts at C1. Get a word right and the next comes from the level above; miss or skip it and the next comes from the level below. The result is one of six levels (B1, B2, C1, C1+, C2, C2+), shown with the levels below it marked solid, yours marked frontier and the ones above marked reach. You can retake it any time.</li>
  <li><strong>Review at that level.</strong> The test reschedules the 107 words built into the app. Those above your frontier are due straight away, those at it in two days, and those below it six or fifteen days later. Words that came up in the test are adjusted by how you did on them.</li>
  <li><strong>Review by producing.</strong> On a reading card you see the word in a sentence and type its reading in hiragana before the meaning is shown. The same words also come back with the word blanked out of its sentence, and as listening cards where you hear the word and choose its meaning from four. Reading cards make up half of the rotation.</li>
  <li><strong>Read at a level you choose.</strong> In Read something, you describe what you want to read, then pick one of the six levels and a length: short, medium or long, about 5, 10 or 16 sentences. The level starts at your placement result. Tap a word for its reading and meaning, and add it to your review from there. Furigana and the English translation stay hidden until you switch them on. Two or three comprehension questions follow the passage.</li>
  <li><strong>Speak with feedback.</strong> Conversation practice builds a short role-play around the review words you get wrong most, and your partner adds a short note when something you said was unnatural. The speaking test is an interview that ends with a written report.</li>
  <li><strong>One number.</strong> The home screen shows your reading accuracy: readings typed correctly out of all those you've been asked for. There are no streaks.</li>
</ul>
<p>The level names follow the CEFR scale, but they're the app's own rough bands, worked out from which words you could read. They aren't a certificate.</p>
<p>The passages, the conversation and the reports are written by AI. AI can get things wrong, including about Japanese, so check anything that looks odd against a dictionary or a native speaker.</p>

<h2>What's free</h2>
<p>Vocabulary review and the placement test are free and work without an account. Reading, look-up and the speaking tools need a free account, which comes with five AI requests a day. A passage is one request. A conversation uses one request to set the scene and one for each message you send. The allowance resets at midnight Japan time.</p>
<p>PeraPera Pro is ¥1,980 a month or ¥19,800 a year, and gives you the full-size AI model and 400 AI requests a month.</p>

<h2>Who it suits less</h2>
<ul>
  <li><strong>Beginners.</strong> The easiest built-in words are ones like <span lang="ja">為替</span> and <span lang="ja">老舗</span>, and nothing in the app teaches kana or basic grammar.</li>
  <li><strong>People who want a Japanese interface.</strong> The app's screens, the word meanings and the feedback are in English.</li>
  <li><strong>People who want a large ready-made word list.</strong> The built-in deck is 107 words. After that, you review the words you add.</li>
</ul>
""",
},
{
"app": "perapera",
"slug": "read-kanji-but-not-say-it",
"date": "2026-11-14",
"title": "Why you can read a kanji word but not say it",
"description": "Knowing what a kanji word means and knowing its reading are separate skills. Why readings lag behind, the common traps, and how to practise them so they stick.",
"body": """
<p class="lede">You see <span lang="ja">相殺</span> in a report and know at once that it means offsetting. Then you have to say it in a meeting, and you aren't sure whether it's <span lang="ja">そうさい</span> or <span lang="ja">そうさつ</span>. Knowing what a kanji word means and knowing how it's read are separate pieces of knowledge, and most reading practice only builds the first.</p>

<h2>Two kinds of knowing</h2>
<p>Kanji carry meaning. If you know the characters, you can often understand a word you have never heard, which is a real advantage of the writing system. It also means silent reading never checks whether you know the sound.</p>
<p>When the sound is needed, something usually supplies it: furigana, a pop-up dictionary, a subtitle. You look, you nod, and you move on. You recognised the reading. You didn't have to produce it, and recognising is the easier of the two.</p>

<h2>Where the gap shows</h2>
<ul>
  <li><strong>Speaking.</strong> You avoid the word, or say it quietly and hope.</li>
  <li><strong>Typing.</strong> Japanese input goes through the reading. If you believe <span lang="ja">融通</span> is <span lang="ja">ゆうつう</span>, the word won't come up.</li>
  <li><strong>Listening.</strong> A word you'd know on paper goes past unrecognised when someone says it, because the sound was never attached to it.</li>
  <li><strong>Reading aloud.</strong> A document you understood perfectly well turns into a string of hesitations.</li>
</ul>

<h2>Why readings go wrong</h2>
<h3>Words read as a whole</h3>
<p>In <span lang="ja">田舎</span> (<span lang="ja">いなか</span>), <span lang="ja">老舗</span> (<span lang="ja">しにせ</span>) and <span lang="ja">為替</span> (<span lang="ja">かわせ</span>), the reading belongs to the whole word. Nothing about the individual characters will get you there. You know these or you don't.</p>
<h3>Sound changes</h3>
<p>A character you know well is read slightly differently inside a particular word. <span lang="ja">発</span> is usually <span lang="ja">はつ</span>, but <span lang="ja">発端</span> is <span lang="ja">ほったん</span>. <span lang="ja">通</span> is usually <span lang="ja">つう</span>, but <span lang="ja">融通</span> is <span lang="ja">ゆうずう</span>.</p>
<h3>A reasonable guess that happens to be wrong</h3>
<p>Many characters share a part that hints at the sound: <span lang="ja">清</span>, <span lang="ja">晴</span>, <span lang="ja">精</span> and <span lang="ja">静</span> can all be read <span lang="ja">せい</span>, like the <span lang="ja">青</span> inside them. Guessing from the familiar part works often enough to become a habit, and the exceptions are where it catches you.</p>
<h3>One character, several readings</h3>
<p><span lang="ja">覆す</span> is <span lang="ja">くつがえす</span>, <span lang="ja">覆う</span> is <span lang="ja">おおう</span>, and <span lang="ja">覆面</span> is <span lang="ja">ふくめん</span>. Knowing the character doesn't tell you which reading a given word takes.</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Five words where the obvious guess is wrong</caption>
  <thead><tr><th scope="col">Word</th><th scope="col">Tempting guess</th><th scope="col">Reading</th></tr></thead>
  <tbody>
    <tr><th scope="row"><span lang="ja">相殺</span> (offsetting)</th><td><span lang="ja">そうさつ</span></td><td><span lang="ja">そうさい</span></td></tr>
    <tr><th scope="row"><span lang="ja">遵守</span> (compliance)</th><td><span lang="ja">そんしゅ</span></td><td><span lang="ja">じゅんしゅ</span></td></tr>
    <tr><th scope="row"><span lang="ja">発端</span> (origin)</th><td><span lang="ja">はったん</span></td><td><span lang="ja">ほったん</span></td></tr>
    <tr><th scope="row"><span lang="ja">融通</span> (flexibility)</th><td><span lang="ja">ゆうつう</span></td><td><span lang="ja">ゆうずう</span></td></tr>
    <tr><th scope="row"><span lang="ja">脆弱</span> (fragile)</th><td><span lang="ja">きじゃく</span></td><td><span lang="ja">ぜいじゃく</span></td></tr>
  </tbody>
</table>
</div>

<h2>How to practise readings so they stick</h2>
<h3>Produce the reading before you check it</h3>
<p>Trying to recall something, and then seeing the answer, fixes it in memory better than reading the answer again. So cover the furigana and commit to a reading first. Typing it in kana is stricter than saying it in your head, because you can't be vague about a long vowel or a small <span lang="ja">っ</span>.</p>
<h3>Learn the word in a sentence</h3>
<p>The reading belongs to the word, not to the character, so practise it attached to a word and a context you could meet again. <span lang="ja">融通が利かない</span> is easier to keep than <span lang="ja">融通</span> alone.</p>
<h3>Spread it out</h3>
<p>Coming back to a word tomorrow, then next week, does more than repeating it ten times tonight. A reading you can still produce after a gap is one you actually have.</p>
<h3>Keep the ones you got wrong</h3>
<p>A confident wrong guess that gets corrected tends to stay corrected. The words worth your time are the ones you misread, so keep a list of them and go back to it.</p>
<h3>Attach the sound</h3>
<p>Say the word aloud when you check it, and hear it if you can. The aim is to know the word when it's spoken as well as when it's written.</p>

<h2>Doing it in PeraPera</h2>
<p><a href="/perapera/">PeraPera</a>'s vocabulary review is built on typing readings. All five words in the table above are in its built-in deck.</p>
<ul>
  <li><strong>Reading cards.</strong> You see the word and a sentence that uses it, and type the reading in hiragana. Katakana is accepted too. The meaning stays hidden until you've answered, and there's an "I don't know" button for when you have no idea.</li>
  <li><strong>What you see afterwards.</strong> The reading, whether yours matched, the meaning, the sentence with a translation, and for the built-in words a short note, often on the misreading to watch for.</li>
  <li><strong>The reading decides.</strong> After the answer you grade yourself Missed, Got it or Easy. If the reading you typed was wrong, the card comes back the next day whichever one you pick. A card you get right returns after a day, then six days, then at longer intervals.</li>
  <li><strong>Two other card types.</strong> In context cards blank the word out of its sentence, give you the meaning, and ask for the reading of the missing word. Listening cards, which appear if your device has a Japanese voice, play the word and ask which of four meanings you heard.</li>
  <li><strong>Your own words.</strong> In My words you can add a word with its reading, meaning and an example sentence, and sort words into sets that you can study separately.</li>
</ul>
<p>A session is up to 12 cards. The home screen shows your reading accuracy across everything you've reviewed.</p>

<h2>What's free</h2>
<p>All of the above is free and needs no account, including the placement test and adding your own words by hand. Your progress is saved in your browser. Signing in with a free account syncs it across devices.</p>
<p>A free account also includes five AI requests a day. Auto-fill uses one to fill in a new word's reading, meaning and example sentence. Look up uses one to translate a pasted sentence and break it down word by word, so you can tap any word to add it. AI can get things wrong, so check a reading it gives you before you spend weeks learning it.</p>

<h2>Who it suits less</h2>
<ul>
  <li><strong>Beginners.</strong> The built-in deck starts at upper-intermediate.</li>
  <li><strong>People who want to practise handwriting.</strong> The app asks you to type readings. It doesn't teach stroke order or writing kanji from memory.</li>
  <li><strong>People who want a Japanese interface.</strong> The screens and the word meanings are in English.</li>
  <li><strong>People who want a large ready-made list.</strong> There are 107 built-in words, from B1 to C2+. Beyond those, you review what you add.</li>
</ul>
<p>If readings are only one part of feeling stuck, <a href="/blog/japanese-intermediate-plateau.html">Getting past the intermediate plateau in Japanese</a> covers the rest.</p>
""",
},
{
"app": "perapera",
"slug": "practise-speaking-japanese-alone",
"date": "2026-11-14",
"title": "How to practise speaking Japanese when you have nobody to practise with",
"description": "Speaking practice needs a reason to say Japanese out loud and a way to find out what was wrong with it. How to get both without a conversation partner.",
"body": """
<p class="lede">Speaking is the hardest skill to practise alone, because it seems to need another person. What it needs is two things: a reason to produce Japanese out loud, and a way to find out what was wrong with it. You can arrange both by yourself.</p>

<h2>Why speaking falls behind</h2>
<p>You can read or listen at any hour, for as long as you like. Speaking only happens when someone is there, so it gets a fraction of the practice time.</p>
<p>Living in Japan doesn't fix this on its own. Daily conversations repeat: the same exchanges at work, in shops and with the same few people. You get quick at those and stay slow at everything else. And once people can understand you, they stop correcting you.</p>

<h2>Ways to speak without a partner</h2>
<h3>Shadowing</h3>
<p>Play a recording and say it along with the speaker, a beat behind. It's good for rhythm, speed and getting your mouth used to long phrases. It doesn't practise the harder part, which is building the sentence yourself.</p>
<h3>Retelling</h3>
<p>Read an article or watch a short video, then explain it out loud in a minute without looking. Notice where you stall or swap in an easier word, because those are the gaps worth filling.</p>
<h3>Rehearsing real situations</h3>
<p>Pick something you'll actually have to do: a phone call to the ward office, explaining a delay to a client, turning down an invitation. Say your side of it aloud, once in polite speech and once in casual speech. Register is a common weak point at this level, and you can practise switching it alone.</p>
<h3>Recording yourself</h3>
<p>Record two minutes of any of the above and listen the next day. You'll hear the hesitations, the fillers and the three phrases you lean on for everything.</p>

<h2>Getting feedback on what you said</h2>
<p>Producing speech alone is the easy half. Finding out what was wrong with it is harder.</p>
<ul>
  <li><strong>Listen back.</strong> This catches slips: things you know and got wrong at speed. It can't catch mistakes you don't know are mistakes.</li>
  <li><strong>Write it down.</strong> Transcribe exactly what you said and look at it as text. Particle and conjugation errors are easier to see on the page.</li>
  <li><strong>Ask a person a narrow question.</strong> A tutor or a patient friend will give you more if you ask "which three sentences sounded unnatural?" than if you ask them to correct everything.</li>
  <li><strong>Ask an AI.</strong> It will comment on every sentence, at any hour. It's useful for grammar, word choice and register, and it can also be wrong.</li>
</ul>
<p>Whatever the source, good feedback is about a sentence you actually said, gives you the natural version of it, and is short enough to act on. Then use it: say the corrected sentence aloud, and try to say the same kind of thing again a few days later.</p>

<h2>Doing it in PeraPera</h2>
<p><a href="/perapera/">PeraPera</a> has four speaking tools. In the first three you hold the mic button and speak, and your browser's speech recognition turns it into text that you can fix before sending. In a browser without speech recognition, you type instead. Your partner's lines are spoken aloud. You can set the voice, the speed and, outside the test, how formal your partner is.</p>
<h3>Conversation practice</h3>
<p>You choose up to ten words from your review; by default it picks the six you get wrong most. The app writes a short role-play scene that needs those words and tells you who you are and what you're trying to do. After each thing you say, your partner replies and, when something was off, adds one short note in English on naturalness, register or grammar. Each target word is ticked when you use it correctly, and those words are then scheduled further out in your review.</p>
<h3>Speaking test</h3>
<p>An interview of 6 to 12 questions, which get harder when you answer well and easier when you struggle. Questions are spoken only. You can reveal the Japanese text or an English translation, but each question you needed them for counts against your level. Afterwards you get an estimated speaking level on the app's six-level scale from B1 to C2+, and a written report: strengths, gaps, grammar to review with your sentence and a corrected one, words to learn, and what to practise next.</p>
<h3>Guided practice</h3>
<p>You pick one weakness, either from your last speaking test or one you type in. You get a short lesson, four spoken drills with one retry each, then a short scene built so that the point has to come up. Each drill answer is marked, with a more natural version when there is one.</p>
<h3>Record a conversation</h3>
<p>For a real conversation with a real person. You read one line alone at the start so the app knows which voice is yours, then talk for up to ten minutes. The recording is transcribed and split into turns, and you tap any line that was given to the wrong speaker. Only your lines are judged. The report lists what you did well and the lines worth fixing, each with a natural version and a reason. Weaknesses it finds are added to Guided practice.</p>

<p>All of this feedback is written by AI, and AI can get things wrong. Treat a correction as something to check, especially when it contradicts what you hear native speakers say. The feedback is also based on the text of what you said. Nothing in PeraPera assesses your pronunciation or pitch accent.</p>

<h2>What's free</h2>
<p>The speaking tools need a free account, which includes five AI requests, 5,000 characters of spoken replies and five minutes of transcription a day. The allowance resets at midnight Japan time. A conversation uses one request to set the scene and one for each message you send, so a free day covers one exchange of four messages. Analysing a recording takes two requests, and the recording has to fit in the five minutes.</p>
<p>A full speaking test takes 8 to 14 requests and a guided session at least six, so in practice those need PeraPera Pro. It costs ¥1,980 a month or ¥19,800 a year, and includes the full-size AI model, 400 AI requests, 150,000 characters of speech and 150 minutes of transcription a month.</p>

<h2>Who it suits less</h2>
<ul>
  <li><strong>Beginners.</strong> The easiest level is upper-intermediate.</li>
  <li><strong>People who want pronunciation coaching.</strong> You'll need a teacher or a shadowing routine for that.</li>
  <li><strong>People who want a Japanese interface.</strong> The app's screens and the coaching notes are in English.</li>
</ul>
<p>Speaking is one part of getting unstuck at this level. <a href="/blog/japanese-intermediate-plateau.html">Getting past the intermediate plateau in Japanese</a> covers the rest, and <a href="/blog/read-kanji-but-not-say-it.html">Why you can read a kanji word but not say it</a> covers readings.</p>
""",
},
]
