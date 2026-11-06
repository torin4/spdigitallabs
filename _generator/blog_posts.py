"""Blog posts. Each body is plain HTML for the inside of the article.

Every statement about how Daily Allowance works is checked against the app's
code (DailyAllowance-kotlin) before it goes in. Dates are ISO (YYYY-MM-DD).
"""

POSTS = [
{
"slug": "daily-spending-allowance",
"date": "2026-11-06",
"title": "What a daily spending allowance is, and why it suits some people better than a monthly budget",
"description": "A daily spending allowance turns the money left after your bills into one number for today. How it works, why rolling over matters, and who it suits.",
"body": """
<p class="lede">A daily spending allowance is the amount you can spend today once your regular bills are taken care of. You check one small number each day instead of keeping a monthly total in your head.</p>

<h2>The basic idea</h2>
<p>Most budgets are monthly because most pay and most bills are monthly. That makes sense for rent, the phone contract and your salary. The rest of your money, the part that goes on food, coffee, transport, a birthday present or a takeaway on a tired evening, gets spent a day at a time.</p>
<p>A daily allowance takes that flexible part and divides it by the days it has to last. If you have $1,200 left each month after your bills, that comes to about $39 a day. That figure is your allowance.</p>
<p>Nothing else about your money changes. Bills still get paid when they're due. You only change how you look at the money that's left.</p>

<h2>Why one small number helps</h2>
<h3>Payday stops feeling like a windfall</h3>
<p>Just after payday, your account looks full. $1,200 for the month sounds like plenty, so the first week's spending feels free, and the shortfall arrives in the last week, when there's little you can do about it. A daily figure makes the 3rd of the month look exactly like the 27th: you have about $39 today, whatever the account says.</p>
<h3>Decisions get smaller</h3>
<p>Asking "can I afford this?" against a monthly budget means remembering what you've already spent this month and what's still to come. Against a daily figure, you compare the price with one number you already know. A $14 lunch on a $39 day is an easy call either way.</p>
<h3>Mistakes stay small and visible</h3>
<p>Going $15 over on a $39 day is obvious that same evening, and it's a $15 problem. In a monthly budget, the same overspend hides among the other entries until the end of the month, when it has grown into "the month went wrong somewhere".</p>

<h2>Rolling over makes it realistic</h2>
<p>A strict daily limit, where anything unspent disappears at midnight, would be miserable to live with. Real spending is lumpy. There's the weekly shop, a dinner out, and days when you spend nothing at all.</p>
<p>The version that works carries the difference forward. Spend less than your allowance and the rest is still there tomorrow. Spend more and tomorrow starts lower. Here is a week with a $40 allowance:</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Five days with a $40 daily allowance</caption>
  <thead><tr><th scope="col">Day</th><th scope="col">Added</th><th scope="col">Spent</th><th scope="col">Balance</th></tr></thead>
  <tbody>
    <tr><th scope="row">Monday</th><td>$40</td><td>$25</td><td>$15</td></tr>
    <tr><th scope="row">Tuesday</th><td>$40</td><td>$62</td><td class="neg">−$7</td></tr>
    <tr><th scope="row">Wednesday</th><td>$40</td><td>$12</td><td>$21</td></tr>
    <tr><th scope="row">Thursday</th><td>$40</td><td>$0</td><td>$61</td></tr>
    <tr><th scope="row">Friday</th><td>$40</td><td>$85</td><td>$16</td></tr>
  </tbody>
</table>
</div>

<p>Tuesday went over, so Wednesday started $7 behind. Thursday was a quiet day, and the cushion it built paid for Friday's dinner. Over the five days, $200 came in and $184 went out. The running balance tells you the one thing worth knowing: you're $16 ahead.</p>
<p>The running balance answers "how am I doing?" without any adding up. Positive means you're ahead of plan, negative means you're behind, and the size tells you by how much.</p>

<h2>Who it suits</h2>
<ul>
  <li><strong>People paid monthly who run short before payday.</strong> Spreading the money evenly is a direct fix for the start-of-month splurge.</li>
  <li><strong>People who find categories tedious.</strong> You don't have to decide in advance how much goes on eating out and how much on groceries. You can still look back at categories later to see where the money went.</li>
  <li><strong>People who prefer a short daily check to a long monthly review.</strong> Logging a purchase and glancing at one number takes a few seconds.</li>
</ul>

<h2>Who it suits less</h2>
<ul>
  <li><strong>People with very uneven income.</strong> Any fixed daily figure is a guess when you don't know next month's pay. It can still work if you base it on a cautious income figure and revisit it often.</li>
  <li><strong>People whose flexible spending is mostly a few large, planned purchases.</strong> A $600 flight looks alarming against a $40 day. Rolling over copes with ordinary lumps, but big one-offs are better planned separately, as a bill spread over several months or paid from savings.</li>
  <li><strong>People who already budget by envelopes or categories and are happy with it.</strong> A daily allowance is another view of the same money. If your current system works, keep it.</li>
</ul>

<h2>How Daily Allowance does it</h2>
<p>Daily Allowance is built around this idea. When you first open it, you can run Quick Setup, which asks for your monthly income and monthly expenses and shows the daily allowance they leave. After that, you can add each bill and each source of pay as its own recurring entry that repeats daily, weekly, monthly or yearly.</p>
<p>The app turns every recurring entry into a daily amount. The Daily Allowance figure divides monthly amounts by 30.4375, the average length of a month, so it stays the same from February to March. Behind it, each bill and each paycheck is spread over the actual days until it comes round again, so a 31-day month adds slightly less per day than a 30-day one.</p>
<p>The big number on the home screen is your Daily Balance, the running total from the table above. Each day's share of your income and bills goes in, every expense you log comes out, and whatever is left carries into tomorrow, in either direction. It doesn't reset at the start of a new month. Below it, once you've logged something today, a bar shows how today's spending compares with your allowance, and a short forecast shows where your balance will be over the next two days.</p>
<p>If you're ahead and want to bank it, Transfer to Kitty Bank moves your whole balance into the app's savings. If you're behind, Top up from Kitty Bank moves back exactly enough to bring you to zero.</p>

<h2>Trying it without an app</h2>
<p>You can test the idea for a week with a notebook. Work out the money you have each month after bills, divide it by 30, and write that number where you'll see it. Each evening, add the allowance to yesterday's balance and take off what you spent. By the end of the week you'll know whether thinking in days suits you.</p>
<p>The next post, <a href="/blog/work-out-your-daily-budget.html">How to work out your daily budget</a>, goes through the arithmetic with a full example.</p>
""",
},
{
"slug": "work-out-your-daily-budget",
"date": "2026-11-06",
"title": "How to work out your daily budget: a worked example",
"description": "From take-home pay to a number you can check each morning, step by step, with the arithmetic shown. All you need is a recent bank statement and a calculator.",
"body": """
<p class="lede">This is a worked example that goes from take-home pay to a number you can check each morning. You'll need two or three recent bank statements and a calculator. The figures are an example; swap in your own as you go.</p>

<h2>Step 1: Start with what actually arrives</h2>
<p>Use your take-home pay, the amount that lands in your account after tax and deductions. In this example it's <strong>$2,800 a month</strong>.</p>
<p>If you're paid weekly or every two weeks, convert it to a monthly figure first:</p>
<ul>
  <li>Weekly: pay × 52 ÷ 12. $650 a week is $650 × 52 ÷ 12 = $2,816.67 a month.</li>
  <li>Every two weeks: pay × 26 ÷ 12.</li>
</ul>
<p>Avoid multiplying weekly pay by four. A month is a little over four weeks, so × 4 leaves out four weeks of pay over a year, and your budget ends up tighter than it needs to be.</p>
<p>If your income changes from month to month, use the lowest of your last few months rather than the average. Being pleasantly surprised is better than coming up short.</p>

<h2>Step 2: List the bills that come round on a schedule</h2>
<p>Go through your statements and pick out everything that leaves on a schedule. For bills that vary, like electricity, use an average of the last few months.</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Monthly bills in the example</caption>
  <thead><tr><th scope="col">Bill</th><th scope="col">Per month</th></tr></thead>
  <tbody>
    <tr><th scope="row">Rent</th><td>$1,050.00</td></tr>
    <tr><th scope="row">Electricity and gas</th><td>$120.00</td></tr>
    <tr><th scope="row">Phone</th><td>$35.00</td></tr>
    <tr><th scope="row">Transport pass</th><td>$90.00</td></tr>
    <tr><th scope="row">Streaming and other subscriptions</th><td>$25.00</td></tr>
  </tbody>
  <tfoot><tr><th scope="row">Total</th><td>$1,320.00</td></tr></tfoot>
</table>
</div>

<p>Subscriptions are the easiest to miss. A statement search for small, identical amounts on the same day each month usually turns up one or two you'd forgotten about.</p>

<h2>Step 3: Turn yearly and weekly costs into monthly ones</h2>
<p>Some costs don't come monthly, but they still need to be counted:</p>
<ul>
  <li>Car insurance, paid once a year: $438 ÷ 12 = <strong>$36.50</strong> a month.</li>
  <li>A weekly exercise class: $15 × 52 ÷ 12 = <strong>$65.00</strong> a month.</li>
</ul>
<p>Yearly bills are the ones that cause trouble. If you don't spread them out, they land in a single month and wipe out several weeks of spending money at once.</p>

<h2>Step 4: Decide what to save first</h2>
<p>If you want to save, take it off now, before you work out the allowance. Otherwise saving becomes whatever happens to be left on the last day of the month, which is often nothing. In the example, <strong>$200</strong> a month goes to savings.</p>

<h2>Step 5: Divide what's left by the days</h2>
<div class="table-scroll">
<table class="ledger">
  <caption>From pay to daily allowance</caption>
  <tbody>
    <tr><th scope="row">Take-home pay</th><td>$2,800.00</td></tr>
    <tr><th scope="row">Monthly bills</th><td class="neg">−$1,320.00</td></tr>
    <tr><th scope="row">Yearly insurance, per month</th><td class="neg">−$36.50</td></tr>
    <tr><th scope="row">Weekly class, per month</th><td class="neg">−$65.00</td></tr>
    <tr><th scope="row">Savings</th><td class="neg">−$200.00</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">Left for everyday spending</th><td>$1,178.50</td></tr>
    <tr><th scope="row">÷ 30.4375 days</th><td>$38.72 a day</td></tr>
  </tfoot>
</table>
</div>

<p class="big-number"><span class="big-number-value">$38.72</span><span class="big-number-label">a day, or about $271 a week</span></p>

<p>Why 30.4375? A year has 365.25 days on average, counting leap years, and 365.25 ÷ 12 = 30.4375. Using the average keeps your daily number the same all year. Short months and long months even out.</p>
<p>Dividing by 30 is fine for a quick estimate, but it gives $39.28 a day. Spend that every day for a year and you'd go through about $206 more than you have, roughly five days' worth.</p>

<h2>Step 6: Check it against real life</h2>
<p>A number on paper is only useful if you can live on it. Two quick checks:</p>
<ul>
  <li><strong>Groceries.</strong> In this plan, food comes out of the daily allowance. If your shop runs to about $90 a week, that's $12.86 a day, which leaves about $25.86 a day for everything else.</li>
  <li><strong>Last month.</strong> Add up what you actually spent last month outside your bills. If it was $1,500 and the plan gives you $1,178.50, expect the first few weeks to feel tight. Either find a bill to cut, lower the savings figure, or accept the tighter month knowing why it feels that way.</li>
</ul>
<p>Also think about the costs that are neither bills nor everyday spending: birthdays, the dentist, car servicing, a trip home. Either add a yearly estimate for them in step 3 or accept that they'll come out of your daily money when they happen. Both work. What causes problems is forgetting them entirely.</p>
<p>None of this is financial advice. It's arithmetic, and the right numbers depend on your situation.</p>

<h2>Doing it in Daily Allowance</h2>
<p>Daily Allowance does steps 3 and 5 for you. Quick Setup, offered when you first open the app, asks for your monthly income and monthly expenses and shows the result with the note "Based on 30.4 days/month average", the same division as above.</p>
<p>To be more precise, add each bill as its own entry: tap +, enter the amount, open More options, switch on Recurring entry and pick how often it repeats: daily, weekly, monthly or yearly. Your recurring entries are listed together under Settings &gt; Daily Allowance. The app converts each one to a daily amount, so you don't have to turn the insurance or the weekly class into monthly figures yourself. Entered that way, the example comes to about $38.71 a day; the app converts weekly and yearly items straight to days, so its figure can differ from a hand calculation by a cent or so. To save first, add your savings as a monthly recurring expense, the same way as a bill.</p>
<p>The free plan includes 5 recurring entries, and Premium removes the limit. If you're on the free plan, group small bills together, for example one "Utilities and phone" entry instead of three.</p>
<p>Once it's set up, log what you spend during the day. Your Daily Balance goes up by each day's share and down with each expense, and whatever is left carries into tomorrow. If you go over one day, the next post covers <a href="/blog/what-to-do-when-you-overspend.html">what to do on a day you overspend</a>.</p>
""",
},
{
"slug": "what-to-do-when-you-overspend",
"date": "2026-11-06",
"title": "What to do on a day you overspend",
"description": "Going over your daily allowance happens. How to measure the damage in days, three ways to make it up, and what to change if it keeps happening.",
"body": """
<p class="lede">Going over your daily allowance happens to everyone, and one day over tells you very little. What matters is what you do over the next few days.</p>

<h2>First, log it</h2>
<p>It's tempting to leave a bad day out, or to log it "later". Don't. Every purchase you don't record makes the numbers wrong in your favor, so your balance looks healthier than it is and the next overspend comes as more of a surprise.</p>
<p>Log the full amount, on the day it happened, while you still remember what it was.</p>

<h2>Measure it in days</h2>
<p>An overspend in dollars is hard to judge. Measured in days of allowance, it's easy to picture.</p>
<p>Say your allowance is $40 a day. You started the day with $20 in hand, then spent $130 on a friend's birthday dinner and a late train home:</p>
<p class="sum">$20 + $40 − $130 = <span class="neg">−$70</span></p>
<p>$70 ÷ $40 = 1.75. You're less than two days behind. Put that way, it's a short stretch of careful days, and nothing you have to start over from.</p>

<h2>Choose how to make it up</h2>
<h3>Spread it over a week</h3>
<p>This is the gentlest option. Spend $30 a day instead of $40 for the next seven days. Each day you gain $10, and after a week you're back to zero:</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Making up $70 at $30 a day</caption>
  <thead><tr><th scope="col">Day</th><th scope="col">Added</th><th scope="col">Spent</th><th scope="col">Balance</th></tr></thead>
  <tbody>
    <tr><th scope="row">Start</th><td></td><td></td><td class="neg">−$70</td></tr>
    <tr><th scope="row">Day 1</th><td>$40</td><td>$30</td><td class="neg">−$60</td></tr>
    <tr><th scope="row">Day 2</th><td>$40</td><td>$30</td><td class="neg">−$50</td></tr>
    <tr><th scope="row">Day 3</th><td>$40</td><td>$30</td><td class="neg">−$40</td></tr>
    <tr><th scope="row">Day 4</th><td>$40</td><td>$30</td><td class="neg">−$30</td></tr>
    <tr><th scope="row">Day 5</th><td>$40</td><td>$30</td><td class="neg">−$20</td></tr>
    <tr><th scope="row">Day 6</th><td>$40</td><td>$30</td><td class="neg">−$10</td></tr>
    <tr><th scope="row">Day 7</th><td>$40</td><td>$30</td><td>$0</td></tr>
  </tbody>
</table>
</div>

<p>Ten dollars a day is usually one skipped coffee and a packed lunch. Most people can manage that without feeling deprived.</p>

<h3>Have one or two quiet days</h3>
<p>If you'd rather get it over with, a day of almost no spending, cooking what's already in the cupboard and walking instead of riding, takes you from −$70 to −$30. A second quiet day puts you $10 ahead.</p>
<p>Be honest with yourself about whether you'll keep it up. A day of strict denial followed by a "reward" is how a $70 problem becomes a $150 one. If quiet days tend to end that way for you, spread it out instead.</p>

<h3>Cover it from savings</h3>
<p>If the overspend was for something you're glad you did and you have savings set aside, moving money back to cover it is a reasonable choice. Just be clear with yourself that this is spending your savings. If it happens every month, the savings figure in your plan is more than you can actually afford.</p>

<p>What doesn't work is ignoring it. When unspent money rolls over, so does the shortfall. It stays in your balance until you make it up, whether you look at it or not.</p>

<h2>When it wasn't everyday spending</h2>
<p>Some overspends are a case of the wrong yardstick. A car repair, a flight home or a replacement laptop isn't day-to-day spending, and measuring it against a $40 day makes it look like a disaster.</p>
<p>For costs like that, step outside the daily allowance. Pay them from savings, or treat them as a bill: split the cost into monthly amounts over the next few months, which lowers your allowance a little each day until it's paid off. A $600 repair spread over six months is about $3.29 a day, and you'll notice that far less than a single −$560 day.</p>

<h2>If it keeps happening</h2>
<p>One overspend is an event. Four in a week is information. The two usual causes are:</p>
<ul>
  <li><strong>A missing bill.</strong> A yearly subscription, a quarterly water bill or a regular transfer to someone is quietly coming out of your daily money. Check your statements for anything you left out of the plan.</li>
  <li><strong>An allowance that's too small for how you live.</strong> If most days run over, more willpower won't fix it. Change the plan: lower a bill, reduce the savings target for now, or accept a smaller allowance with your eyes open and decide what you'll cut.</li>
</ul>
<p>Look back over the last month and count the days you went over. A handful of scattered red days is normal. A solid run of them means the numbers need changing.</p>

<h2>How Daily Allowance handles an overspend</h2>
<ul>
  <li><strong>You see it the same day.</strong> Under your Daily Balance, the Daily Allowance bar turns red and shows "Over by" and the amount once today's spending passes your allowance.</li>
  <li><strong>The shortfall carries forward.</strong> Your Daily Balance goes negative, and each new day's share of your income and bills is added on top, so it climbs back as you spend less than your allowance. It doesn't reset at the end of the month.</li>
  <li><strong>The forecast shows the way back.</strong> The home screen shows where your balance will be tomorrow and the day after, before any new spending.</li>
  <li><strong>Top up from Kitty Bank.</strong> When your balance is negative, this button moves exactly the shortfall from your Kitty Bank savings, bringing your balance back to zero.</li>
  <li><strong>Spread over months.</strong> With Premium, you can turn a large purchase into monthly payments. The app warns that your daily allowance will be reduced every day until it's paid off.</li>
  <li><strong>Exclude from daily balance.</strong> For an entry that shouldn't count against your daily money, such as something paid from a separate account, switch this on and it won't affect your balance or allowance.</li>
  <li><strong>The calendar shows the pattern.</strong> In Analytics, a calendar colors each day of the month by whether you stayed under your allowance, so a run of red days is easy to spot.</li>
</ul>
<p>One bad day out of thirty, recorded honestly and made up over a week, barely changes the month.</p>
""",
},
]
