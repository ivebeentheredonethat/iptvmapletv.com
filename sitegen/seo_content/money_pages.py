"""Supporting copy for the two conversion pages that are built in pages.py: /iptv-plans-canada/ and /try-iptv-canada/.

Kept here (not inline in pages.py) so the wording is easy to edit. Prices are never typed by hand: they come from plans.json.
"""
from ..components import FEATURES, checks
from ._util import plan, price_range

LOW, PER_MONTH = price_range()


def _card(inner):
    return f'<section class="section section--tight"><div class="container narrow"><div class="prose-card prose reveal">{inner}</div></div></section>'


EXTRA_PRICING = '''
<h2>IPTV subscription, plans, packages: what each term means</h2>
<p>An <strong>IPTV subscription</strong> (people type “ip tv subscription”, “iptv sub”, “iptv subscribe”, “buy iptv subscription” or “iptv premium subscription”) is a paid plan that gives you a login for live channels, sports and on-demand video. “IPTV plans” and “IPTV packages” mean the same: our options differ by length (1, 6 or 12 months) and by the number of screens. Compare the price table above, or read the full breakdown on <a href="/iptv-price/">IPTV prices in Canada</a>.</p>
<ul>
<li><strong>Best IPTV subscription:</strong> the one you can test first. Start the <a href="/try-iptv-canada/">free trial</a>.</li>
<li><strong>Premium subscription:</strong> “premium” is a marketing word; what matters is channels, stability and support.</li>
<li><strong>Buying elsewhere (eBay, marketplaces):</strong> no trial, no support history. See <a href="/iptv-providers/">comparing providers</a>.</li>
</ul>
<p>French: <a href="/abonnement-iptv/">abonnement IPTV</a>. Questions? <a href="/go/wa">WhatsApp us</a>.</p>
'''

EXTRA_TRIAL = '''
<h2>Free trial IPTV: questions we hear</h2>
<p>A <strong>free trial IPTV</strong> (also “trial IPTV”, “IPTV tester” or “try IPTV”) lets you test the service before paying. Ours lasts 24 hours and needs no credit card. A good trial test: open a live sports channel, a movie from the on-demand library, then switch channels ten times to see how fast it responds. Then check it on your own device with one of the guides: <a href="/iptv-firestick/">Firestick</a>, <a href="/iptv-smarters-pro/">Smarters</a>, <a href="/tivimate/">TiviMate</a>. When you are ready, see the <a href="/iptv-plans-canada/">plans</a>. If the free trial doesn’t start, check <a href="/iptv-ne-fonctionne-plus/">troubleshooting</a> or WhatsApp us.</p>
'''


def pricing_copy():
    return _card(f"""
<h2>What an IPTV subscription in Canada includes</h2>
<p>An <strong>IPTV subscription</strong> gives you live TV, sports, movies and series over your internet connection, on the TVs, phones and computers you already own. Every IPTVMaple plan includes the same things; only the number of screens and the length of the plan change:</p>
{checks(FEATURES)}

<h2>How an IPTV subscription works</h2>
<ol>
<li><strong>Choose your plan.</strong> Pick 1 to 5 screens and 1, 6 or 12 months. Prices start at ${LOW} and the 12-month plan works out to about ${PER_MONTH:.2f} a month for one screen.</li>
<li><strong>Get your login.</strong> We send a server URL, username and password by email and WhatsApp, usually within minutes.</li>
<li><strong>Install an app and watch.</strong> Use <a href="/tivimate/">TiviMate</a>, <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> or another player. Follow the <a href="/how-it-works/">setup guides</a> for your device.</li>
</ol>

<h2>Which IPTV subscription should I choose?</h2>
<table>
<thead><tr><th>Your situation</th><th>Best choice</th></tr></thead>
<tbody>
<tr><td>You want to see if it works for you</td><td>Start the <a href="/try-iptv-canada/">free 24-hour trial</a>, then 1 month at ${LOW}</td></tr>
<tr><td>One person, one main TV</td><td>1 screen, 12 months: ${plan(1, 12)['price']}</td></tr>
<tr><td>A couple with TVs in two rooms</td><td>2 screens, 12 months: ${plan(2, 12)['price']}</td></tr>
<tr><td>A family with several TVs and phones</td><td>3 to 5 screens, 12 months: ${plan(3, 12)['price']} to ${plan(5, 12)['price']}</td></tr>
<tr><td>You travel or move often</td><td>6 months: ${plan(1, 6)['price']} for one screen</td></tr>
</tbody>
</table>
<p>Count the screens that are on <em>at the same time</em>, not the devices you own. If you’re not sure, start with fewer; you can always order a bigger plan.</p>

<h2>Buy IPTV online with less risk</h2>
<ul>
<li><strong>Try before you pay.</strong> The free trial needs no credit card.</li>
<li><strong>7-day money-back guarantee</strong> on every purchase: see the <a href="/refund/">refund policy</a>.</li>
<li><strong>No contract and no hidden fees.</strong></li>
<li><strong>Real support</strong> on WhatsApp and email, day and night, in English and French.</li>
</ul>

<h2>IPTV subscription vs cable and streaming apps</h2>
<p>Cable and satellite TV with sports commonly cost $80–$150 or more a month, and streaming apps cost $15–$25 each. An IPTV plan puts live channels, sports and on-demand video in one subscription. See the full numbers in our <a href="/iptv-price/">IPTV price guide</a>, and learn how to evaluate any service with the <a href="/iptv-providers/">IPTV provider scorecard</a>.</p>

<h2>Before you subscribe</h2>
<p>Check the <a href="/channels-list/">channels list</a> for the channels you care about, confirm your device is covered in the <a href="/iptv-devices/">device guides</a> and <a href="/iptv-apps/">app guides</a>, and read our honest explainer, <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> Living in Québec? See our <a href="/abonnement-iptv/" hreflang="fr-CA" lang="fr-CA">forfaits en français</a>.</p>
""" + EXTRA_PRICING)


def trial_copy():
    return _card(f"""
<h2>What you get with the free IPTV trial</h2>
<p>The IPTVMaple trial is a full 24-hour test of the service, not a cut-down demo. You can use it on your own TV or phone, with your own internet connection.</p>
{checks(["24 hours of access to live TV, sports, movies and series", "HD and 4K channels, including Canadian channels in English and French", "No credit card and no commitment", "Your login by email and WhatsApp", "Works with TiviMate, IPTV Smarters Pro and the other supported apps"])}

<h2>How to start your free IPTV trial</h2>
<ol>
<li><strong>Fill in the form above</strong> with your name, email, country and WhatsApp number.</li>
<li><strong>Receive your login</strong> by email and WhatsApp, usually within a few minutes.</li>
<li><strong>Install an app</strong> on your device. Pick yours in the <a href="/how-it-works/">setup guides</a>: <a href="/iptv-firestick/">Firestick</a>, <a href="/iptv-samsung-tv/">Samsung</a>, <a href="/iptv-lg-tv/">LG</a>, <a href="/iptv-apple-tv/">Apple TV</a>, <a href="/iptv-android-tv/">Android TV</a> or <a href="/iptv-pc-mac/">PC and Mac</a>.</li>
<li><strong>Enter your login</strong> and start watching.</li>
</ol>

<h2>What to test in 24 hours</h2>
<ul>
<li><strong>A live game at peak time</strong>, such as hockey on a Saturday night.</li>
<li><strong>Your local and French channels</strong> and the TV guide.</li>
<li><strong>The device you will really use</strong>, not just your phone.</li>
<li><strong>Support</strong>: send a real question and see how fast the answer comes.</li>
</ul>
<p>If anything buffers, our <a href="/iptv-buffering-fix/">buffering fixes</a> solve most problems.</p>

<h2>After the trial</h2>
<p>Because no card is needed, nothing is charged when the trial ends. If you want to keep watching, <a href="/iptv-plans-canada/">choose a plan</a> from ${LOW}. Every purchase is covered by a <a href="/refund/">7-day money-back guarantee</a>.</p>

<h2>A free trial is not a free playlist</h2>
<p>Free IPTV playlists shared on forums are not trials: they usually stop working within hours and can carry risks. Read <a href="/m3u-playlist/">what an M3U playlist is</a> and <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> before trying one. A real trial comes from a business that also offers support and a refund policy. Not sure which service to try? Use the <a href="/iptv-providers/">provider scorecard</a>.</p>
""" + EXTRA_TRIAL)


TRIAL_FAQ = [
    {"q": "Is the IPTV free trial really free?",
     "a": "<p>Yes. The IPTVMaple trial lasts 24 hours and needs no credit card, so nothing is charged when it ends.</p>"},
    {"q": "Do I need a credit card for the free IPTV trial?",
     "a": "<p>No. You only provide your name, email, country and WhatsApp number so we can send your login.</p>"},
    {"q": "How fast do I get my trial login?",
     "a": "<p>Usually within a few minutes, by email and on WhatsApp. If you haven’t received it, check your spam folder or message our team.</p>"},
    {"q": "What can I watch during the trial?",
     "a": "<p>The same live TV, sports, movies and series as a paid plan, in HD and 4K, including Canadian channels in English and French.</p>"},
    {"q": "Which devices work with the free trial?",
     "a": "<p>Firestick, Android TV, Samsung and LG smart TVs, Apple TV, iPhone, iPad, Windows, Mac and MAG or Formuler boxes. See the setup guides.</p>"},
    {"q": "What happens after the 24 hours?",
     "a": "<p>The trial simply ends. To keep watching, choose a plan from $9. Every plan has a 7-day money-back guarantee.</p>"},
]


def home_copy():
    return _card("""
<h2>IPTV in Canada: Canadian IPTV for every province</h2>
<p>IPTVMaple is <strong>IPTV from Canada</strong>, built for people who want <strong>Canadian IPTV</strong> without cable. Whether you search for “Canada IPTV”, “IPTV in Canada” or “best IPTV for Canada”, you get the same thing here: live TV, sports, movies and series over your internet connection, on the devices you already own. If you moved away and want Canadian television back (“IPTV back to Canada”), the lineup carries the national networks and regional feeds, and works anywhere you have broadband.</p>
<ul>
<li><strong>Start free:</strong> <a href="/try-iptv-canada/">24-hour IPTV trial</a>, no card.</li>
<li><strong>Compare:</strong> <a href="/best-iptv-canada/">how to choose the best IPTV</a>, <a href="/iptv-providers/">providers</a> and <a href="/iptv-price/">prices</a>.</li>
<li><strong>Your area:</strong> <a href="/iptv-near-me/">IPTV by province and city</a>, <a href="/iptv-quebec/">IPTV Québec</a>, <a href="/usa/">IPTV USA</a>.</li>
<li><strong>Your device:</strong> <a href="/iptv-firestick/">Firestick</a>, <a href="/iptv-smarters-pro/">Smarters Pro</a>, <a href="/tivimate/">TiviMate</a>, <a href="/iptv-box/">IPTV boxes</a>.</li>
<li><strong>New to this?</strong> <a href="/iptv-for-beginners/">IPTV for beginners</a>.</li>
</ul>
""")
