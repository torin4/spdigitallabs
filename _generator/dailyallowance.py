from icons import EXTERNAL
from chrome import EMAIL, hero, features, feature_rows, build_pages

V = "?v=2"
OVERVIEW = hero("dailyallowance", "Available on iPhone",
    "Know exactly how much you can spend today.",
    "Daily Allowance turns your income and bills into one simple daily number, then keeps track of the rest: what you spent, what you saved, and how this month compares.",
    '<a class="button" href="https://apps.apple.com/app/id6829595254">Get it on the App Store' + EXTERNAL + '</a><span class="label">Free · Premium optional</span>') + """

<section aria-label="Main features">
""" + feature_rows([
    ("/assets/screens/dailyallowance-home.jpg" + V, "Home screen showing a Daily Balance of $96.33, a chart of the coming days, and today's entries.", "One number for today", "Tell Daily Allowance what comes in, like your pay, and what goes out every month, like rent and phone bills. It works out what's left for everyday spending and turns it into a daily amount. The big number on the home screen is what you can spend today. Spend less and the rest carries over to tomorrow; spend more and tomorrow's number is smaller."),
    ("/assets/screens/dailyallowance-categories.jpg" + V, "Analytics with a category breakdown of a month's spending.", "See where it went", "Each thing you buy goes into a category, such as food, transport or shopping. The Analytics screen shows how much went to each category this month and how that compares with last month. You can see at a glance where your money really goes, and which costs crept up."),
    ("/assets/screens/dailyallowance-heatmap.jpg" + V, "Calendar heatmap with each day green for under the allowance or red for over.", "Every day, over or under", "A calendar shows your whole month at once. Each day is green if you spent less than your daily amount and red if you spent more, and the shade shows by how much. It's an easy way to spot patterns, like weekends that always run over."),
    ("/assets/screens/dailyallowance-insights.jpg" + V, "An AI insights report summarizing a month's spending pace.", "Reports in plain language", "With Premium, you can ask questions about your spending in your own words, or get a short report at the end of each month. The answers are written from your own totals, so they're about your money, not general tips. AI can get things wrong, so the app tells you that, and the reports aren't financial advice."),
]) + """
</section>

<section aria-labelledby="more-title">
  <h2 id="more-title" class="section-title">More</h2>
""" + features([
    ("Kitty Bank", "Move what you didn't spend into savings and watch it build toward your goal."),
    ("Share a budget", "With Premium, budget together with up to five people on their own phones."),
    ("Home screen widget", "See your balance and add an entry without opening the app."),
    ("Works offline", "Entries save on your phone and sync when you're back online."),
    ("Your currency and language", "Pick your currency, and use the app in English, Japanese and several other languages."),
    ("Export to CSV", "Back up your entries as a spreadsheet whenever you like."),
]) + f"""
</section>

<section aria-labelledby="help-title">
  <h2 id="help-title" class="section-title">Help and policies</h2>
  <ul class="help-list">
    <li><a href="/dailyallowance/support.html">Support and questions</a></li>
    <li><a href="/dailyallowance/privacy.html">Privacy Policy</a></li>
    <li><a href="/dailyallowance/terms.html">Terms of Service</a></li>
    <li><a href="/dailyallowance/delete-account.html">Delete your account</a></li>
    <li>Questions: {EMAIL}</li>
  </ul>
</section>
"""

PAGES = {
    "index.html": ("Daily Allowance", "Know exactly how much you can spend today, after your bills are covered.", OVERVIEW, "en", "wrap app-page"),
}


def build(root):
    build_pages(root, "dailyallowance", PAGES)
