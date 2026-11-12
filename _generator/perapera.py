from icons import EXTERNAL
from chrome import EMAIL, hero, features, feature_rows, build_pages
from perapera_ja import PAGES_JA

APP = "https://japanese-app-kappa.vercel.app"

OVERVIEW = hero("perapera", "Web app",
    "Japanese practice for learners who are already good.",
    "PeraPera is for adult learners from upper-intermediate to near-native (CEFR B1 to C2). You type the reading of every word before anything is shown, then use its AI tools: passages written for you at your level, a conversation partner to speak with, and detailed feedback on what you said.",
    f'<a class="button" href="{APP}/">Open PeraPera' + EXTERNAL + '</a><span class="label">Vocabulary review is free · No account needed</span>') + """

<section aria-label="Main features">
""" + feature_rows([
    ("/assets/screens/perapera-review.jpg", "A review card showing the word 田舎 in a sentence, with a box to type its reading.", "Type the reading first", "Most vocabulary apps let you pick an answer from a list. PeraPera makes you produce it: you see the word in a sentence and type its reading in hiragana before the meaning appears. Words come back as cloze sentences and listening questions too, so you know each one in more than one way."),
    ("/assets/screens/perapera-level.jpg", "A placement result: an estimated reading level of C1+, high-advanced, with B1 to C1 marked solid, C1+ as the frontier and C2 still to reach.", "Find your level in two minutes", "A short placement test shows you one word at a time and asks for its reading. Get it right and the next word is harder; miss it and the next is easier. It settles on the level where words start to get hard for you, shown as a CEFR level from B1 to C2, and shows which levels are solid and which are still a reach. Review then concentrates on your frontier. Retake it whenever you like."),
    ("/assets/screens/perapera-reader.jpg", "The graded reader setup screen, asking for a topic, a level and a length.", "AI reading at your level", "Say what you'd like to read, such as a news article, a folktale or a business email, and pick a level and a length. The AI writes a passage for you on the spot, so there is always something new to read at the right difficulty. Tap any word to see its reading and meaning, then answer a couple of comprehension questions."),
    ("/assets/screens/perapera-conversation.jpg", "A conversation in Japanese with an AI coworker about a weekend trip. Target words are ticked off as they are used, and a note corrects a grammar slip.", "An AI conversation partner", "Speak with an AI partner in Japanese, out loud, about whatever you choose. Work through guided practice, or take a speaking test. Afterwards the AI reviews the session: what you did well, the gaps, the grammar to go back over and the words worth learning. You can also record a real conversation with someone, and the AI transcribes it and reviews how you did."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([('AI look-up', 'Paste in a word, a sentence or a subtitle line and the AI translates it and breaks it down word by word. Tap any word to add it to your review, or type one in and let the AI fill in the rest.'),
    ('An honest number', 'PeraPera shows your reading accuracy over time. There are no streaks to protect.'),
    ('On all your devices', 'Sign in to keep your words and progress in sync across your phone and computer.')]) + f"""
</section>

<section aria-labelledby="plans-title">
  <h2 id="plans-title" class="section-title">Plans</h2>
  <div class="plans">
    <div class="plan"><h3>Free</h3><span class="price">Free</span><p>Vocabulary review and the placement test, with no account. A free account adds five AI requests a day for reading and conversation.</p></div>
    <div class="plan"><h3>PeraPera Pro</h3><span class="price">¥1,980<small> / month</small></span><p>Or ¥19,800 a year. The full-size AI model, 400 AI requests, 150,000 characters of speech and 150 minutes of transcription every month.</p></div>
  </div>
  <p class="plans-note">Prices include tax. Billed in Japanese yen through Stripe. Pro renews until you cancel; cancel anytime and keep it through the period you've paid for. The app is in English.</p>
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="{APP}/privacy.html">Privacy Policy</a></li>
    <li><a href="{APP}/terms.html">Terms of Use</a></li>
    <li><a href="{APP}/tokushoho.html" lang="ja" hreflang="ja">特定商取引法に基づく表記</a></li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("PeraPera", "Japanese practice for advanced learners: type the reading of every word, read AI passages at your level, and practise conversation with an AI partner that gives feedback.", OVERVIEW, "en", "wrap app-page"),
}


def build(root):
    build_pages(root, "perapera", PAGES, PAGES_JA)
