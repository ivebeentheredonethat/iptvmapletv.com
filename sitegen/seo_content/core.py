"""Core commercial & informational guides (no hub — breadcrumb is Home → page)."""
from html import escape

from ..components import data

_R = data("reviews")
_REVIEWS = "".join(
    f'<blockquote><p><strong>{escape(x["title"])}</strong> ★★★★★</p><p>{escape(x["body"])}</p><p><em>— {escape(x["name"])}, {escape(x["country"])}</em></p></blockquote>'
    for x in _R["reviews"])
_WA = "".join(
    f'<blockquote><p>“{escape(x["text"])}”</p><p><em>— {escape(x["name"])}, {escape(x["country"])} (WhatsApp)</em></p></blockquote>'
    for x in _R["whatsapp"])

PAGES = [
    # ------------------------------------------------------------------ BEST IPTV CANADA
    dict(
        slug="best-iptv-canada", hub="guides",
        title="Best IPTV Canada 2026: How to Choose a Provider | IPTVMaple",
        description="How to choose the best IPTV service in Canada in 2026: 8 criteria, red flags, IPTV vs cable vs streaming, and how IPTVMaple compares. Try it free for 24h.",
        kicker="Buyer’s guide", h1='Best <span class="grad-text">IPTV in Canada</span> (2026): how to choose',
        lead="There are hundreds of IPTV providers. Here’s the checklist we’d use to pick one — and how to test any service before you pay.",
        crumb="Best IPTV Canada 2026", blurb="8 criteria for choosing an IPTV provider.",
        answer="<p>The <strong>best IPTV service in Canada</strong> is one that carries Canadian channels in English and French (TSN, Sportsnet, RDS, TVA, CBC, CTV), stays stable during live sports, works with the apps you already use, offers a <strong>free trial</strong> and a <strong>money-back guarantee</strong>, and has real <strong>24/7 support</strong>. Test any provider on a busy night — like Saturday hockey — before paying for a long plan.</p>",
        body="""
<h2>8 things the best IPTV providers in Canada have in common</h2>
<ol>
<li><strong>Canadian channels, both languages</strong> — local CBC, CTV, Global and Citytv, plus TVA, ICI Radio-Canada, Noovo, RDS and TVA Sports.</li>
<li><strong>Sports that hold up at peak time</strong> — TSN, Sportsnet, NHL Center Ice, NBA League Pass and PPV that don’t freeze on a Saturday night.</li>
<li><strong>A free trial</strong> — at least 24 hours of full access, so you can test on your own TV and internet.</li>
<li><strong>A clear refund policy</strong> — written, with a time limit (for example, <a href="/refund/">7 days</a>).</li>
<li><strong>Works with standard apps</strong> — Xtream Codes and M3U logins for <a href="/tivimate/">TiviMate</a>, <a href="/iptv-smarters-pro/">IPTV Smarters</a> and smart TV apps.</li>
<li><strong>Human support</strong> — a WhatsApp or email team that answers in minutes, not days.</li>
<li><strong>Transparent pricing</strong> — prices on the website, no “message us for price”.</li>
<li><strong>Multi-device plans</strong> — the option to watch on 2–5 screens at once.</li>
</ol>

<h2>Red flags to avoid</h2>
<ul>
<li>“Lifetime” IPTV for a one-time payment — these services rarely last.</li>
<li>No trial, no refund policy, or payment only by gift card.</li>
<li>Pre-loaded “free TV” boxes sold with no ongoing support.</li>
<li>No website, or a website with no contact details.</li>
</ul>

<h2>IPTV vs cable vs streaming apps</h2>
<table>
<thead><tr><th></th><th>Cable / satellite</th><th>Streaming apps</th><th>IPTV (IPTVMaple)</th></tr></thead>
<tbody>
<tr><td>Typical monthly cost</td><td>$80–$150+ with sports</td><td>$15–$25 per app, adds up fast</td><td>From $9 (≈$4/month on 12-month plans)</td></tr>
<tr><td>Live Canadian channels</td><td>Yes</td><td>Limited</td><td>Yes, English &amp; French</td></tr>
<tr><td>Live sports &amp; PPV</td><td>Extra packages</td><td>Split across services</td><td>Included</td></tr>
<tr><td>Contract</td><td>Often</td><td>No</td><td>No</td></tr>
<tr><td>Devices</td><td>Rented box</td><td>Most devices</td><td>Most devices</td></tr>
</tbody>
</table>

<h2>How IPTVMaple measures up</h2>
<ul>
<li>50,000+ live channels including the full Canadian lineup in English and French</li>
<li>300,000+ movies and series on demand</li>
<li>HD and 4K with anti-freeze servers</li>
<li>Free 24-hour trial and 7-day money-back guarantee</li>
<li>1 to 5 simultaneous devices, from $9 — see <a href="/iptv-plans-canada/">all plans</a></li>
<li>24/7 human support on WhatsApp and email</li>
</ul>
<p>Read what customers say on our <a href="/iptv-reviews/">IPTV reviews</a> page.</p>

<h2>How to test an IPTV service properly</h2>
<ol>
<li>Start the trial on the device you’ll really use (not just your phone).</li>
<li>Watch a big live game at peak time.</li>
<li>Check the French and local channels you care about.</li>
<li>Message support with a question and time the answer.</li>
</ol>
""",
        faq=[
            ("What is the best IPTV service in Canada?", "<p>The best IPTV service is the one that passes your own test: Canadian channels in both languages, stable sports at peak time, a free trial, a refund policy and fast support. IPTVMaple offers all of these — start with the free 24-hour trial.</p>"),
            ("How much does IPTV cost in Canada?", "<p>Reputable IPTV services typically cost $9–$20 per month, less on long plans. IPTVMaple starts at $9 for one month, or $49 for 12 months on one device.</p>"),
            ("Is IPTV better than cable?", "<p>For most households IPTV is cheaper, has more channels, needs no contract and works on the devices you already own. Cable’s advantage is that it doesn’t depend on your internet connection.</p>"),
            ("Do IPTV providers offer free trials?", "<p>Good ones do. IPTVMaple gives 24 hours of full access with no credit card.</p>"),
            ("What internet speed do I need for IPTV?", "<p>About 10 Mbps for HD and 25 Mbps for 4K per screen.</p>"),
        ],
        related=["iptv-reviews", "what-is-iptv", "4k-iptv", "iptv-sports"],
        keywords=["best iptv canada", "best iptv in canada", "best iptv for canada", "best iptv canada 2026", "best iptv 2026", "best iptv service canada", "best iptv provider canada", "best canadian iptv provider", "iptv providers canada", "iptv providers in canada", "iptv provider canada", "iptv service canada", "iptv providers", "provider iptv", "iptv service provider", "best iptv provider", "best iptv service", "best iptv services", "best iptv service provider", "best iptv providers", "best iptv", "iptv best", "ip tv best", "top iptv", "top iptv providers", "iptv top", "top 10 iptv", "top 5 iptv", "the best iptv", "the best iptv service", "iptv service", "service iptv", "iptv supplier", "great iptv", "good iptv", "iptv stable", "iptv fiable"],
    ),
    # ------------------------------------------------------------------ WHAT IS IPTV
    dict(
        slug="what-is-iptv", hub="guides",
        title="What Is IPTV? How It Works — Beginner’s Guide 2026 | IPTVMaple",
        description="What is IPTV (Internet Protocol Television)? How it works, what you need, IPTV vs cable and streaming, and how to get started — a simple 2026 guide for Canadians.",
        kicker="Beginner’s guide", h1='What is <span class="grad-text">IPTV</span>? A beginner’s guide',
        lead="IPTV explained in plain English: what it is, how it works, what you need and how it compares to cable.",
        crumb="What is IPTV?", blurb="IPTV explained in plain English.",
        answer="<p><strong>IPTV (Internet Protocol Television)</strong> is TV delivered over the internet instead of through cable or satellite. An IPTV service streams live channels, movies and series to an app on your TV, streaming stick, phone or computer. You need three things: an internet connection, a device, and an IPTV subscription with a player app.</p>",
        body="""
<h2>How IPTV works</h2>
<p>With cable, channels travel through a coaxial wire to a box rented from your provider. With IPTV, the same kind of video is sent as data over your internet connection. An IPTV <a href="/iptv-apps/">player app</a> requests the channel you pick and plays it instantly, just like a video on demand.</p>
<p>The term covers several types of service (see the <a href="https://en.wikipedia.org/wiki/Internet_Protocol_television" target="_blank" rel="noopener">Wikipedia overview of IPTV</a>):</p>
<ul>
<li><strong>Live TV</strong> — channels broadcast in real time, with a TV guide (EPG).</li>
<li><strong>Video on demand (VOD)</strong> — movies and series you start whenever you want.</li>
<li><strong>Catch-up / time-shift</strong> — watch programs that aired earlier.</li>
</ul>

<h2>What you need to watch IPTV</h2>
<ol>
<li><strong>Internet</strong> — 10 Mbps for HD, 25 Mbps for 4K.</li>
<li><strong>A device</strong> — Firestick, Android TV box, smart TV, Apple TV, phone or computer (<a href="/iptv-devices/">see all devices</a>).</li>
<li><strong>A player app</strong> — TiviMate, IPTV Smarters, SmartOne, etc.</li>
<li><strong>A subscription</strong> — the service that provides the channels, like <a href="/iptv-plans-canada/">IPTVMaple</a>.</li>
</ol>

<h2>IPTV vs cable vs streaming services</h2>
<ul>
<li><strong>vs cable</strong> — no rented box, no technician, no contract; usually far cheaper, with many more channels.</li>
<li><strong>vs Netflix-style apps</strong> — those are on-demand only; IPTV adds live TV, news and sports.</li>
</ul>

<h2>IPTV words you’ll see</h2>
<table>
<thead><tr><th>Term</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>EPG</td><td>Electronic program guide — the TV guide grid</td></tr>
<tr><td><a href="/m3u-playlist/">M3U</a></td><td>A playlist link containing your channels</td></tr>
<tr><td><a href="/xtream-codes-iptv/">Xtream Codes</a></td><td>A login with server URL, username and password</td></tr>
<tr><td>VOD</td><td>Video on demand — movies and series</td></tr>
<tr><td>Connections</td><td>How many devices can play at the same time</td></tr>
<tr><td>Anti-freeze</td><td>Server technology that reduces buffering</td></tr>
</tbody>
</table>

<h2>How to get started</h2>
<p>The easiest way to understand IPTV is to try it. Request the <a href="/try-iptv-canada/">free 24-hour trial</a>, install an app on your TV, and our team will walk you through it on WhatsApp.</p>
""",
        faq=[
            ("What does IPTV stand for?", "<p>Internet Protocol Television — TV delivered over an internet connection instead of cable or satellite.</p>"),
            ("Do I need a smart TV for IPTV?", "<p>No. Any TV with an HDMI port works with a Firestick or Android box. Smart TVs can also use IPTV apps directly.</p>"),
            ("Is IPTV the same as Netflix?", "<p>Not quite. Netflix is on-demand only. IPTV includes live TV channels, sports and news, plus on-demand movies and series.</p>"),
            ("Does IPTV use a lot of data?", "<p>About 1.5–3 GB per hour in HD and 7 GB or more per hour in 4K. Most Canadian home internet plans are unlimited.</p>"),
            ("Is IPTV hard to set up?", "<p>No — install an app, enter your login and start watching. It takes about 5–10 minutes.</p>"),
        ],
        related=["iptv-apps", "iptv-devices", "m3u-playlist", "best-iptv-canada"],
        keywords=["ip television", "iptv tv", "iptv", "iptv what is it", "television iptv", "tv ip", "iptv for beginners", "online iptv", "online ip tv", "ip tv online", "iptv live", "live iptv", "live ip tv", "iptv stream", "stream iptv", "iptv streaming service", "iptv watch tv online", "watch iptv", "ott tv", "iptv vod"],
    ),
    # ------------------------------------------------------------------ 4K IPTV
    dict(
        slug="4k-iptv", hub="guides",
        title="4K IPTV in Canada: Premium Ultra HD Channels | IPTVMaple",
        description="Premium 4K IPTV in Canada: Ultra HD sports, movies and channels, what you need for 4K (speed, device, TV) and how to avoid buffering. Try IPTVMaple free 24h.",
        kicker="4K &amp; premium", h1='Premium <span class="grad-text">4K IPTV</span> in Canada',
        lead="Sports, movies and series in Ultra HD — and the simple setup that makes 4K IPTV look its best.",
        crumb="4K IPTV", blurb="Ultra HD channels and how to get the best picture.",
        answer="<p><strong>4K IPTV</strong> streams channels and movies in Ultra HD (3840×2160) — four times the detail of Full HD. To watch it you need a <strong>4K TV</strong>, a <strong>4K device</strong> (Firestick 4K, Apple TV 4K, Nvidia Shield, Formuler) and about <strong>25 Mbps</strong> per stream. IPTVMaple includes 4K sports, channels and movies in every plan.</p>",
        body="""
<h2>What’s available in 4K</h2>
<ul>
<li>Live sports on 4K and UHD feeds — including Sky Sports UHD and 4K event channels</li>
<li>Canadian channels delivered in high-bitrate 4K feeds</li>
<li>4K movies and series in the on-demand library</li>
</ul>

<h2>What you need for 4K IPTV</h2>
<table>
<thead><tr><th>Requirement</th><th>Recommendation</th></tr></thead>
<tbody>
<tr><td>Internet</td><td>25 Mbps per 4K stream; wired or 5 GHz Wi-Fi</td></tr>
<tr><td>Device</td><td><a href="/iptv-firestick/">Fire TV Stick 4K / 4K Max</a>, <a href="/iptv-apple-tv/">Apple TV 4K</a>, Nvidia Shield, <a href="/formuler-iptv/">Formuler Z11</a></td></tr>
<tr><td>TV</td><td>4K TV with an HDCP 2.2 HDMI port</td></tr>
<tr><td>App</td><td><a href="/tivimate/">TiviMate</a>, iPlayTV or IMPlayer</td></tr>
</tbody>
</table>

<h2>HD vs Full HD vs 4K</h2>
<ul>
<li><strong>HD (720p)</strong> — fine for phones and small screens; ~5–10 Mbps.</li>
<li><strong>Full HD (1080p)</strong> — sharp on most TVs; ~10–15 Mbps.</li>
<li><strong>4K (2160p)</strong> — best on 55″ and larger TVs; ~25 Mbps.</li>
</ul>
<p>Not every broadcast is produced in 4K. When a 4K feed isn’t available, you’ll get the best HD version instead.</p>

<h2>Premium IPTV features</h2>
<p>Besides picture quality, a premium IPTV service should offer anti-freeze servers, catch-up, a full TV guide, fast channel switching and real support. IPTVMaple includes all of it in every plan — no “premium tier” upsell. See <a href="/iptv-plans-canada/">plans and prices</a>.</p>
""",
        faq=[
            ("Is IPTV available in 4K?", "<p>Yes. IPTVMaple includes 4K sports, channels and movies wherever a 4K feed exists.</p>"),
            ("What speed do I need for 4K IPTV?", "<p>About 25 Mbps per 4K stream. Two 4K TVs at once need about 50 Mbps.</p>"),
            ("Why doesn’t my 4K channel look 4K?", "<p>Check that your device, HDMI port and TV all support 4K, and that the app’s output resolution is set to 4K.</p>"),
            ("Is there 8K IPTV?", "<p>There is almost no 8K broadcast content today. 4K is the highest quality widely available for live TV.</p>"),
        ],
        related=["iptv-box", "iptv-sports", "best-iptv-canada"],
        keywords=["iptv 4k", "4k iptv", "8k iptv", "iptv 8k", "iptv8k", "premium iptv", "iptv premium", "iptv premium 4k", "iptv premium subscription", "hd iptv", "iptv full hd", "ip tv 4k", "iptv 4k ott", "4k ott iptv", "private iptv", "iptv max"],
    ),
    # ------------------------------------------------------------------ REVIEWS
    dict(
        slug="iptv-reviews", hub="guides",
        title="IPTVMaple Reviews: What Canadian Customers Say | IPTVMaple",
        description="Real IPTVMaple reviews from customers in Canada and abroad, plus how to judge IPTV reviews and test the service yourself with a free 24-hour trial.",
        kicker="Reviews", h1='IPTVMaple <span class="grad-text">reviews</span>',
        lead="Real words from customers — plus how to read IPTV reviews critically and test the service yourself.",
        crumb="IPTV reviews", blurb="What customers say, and how to test yourself.",
        answer="<p>IPTVMaple customers mostly mention <strong>picture quality</strong>, <strong>stable sports</strong> and <strong>fast WhatsApp support</strong>. The best review is your own, though: request the <strong>free 24-hour trial</strong>, test it on your TV during a big game, and you’re also covered by a <strong>7-day money-back guarantee</strong> after you buy.</p>",
        body=f"""
<h2>Customer reviews</h2>
{_REVIEWS}

<h2>Messages from our WhatsApp support chat</h2>
{_WA}

<h2>How to judge IPTV reviews</h2>
<ul>
<li><strong>Look for specifics</strong> — a device, a channel, a problem that was fixed. Vague five-star lines say little.</li>
<li><strong>Check dates</strong> — IPTV quality changes; recent reviews matter most.</li>
<li><strong>Be wary of “lifetime” deals</strong> praised in reviews — they rarely last.</li>
<li><strong>Test it yourself</strong> — no review replaces a trial on your own internet and TV.</li>
</ul>

<h2>Try before you trust</h2>
<p>Start with the <a href="/try-iptv-canada/">free trial</a>. If you subscribe and aren’t satisfied, our <a href="/refund/">refund policy</a> gives you 7 days to get your money back. Compare us against others with our <a href="/best-iptv-canada/">guide to choosing an IPTV provider</a>.</p>
""",
        faq=[
            ("Is IPTVMaple reliable?", "<p>Customers highlight stable streams and quick support. The best way to check is the free 24-hour trial on your own setup.</p>"),
            ("What if I’m not satisfied?", "<p>IPTVMaple offers a 7-day money-back guarantee after purchase.</p>"),
            ("Where can I leave a review?", "<p>Send your feedback to our team on WhatsApp or by email — we read every message.</p>"),
            ("Can I talk to support before buying?", "<p>Yes, message us on WhatsApp any time — we answer questions before and after you subscribe.</p>"),
        ],
        related=["best-iptv-canada", "what-is-iptv"],
        keywords=["iptv canada reviews", "iptv reviews", "iptv trustpilot", "trustpilot iptv"],
    ),
]
