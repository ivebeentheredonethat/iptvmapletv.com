"""Depth pass, part 1: the IPTV basics, app and guide pages. See deep.py for how entries are applied."""

DATA = {}

# =============================================================================================== WHAT IS IPTV (full rewrite)
DATA["what-is-iptv"] = dict(
    meta=dict(
        title="What Is IPTV? How It Works, Cost & Setup (2026) | IPTVMaple",
        description="What is IPTV? A plain-English guide to how IPTV works, what you need, how it compares with cable and streaming, what it costs and how to start in Canada.",
        answer="<p><strong>IPTV (Internet Protocol Television) is television delivered over your internet connection</strong> instead of a cable, satellite or antenna signal. You watch live channels, sports, movies and series through an app on a smart TV, Firestick, phone or computer. In Canada, IPTV subscriptions start at about $9 a month, and you can try IPTVMaple free for 24 hours.</p>",
    ),
    replace="""
<h2>What IPTV means</h2>
<p>IPTV stands for <strong>Internet Protocol Television</strong>. Cable sends channels down a coaxial wire and satellite sends them from a dish. IPTV sends the same kind of video as data over the internet connection you already pay for. The result is the familiar TV experience (a channel list, a TV guide, live sports) plus a library of movies and series you can start whenever you like.</p>
<p>The name covers several different services, from the TV packages offered by telecom companies to independent subscription services, so it helps to know which one you are looking at. See the <a href="https://en.wikipedia.org/wiki/Internet_Protocol_television" target="_blank" rel="noopener">Wikipedia overview of IPTV</a> for the technical background.</p>

<h2>How IPTV works, step by step</h2>
<ol>
<li><strong>Channels are captured and encoded.</strong> The provider receives each channel and compresses it into a stream your device can play (HD or 4K).</li>
<li><strong>Servers deliver the stream.</strong> Load-balanced servers send the video over the internet to thousands of viewers at once.</li>
<li><strong>Your app connects.</strong> A <a href="/iptv-apps/">player app</a> logs in with your details, loads the channel list and TV guide, and requests the channel you pick.</li>
<li><strong>The video plays.</strong> Your device decodes the stream. Because it is just data, you can watch on a TV, phone, tablet or computer.</li>
</ol>

<h2>The three kinds of IPTV</h2>
<table>
<thead><tr><th>Type</th><th>Examples</th><th>How you pay</th></tr></thead>
<tbody>
<tr><td>Telecom TV delivered over IP</td><td>Bell Fibe TV, Telus Optik TV</td><td>A TV package, often bundled with internet</td></tr>
<tr><td>Licensed streaming apps</td><td>Crave, CBC Gem, Sportsnet+</td><td>One subscription per app</td></tr>
<tr><td>Independent IPTV subscriptions</td><td>IPTVMaple and similar services</td><td>One plan covers live TV, sports and on-demand video</td></tr>
</tbody>
</table>
<p>People searching for “IPTV” usually mean the third kind. Our <a href="/iptv-providers/">guide to IPTV providers</a> shows how to compare them, and <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> explains why licensing matters.</p>

<h2>What you need to watch IPTV</h2>
<table>
<thead><tr><th>Item</th><th>What to have</th></tr></thead>
<tbody>
<tr><td>Internet</td><td>About 10 Mbps for HD and 25 Mbps for 4K, per screen</td></tr>
<tr><td>A device</td><td>Firestick, Android TV box, smart TV, Apple TV, phone or computer. See the <a href="/iptv-devices/">device guides</a></td></tr>
<tr><td>A player app</td><td>TiviMate, IPTV Smarters Pro, SmartOne and others: <a href="/iptv-apps/">compare IPTV apps</a></td></tr>
<tr><td>A subscription</td><td>The service that supplies the channels, such as <a href="/iptv-plans-canada/">IPTVMaple</a></td></tr>
</tbody>
</table>
<p>You do not need a special TV, a satellite dish or a technician visit. You keep your current internet provider.</p>

<h2>IPTV vs cable vs satellite vs streaming apps</h2>
<table>
<thead><tr><th></th><th>Cable</th><th>Satellite</th><th>Streaming apps</th><th>IPTV</th></tr></thead>
<tbody>
<tr><td>Delivered by</td><td>Coaxial or fibre</td><td>Dish</td><td>Internet</td><td>Internet</td></tr>
<tr><td>Live TV</td><td>Yes</td><td>Yes</td><td>Limited</td><td>Yes</td></tr>
<tr><td>On-demand library</td><td>Limited</td><td>Limited</td><td>Yes, per app</td><td>Yes</td></tr>
<tr><td>Equipment</td><td>Rented box</td><td>Dish and receiver</td><td>Any device</td><td>Any device</td></tr>
<tr><td>Contract</td><td>Often</td><td>Often</td><td>No</td><td>Usually none</td></tr>
<tr><td>Typical cost</td><td>$80–$150+ with sports</td><td>Similar</td><td>$15–$25 per app</td><td>From $9, see <a href="/iptv-price/">IPTV prices</a></td></tr>
</tbody>
</table>

<h2>What you can watch on IPTV</h2>
<ul>
<li><strong>Live TV with a program guide (EPG)</strong> — channels from Canada and many other countries.</li>
<li><strong>Sports</strong> — hockey, basketball, football, UFC, F1 and pay-per-view. See <a href="/iptv-sports/">IPTV for sports</a>.</li>
<li><strong>Movies and series on demand (VOD)</strong> — a large library you can start any time.</li>
<li><strong>Catch-up</strong> — replay recent programs on supported channels.</li>
<li><strong>Several screens at once</strong> — depending on your plan, from 1 to 5.</li>
</ul>
<p>In Canada that includes the national networks (CBC, CTV, Global, Citytv), the French channels (TVA, ICI Radio-Canada, Noovo, RDS, TVA Sports), TSN and Sportsnet. Browse the <a href="/channels-list/">channels list</a>.</p>

<h2>How much does IPTV cost?</h2>
<p>IPTV plans on IPTVMaple start at $9 for one month, or about $4.08 a month on the 12-month plan for one screen. Cable with sports commonly costs $80–$150 or more a month. Full numbers are on the <a href="/iptv-price/">IPTV price</a> page.</p>

<h2>Is IPTV legal and safe?</h2>
<p>The technology is legal. Whether a particular service is lawful depends on whether it has rights to the content it distributes. Read our honest explainer on <a href="/is-iptv-legal-in-canada/">IPTV legality in Canada</a>. For safety, download apps only from official sources, avoid “modded” apps and free playlists from forums, and keep your login private.</p>

<h2>Does IPTV use a lot of data?</h2>
<p>It uses the same data as any video streaming: roughly 2–4 GB per hour in HD and about 7–11 GB per hour in 4K, depending on the channel. If your home internet has a monthly data cap, check it before streaming a lot of 4K.</p>

<h2>IPTV words you will see</h2>
<table>
<thead><tr><th>Term</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>EPG</td><td>Electronic program guide, the TV guide grid</td></tr>
<tr><td><a href="/m3u-playlist/">M3U</a></td><td>A playlist link that contains your channels</td></tr>
<tr><td><a href="/xtream-codes-iptv/">Xtream Codes</a></td><td>A login with server URL, username and password</td></tr>
<tr><td>VOD</td><td>Video on demand: movies and series</td></tr>
<tr><td>Catch-up</td><td>Watching a program that already aired</td></tr>
<tr><td>Connections</td><td>How many screens can play at the same time</td></tr>
<tr><td>Anti-freeze</td><td>Server technology that reduces buffering</td></tr>
</tbody>
</table>

<h2>How to get started</h2>
<ol>
<li>Start the <a href="/try-iptv-canada/">free 24-hour trial</a> (no credit card).</li>
<li>Receive your login by email and WhatsApp.</li>
<li>Install an app such as <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>. The <a href="/how-it-works/">setup guides</a> cover every device.</li>
<li>If it works for you, <a href="/iptv-plans-canada/">choose a plan</a>. A <a href="/refund/">7-day money-back guarantee</a> applies.</li>
</ol>
<p>If something buffers, the <a href="/iptv-buffering-fix/">buffering fixes</a> solve most problems. Want to watch on a computer? See <a href="/watch-iptv-online/">watch IPTV online</a>.</p>
""",
    faq=[
        ("Is IPTV the same as streaming?",
         "<p>IPTV is a type of streaming focused on television: live channels with a TV guide, plus on-demand video. Apps like Netflix are on-demand only. Both use your internet connection.</p>"),
        ("How is IPTV different from cable?",
         "<p>Cable sends channels over a wire to a rented box. IPTV sends them over your internet connection to an app on a device you already own, usually with no contract and a much lower price.</p>"),
        ("Do I need an internet connection for IPTV?",
         "<p>Yes. IPTV needs about 10 Mbps for HD and 25 Mbps for 4K per screen. A wired Ethernet connection or 5 GHz Wi-Fi gives the most stable picture.</p>"),
        ("Can I use IPTV on my phone?",
         "<p>Yes. Install an app such as IPTV Smarters Pro or Smarters Player Lite on your phone or tablet and log in with your IPTV details.</p>"),
    ],
    related=["iptv-price", "is-iptv-legal-in-canada", "iptv-providers", "watch-iptv-online"],
)

# =============================================================================================== IPTV APPS (hub)
DATA["iptv-apps"] = dict(
    meta=dict(title="Best IPTV Player & Apps in Canada (2026) | IPTVMaple"),
    add="""
<h2>IPTV apps compared</h2>
<table>
<thead><tr><th>App</th><th>Devices</th><th>Login</th><th>Guide</th><th>Price</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><a href="/tivimate/">TiviMate</a></td><td>Android TV, Fire TV</td><td>Xtream, M3U</td><td>Excellent grid</td><td>Free; <a href="/tivimate-premium/">Premium</a> optional</td><td>Daily live TV with a remote</td></tr>
<tr><td><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></td><td>Android, Fire TV, Windows, Mac</td><td>Xtream, M3U</td><td>Good</td><td>Free</td><td>First-time users, computers</td></tr>
<tr><td><a href="/smarters-player-lite/">Smarters Player Lite</a></td><td>iPhone, iPad, Apple TV</td><td>Xtream, M3U</td><td>Good</td><td>Free</td><td>Apple devices</td></tr>
<tr><td><a href="/xciptv/">XCIPTV</a></td><td>Android, Fire TV</td><td>Xtream, M3U</td><td>Good</td><td>Free</td><td>Older Firesticks</td></tr>
<tr><td><a href="/implayer/">IMPlayer</a></td><td>Android TV, Fire TV, Apple</td><td>Xtream, M3U</td><td>Grid</td><td>Free; Premium optional</td><td>Mixed Android and Apple homes</td></tr>
<tr><td><a href="/iplaytv/">iPlayTV</a></td><td>Apple TV, iPhone, iPad</td><td>M3U, Xtream</td><td>Grid</td><td>Paid</td><td>Apple TV with a cable-style guide</td></tr>
<tr><td><a href="/stbemu/">STBEmu Pro</a></td><td>Android</td><td>Portal (MAC)</td><td>MAG-style</td><td>Free and Pro</td><td>Fans of the MAG interface</td></tr>
<tr><td><a href="/mytvonline/">MyTVOnline 3</a></td><td>Formuler boxes</td><td>Portal, Xtream</td><td>Good</td><td>Included with the box</td><td>Formuler owners</td></tr>
<tr><td><a href="/smart-iptv/">Smart IPTV</a></td><td>Samsung, LG</td><td>M3U (by MAC)</td><td>Basic</td><td>One-time activation</td><td>Older smart TVs</td></tr>
<tr><td><a href="/smartone-iptv/">SmartOne IPTV</a></td><td>Samsung, LG, Android</td><td>M3U, Xtream (by MAC)</td><td>Good</td><td>Varies</td><td>Smart TVs</td></tr>
<tr><td><a href="/flix-iptv/">Flix IPTV</a></td><td>Samsung, LG, Android, Fire TV, Apple</td><td>M3U (by MAC)</td><td>Good</td><td>Trial then activation</td><td>Smart TVs with movies and series</td></tr>
<tr><td><a href="/kodi-iptv/">Kodi</a></td><td>Windows, Mac, Android, Fire TV, Linux</td><td>M3U (add-on)</td><td>Good</td><td>Free</td><td>A full media centre</td></tr>
<tr><td><a href="/vlc-iptv/">VLC</a></td><td>Windows, Mac, mobile</td><td>M3U</td><td>None</td><td>Free</td><td>A quick test</td></tr>
</tbody>
</table>
<p>Prices and activation rules are set by each app’s developer and can change. Check the app’s own page before you pay.</p>

<h2>How to choose an IPTV player in 60 seconds</h2>
<ol>
<li><strong>Start with your device.</strong> Firestick or Android TV: TiviMate. Samsung or LG: a smart TV app. Apple: Smarters Player Lite or iPlayTV. Computer: Smarters Pro or VLC.</li>
<li><strong>Prefer Xtream Codes</strong> over an M3U link whenever the app supports it. The guide, movies and series load automatically.</li>
<li><strong>Try the free option first.</strong> Every IPTVMaple plan works with free players; paid upgrades only add convenience.</li>
<li><strong>Keep a backup app.</strong> Many people install two, for example TiviMate on the TV and Smarters on the phone.</li>
</ol>

<h2>IPTV app safety checklist</h2>
<ul>
<li>Download only from an official store or the developer’s own website. Avoid “modded”, “cracked” or “premium unlocked” files.</li>
<li>Don’t paste your login or M3U link into websites that offer to “check” or “play” it online. See <a href="/watch-iptv-online/">watch IPTV online</a>.</li>
<li>Be wary of apps that ask for permissions a TV player doesn’t need, such as contacts or SMS.</li>
<li>Keep your login private; sharing it beyond your plan’s screen limit can get it locked.</li>
</ul>

<h2>More app guides</h2>
<p>Going deeper on specific apps and devices:</p>
<ul>
<li>TiviMate: <a href="/tivimate-firestick/">install on Firestick</a>, <a href="/tivimate-premium/">Premium cost and features</a>, <a href="/tivimate-devices/">which devices it supports</a>.</li>
<li>IPTV Smarters: <a href="/iptv-smarters-pro-firestick/">Firestick</a>, <a href="/iptv-smarters-pro-samsung-lg/">Samsung and LG</a>, <a href="/iptv-smarters-pro-pc-mac/">PC and Mac</a>, <a href="/iptv-smarters-pro-download/">safe download</a>.</li>
<li>Media servers: <a href="/plex-iptv/">Plex</a>, <a href="/jellyfin-iptv/">Jellyfin and Emby</a>, <a href="/stremio-iptv/">Stremio</a>.</li>
<li>Prefer to read in French? <a href="/lecteur-iptv/">Meilleur lecteur IPTV</a>.</li>
</ul>
""",
    faq=[
        ("What is an IPTV player?",
         "<p>An IPTV player is an app that connects to an IPTV subscription and shows its channels, TV guide and on-demand library. It contains no channels by itself; the subscription provides them.</p>"),
        ("Which IPTV app has the best TV guide?",
         "<p>TiviMate has the best cable-style grid guide on Android TV and Fire TV. On Apple TV, iPlayTV is closest. IPTV Smarters Pro has a simpler list-and-grid guide that works everywhere.</p>"),
        ("Do I need to pay for an IPTV app?",
         "<p>No. Free players such as IPTV Smarters Pro, XCIPTV and the free version of TiviMate work with every IPTVMaple plan. Paid upgrades add features like recording or multiple playlists.</p>"),
        ("Can I watch IPTV without an app?",
         "<p>Almost always you need an app or player. A browser can play only some stream formats, and online players are risky for your login. Install an app from an official source.</p>"),
    ],
    related=["tivimate-premium", "tivimate-devices", "iptv-smarters-pro-download", "watch-iptv-online", "plex-iptv", "jellyfin-iptv", "stremio-iptv"],
)

# =============================================================================================== IPTV BOX
DATA["iptv-box"] = dict(
    add="""
<h2>How to choose an IPTV box in five questions</h2>
<ol>
<li><strong>Which TV and ports?</strong> Any TV with HDMI works. A 4K TV needs an HDMI port that supports HDCP 2.2.</li>
<li><strong>HD or 4K?</strong> If you want 4K sports, choose a 4K device and plan on about 25 Mbps per screen.</li>
<li><strong>Do you want other apps?</strong> Android TV and Fire TV boxes run YouTube and other apps too. A MAG box only plays its IPTV portal.</li>
<li><strong>Wi-Fi or Ethernet?</strong> Choose a box with an Ethernet port if your router can reach the TV. It is the single best fix for buffering.</li>
<li><strong>How technical are you?</strong> Beginners do well with a Firestick or a MAG box; power users prefer Nvidia Shield or Formuler.</li>
</ol>

<h2>Which box for which person</h2>
<table>
<thead><tr><th>You are…</th><th>Choose</th><th>Why</th></tr></thead>
<tbody>
<tr><td>On a budget with one TV</td><td><a href="/iptv-firestick/">Fire TV Stick 4K</a> or a similar Google TV device</td><td>Low price, large app store, easy setup</td></tr>
<tr><td>A sports fan with a 4K TV</td><td>Fire TV Stick 4K Max, Nvidia Shield or Formuler Z11</td><td>Enough power for 4K feeds and long channel lists</td></tr>
<tr><td>Not technical and want plug-and-play</td><td><a href="/mag-box-iptv/">MAG box</a></td><td>No app store to manage</td></tr>
<tr><td>Living in the Apple world</td><td>Apple TV 4K</td><td>See <a href="/iptv-apple-tv/">IPTV on Apple TV</a></td></tr>
<tr><td>Someone who already owns a smart TV</td><td>The TV’s own IPTV app, or a stick for TiviMate</td><td>See <a href="/tivimate-devices/">where TiviMate runs</a></td></tr>
</tbody>
</table>

<h2>What “IPTV with box” really means</h2>
<p>People who search for “IPTV with box” are usually looking for a ready-to-use bundle. Be careful: a box that comes pre-loaded with “free channels for life” is typically an uncertified device with outdated software. IPTVMaple sells subscriptions, not boxes, so you can buy a mainstream device from any retailer and add a subscription you can test first with the <a href="/try-iptv-canada/">free 24-hour trial</a>. Compare costs on the <a href="/iptv-price/">IPTV price</a> page.</p>

<h2>Set up any IPTV box in five steps</h2>
<ol>
<li>Connect the box to the TV with HDMI and to your router with Ethernet if possible.</li>
<li>Power it on and sign in to its app store (Google Play or Amazon Appstore), or open its built-in portal for MAG boxes.</li>
<li>Install a player: <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</li>
<li>Enter the login from your provider (Xtream Codes) or, for MAG and Formuler portals, the portal address.</li>
<li>Pick the channel groups you watch and hide the rest so the guide loads quickly.</li>
</ol>
<p>If anything stutters, follow the <a href="/iptv-buffering-fix/">buffering fixes</a>.</p>
""",
    faq=[
        ("Is a MAG box better than an Android box?",
         "<p>A MAG box is simpler: it only plays IPTV through its portal, with no app store to manage. An Android TV box is more flexible and runs apps like TiviMate, YouTube and others. Choose by how technical you are.</p>"),
        ("Do I need an Ethernet cable for an IPTV box?",
         "<p>It is not required, but it is the best way to prevent buffering, especially during live sports. If your router is far from the TV, use 5 GHz Wi-Fi or a powerline adapter.</p>"),
        ("What does “IPTV with box” mean?",
         "<p>It means a subscription sold together with a device. IPTVMaple sells subscriptions only; you can buy any mainstream box or stick from a retailer and add your login.</p>"),
    ],
    related=["iptv-price", "tivimate-devices", "iptv-buffering-fix"],
)

# =============================================================================================== M3U
DATA["m3u-playlist"] = dict(
    add="""
<h2>The parts of an M3U entry explained</h2>
<table>
<thead><tr><th>Part</th><th>What it does</th></tr></thead>
<tbody>
<tr><td><code>#EXTM3U</code></td><td>Marks the file as an extended M3U playlist</td></tr>
<tr><td><code>#EXTINF:-1</code></td><td>Starts a channel entry (-1 means a live stream with no fixed length)</td></tr>
<tr><td><code>tvg-id</code></td><td>Matches the channel to a row in the TV guide (EPG)</td></tr>
<tr><td><code>tvg-name</code></td><td>The channel name used for guide matching</td></tr>
<tr><td><code>tvg-logo</code></td><td>Address of the channel logo</td></tr>
<tr><td><code>group-title</code></td><td>The category the channel is listed under</td></tr>
<tr><td>Last line</td><td>The stream address your player opens</td></tr>
</tbody>
</table>

<h2>Common M3U problems and fixes</h2>
<table>
<thead><tr><th>Problem</th><th>Cause</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>No channels appear</td><td>Wrong link, expired subscription, or the player cannot reach the server</td><td>Recopy the link; check the plan is active; try Xtream Codes instead</td></tr>
<tr><td>Channels load but there is no guide</td><td>No EPG link set</td><td>Add the XMLTV link in the player’s EPG settings</td></tr>
<tr><td>Guide is an hour off</td><td>Time zone mismatch</td><td>Set the EPG time shift for your province</td></tr>
<tr><td>Link won’t open in a browser</td><td>Browsers can’t play M3U lists directly</td><td>Open it in VLC or an IPTV app. See <a href="/watch-iptv-online/">watch IPTV online</a></td></tr>
<tr><td>Very slow to load</td><td>Huge playlist with every channel and movie</td><td>Hide groups you don’t watch, or use Xtream Codes</td></tr>
</tbody>
</table>

<h2>Keep your M3U link private</h2>
<p>An M3U link from a paid service includes your username and password inside the address. Anyone who sees it can use your subscription and the provider may lock it. Don’t post it in forums or paste it into online “M3U checkers”, and ask your provider to change the password if it leaks.</p>

<h2>M3U or Xtream Codes: which should I use?</h2>
<p>Use <a href="/xtream-codes-iptv/">Xtream Codes</a> when your app supports it: three short fields instead of one long link, with the guide and on-demand sections organized for you. Use M3U for VLC, Kodi, smart TV apps and anything that has no Xtream option. Prefer French? <a href="/liste-iptv-m3u/">Liste IPTV M3U</a>.</p>
""",
    faq=[
        ("Why does my M3U link show no channels?",
         "<p>The usual causes are a mistyped link, an expired subscription, or a player that cannot reach the server. Recopy the link, check that your plan is active and try an Xtream Codes login instead.</p>"),
        ("How do I add a TV guide to an M3U playlist?",
         "<p>Add the XMLTV (EPG) link in the player’s guide settings. Your provider supplies it; the tvg-id values in the playlist are used to match the guide to each channel.</p>"),
        ("Why won’t my M3U link play in Chrome?",
         "<p>Browsers can’t open M3U lists or raw IPTV streams directly. Use VLC or an IPTV app, or read our guide on watching IPTV online.</p>"),
    ],
    related=["watch-iptv-online", "iptv-buffering-fix", "is-iptv-legal-in-canada"],
)

# =============================================================================================== XTREAM CODES
DATA["xtream-codes-iptv"] = dict(
    add="""
<h2>The three details in an Xtream Codes login</h2>
<table>
<thead><tr><th>Field</th><th>Example</th><th>Tip</th></tr></thead>
<tbody>
<tr><td>Server URL</td><td><code>http://line.example.com:8080</code></td><td>Keep the http:// and the port exactly as sent</td></tr>
<tr><td>Username</td><td>a short code or name</td><td>Case-sensitive</td></tr>
<tr><td>Password</td><td>letters and numbers</td><td>Copy and paste to avoid typos</td></tr>
</tbody>
</table>

<h2>Xtream Codes, M3U or portal?</h2>
<table>
<thead><tr><th></th><th>Xtream Codes</th><th>M3U link</th><th>Portal (MAC)</th></tr></thead>
<tbody>
<tr><td>Used by</td><td>TiviMate, IPTV Smarters, XCIPTV</td><td>VLC, Kodi, smart TV apps</td><td>MAG, Formuler, STBEmu</td></tr>
<tr><td>Guide</td><td>Automatic</td><td>Needs an EPG link</td><td>Built in</td></tr>
<tr><td>On-demand sections</td><td>Organized</td><td>Mixed in the list</td><td>Organized</td></tr>
<tr><td>What you enter</td><td>Three fields</td><td>One long link</td><td>MAC address, then a portal URL</td></tr>
</tbody>
</table>

<h2>Fixing an Xtream Codes login that won’t work</h2>
<ol>
<li>Copy the server URL, username and password again from the message we sent. Look for spaces.</li>
<li>Make sure the URL starts with <code>http://</code> or <code>https://</code> and includes the port if one was given.</li>
<li>Check your subscription hasn’t expired and that no more screens than your plan allows are playing.</li>
<li>Try the M3U link in the same app. If that works, the problem is the Xtream fields.</li>
<li>Restart the app and your router. Still stuck? Message support with a screenshot.</li>
</ol>
<p>See <a href="/iptv-server/">what an IPTV server is</a> for more on URLs and ports, and <a href="/m3u-playlist/">M3U playlists</a> for the link format.</p>
""",
    faq=[
        ("Where do I find my Xtream Codes details?",
         "<p>Your provider sends them when you subscribe or start a trial. With IPTVMaple they arrive by email and WhatsApp: a server URL, username and password.</p>"),
        ("Can I use Xtream Codes on a smart TV?",
         "<p>Some TV apps (such as Smarters Player Lite and SmartOne) accept Xtream Codes; others use an M3U link uploaded by MAC address. See the Samsung and LG guides.</p>"),
    ],
    related=["iptv-smarters-pro-samsung-lg", "tivimate-firestick"],
)

# =============================================================================================== IPTV SERVER
DATA["iptv-server"] = dict(
    add="""
<h2>“IPTV server not working”: a checklist</h2>
<table>
<thead><tr><th>Check</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Is your internet working?</td><td>Open any website or video on the same network</td></tr>
<tr><td>Is the server URL correct?</td><td>Recopy it, including http:// and the port</td></tr>
<tr><td>Is the subscription active?</td><td>Check the expiry date in your message or with support</td></tr>
<tr><td>Are too many screens playing?</td><td>Stop extra streams; plans cover 1 to 5 screens</td></tr>
<tr><td>Is only one channel failing?</td><td>That is the channel’s source, not the server. Tell support the channel name and time</td></tr>
<tr><td>Does it fail only in the evening?</td><td>Likely your provider’s network. See the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>

<h2>What is an “IPTV line”?</h2>
<p>An IPTV “line” is one subscription login on the server: a username and password tied to your plan and its number of screens. Providers talk about lines when they count subscriptions. For a customer it simply means your personal login, so keep it private. The formats are explained in <a href="/xtream-codes-iptv/">Xtream Codes</a> and <a href="/m3u-playlist/">M3U</a>.</p>
""",
    faq=[
        ("What is an IPTV line?",
         "<p>A line is one subscription login: a username and password tied to your plan and its number of simultaneous screens.</p>"),
    ],
)

# =============================================================================================== 4K
DATA["4k-iptv"] = dict(
    add="""
<h2>How much bandwidth do several 4K screens need?</h2>
<table>
<thead><tr><th>4K screens at once</th><th>Download speed to plan for</th></tr></thead>
<tbody>
<tr><td>1</td><td>25 Mbps</td></tr>
<tr><td>2</td><td>50 Mbps</td></tr>
<tr><td>3</td><td>75 Mbps</td></tr>
</tbody>
</table>
<p>Add a margin for other devices on your network. If your connection can’t sustain 4K on every screen, use HD on the extra TVs.</p>

<h2>How to be sure you’re watching 4K</h2>
<ol>
<li>Pick a channel marked 4K in the guide, and a programme that is produced in 4K.</li>
<li>Check that your device’s output is set to 4K in its display settings, and that the HDMI port supports 4K.</li>
<li>Look at your TV’s info overlay or the player’s stream info, which shows the resolution.</li>
</ol>
<p>Many live broadcasts are still produced in HD, so a 4K channel can show HD content. That is the broadcaster’s choice, not a fault of your setup.</p>

<h2>Best settings for 4K sports</h2>
<ul>
<li>Use Ethernet. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li>Turn on auto frame rate in <a href="/tivimate/">TiviMate</a>, or “Match frame rate” on Apple TV.</li>
<li>Switch off your TV’s motion smoothing for live sports if you see artifacts.</li>
</ul>
<p>Choosing a device? Read the <a href="/iptv-box/">IPTV box guide</a>.</p>
""",
    faq=[
        ("How many Mbps do I need for 4K IPTV on two TVs?",
         "<p>Plan on about 50 Mbps: 25 Mbps for each 4K stream, plus a margin for other devices on your network.</p>"),
    ],
)

# =============================================================================================== TIVIMATE (pillar) & SMARTERS (pillar)
DATA["tivimate"] = dict(
    meta=dict(keywords=["tivimate", "tivi mate", "tivimate iptv", "tivimate iptv player", "tivimate player"]),
    add="""
<h2>More TiviMate guides</h2>
<ul>
<li><a href="/tivimate-firestick/">TiviMate on Firestick: step-by-step install</a>: Downloader, developer options and fixes.</li>
<li><a href="/tivimate-premium/">TiviMate Premium: cost, features and activation</a>: what the paid tier adds and how the account works.</li>
<li><a href="/tivimate-devices/">Which devices TiviMate supports</a>: Samsung, LG, Apple TV, Roku, PC and Mac answered honestly.</li>
</ul>

<h2>Is TiviMate safe?</h2>
<p>The real TiviMate app from the developer is safe. The risk comes from copies: “cracked Premium”, “free Premium” and “modded” files from random sites can carry malware. On Android TV and Google TV, install from Google Play. On Fire TV, use the official address from tivimate.com in Downloader.</p>

<h2>If TiviMate isn’t available on your device</h2>
<p>Use <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> on phones and computers, <a href="/smarters-player-lite/">Smarters Player Lite</a> or <a href="/iplaytv/">iPlayTV</a> on Apple devices, and a smart TV app on Samsung or LG. The <a href="/iptv-apps/">IPTV apps guide</a> compares them all.</p>
""",
    faq=[
        ("Is TiviMate safe to install?",
         "<p>The official app from the developer is safe. Avoid cracked or modded copies from other websites, which can contain malware. Use Google Play on Android TV and the official address in Downloader on Fire TV.</p>"),
    ],
    related=["tivimate-firestick", "tivimate-premium", "tivimate-devices"],
)

DATA["iptv-smarters-pro"] = dict(
    meta=dict(keywords=["ip tv smarters pro", "iptv smarters", "smarters pro", "smarterspro", "iptv smarter", "iptv smarters pro", "ip tv smarters", "iptv smarter pro",
                        "iptv smart pro", "smarters iptv pro", "tv smarters pro", "iptv smarters player", "iptvsmarterspro", "smart pro iptv", "smarters player",
                        "ip tv smarter pro", "ip tv smart pro", "ip tv smart", "iptv smarters lite"]),
    add="""
<h2>Smarters Pro guides by device</h2>
<ul>
<li><a href="/iptv-smarters-pro-firestick/">Firestick and Fire TV</a></li>
<li><a href="/iptv-smarters-pro-samsung-lg/">Samsung and LG smart TVs</a></li>
<li><a href="/iptv-smarters-pro-pc-mac/">Windows and Mac</a></li>
<li><a href="/iptv-smarters-pro-download/">Where to download it safely</a> (Android, APK, Google Play)</li>
<li><a href="/smarters-player-lite/">iPhone, iPad and Apple TV</a> (Smarters Player Lite)</li>
<li><a href="/iptv-smarters-pro-francais/">En français</a></li>
</ul>

<h2>Smarters, smarter, smasters: all the same app</h2>
<p>People search for this app under many spellings: IPTV Smarters, IPTV Smarter Pro, Smarters Pro and even “Smasters”. They all mean the same player. The official name is <strong>IPTV Smarters Pro</strong>, and on Apple devices <strong>Smarters Player Lite</strong>. If a site offers something with a different name and promises free channels, it is not this app.</p>
""",
    faq=[
        ("Is “IPTV Smasters Pro” the same as IPTV Smarters Pro?",
         "<p>Yes. “Smasters” is a common misspelling. The app is called IPTV Smarters Pro, and on iPhone and Apple TV it is Smarters Player Lite.</p>"),
    ],
    related=["iptv-smarters-pro-firestick", "iptv-smarters-pro-samsung-lg", "iptv-smarters-pro-pc-mac", "iptv-smarters-pro-download"],
)

DATA["best-iptv-canada"] = dict(
    add="""
<h2>Keep researching</h2>
<p>If you are still comparing options, these guides go deeper: the <a href="/iptv-providers/">IPTV provider scorecard</a>, <a href="/iptv-price/">IPTV prices in Canada</a>, <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> and how to use <a href="/iptv-reddit/">Reddit advice</a> without being misled. When you’re ready, <a href="/try-iptv-canada/">test IPTVMaple free for 24 hours</a>.</p>
""",
    related=["iptv-providers", "iptv-price", "is-iptv-legal-in-canada", "iptv-reddit"],
)

# =============================================================================================== SMALL APP PAGES
DATA["stbemu"] = dict(
    add="""
<h2>STBEmu vs STBEmu Pro</h2>
<table>
<thead><tr><th></th><th>STBEmu</th><th>STBEmu Pro</th></tr></thead>
<tbody>
<tr><td>Cost</td><td>Free</td><td>Paid, one time</td></tr>
<tr><td>Interface</td><td>MAG-style portal</td><td>MAG-style portal with extra options</td></tr>
<tr><td>Best for</td><td>Trying the portal</td><td>Daily use on an Android box</td></tr>
</tbody>
</table>
<p>Prices and features are set by the developer, so check the Google Play listing. The portal setup in the steps above is the same for both.</p>

<h2>Which STB model should I choose?</h2>
<p>STBEmu imitates a MAG set-top box. For most portals, <strong>MAG 250</strong> or <strong>MAG 254</strong> works. If channels load but video fails, try another model in <em>STB configuration</em>, restart the app and test again. Settings such as the video player (hardware or software decoder) and resolution are in the same menu.</p>

<h2>STBEmu troubleshooting</h2>
<table>
<thead><tr><th>Symptom</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Black screen after choosing a channel</td><td>Switch between the hardware and software video player</td></tr>
<tr><td>Portal loads but channels are empty</td><td>The MAC activated with us must match the app’s MAC exactly</td></tr>
<tr><td>App asks for the MAC again after a reinstall</td><td>A reinstall can change it. Send us the new one, or restore the old MAC in settings</td></tr>
</tbody>
</table>
<p>Prefer an app with a modern guide? See <a href="/tivimate-firestick/">TiviMate on Firestick</a> or the full <a href="/iptv-apps/">IPTV apps comparison</a>.</p>
""",
    faq=[
        ("Why do I get a black screen in STBEmu?",
         "<p>Switch between the hardware and software video player in STBEmu’s settings, and try another STB model such as MAG 250 or MAG 254. Restart the app after each change.</p>"),
    ],
)

DATA["mytvonline"] = dict(
    add="""
<h2>MyTVOnline troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>“Portal not reachable” or loading forever</td><td>Re-enter the portal URL exactly as sent; check the Formuler is online</td></tr>
<tr><td>“Not authorized”</td><td>The MAC we activated must match the box. Send us the MAC shown on screen again</td></tr>
<tr><td>No guide data</td><td>Refresh the guide; check the time zone in the box’s settings</td></tr>
<tr><td>Channels freeze</td><td>Use Ethernet and see the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>

<h2>MyTVOnline or TiviMate on a Formuler?</h2>
<p>MyTVOnline is built for Formuler remotes and is the simplest way to start. TiviMate has a more polished guide and the Premium features such as catch-up and recording. You can install both and use the same login. The model-by-model comparison is in the <a href="/formuler-iptv/">Formuler guide</a>; compare other options in the <a href="/iptv-box/">IPTV box guide</a>.</p>
""",
    faq=[
        ("Why does MyTVOnline say “not authorized”?",
         "<p>The MAC address we activated must match the one on your box exactly. Send us the MAC address shown on the first screen and we will fix it.</p>"),
    ],
)

DATA["xciptv"] = dict(
    add="""
<h2>XCIPTV, TiviMate or IPTV Smarters?</h2>
<table>
<thead><tr><th></th><th>XCIPTV</th><th><a href="/tivimate/">TiviMate</a></th><th><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></th></tr></thead>
<tbody>
<tr><td>Strength</td><td>Light and fast</td><td>Best guide</td><td>Runs everywhere</td></tr>
<tr><td>Older Firestick</td><td>Good choice</td><td>Fine if you trim groups</td><td>Fine</td></tr>
<tr><td>Player engines</td><td>ExoPlayer and VLC</td><td>Built-in</td><td>Built-in plus external</td></tr>
<tr><td>Price</td><td>Free</td><td>Free; Premium optional</td><td>Free</td></tr>
</tbody>
</table>
<p>XCIPTV may also offer paid upgrades in some versions; check the app for what is current. Install it on a stick with our <a href="/tivimate-firestick/">Downloader steps</a>, which work the same way for any APK from a developer’s official website.</p>
""",
)

DATA["implayer"] = dict(
    add="""
<h2>IMPlayer or TiviMate?</h2>
<table>
<thead><tr><th></th><th>IMPlayer</th><th><a href="/tivimate/">TiviMate</a></th></tr></thead>
<tbody>
<tr><td>Devices</td><td>Android TV, Fire TV, Apple</td><td>Android TV, Fire TV only</td></tr>
<tr><td>Sync across devices</td><td>Yes, with an IMPlayer account</td><td>Premium account across Android devices</td></tr>
<tr><td>Guide</td><td>Grid</td><td>Excellent grid</td></tr>
<tr><td>Best for</td><td>Mixed Android and Apple households</td><td>Android TV and Firestick homes</td></tr>
</tbody>
</table>
<p>If your household uses Apple TV in one room and a Firestick in another, IMPlayer lets you keep the same playlist and favourites. Otherwise <a href="/tivimate/">TiviMate</a> is usually the better live-TV choice. See <a href="/iptv-apps/">all IPTV apps</a>.</p>
""",
)

DATA["smart-iptv"] = dict(
    add="""
<h2>Smart IPTV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Playlist doesn’t load after upload</td><td>Restart the app; confirm the MAC you entered matches the one on screen exactly</td></tr>
<tr><td>Channels show but no movies and series</td><td>The app focuses on live channels; use SmartOne or Flix IPTV for on-demand sections</td></tr>
<tr><td>“Trial expired”</td><td>Activate the app on the developer’s website; the fee goes to the developer</td></tr>
<tr><td>App isn’t in the TV store</td><td>Availability depends on TV year and region. See <a href="/iptv-samsung-tv/">Samsung</a> and <a href="/iptv-lg-tv/">LG</a> alternatives</td></tr>
</tbody>
</table>
<p>Always upload your playlist on the app’s official website only, and keep your M3U link private. Compare the three smart TV apps in <a href="/flix-iptv/">Flix IPTV</a> and <a href="/smartone-iptv/">SmartOne IPTV</a>.</p>
""",
)

DATA["smartone-iptv"] = dict(
    add="""
<h2>SmartOne IPTV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Playlist not found</td><td>Re-enter the MAC address on the official SmartOne website exactly as shown on the TV</td></tr>
<tr><td>Empty guide</td><td>Upload the playlist again with the EPG link included</td></tr>
<tr><td>Slow channel changes</td><td>Trim the playlist to the groups you watch, or add a stick (<a href="/tivimate-firestick/">TiviMate on Firestick</a>)</td></tr>
<tr><td>App missing on your TV</td><td>Try Flix IPTV or Smart IPTV, or see the <a href="/iptv-smarters-pro-samsung-lg/">Smarters guide for Samsung and LG</a></td></tr>
</tbody>
</table>
""",
)

DATA["flix-iptv"] = dict(
    add="""
<h2>Flix IPTV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Playlist upload fails</td><td>Check both the MAC address and device key; use the official Flix IPTV website only</td></tr>
<tr><td>Trial ended</td><td>Flix IPTV activation is handled by the developer on their site</td></tr>
<tr><td>No guide data</td><td>Add the EPG link when you upload the playlist</td></tr>
<tr><td>Stutters on Wi-Fi</td><td>Use an Ethernet cable to the TV. See the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>
<p>Not sure which app to pick? The comparison table in the <a href="/iptv-apps/">IPTV apps guide</a> lists price, devices and login type for each.</p>
""",
)

DATA["iplaytv"] = dict(
    add="""
<h2>iPlayTV, Smarters Player Lite or IMPlayer on Apple TV?</h2>
<table>
<thead><tr><th></th><th>iPlayTV</th><th><a href="/smarters-player-lite/">Smarters Player Lite</a></th><th><a href="/implayer/">IMPlayer</a></th></tr></thead>
<tbody>
<tr><td>Price</td><td>Paid</td><td>Free</td><td>Free; Premium optional</td></tr>
<tr><td>Guide</td><td>Cable-style grid</td><td>Good</td><td>Grid</td></tr>
<tr><td>Logins</td><td>M3U, Xtream</td><td>Xtream, M3U</td><td>Xtream, M3U</td></tr>
<tr><td>Best for</td><td>The nicest Apple TV experience</td><td>Starting free</td><td>Sharing with Android devices</td></tr>
</tbody>
</table>
<p>Prices and features are set by each developer. Setup for all of them is described in <a href="/iptv-apple-tv/">IPTV on Apple TV</a>. Vous préférez le français? <a href="/iptv-sur-apple-tv-iphone/">IPTV sur Apple TV et iPhone</a>.</p>
""",
)

DATA["kodi-iptv"] = dict(
    add="""
<h2>Installing Kodi</h2>
<ul>
<li><strong>Windows and Mac:</strong> download from <a href="https://kodi.tv/" rel="noopener">kodi.tv</a>.</li>
<li><strong>Android and Android TV:</strong> Google Play.</li>
<li><strong>Fire TV:</strong> use the official Kodi APK from kodi.tv with Downloader (see the <a href="/tivimate-firestick/">Downloader steps</a>).</li>
</ul>

<h2>Common Kodi IPTV problems</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>“No channels” after enabling the add-on</td><td>Re-enter the M3U URL, choose <em>Remote path</em>, restart Kodi</td></tr>
<tr><td>Channels but no guide</td><td>Add the XMLTV URL on the EPG tab and wait for the first update</td></tr>
<tr><td>Guide is off by hours</td><td>Set the EPG time shift in the add-on settings</td></tr>
<tr><td>Playback stutters</td><td>Enable hardware decoding in Kodi’s player settings; see the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>
<p>Want the same idea on a server? <a href="/jellyfin-iptv/">Jellyfin</a> has a built-in M3U tuner. For a simpler TV experience use <a href="/tivimate/">TiviMate</a>.</p>
""",
    related=["stremio-iptv"],
)

DATA["vlc-iptv"] = dict(
    add="""
<h2>VLC tips for IPTV</h2>
<ul>
<li><strong>Save the playlist.</strong> After opening the network stream, use <em>Media → Save Playlist to File</em> so you don’t have to paste the link each time.</li>
<li><strong>Turn on hardware decoding</strong> in <em>Tools → Preferences → Input / Codecs</em> if video stutters.</li>
<li><strong>Deinterlace</strong> for sports channels that look combed: <em>Video → Deinterlace</em>.</li>
<li><strong>Trim the list.</strong> Huge playlists are slow in VLC; ask your provider for a smaller list or use an app with groups.</li>
</ul>

<h2>When to use something other than VLC</h2>
<table>
<thead><tr><th>You want…</th><th>Use</th></tr></thead>
<tbody>
<tr><td>A TV guide and favourites</td><td><a href="/iptv-smarters-pro-pc-mac/">IPTV Smarters Pro for PC and Mac</a></td></tr>
<tr><td>A full media centre</td><td><a href="/kodi-iptv/">Kodi</a></td></tr>
<tr><td>A living-room experience</td><td>A Firestick with <a href="/tivimate/">TiviMate</a></td></tr>
</tbody>
</table>
<p>En français: <a href="/iptv-sur-pc-mac/">IPTV sur PC et Mac</a>.</p>
""",
)

DATA["smarters-player-lite"] = dict(
    add="""
<h2>Smarters Player Lite on other devices</h2>
<p>Smarters Player Lite is the version used on Apple devices, and it can also appear in the app stores of Samsung and LG TVs. For those TVs, see <a href="/iptv-smarters-pro-samsung-lg/">IPTV Smarters on Samsung and LG</a>. On a Fire TV Stick or Android TV, use <a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro</a> or <a href="/tivimate/">TiviMate</a>.</p>

<h2>Apple TV remote tips</h2>
<ul>
<li>Type your login faster by using the iPhone as a keyboard (Control Center, Apple TV Remote).</li>
<li>Swipe on the Siri Remote touch surface to scroll the channel list.</li>
<li>Long-press a channel to add it to favourites.</li>
</ul>
<p>Compare Apple TV apps in the <a href="/iplaytv/">iPlayTV</a> guide and the <a href="/iptv-apple-tv/">Apple TV guide</a>. En français: <a href="/iptv-sur-apple-tv-iphone/">IPTV sur Apple TV et iPhone</a>.</p>
""",
)
