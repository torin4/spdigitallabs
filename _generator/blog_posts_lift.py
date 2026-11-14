"""Lift blog posts. Every statement about how Lift works is checked against the app's code (../lift)."""

POSTS = [
{
"app": "lift",
"slug": "when-to-add-weight",
"date": "2026-11-14",
"title": "When to add weight to a lift: a simple rule",
"description": "Pick a rep target, add one small step when every set reaches it, and hold when it doesn't. A worked example over seven sessions, and how Lift applies it.",
"body": """
<p class="lede">Most people who train with weights ask the same question every session: is today the day to go heavier? A simple rule, written down and followed, answers it before you reach the machine.</p>

<h2>The rule</h2>
<p>A common approach has three parts:</p>
<ul>
  <li><strong>Pick a rep target</strong> for the exercise, for example 3 sets of 10.</li>
  <li><strong>When every set reaches the target at the same weight, add one step</strong> next session.</li>
  <li><strong>When any set falls short, keep the weight</strong> and try again next session.</li>
</ul>
<p>Nothing more is needed to get started. The rule is useful because it settles the decision in advance, from what you actually did last time, so how you feel on the day doesn't come into it.</p>

<h2>What counts as a step</h2>
<p>A step is the smallest increase the equipment allows. On a machine it is one plate of the weight stack, often 2.5 kg, though stacks differ. On a barbell it is the smallest pair of plates the gym has. Dumbbells go up by whatever the rack offers.</p>
<p>Use the smallest step you can. Going from 40 kg to 42.5 kg is an increase of about 6%, which is already a lot to ask for the same ten reps. Skipping a step to save time usually costs you the next two sessions.</p>

<h2>A worked example</h2>
<p>Here is a chest press, 3 sets with a target of 10 reps, on a machine with 2.5 kg steps:</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Seven sessions on the chest press, target 3 × 10</caption>
  <thead><tr><th scope="col">Session</th><th scope="col">Weight</th><th scope="col">Reps</th><th scope="col">Next time</th></tr></thead>
  <tbody>
    <tr><th scope="row">1</th><td>40 kg</td><td>10, 10, 10</td><td>42.5 kg</td></tr>
    <tr><th scope="row">2</th><td>42.5 kg</td><td>10, 10, 8</td><td>42.5 kg</td></tr>
    <tr><th scope="row">3</th><td>42.5 kg</td><td>10, 10, 9</td><td>42.5 kg</td></tr>
    <tr><th scope="row">4</th><td>42.5 kg</td><td>10, 10, 10</td><td>45 kg</td></tr>
    <tr><th scope="row">5</th><td>45 kg</td><td>10, 9, 8</td><td>45 kg</td></tr>
    <tr><th scope="row">6</th><td>45 kg</td><td>10, 10, 8</td><td>45 kg</td></tr>
    <tr><th scope="row">7</th><td>45 kg</td><td>10, 9, 9</td><td>40 kg</td></tr>
  </tbody>
</table>
</div>

<p>Session 1 reached the target on every set, so the weight went up. Sessions 2 and 3 fell short on the last set, so the weight stayed, and the last set crept from 8 reps to 9 to 10. That took three sessions at 42.5 kg, which is normal. The reps are where the progress shows between increases.</p>
<p>Sessions 5 to 7 are the other case. Three sessions in a row at 45 kg, and the sets still aren't all reaching 10. The last row, where the weight drops, is covered below.</p>

<h2>When you stop moving</h2>
<p>Holding a weight for a session or two is part of the rule. Holding it for many sessions with no change is a sign that the rule needs a second half. A common answer is to take the weight down by about a tenth, work back up through weights you can complete, and meet the stuck weight again a few weeks later.</p>
<p>In the example, that is:</p>
<p class="sum">45 kg × 0.9 = 40.5 kg, rounded to the 2.5 kg step = 40 kg</p>
<p>How many stuck sessions to allow before easing off is a judgment call. Three is a reasonable place to start.</p>

<h2>The version with a rep range</h2>
<p>You'll also see this rule written with a range instead of a single target, often called double progression: work between, say, 8 and 12 reps, add reps until every set reaches 12, then add weight and start again from 8. It is the same idea with a wider gap between increases, and it suits equipment with large steps, where the next weight up is a big jump.</p>
<p>A single target is simpler to log and to check, since a set either reached the number or it didn't. If the steps on your equipment are small, it is usually enough.</p>

<h2>What the rule doesn't know</h2>
<ul>
  <li><strong>How the reps were done.</strong> Ten reps cut short or bounced are not the ten reps you did last month. Count a rep only if you'd have counted it then.</li>
  <li><strong>How you are today.</strong> A bad night's sleep or a long gap since the last session doesn't appear in the numbers. The rule gives you a starting point, and you can always choose less.</li>
  <li><strong>Your body.</strong> It is arithmetic on a log. It can't tell an easy set from a hard one, and it knows nothing about an old injury.</li>
</ul>
<p>None of this is medical advice or coaching. If something hurts, stop, and if you have a health concern, talk to a doctor before changing how you train.</p>

<h2>How Lift does it</h2>
<p><a href="/lift/">Lift</a> applies this rule from your own log and shows its working. Each exercise in a routine has a number of sets, one rep target, a rest time and a weight step. Lift uses a single rep target, not a range. A new exercise starts at 3 sets of 10, and you can change every one of those numbers when you edit the routine.</p>
<p>Before each exercise, Lift suggests a weight from the last session in which you did it:</p>
<ul>
  <li><strong>Every set at the same weight, all at or above the target:</strong> it adds one step. Sessions 1 and 4 in the table.</li>
  <li><strong>Same weight, but a set below the target:</strong> it holds. Sessions 2, 3, 5 and 6.</li>
  <li><strong>The same weight three sessions running without clearing the target:</strong> it suggests about 10% less, rounded to your step. Session 7, where it suggests 40 kg.</li>
  <li><strong>Fewer sets done than planned:</strong> it holds until you finish them all. A skipped set is recorded as skipped and is never treated as a failed one, and if you skipped the whole exercise last time, Lift works from the session before.</li>
  <li><strong>The first time you do an exercise:</strong> there is no suggestion. You choose the weight, and Lift works from that next time.</li>
</ul>
<p>There are a few more rules for sessions where the weight changed between sets. Tap Why on any suggestion to see the sets it used and the rule it applied.</p>
<p>The step starts from the type of equipment, for example 2.5 kg for machines, cables and barbells and 2 kg for dumbbells. Weight stacks differ, so set Step for each exercise in the routine editor to match yours. Bodyweight exercises start with no step, and Lift then holds the weight and says so. If you change an exercise's rep target, the next suggestion is rescaled to suit the new number of reps, and the normal rules carry on from there.</p>
<p>A suggestion never locks you in. Type a different weight and Lift works from what you actually did. Lift works in kilograms only.</p>
<p>All of this is free and works without an account. Lift Pro, the paid plan, builds routines for you. It doesn't change how weights are suggested: a generated routine has a rep target for each exercise, and the weights still come from your own log.</p>
<p>The rule depends on a log you can trust. <a href="/blog/how-to-keep-a-workout-log.html">How to keep a workout log you will actually use</a> covers what to write down, and <a href="/blog/count-weekly-sets-per-muscle.html">How to count weekly sets per muscle group</a> covers the other number worth watching.</p>
""",
},
{
"app": "lift",
"slug": "how-to-keep-a-workout-log",
"date": "2026-11-14",
"title": "How to keep a workout log you will actually use",
"description": "What to write down for each set, why machine settings and skipped sets are worth recording, and how to read the log back before your next session.",
"body": """
<p class="lede">A workout log is only useful if it answers a question next time: what did I do here last week, and what should I do today? Most logs fail because they record too much to keep up, or too little to answer that.</p>

<h2>What to write down</h2>
<p>For each set, two numbers: the weight and the reps. For each exercise, its name and the order you did it in. For the session, the date. Everything else in this post is optional, and those few things are not.</p>
<p>Write each set down when you finish it, not at the end of the session. By the time you are changing your shoes, you won't remember whether the third set of rows was 9 reps or 10, and that difference is exactly what decides <a href="/blog/when-to-add-weight.html">whether to add weight next time</a>.</p>
<p>One line per set is better than a summary. "3 × 10 at 40 kg" hides the session where the sets went 10, 10, 7. Written out, a single exercise looks like this:</p>

<div class="table-scroll">
<table class="ledger">
  <caption>One exercise in a log: lat pulldown</caption>
  <thead><tr><th scope="col">Set</th><th scope="col">Weight</th><th scope="col">Reps</th></tr></thead>
  <tbody>
    <tr><th scope="row">1</th><td>45 kg</td><td>10</td></tr>
    <tr><th scope="row">2</th><td>45 kg</td><td>10</td></tr>
    <tr><th scope="row">3</th><td>45 kg</td><td>8</td></tr>
    <tr><th scope="row">4</th><td>Skipped</td><td></td></tr>
  </tbody>
</table>
</div>

<p>Next to it, one line for the setup: seat 4, thigh pad 2.</p>

<h2>Machine settings</h2>
<p>The seat height, the pad position, which pin hole, how wide a grip. These are the things you forget between sessions, and they change the exercise. A leg press with the seat one notch further back is a different lift at the same weight, so last week's number stops being a fair comparison.</p>
<p>Write the setting down once, next to the exercise, and update it only when it changes. It also saves the first minute at each machine.</p>

<h2>Skipped sets</h2>
<p>If you planned four sets and did three, write that the fourth was skipped. Don't leave a gap, and don't write a zero.</p>
<p>The difference matters when you read the log back. A blank could mean you forgot to write it down. A zero looks like a set you tried and failed. "Skipped" says what happened: the machine was taken, you ran out of time, or you chose to stop. It also keeps the record honest about how much you did that day.</p>

<h2>A short note</h2>
<p>One line is enough, and only when there is something to say: the machine was a different model, you trained after a long gap, the last set felt easier than the reps suggest. Notes explain numbers that would otherwise look odd a month later.</p>

<h2>What to leave out</h2>
<p>Anything you won't keep up. Tempo, time under tension and a rating for every set are all fine if you use them, but a log with five fields per set tends to be abandoned by the third week. Start with weight and reps. Add a field only when you have wanted it more than once.</p>

<h2>Reading it back</h2>
<p>A log earns its keep in the minute before each exercise. Three ways to read it:</p>
<ul>
  <li><strong>Last time.</strong> Look at the same exercise in the previous session, set by set. That tells you the weight to start from and the reps to match or pass.</li>
  <li><strong>One exercise over weeks.</strong> Follow a single exercise back a month or two. A weight that hasn't moved is easier to see in a row of sessions than from memory.</li>
  <li><strong>The week as a whole.</strong> Count the sets you did for each part of the body. <a href="/blog/count-weekly-sets-per-muscle.html">How to count weekly sets per muscle group</a> shows how.</li>
</ul>
<p>Paper does all of this. A notebook with one page per session works, and so does the record sheet some gyms print. The weak point of paper is reading back: finding the last time you did an exercise means turning pages.</p>
<p>None of this is medical advice or coaching. A log records what you did. It doesn't tell you what is right for your body.</p>

<h2>Doing it in Lift</h2>
<p><a href="/lift/">Lift</a> is a workout log built around these points. You build a routine once, with the exercises in the order you do them, and each workout is a run through that list.</p>
<ul>
  <li><strong>One tap per set.</strong> Once you have done an exercise before, each set opens with a suggested weight filled in and a Last time column showing the weight and reps of the same set in your previous session. Tap the check and the set is logged at that weight and the exercise's rep target, and the rest timer starts. Change a number first only if it was different.</li>
  <li><strong>Skipped is its own state.</strong> Tap a set number to mark the set skipped, or Skip to skip the whole exercise. Any set you haven't logged when you finish is saved as skipped. Skipped sets are left out of set counts and volume.</li>
  <li><strong>Setup carries over.</strong> Each exercise has a Setup field for the seat or pad position. Whatever you last wrote there is filled in the next time you do that exercise.</li>
  <li><strong>Notes.</strong> Each exercise has a notes box, saved with the session.</li>
  <li><strong>Rest timer.</strong> It counts down the rest time set for that exercise, with buttons to add or take off 15 seconds, or to skip it.</li>
  <li><strong>Nothing lost mid-workout.</strong> If the app is closed during a workout, it reopens on the exercise you were on, with your sets and the timers as they were.</li>
</ul>
<p>To read the log back, History charts the working weight of any exercise session by session, with the sets of recent sessions listed underneath, and lists every session you have logged. Open a session to see each set, the setup and the notes, and use Edit this session to correct it. "Log a past workout" adds one you forgot, under the date it happened. Body measurements, such as your bodyweight, are kept separately on the Body screen.</p>

<h3>Accounts, offline use and your data</h3>
<p>Lift works without an account. Your log is then stored in your browser, on that device only, so clearing the browser's data for the site or losing the device loses the log. After the first visit it opens and saves with no connection.</p>
<p>If you sign in with Google, your log is also backed up and kept in step on every device where you sign in. Anything you log offline is synced when you are back online. Signing in is free.</p>
<p>Either way, Settings &gt; Export everything saves your routines, sessions, body measurements and settings as one file, and Import a backup puts a saved file back, replacing what is in the app.</p>
<p>Logging, history and sync are all free. Lift Pro is an optional paid plan that builds routines for you. It doesn't add anything to the log itself.</p>

<h2>Who it suits less</h2>
<ul>
  <li><strong>People who think in pounds.</strong> Lift works in kilograms only.</li>
  <li><strong>People who log a rating for each set.</strong> There is no field for how hard a set felt. The notes box is the only place for it.</li>
  <li><strong>People who train by rep ranges or mark warm-up sets.</strong> Each exercise has one rep target, and every set is the same kind of set.</li>
  <li><strong>People who do something different every session.</strong> Lift is quickest when you repeat a routine. You can add an exercise during a workout, but there is no blank session to fill in as you go.</li>
</ul>
""",
},
{
"app": "lift",
"slug": "count-weekly-sets-per-muscle",
"date": "2026-11-14",
"title": "How to count weekly sets per muscle group",
"description": "What a weekly set target is, how to count compound lifts, and how the count shows which muscle groups you have been leaving out. With a worked week.",
"body": """
<p class="lede">Counting the sets you do for each muscle group in a week is a simple way to see whether your training covers what you think it covers. It takes a log and a few minutes, and it often turns up a part of the body you had quietly stopped training.</p>

<h2>What a weekly set target is</h2>
<p>A weekly set target is a range, such as 6 to 14 sets a week for chest. You count the sets you did for that muscle group over seven days and see whether the total lands inside the range.</p>
<p>Sets are a convenient unit because they are easy to count and hard to distort. A total of kilograms lifted, the other figure people track, swings with the exercise you chose: a leg press moves far more weight than a lateral raise, and a pull-up moves none on paper. A set is a set on any equipment.</p>
<p>What range to use varies a lot between programs and people. A common starting point is around ten sets a week for a large muscle group and fewer for small ones, adjusted over time to what you can do and recover from. Treat any range as a place to start. It is not a prescription.</p>

<h2>Which sets to count</h2>
<p>The usual convention is to count working sets, the ones done at your training weight with real effort, and to leave out warm-ups. Sets you planned but didn't do don't count either. Whatever you decide, count the same way every week, or the totals can't be compared.</p>

<h2>How to count compound lifts</h2>
<p>A bench press works the chest, the shoulders and the triceps. So which gets the set? There are two common answers:</p>
<ul>
  <li><strong>One muscle group per exercise.</strong> Each exercise is filed under the muscle it mainly trains, and each set counts once. Bench press is chest, a row is back, a squat is quads.</li>
  <li><strong>Part credit.</strong> The main muscle gets a full set and the helpers get a fraction, often a half. Three sets of bench press become 3 for chest and 1.5 each for shoulders and triceps.</li>
</ul>
<p>The first is simpler and easy to do by hand, but it under-counts the muscles that assist. If your week is mostly presses and rows, your arms will look less trained than they are. The second is closer to what happened but needs a table of every exercise and takes longer. Either works if you stick to it and know which way it leans.</p>

<h2>A worked week</h2>
<p>Three sessions, counted with one muscle group per exercise:</p>
<ul>
  <li><strong>Monday:</strong> barbell bench press, lat pulldown, back squat, overhead press. 3 sets each.</li>
  <li><strong>Wednesday:</strong> chest press machine, machine row, leg press, lying leg curl. 3 sets each.</li>
  <li><strong>Friday:</strong> barbell bench press, barbell row, Romanian deadlift, 3 sets each. Barbell curl, 3 sets planned, the last one skipped.</li>
</ul>

<div class="table-scroll">
<table class="ledger">
  <caption>The week's sets against a target range</caption>
  <thead><tr><th scope="col">Muscle group</th><th scope="col">Sets</th><th scope="col">Target</th><th scope="col">Result</th></tr></thead>
  <tbody>
    <tr><th scope="row">Chest</th><td>9</td><td>6 to 14</td><td>In range</td></tr>
    <tr><th scope="row">Back</th><td>9</td><td>6 to 14</td><td>In range</td></tr>
    <tr><th scope="row">Quads</th><td>6</td><td>6 to 14</td><td>In range</td></tr>
    <tr><th scope="row">Hamstrings</th><td>6</td><td>4 to 12</td><td>In range</td></tr>
    <tr><th scope="row">Shoulders</th><td>3</td><td>6 to 14</td><td>Under</td></tr>
    <tr><th scope="row">Biceps</th><td>2</td><td>4 to 12</td><td>Under</td></tr>
    <tr><th scope="row">Glutes</th><td>0</td><td>4 to 12</td><td>Under</td></tr>
    <tr><th scope="row">Abs</th><td>0</td><td>4 to 12</td><td>Under</td></tr>
    <tr><th scope="row">Obliques</th><td>0</td><td>3 to 10</td><td>Under</td></tr>
  </tbody>
</table>
</div>

<p>The skipped curl set isn't counted, so biceps has 2. The Romanian deadlift is filed under hamstrings and the squat under quads, so glutes shows nothing even though both lifts use them. That is the one-muscle convention leaning the way described above.</p>

<h2>Reading the count</h2>
<ul>
  <li><strong>Look for zeros first.</strong> A muscle group with no sets for several weeks running is the clearest finding. In the example, abs and obliques have nothing, and no exercise in the week is aimed at them.</li>
  <li><strong>Then look for lopsided pairs.</strong> Chest far ahead of back, or quads far ahead of hamstrings, shows up as soon as the numbers are side by side.</li>
  <li><strong>Read "under" with the convention in mind.</strong> Shoulders has 3 sets of its own here, but two bench sessions also involved them. A low count for an assisting muscle means less than a low count for one nothing else trains.</li>
  <li><strong>Read "over" as a question.</strong> A total above your range isn't wrong. It is a prompt to check whether that was the plan.</li>
</ul>
<p>The fix is usually small: swap one exercise, or add two or three sets where the gap is. Rebuilding the whole week over one count is rarely needed. Look again after a few weeks.</p>
<p>None of this is medical advice or coaching. The count describes what you did. How much is right for you depends on things a tally can't see.</p>

<h2>How Lift does it</h2>
<p><a href="/lift/">Lift</a> keeps this count for you on its Stats screen, from the sessions you log.</p>
<ul>
  <li><strong>One muscle group per exercise.</strong> Every exercise in Lift's library belongs to one of 15 groups, and each set counts once, towards that group. Barbell bench press counts for chest, back squat for quads, deadlift for back, Romanian deadlift for hamstrings, overhead press for shoulders. There is no part credit, so the counts in the table above are the ones Lift would show for that week, against its default ranges. When you create your own exercise, you choose its group.</li>
  <li><strong>A rolling seven days.</strong> The count covers sessions dated today and the six days before, so it moves forward every day. It doesn't reset on Monday.</li>
  <li><strong>Every logged set counts.</strong> Skipped sets are left out. Lift doesn't know how hard a set was and has no warm-up set type, so a warm-up you log is counted like any other set. If you want the count to mean working sets, log only those.</li>
  <li><strong>A range for each group.</strong> Each bar is marked Under, In range or Over against a target range. The ranges start from defaults, for example 6 to 14 for chest, back, quads and shoulders, and 4 to 12 for hamstrings, glutes, abs, biceps, triceps and calves. They are starting points. Tap Edit targets to set your own.</li>
  <li><strong>Zeros are shown for seven groups.</strong> Chest, back, quads, hamstrings, glutes, abs and obliques always appear, even with no sets. The other groups, including shoulders, biceps, triceps and calves, appear only once they have at least one set in the seven days. If one of those is missing from the screen, its count is zero.</li>
</ul>
<p>The same screen shows the number of sessions and sets in the last seven days, and how the working weight of your recent exercises changed between the last two sessions.</p>
<p>Stats is free and works without an account, from the log on your device. Lift Pro, the paid plan, builds routines from the choices you make. It is separate from this count.</p>
<p>The count is only as good as the log behind it. <a href="/blog/how-to-keep-a-workout-log.html">How to keep a workout log you will actually use</a> covers what to record, and <a href="/blog/when-to-add-weight.html">When to add weight to a lift</a> covers the other decision a log helps with.</p>
""",
},
]
