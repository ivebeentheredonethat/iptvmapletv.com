"""Gap pass, part 5 (audit fixes): depth for pages under 600 words and outbound authority links."""

DATA = {}

DATA["iptv-resellers"] = dict(add="""
<h2>Red flags when you buy from a reseller</h2>
<ul>
<li><strong>No named business.</strong> A real seller has a website, an email address and a policy page. If you can only reach someone through a social media account, you have nothing to fall back on if the service stops.</li>
<li><strong>Payment only by gift card or crypto.</strong> These make refunds impossible. Cards and payment processors give you dispute rights; ours are described on the <a href="/refund/">refund page</a>.</li>
<li><strong>Prices far below the market.</strong> Compare against the <a href="/iptv-price/">published price range</a>: if a yearly price is a fraction of it, the seller is probably covering the gap by cutting corners.</li>
<li><strong>Pressure to pay today.</strong> Countdown timers and “last slots” are sales tactics, not facts.</li>
<li><strong>No trial at all.</strong> Even a short test shows how the service behaves on your own connection.</li>
</ul>

<h2>What a good arrangement looks like</h2>
<p>You deal with one business that publishes its prices, answers on WhatsApp and email, and tells you plainly how to cancel or get a refund. Whether that business runs its own servers matters less than whether it takes responsibility when something breaks. That is the standard we hold ourselves to, and you can check it before paying: start the <a href="/try-iptv-canada/">free 24-hour trial</a>, ask us anything on <a href="/go/wa">WhatsApp</a>, and read the <a href="/about-iptvmaple/">about page</a>.</p>
<p>In Canada the legal side matters too. Rules differ for personal viewing and for selling access, so read <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> and the <a href="https://crtc.gc.ca/eng/home-accueil.htm" rel="noopener" target="_blank">CRTC’s</a> information on broadcasting before you build a business around resale.</p>
""")

DATA["iptv-for-beginners"] = dict(add="""
<h2>Which device should a beginner buy?</h2>
<p>If you don’t own a streaming device yet, buy a <a href="/iptv-firestick/">Fire TV Stick 4K</a>. It costs less than a month of cable, plugs into any HDMI port and works with the best player app, <a href="/tivimate-firestick/">TiviMate</a>. If your smart TV is recent, you may not need any extra hardware: see the <a href="/iptv-samsung-tv/">Samsung</a> and <a href="/iptv-lg-tv/">LG</a> guides. Phones and tablets work too (<a href="/iptv-smarters-pro-download/">download Smarters</a>).</p>

<h2>Common beginner mistakes</h2>
<ul>
<li><strong>Using Wi-Fi from another room.</strong> Plug the device into the router with an Ethernet adapter, or move the router closer. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>Typing the login by hand and getting one character wrong.</strong> Copy and paste the details we send you.</li>
<li><strong>Buying a long plan before testing.</strong> Use the free trial first.</li>
<li><strong>Trusting free lists from forums.</strong> They usually stop working within days (<a href="/m3u-playlist/">why</a>).</li>
<li><strong>Picking the wrong plan size.</strong> Count the screens that might be in use at the same time, not the number of TVs you own. The <a href="/iptv-price/">price guide</a> shows the cost per screen.</li>
</ul>

<h2>What to watch first</h2>
<p>Open the sports category and find a live game, then the on-demand section for a recent movie. Add the channels you use most to favourites. If you follow a sport, check its page: <a href="/nhl-iptv/">NHL</a>, <a href="/premier-league-iptv/">Premier League</a>, <a href="/ufc-iptv/">UFC</a>. Questions at any point? <a href="/go/wa">WhatsApp</a> or help@iptvmapletv.com.</p>
""")

DATA["iptv-lifetime"] = dict(add="""
<h2>What happens when a lifetime seller disappears</h2>
<p>Most “lifetime” customers find out the same way: the channels stop, the seller’s site is gone, and the payment cannot be traced. The money is not recoverable from a gift card, and a card chargeback has a time limit. By contrast a plan with a fixed end date has a clear value: you know what you paid for and when it ends.</p>
<p>If you still want to pay once for a long period, the 12-month plan is the closest honest option. At the 1-screen price, it works out to about <a href="/iptv-price/">$4 a month</a>, and if you are unhappy the <a href="/refund/">refund policy</a> applies. Add the screens you need on the <a href="/iptv-plans-canada/">plans page</a>.</p>
""")

DATA["iplaytv"] = dict(add="""
<h2>iPlayTV features worth knowing</h2>
<ul>
<li><strong>Playlist and Xtream support.</strong> You can load a link or log in with a server, username and password (<a href="/xtream-codes-iptv/">Xtream explained</a>).</li>
<li><strong>Apple devices first.</strong> It was built for iPhone, iPad and Apple TV, so it feels native there. On Android and Firestick, <a href="/tivimate/">TiviMate</a> is usually the better choice.</li>
<li><strong>Favourites and channel groups.</strong> Hide channels you never watch so the list is short.</li>
<li><strong>TV guide.</strong> Add an XMLTV address if your subscription provides one.</li>
</ul>
<p>If a channel won’t play, first check the login, then your internet speed (<a href="/iptv-buffering-fix/">fixes</a>). Still stuck? <a href="/go/wa">Message us</a> with a screenshot.</p>
""")

DATA["flix-iptv"] = dict(add="""
<h2>Setup checklist for Flix IPTV</h2>
<ol>
<li>Install the app from your device’s store.</li>
<li>Note any activation or device code the app displays.</li>
<li>Enter your server details exactly as sent: no spaces before or after.</li>
<li>Wait for the channel list and guide to load, which can take a minute on first start.</li>
<li>If a channel shows a black screen, switch the player setting from hardware to software decoding.</li>
</ol>
<p>Prefer something simpler? <a href="/tivimate-firestick/">TiviMate</a> and <a href="/iptv-smarters-pro-firestick/">Smarters Pro</a> have step-by-step guides here, and our <a href="/iptv-for-beginners/">beginner guide</a> explains the basics.</p>
""")

DATA["iptv-pc-mac"] = dict(add="""
<h2>Windows and Mac tips</h2>
<ul>
<li><strong>Use a wired connection</strong> for a laptop on a desk; Wi-Fi on a crowded channel is the most common cause of freezing.</li>
<li><strong>Update graphics drivers</strong> on Windows if 4K channels stutter.</li>
<li><strong>Fullscreen on a TV:</strong> use an HDMI cable and set the display to “duplicate” so the TV mirrors the laptop.</li>
<li><strong>Keep the player updated.</strong> Old versions of VLC and Kodi can fail on newer stream formats.</li>
</ul>
<p>Compare the options on <a href="/vlc-iptv/">VLC</a>, <a href="/kodi-iptv/">Kodi</a> and the <a href="/iptv-smarters-pro-pc-mac/">Smarters desktop app</a>.</p>
""")

DATA["xtream-codes-iptv"] = dict(add="""
<h2>Further reading</h2>
<p>Xtream Codes is a panel API, not a service in itself. The playlist format it can also export is explained in the <a href="https://en.wikipedia.org/wiki/M3U" rel="noopener" target="_blank">M3U article on Wikipedia</a>, and our own <a href="/m3u-playlist/">M3U guide</a> covers how apps use it. For the broader picture see <a href="/what-is-iptv/">what IPTV is</a>.</p>
""")

DATA["iptv-buffering-fix"] = dict(add="""
<h2>Measure before you guess</h2>
<p>Run a speed test on the same device you watch on, for example with <a href="https://www.speedtest.net/" rel="noopener" target="_blank">Speedtest by Ookla</a>, and compare the result with the table in the <a href="/iptv-for-beginners/">beginner guide</a>: about 10 Mbps per HD screen and 25 Mbps per 4K screen. If the test is fast but video still freezes, the cause is usually Wi-Fi interference, an overloaded router or a device that is too old, in that order.</p>
""")


# ---- link every city from its country hub, and tie the loose guides into the guide cluster (audit: pages with < 3 inbound links)
def _links():
    from .geo import CA_CITY_SLUG, US_CITY_SLUG, STATE_BY_ABBR
    from .geo_ca_data import CITIES as CA
    from .geo_us_data import CITIES as US
    ca = ", ".join(f'<a href="/{CA_CITY_SLUG[c[1]]}/">{c[1]}</a>' for c in sorted(CA, key=lambda c: c[1]))
    us = ", ".join(f'<a href="/{US_CITY_SLUG[c[1]]}/">{c[1]}, {c[0]}</a>' for c in sorted(US, key=lambda c: c[1]) if c[0] != "DC" and c[1] in US_CITY_SLUG)
    return ca, us


_ca, _us = _links()
DATA["canada"] = dict(add=f"<h2>All Canadian city guides</h2><p>{_ca}.</p>")
DATA["usa"] = dict(add=f"<h2>All US city guides</h2><p>{_us}.</p>")
DATA["iptv-price"] = dict(add="""
<h2>Understand who you are paying</h2>
<p>A low price means little if the seller disappears. Read <a href="/iptv-resellers/">IPTV resellers explained</a> before buying from anyone, and see <a href="/3-smarter-ways-to-stream-tv-without-cable-in-2025/">three ways to stream TV without cable</a> to compare IPTV with licensed apps and bundles.</p>
""")
DATA["iptv-providers"] = dict(add="""
<p>New to the idea of replacing cable? <a href="/3-smarter-ways-to-stream-tv-without-cable-in-2025/">Three ways to stream TV without cable in Canada</a> compares apps, bundles and IPTV.</p>
""")
