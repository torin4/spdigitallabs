"""Hanjo blog posts. Every statement about how Hanjo works is checked against the app's code (../house-designer)."""

POSTS = [
{
"app": "hanjo",
"slug": "read-a-japanese-floor-plan",
"date": "2026-11-14",
"title": "How to read a Japanese floor plan: jo, tsubo, LDK and the 910 mm grid",
"description": "What jo, tsubo and 3LDK mean on a Japanese house plan, how to convert them to square metres, and why the walls sit on a 910 mm grid.",
"body": """
<p class="lede">A Japanese house plan uses a few units and abbreviations you won't find on plans elsewhere. Once you know what a jo, a tsubo and "3LDK" stand for, and why so many dimensions are multiples of 910 mm, the plan reads like any other.</p>

<h2>Jo: room sizes counted in tatami mats</h2>
<p>One jo (<span lang="ja">畳</span>) is the area of one tatami mat. Rooms are described by how many mats would cover the floor, whether or not the room has tatami: a 6-jo bedroom, a 16-jo living room.</p>
<p>The catch is that mats are not one size. They vary by region and by type of building. These are the usual nominal sizes:</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Common tatami sizes</caption>
  <thead><tr><th scope="col">Type</th><th scope="col">Size</th><th scope="col">Area</th></tr></thead>
  <tbody>
    <tr><th scope="row">Kyoma (Kyoto and western Japan)</th><td>955 × 1,910 mm</td><td>1.82 m²</td></tr>
    <tr><th scope="row">Chukyoma (around Nagoya)</th><td>910 × 1,820 mm</td><td>1.66 m²</td></tr>
    <tr><th scope="row">Edoma (Tokyo and eastern Japan)</th><td>880 × 1,760 mm</td><td>1.55 m²</td></tr>
    <tr><th scope="row">Danchima (apartment blocks)</th><td>850 × 1,700 mm</td><td>1.45 m²</td></tr>
  </tbody>
</table>
</div>

<p>For property advertising, Japan's fair competition rules for real estate say one jo must be at least 1.62 m². That is the figure most conversions use:</p>
<p class="sum">6 jo × 1.62 = 9.72 m²</p>
<p>Treat a jo count as a rough size. Two "6-jo" rooms on different plans can differ by a noticeable amount, so check the dimensions too.</p>

<h2>Tsubo: land, floor area and price</h2>
<p>One tsubo (<span lang="ja">坪</span>) is about 3.31 m², roughly the area of two tatami mats. Plots of land, the total floor area of a house and building costs are all commonly quoted in tsubo. A 100 m² house is 100 ÷ 3.3058 = 30.25 tsubo.</p>
<p>Builders often quote a price per tsubo (tsubo-tanka). What that price includes differs from builder to builder, so when you compare quotes, check that they cover the same work.</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Jo, square metres and tsubo</caption>
  <thead><tr><th scope="col">Jo</th><th scope="col">Square metres</th><th scope="col">Tsubo</th></tr></thead>
  <tbody>
    <tr><th scope="row">4.5</th><td>7.29</td><td>2.21</td></tr>
    <tr><th scope="row">6</th><td>9.72</td><td>2.94</td></tr>
    <tr><th scope="row">8</th><td>12.96</td><td>3.92</td></tr>
    <tr><th scope="row">10</th><td>16.20</td><td>4.90</td></tr>
    <tr><th scope="row">16</th><td>25.92</td><td>7.84</td></tr>
  </tbody>
</table>
</div>

<h2>The 910 mm grid</h2>
<p>Traditional timber houses are laid out in ken, a length of about 1,818 mm that is usually drawn as 1,820 mm. Half of that, 910 mm, is the module most Japanese house plans are drawn on. Walls, posts, doors and windows fall on the grid, which is why you keep seeing 910, 1,820, 2,730 and 3,640 on a plan. Some builders use a 1,000 mm metre module instead.</p>
<p>Dimensions are normally measured to the centre of each wall (<span lang="ja">壁芯</span>, kabeshin), so the clear space is smaller than the number on the plan. A corridor one module wide is 910 mm from wall centre to wall centre and about 780 mm between the finished walls, depending on how thick the walls are.</p>
<p>The same goes for areas. A typical 6-jo room is 2,730 × 3,640 mm on the grid, which is 9.94 m² to the wall centres. The floor you can actually stand on is a little less.</p>

<h2>LDK: counting the rooms</h2>
<p>L is living, D is dining and K is kitchen. The number in front counts the other rooms, usually bedrooms. So a 3LDK has three rooms plus a combined living, dining and kitchen space. A 1K is one room with a separate kitchen, and a 1R is a single room.</p>
<p>An S, as in 2SLDK, is a service room: a room that can't be counted as a habitable room, usually because it doesn't have enough window. It's often used as a storeroom or study.</p>
<p>A few other words turn up on most plans:</p>
<ul>
  <li><strong>Washitsu</strong> is a Japanese-style room, usually with tatami.</li>
  <li><strong>Genkan</strong> is the entrance, where shoes come off.</li>
  <li><strong>Oshiire</strong> is a deep closet, made for futons.</li>
  <li><strong>Engawa</strong> is a strip of floor along the outside edge of the house, like a veranda.</li>
  <li><strong>Doma</strong> is an indoor floor at ground level that you can walk on in shoes.</li>
</ul>

<h2>Coverage and floor area ratio</h2>
<p>Two ratios limit how much house a plot can hold. The building coverage ratio (<span lang="ja">建蔽率</span>, kenpei-ritsu) is the building's footprint divided by the site area. The floor area ratio (<span lang="ja">容積率</span>, yoseki-ritsu) is the total floor area of all storeys divided by the site area. The limits depend on the plot's use zone and on local rules, and the land listing or the municipality will tell you what they are. On a 150 m² plot with limits of 50% and 100%:</p>
<p class="sum">150 m² × 50% = 75 m² footprint, and 150 m² × 100% = 150 m² of floor</p>

<h2>Doing it in Hanjo</h2>
<p><a href="/hanjo/">Hanjo</a> is a house design app built around these conventions. It runs in a browser, you need a free account to use it, and drawing is free.</p>
<ul>
  <li><strong>The grid.</strong> A new design uses the 910 mm module, and points snap to the half module, 455 mm. You can change the Module setting to 1000. Hold Alt while drawing to place something freely, to the millimetre. Lengths are always in millimetres.</li>
  <li><strong>Rooms.</strong> With the Room tool, drag a rectangle and the walls follow. A room that shares an edge with another reuses the wall that's already there. The Wall tool draws one wall at a time.</li>
  <li><strong>Jo, tsubo and square metres together.</strong> Once you're zoomed in far enough, each room's label shows its area in all three. Hanjo uses 1.62 m² per jo and 3.3058 m² per tsubo, and measures to wall centres.</li>
  <li><strong>Japanese room types.</strong> A room's Use can be LDK, Washitsu, Genkan, Oshiire, Engawa or Doma, among others, and door styles include Fusuma and Shoji.</li>
  <li><strong>The two ratios.</strong> The Checks tab lists each floor's area and the total in square metres and tsubo, and shows coverage and floor area ratio against the limits you enter for your plot.</li>
</ul>
<p>Hanjo doesn't count your rooms and label the house "3LDK" for you. Its ratios are also simplified: for example, it doesn't apply the floor-area exemptions that garages can get.</p>

<h3>Tracing a plan you were given</h3>
<p>If a builder or an estate agent has given you a plan, you can draw over it. Use Import a plan to trace, below the tools, and choose a PNG, JPEG or WebP image, or a PDF. Only the first page of a PDF is used. The drawing appears half transparent on the floor you're working on.</p>
<p>Then set its scale. Choose Calibrate scale, click two points on the drawing whose real distance you know, such as the two ends of a dimensioned wall, and type that distance in millimetres. You can drag the drawing into place, change its Opacity and Rotation, and Lock it so it stays put while you draw rooms on top. If the plan was drawn on a 910 mm module, its walls should line up with the grid.</p>

<p>Hanjo is a planning tool, not an architect. Have a licensed architect (<span lang="ja">建築士</span>) or builder check any design before you rely on it. Once your plan is drawn, <a href="/blog/check-a-house-plan.html">How to check a house plan before you commit to it</a> covers what to look for.</p>
""",
},
{
"app": "hanjo",
"slug": "check-a-house-plan",
"date": "2026-11-14",
"title": "How to check a house plan before you commit to it",
"description": "A plan can look fine on paper and still be awkward to live in. What to check: routes, furniture, door swings and sunlight, and how to test them in Hanjo.",
"body": """
<p class="lede">A floor plan can look fine on paper and still be awkward to live in. Changes are cheap while the house is a drawing and expensive once it's built, so it's worth an hour of checking how you'd actually move through it.</p>

<h2>Walk the daily routes</h2>
<p>Pick the trips you make every day and trace each one on the plan with a finger:</p>
<ul>
  <li>From the front door to the kitchen, carrying shopping.</li>
  <li>From the washing machine to where clothes dry, and from there to where they're put away.</li>
  <li>From each bedroom to the toilet at night.</li>
  <li>From the front door to the living room, as a guest would walk it.</li>
</ul>
<p>Count the doors and corners on each route, and notice what the route passes through. A laundry route that crosses the living room, or a toilet that opens straight off the dining area, is easy to miss on a plan and hard to ignore in a house.</p>

<h2>Put real furniture in</h2>
<p>An empty room always looks big enough. Draw the furniture you own, or plan to buy, at its real size: the bed, the sofa, the dining table with its chairs pulled out, the fridge with its door open.</p>
<p>Then look at what's left. A common rule of thumb is that one person needs about 600 mm to walk past something, and more on a route two people use at once. Check the gap between the bed and the wall, behind the dining chairs, and between the kitchen counter and whatever faces it.</p>

<h2>Check every door</h2>
<p>A hinged door sweeps a quarter circle as wide as the door itself. For each one, ask:</p>
<ul>
  <li>Does it hit furniture, or another door, as it opens?</li>
  <li>Does it open against a wall, or into the middle of the room?</li>
  <li>Can you stand clear of it while you open it, especially in a toilet or a small washroom?</li>
</ul>
<p>Sliding doors avoid the sweep, but they need a stretch of clear wall to slide along, and nothing can be fixed to that part of the wall.</p>

<h2>See where the sun falls</h2>
<p>The sun's height at noon depends on the season and on how far north you are. At noon it stands at 90° minus your latitude, plus or minus 23.4° for the tilt of the earth. At 35° north, about the latitude of Tokyo, Nagoya and Osaka, the winter figure is:</p>
<p class="sum">90° − 35° − 23.4° = 31.6°</p>

<div class="table-scroll">
<table class="ledger">
  <caption>Height of the noon sun at 35° north</caption>
  <thead><tr><th scope="col">Day</th><th scope="col">Sun above the horizon</th></tr></thead>
  <tbody>
    <tr><th scope="row">Summer solstice, around 21 June</th><td>about 78°</td></tr>
    <tr><th scope="row">Equinoxes, March and September</th><td>about 55°</td></tr>
    <tr><th scope="row">Winter solstice, around 21 December</th><td>about 32°</td></tr>
  </tbody>
</table>
</div>

<p>That difference is what eaves are for. The high summer sun is blocked by the overhang above a south window, and the low winter sun comes in under it and reaches deep into the room. So look at each main room at three times of day in both summer and winter: where the morning sun lands, whether the living room gets winter sun at all, and whether a west window will make a room hot on summer afternoons.</p>
<p>Remember what is outside the plan. A neighbour's two-storey house to the south can shade your ground floor all winter, whatever your own drawing shows.</p>

<h2>Doing it in Hanjo</h2>
<p><a href="/hanjo/">Hanjo</a> draws the 3D house from your plan, so these checks don't need a separate model. All of this is in the free part of the app. You need an account to use it.</p>
<h3>Furniture and doors</h3>
<p>The Library tool has furniture at real sizes: beds, sofas, dining tables, kitchens, unit baths, appliances. Pick an item and click the plan to place it. It snaps to a nearby wall, and holding Alt places it freely.</p>
<p>The Checks tab then lists what Hanjo finds, and clicking a line selects the thing on the plan. It reports "Furniture blocks a door" when something stands in the swing of a hinged door, or when less than 600 mm of clear way is left through a doorway. Rugs and other low things don't count. It also flags a room whose Use is Corridor when its clear width is under 750 mm, and stairs that are narrower than 750 mm, have risers over 230 mm or treads under 150 mm, which are Japan's minimums for stairs in a house. Those stair figures are legal minimums and make a steep stair. Most people want a gentler one.</p>
<h3>3D and the walk-through</h3>
<p>Switch from Plan to 3D at the top. Hide floors above cuts the house open at the floor you're on so you can look down into the rooms. Hide near walls removes whichever walls face you as you turn the house, Half-height inside walls cuts the partitions down, and Hide furniture clears the rooms.</p>
<p>Walk through puts you inside at an eye height of 1.5 m. Move with W, A, S and D or the arrow keys, drag to look around, and press Esc to leave. Walls stop you and doorways let you through, so a route that is awkward on the plan is awkward here too. You walk one floor at a time, and a small map shows where you are and lets you jump to another spot. A door can be shown open or closed in 3D, so you can see what an open door gets in the way of.</p>
<h3>Sunlight</h3>
<p>In 3D, the Time of day slider runs from 4:00 to 22:00 in half-hour steps, and Season switches between 21 June, the equinoxes and 21 December. Hanjo works out the sun's position from the Latitude and North settings of your site and shows it, for example "Sun 32° up, bearing 180°". The house casts shadows on itself and on the ground, and lamps come on after sunset.</p>
<p>The latitude starts at 35.5° north, so change it if you're building somewhere else, and set North to match your plot. The time is solar time, where noon is the moment the sun is due south, so it can differ a little from the clock.</p>

<h2>What Hanjo doesn't check</h2>
<ul>
  <li><strong>Your neighbours.</strong> The 3D view shows your house and your plot. Buildings, trees and slopes outside it aren't modelled, so their shadows aren't either.</li>
  <li><strong>The routes themselves.</strong> Hanjo tells you when a door is blocked or a corridor is narrow. Whether the laundry route makes sense is still your call.</li>
  <li><strong>Structure.</strong> Nothing in Hanjo checks whether the house will stand up, and its regulation checks are simplified.</li>
</ul>
<p>Hanjo is a planning tool, not an architect. Have a licensed architect (<span lang="ja">建築士</span>) or builder check any design before you rely on it. The easiest way to get that check is to show them the plan: <a href="/blog/share-a-house-plan.html">How to share a house plan with your builder and keep track of versions</a> covers how. If the units on your plan are new to you, start with <a href="/blog/read-a-japanese-floor-plan.html">How to read a Japanese floor plan</a>.</p>
""",
},
{
"app": "hanjo",
"slug": "share-a-house-plan",
"date": "2026-11-14",
"title": "How to share a house plan with your builder and keep track of versions",
"description": "How to show a house plan to your partner, family or builder, collect comments in one place, and keep track of which version everyone is looking at.",
"body": """
<p class="lede">A house plan goes through many rounds between you, your family and your builder. Most of the confusion comes from two things: comments scattered across emails and chats, and people looking at different versions of the drawing.</p>

<h2>Keep one current plan</h2>
<p>Decide where the current plan lives and who is allowed to change it. Everything else is a copy. If you email a PDF, that PDF is out of date the next time you move a wall, and a comment on it may be about something you've already fixed.</p>
<p>If you can, share a link to the plan itself, so whoever opens it sees it as it stands today. When you have to send a file, put the version name and the date on it.</p>

<h2>Name each version when you send it</h2>
<p>Save a version every time you send the plan to someone or agree something with them, and give it a name that says what changed: "Rev B, bigger kitchen" is more use in three weeks than "final 2". Then a builder who says "the stair in the plan you sent on the 3rd" is pointing at something you can open.</p>
<p>Try big changes on a copy. If you want to see what happens when the bathroom moves upstairs, do it on a separate copy and compare it with the current plan, so a bad idea is easy to throw away.</p>

<h2>Put comments on the plan</h2>
<p>"The door by the kitchen" can mean three different doors. A comment pinned to a spot on the drawing can only mean one. Whatever tool you use, try to get comments attached to the place they're about, one issue per comment.</p>
<p>Close comments as you deal with them. A list of twenty comments where fifteen are already dealt with hides the five that matter.</p>

<h2>Decide who needs what</h2>
<ul>
  <li><strong>Your partner or family</strong> need to look around and say what they think.</li>
  <li><strong>Your builder or architect</strong> need to see exact dimensions and tell you what won't work. They will usually redraw the plan in their own CAD software, so they also need something they can print or measure from.</li>
  <li><strong>Parents, friends, the bank</strong> may only need to look.</li>
</ul>
<p>Give each person the least access that does the job. And remember that a plan shows the size, shape and orientation of your plot, so think about who gets a link that anyone can open.</p>

<h2>Doing it in Hanjo</h2>
<p>Sharing in <a href="/hanjo/">Hanjo</a> is free. Open your design, choose Share and then Start sharing. Hanjo keeps a copy of the current design online and updates it a moment after each change you make. Nobody you share with can change your design. They can look, and some can comment.</p>
<h3>People you invite</h3>
<p>Under People, add someone's email address and choose a role:</p>
<ul>
  <li><strong>Can comment</strong> lets them pin comments to the plan and reply.</li>
  <li><strong>Architect</strong> does the same, and can also resolve or reopen other people's comments.</li>
  <li><strong>View only</strong> lets them see the design and read the comments, but not write any.</li>
</ul>
<p>Hanjo doesn't email the invitation. Copy the invitation link from the dialog and send it yourself. They open it and sign in, with Google or an email address and password, using the address you added. An account is free.</p>
<h3>View-only links</h3>
<p>A view-only link opens the design for anyone who has it, without signing in. They can't see or write comments. You choose whether it lasts 7 days, 30 days or has no end date. The link is shown once when you create it, so copy it then. You can turn a link off at any time.</p>
<h3>What they see</h3>
<p>Guests get the plan, the 3D view with its walk-through and sunlight controls, and the areas, checks and rough cost panels. They can also use Print / PDF. They don't see your saved versions, your proposals or any drawings you imported to trace. Those aren't part of the shared copy.</p>
<h3>Comments</h3>
<p>Once a design is shared, you and anyone who can comment get a Comment tool. Click the plan where the comment belongs and write it. Each comment gets a numbered pin, others can reply, and Resolve hides it from the list until you choose Show resolved. Comments show the email address of whoever wrote them.</p>
<h3>Versions and proposals</h3>
<p>The Versions tab has Save version, which stores the design as it is under a name you give it. Click a saved version to look at it: Hanjo highlights the walls that differ from the current design, and Restore this version brings it back. New proposal makes a copy to try a change on. You can compare it with the current design, then Accept it or Reject it.</p>
<h3>Sending a drawing</h3>
<p>Print / PDF opens your browser's print dialog with one A3 landscape sheet per floor, with dimensions, an area table and a title block showing the scale and date. Hanjo picks the scale from 1:50, 1:100, 1:200 or 1:500 so the plot fits. Choose Save as PDF there to get a file, and print at 100% for the scale to be true.</p>
<p>When the builder sends their own drawing back, you can import it and trace or compare it. <a href="/blog/read-a-japanese-floor-plan.html">How to read a Japanese floor plan</a> explains how, along with the units builders use.</p>
<h3>Stopping</h3>
<p>Stop sharing deletes the online copy, its comments and every link. The design in your account is kept.</p>

<h2>Where it falls short</h2>
<ul>
  <li><strong>Only you can edit.</strong> Even the Architect role can't change the design, and two people can't work on it at once.</li>
  <li><strong>No CAD export.</strong> Hanjo prints to PDF and saves a copy as a file that only Hanjo opens. It doesn't export DXF or other CAD formats, so a builder will redraw from the PDF.</li>
  <li><strong>Comments aren't live.</strong> New comments appear when you come back to the window, or within about 30 seconds. Hanjo doesn't send an email when someone comments.</li>
  <li><strong>Sharing is managed from one browser.</strong> The Share controls for a design are in the browser where you started sharing it.</li>
  <li><strong>Versions aren't shared.</strong> Guests always see the current design, so tell them which version name it matches when you ask for comments.</li>
</ul>
<p>A builder's comments are the start of a professional check, and they don't replace one. Hanjo is a planning tool, not an architect. Have a licensed architect (<span lang="ja">建築士</span>) or builder check any design before you rely on it. Before you send the plan, it's worth running through <a href="/blog/check-a-house-plan.html">How to check a house plan before you commit to it</a> yourself.</p>
""",
},
]
