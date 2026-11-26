from chrome import EMAIL, hero, features, build_pages
from caloriecount_policies import PRIVACY, TERMS, SUPPORT, DELETE_ACCOUNT, META
from caloriecount_ja import PAGES_JA

OVERVIEW = hero("caloriecount", "Coming soon",
    "Calorie counting in one number.",
    "Calorie Count compares what you ate with what you burn and shows you the difference. Take a photo of a meal and AI estimates its calories. That number is all it shows.",
    '<span class="label">Coming soon to the App Store and Google Play</span>') + """

<section aria-labelledby="what-title">
  <h2 id="what-title" class="section-title">What it does</h2>
""" + features([
    ('AI estimates from a photo', 'Take a photo of your meal, or describe it in a few words, and AI estimates the calories. You can also type the number yourself.'),
    ('What you burn, worked out for you', 'Tell the app about yourself once. It works out what you burn in a day from your size, your steps and your workouts. Steps and weigh-ins can come from Apple Health or Health Connect.'),
    ('Checked against your own weight', 'After two weeks of logging food and weighing in, the app checks its figure against your own numbers.'),
    ('A healthy range to aim for', 'The app shows a range to eat in each day. It is far enough under what you burn to lose weight, and not so far that it costs muscle. It tells you if you are losing weight too fast.'),
    ('One number on the screen', 'The main screen shows how far under or over you are today. A two-week view adds up the days and shows them beside your weight. Tap a day to see what you ate.'),
    ('Your usual foods, one tap away', 'Foods you have logged before appear when you add a meal. The ones you usually eat at that time of day come first.'),
    ('Your log stays on your phone', 'Everything you log is kept on your phone and works offline. Sign in only if you want a backup or to use a second phone. There are no ads.'),
    ('Free to use', 'Typing in calories is always free and unlimited, and you get one AI estimate a day. Premium removes the daily limit.'),
]) + f"""
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/caloriecount/support.html">Support and questions</a></li>
    <li><a href="/caloriecount/privacy.html">Privacy Policy</a></li>
    <li><a href="/caloriecount/terms.html">Terms of Service</a></li>
    <li><a href="/caloriecount/delete-account.html">Delete your account</a></li>
    <li>The numbers are estimates, not medical advice.</li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("Calorie Count", "Calorie counting in one number: what you ate against what you burn. AI estimates a meal from a photo. Coming soon to iPhone and Android.", OVERVIEW, "en", "wrap app-page"),
    "support.html": (*META["support"], SUPPORT, "en", "wrap page"),
    "privacy.html": (*META["privacy"], PRIVACY, "en", "wrap page"),
    "terms.html": (*META["terms"], TERMS, "en", "wrap page"),
    "delete-account.html": (*META["delete-account"], DELETE_ACCOUNT, "en", "wrap page"),
}


def build(root):
    build_pages(root, "caloriecount", PAGES, PAGES_JA)
