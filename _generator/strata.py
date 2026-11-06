from icons import EXTERNAL
from chrome import EMAIL, hero, features, shots, feature_rows, build_pages

OVERVIEW = hero("strata", "Web app",
    "Read Scripture grounded in the history it grew out of.",
    "Strata is a Bible reading app that opens every passage in four layers: what it meant then, what it carries always, how it turns to address you now, and a question for you to answer. It starts with Genesis, read in movements and daily readings.",
    '<a class=\"button\" href=\"https://stratabible.app/\">Open Strata' + EXTERNAL + '</a><span class="label">Genesis 1 to 11 free · No account needed</span>') + """

<section aria-label="Main features">
""" + feature_rows([
    ("/assets/screens/strata-home.jpg", "Strata home screen with Genesis and Exodus.", "A library, read in movements", "Strata takes you through each book of the Bible in short daily readings. The readings are grouped into larger sections called movements. Each movement opens with an introduction that sets the scene and ends with a capstone that ties it together, so you always know where you are in the story. It starts with Genesis, and more books are added as they're published."),
    ("/assets/screens/strata-history.jpg", "A reading of Genesis 1 opening with the history layer about the Babylonian exile.", "The history behind every passage", "Every reading starts with the history: who wrote the passage, when, and what was happening to the people who first heard it. Knowing a story was told during exile or war changes how it reads. Strata names its sources and sums up what scholars say in plain words, without long quotations."),
    ("/assets/screens/strata-turn.jpg", "The meaning and the turn layers of a reading, ending with a question to answer.", "Meaning, the turn, and your response", "After the history come three more steps. First, what the passage has meant to readers in every age. Then the turn: how it speaks to your life today. Last, a question for you to answer in your own words. Where the Bible holds different voices or open tensions, Strata shows them honestly instead of boiling them down to a tidy lesson."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([('A companion on every reading', 'With Strata Plus, an AI companion draws out the meaning, the turn and a question for each reading, made for you.'),
    ('Your notes, synced', 'Sign in to keep highlights, notes and your responses on all your devices.'),
    ('Public domain text', 'Scripture is the Berean Standard Bible, in the public domain.')]) + f"""
</section>

<section aria-labelledby="plans-title">
  <h2 id="plans-title" class="section-title">Plans</h2>
  <div class="plans">
    <div class="plan"><h3>Free</h3><span class="price">Free</span><p>The primeval history, Genesis 1 to 11, for everyone. Signing in adds one free draw of the companion.</p></div>
    <div class="plan"><h3>Strata Plus</h3><span class="price">US$6.99<small> / month</small></span><p>Or US$49 a year. All of Genesis, every book as it's published, the companion on every reading, and your notes synced.</p></div>
  </div>
  <p class="plans-note">You can also buy a single book outright to keep, such as Genesis for US$14.99. Billed in US dollars through Stripe; cancel Plus anytime and keep access through the period you've paid for.</p>
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="https://stratabible.app/privacy">Privacy Policy</a></li>
    <li><a href="https://stratabible.app/terms">Terms of Service</a></li>
    <li><a href="https://stratabible.app/pricing">Pricing</a></li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("Strata", "A Bible reading app that grounds every passage in its history, its meaning, and what it asks of you now.", OVERVIEW, "en", "wrap app-page"),
}


def build(root):
    build_pages(root, "strata", PAGES)
