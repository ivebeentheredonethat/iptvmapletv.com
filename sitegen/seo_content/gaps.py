"""New pages added in the gap pass: lifetime IPTV, IPTV resellers, IPTV for beginners."""
D = dict(published="2026-10-01", updated="2026-10-01")

PAGES = [
    dict(
        slug="iptv-lifetime", hub="guides", **D,
        title="Lifetime IPTV Subscription: Is It Worth It? | IPTVMaple",
        description="Lifetime IPTV deals sound cheap, but what do you actually get? How lifetime pricing works, the risks, better ways to save and what to ask before paying.",
        kicker="Buying guide", h1='Lifetime IPTV: <span class="grad-text">deal or trap?</span>',
        lead="A one-time price for “forever” sounds great. Here is why it rarely works out, and how to save money without the risk.",
        crumb="Lifetime IPTV", blurb="Why lifetime IPTV deals are risky and what to do instead.",
        answer="<p><strong>A lifetime IPTV subscription is almost never worth it.</strong> Running an IPTV service costs money every month (servers, bandwidth, content), so a one-time payment means the seller either shuts down, resells access they can’t keep, or limits what “lifetime” means. A long plan with a free trial and a refund policy is the safer way to save.</p>",
        body="""
<h2>How lifetime pricing works</h2>
<p>When a seller offers “lifetime IPTV” for a single payment, the money has to cover years of costs. It can only work if the seller (a) closes after collecting enough sign-ups, (b) sells you access that is cut when their supplier changes, or (c) redefines “lifetime” as the life of the product, which they decide.</p>
<table>
<thead><tr><th>Claim</th><th>What it can really mean</th></tr></thead>
<tbody>
<tr><td>“Lifetime” access</td><td>Until the seller stops or changes the terms</td></tr>
<tr><td>“Lifetime free channels” on a box</td><td>An unlicensed list that can stop at any time</td></tr>
<tr><td>“Lifetime IPTV promo”</td><td>A sales tactic: urgency, limited time</td></tr>
</tbody>
</table>

<h2>Better ways to pay less</h2>
<ul>
<li><strong>Take a longer plan.</strong> The 12-month plan costs far less per month than monthly billing: see the <a href="/iptv-price/">price table</a>.</li>
<li><strong>Test first.</strong> Our <a href="/try-iptv-canada/">free 24-hour trial</a> needs no card.</li>
<li><strong>Refer friends.</strong> <a href="/refer-a-friend/">Referral credit</a> lowers the cost.</li>
<li><strong>Check the refund policy</strong> before paying anyone: read <a href="/refund/">our refund policy</a>.</li>
</ul>

<h2>Questions to ask any seller</h2>
<ol>
<li>How long has the service operated, and who answers support?</li>
<li>What happens if the supplier cuts you off?</li>
<li>Is there a trial, and a written refund policy?</li>
<li>Does it publish its prices? See <a href="/iptv-providers/">how to compare providers</a>.</li>
</ol>
<p>Also read: <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> and <a href="/best-iptv-canada/">how to choose the best IPTV</a>.</p>
""",
        faq=[
            ("Is there a lifetime IPTV plan at IPTVMaple?",
             "<p>No. We offer 1, 6 and 12-month plans, with the 12-month plan giving the lowest monthly cost. See <a href=\"/iptv-plans-canada/\">plans</a>.</p>"),
            ("Why are lifetime IPTV deals so cheap?",
             "<p>Because the cost of running the service over many years is not covered by one low payment. That gap is the risk you carry.</p>"),
            ("Is a 12-month plan a good alternative?",
             "<p>Yes. It costs much less per month than monthly billing, and you only commit for a year, after a free trial.</p>"),
        ],
        related=["iptv-price", "iptv-providers", "best-iptv-canada", "iptv-resellers"],
        keywords=["lifetime iptv", "iptv lifetime", "iptv promo", "iptv promotions"],
    ),
    dict(
        slug="iptv-resellers", hub="guides", **D,
        title="IPTV Resellers Explained: Supplier vs Reseller | IPTVMaple",
        description="What is an IPTV reseller, how do suppliers and resellers differ, and how can you tell a stable service from a middleman? A buyer's guide for Canada.",
        kicker="Buying guide", h1='IPTV resellers <span class="grad-text">explained</span>',
        lead="Reseller, supplier, panel, provider: the words get mixed up. Here is what each one means for you as a viewer.",
        crumb="IPTV resellers", blurb="Supplier vs reseller, and how to tell which one you are buying from.",
        answer="<p><strong>An IPTV supplier runs the servers; an IPTV reseller sells access to someone else’s servers under their own name.</strong> Buying from a reseller is not automatically bad, but support and stability depend on a supplier you can’t see. Ask who runs the service, test the free trial, and avoid anyone who won’t answer.</p>",
        body="""
<h2>Supplier, reseller, provider</h2>
<table>
<thead><tr><th>Term</th><th>What they do</th><th>What it means for you</th></tr></thead>
<tbody>
<tr><td>Supplier</td><td>Runs servers and sources the channels</td><td>Controls quality and uptime</td></tr>
<tr><td>Reseller</td><td>Buys credits or access and sells it to customers</td><td>Depends on the supplier; support may be slow</td></tr>
<tr><td>Provider</td><td>The business you pay: may be either</td><td>Check how they answer questions</td></tr>
</tbody>
</table>

<h2>How to evaluate a seller</h2>
<ul>
<li>Is there a <a href="/try-iptv-canada/">free trial</a> with no card?</li>
<li>Are the prices public (<a href="/iptv-price/">example</a>)?</li>
<li>Is there a real contact (WhatsApp and email) and a <a href="/refund/">refund policy</a>?</li>
<li>Does the seller promise <a href="/iptv-lifetime/">lifetime access</a>? Walk away.</li>
</ul>

<h2>Looking to resell IPTV yourself?</h2>
<p>We don’t run a reseller programme on this website. If you want to talk about partnerships, <a href="/contact/">contact us</a>. For anyone starting a business, check the licensing rules for your province first: see <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a>.</p>
<p>More: <a href="/iptv-providers/">IPTV providers compared</a> and <a href="/best-iptv-canada/">best IPTV in Canada</a>.</p>
""",
        faq=[
            ("What does IPTV reseller mean?",
             "<p>A reseller buys access to an IPTV service from a supplier and sells it on under their own brand.</p>"),
            ("Do you offer a reseller programme?",
             "<p>No, not on this site. For business enquiries use the <a href=\"/contact/\">contact page</a>.</p>"),
            ("How do I know if my IPTV is from a reseller?",
             "<p>Ask who runs the servers and who handles outages. If the answers are vague, treat it as a reseller and rely on the trial and refund policy.</p>"),
        ],
        related=["iptv-providers", "iptv-lifetime", "iptv-price", "best-iptv-canada"],
        keywords=["iptv resellers", "iptv reseller", "best iptv resell", "iptvresale", "iptv supplier"],
    ),
    dict(
        slug="iptv-for-beginners", hub="guides", **D,
        title="IPTV for Beginners: Start Watching in 10 Minutes | IPTVMaple",
        description="New to IPTV? A plain-English beginner guide to what you need, which device and app to pick, how to start a free trial and what to check first. Canada.",
        kicker="Beginner guide", h1='IPTV for beginners: <span class="grad-text">start in 10 minutes</span>',
        lead="No jargon. Four things to pick, in order, and you will be watching.",
        crumb="IPTV for beginners", blurb="A no-jargon first-time guide to getting started with IPTV.",
        answer="<p><strong>To start with IPTV you need four things: an internet connection of about 10 Mbps per screen, a device (a Firestick is the easiest), a player app and a subscription.</strong> Begin with a free trial, install TiviMate or IPTV Smarters Pro, enter the login we send you and open any channel.</p>",
        body="""
<h2>The four things you need</h2>
<table>
<thead><tr><th>Step</th><th>What to do</th><th>Guide</th></tr></thead>
<tbody>
<tr><td>1. Internet</td><td>About 10 Mbps per screen for HD, 25 Mbps for 4K</td><td><a href="/iptv-buffering-fix/">Speed and buffering</a></td></tr>
<tr><td>2. A device</td><td>A Fire TV Stick is the best starting point</td><td><a href="/iptv-firestick/">Firestick</a>, <a href="/iptv-devices/">all devices</a></td></tr>
<tr><td>3. An app</td><td>TiviMate on Firestick, Smarters Pro on phones</td><td><a href="/tivimate/">TiviMate</a>, <a href="/iptv-smarters-pro/">Smarters</a></td></tr>
<tr><td>4. A subscription</td><td>Start with the free trial</td><td><a href="/try-iptv-canada/">Free trial</a></td></tr>
</tbody>
</table>

<h2>Words you will see</h2>
<ul>
<li><strong>M3U:</strong> a playlist link (<a href="/m3u-playlist/">explained</a>).</li>
<li><strong>Xtream Codes:</strong> a login made of server, username and password (<a href="/xtream-codes-iptv/">explained</a>).</li>
<li><strong>EPG:</strong> the TV guide.</li>
<li><strong>VOD:</strong> movies and series on demand.</li>
</ul>

<h2>Your first 10 minutes</h2>
<ol>
<li>Start the <a href="/try-iptv-canada/">free trial</a>.</li>
<li>Plug in your Firestick and install the app.</li>
<li>Enter the login. Wait a minute for the guide to load.</li>
<li>Try a live sports channel and a movie.</li>
<li>If it works, choose a <a href="/iptv-plans-canada/">plan</a>. If not, <a href="/go/wa">message us</a>.</li>
</ol>
<p>Want the background first? Read <a href="/what-is-iptv/">What is IPTV?</a>. Cord cutters should see <a href="/cord-cutting-guide/">the cord-cutting guide</a>.</p>
""",
        faq=[
            ("Is IPTV hard to set up?",
             "<p>No. On a Firestick it takes about ten minutes: install an app, enter a login, pick a channel.</p>"),
            ("Do I need a special box?",
             "<p>No. A Fire TV Stick, Android TV, a phone or a computer is enough. See <a href=\"/iptv-devices/\">devices</a>.</p>"),
            ("What internet speed do I need?",
             "<p>About 10 Mbps per screen for HD and 25 Mbps for 4K.</p>"),
        ],
        related=["what-is-iptv", "iptv-firestick", "tivimate", "iptv-price"],
        keywords=["iptv for beginners", "beginner iptv"],
    ),
]
