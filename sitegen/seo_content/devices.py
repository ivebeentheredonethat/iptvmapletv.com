"""Devices cluster. Hub: /iptv-devices/"""

PAGES = [
    # ------------------------------------------------------------------ HUB
    dict(
        slug="iptv-devices", hub="devices", hub_page=True,
        title="IPTV Devices: Setup Guides for Every Screen (2026) | IPTVMaple",
        description="IPTV setup guides for Firestick, Android TV boxes, Formuler, MAG, Samsung, LG, Apple TV, Roku, iPhone and PC. Pick your device and start watching today.",
        kicker="Devices", h1='IPTV on <span class="grad-text">every device</span>',
        lead="Firestick, smart TVs, Apple TV, Android boxes, phones and computers — pick your device for a step-by-step setup guide.",
        crumb="IPTV devices", blurb="Setup guides for every screen in your home.",
        answer="<p>IPTVMaple works on almost any screen: <strong>Amazon Firestick</strong>, <strong>Android TV boxes</strong> (Formuler, Nvidia Shield, onn), <strong>MAG boxes</strong>, <strong>Samsung</strong> and <strong>LG</strong> smart TVs, <strong>Apple TV</strong>, <strong>iPhone and Android phones</strong>, and <strong>Windows or Mac</strong> computers. The best overall experience is a Firestick 4K or Android TV box with the TiviMate app.</p>",
        body="""
<h2>Which device is best for IPTV?</h2>
<table>
<thead><tr><th>Device</th><th>Best for</th><th>Recommended app</th></tr></thead>
<tbody>
<tr><td><a href="/iptv-firestick/">Amazon Firestick 4K</a></td><td>Best value, any TV with HDMI</td><td>TiviMate</td></tr>
<tr><td><a href="/iptv-box/">Android TV box</a></td><td>Power users, 4K, recording</td><td>TiviMate</td></tr>
<tr><td><a href="/formuler-iptv/">Formuler Z11 Pro Max</a></td><td>Dedicated IPTV box</td><td>MyTVOnline 3</td></tr>
<tr><td><a href="/mag-box-iptv/">MAG box</a></td><td>Plug-and-play simplicity</td><td>Built-in portal</td></tr>
<tr><td><a href="/iptv-samsung-tv/">Samsung</a> / <a href="/iptv-lg-tv/">LG</a> smart TV</td><td>No extra device</td><td>SmartOne, Flix IPTV</td></tr>
<tr><td><a href="/iptv-apple-tv/">Apple TV</a></td><td>Apple households</td><td>iPlayTV, Smarters Lite</td></tr>
<tr><td><a href="/iptv-iphone/">iPhone / iPad</a>, Android phone</td><td>Watching on the go</td><td>Smarters</td></tr>
<tr><td><a href="/iptv-pc-mac/">Windows / Mac</a></td><td>Desk and laptop</td><td>Smarters, VLC</td></tr>
</tbody>
</table>

<h2>What internet speed do you need?</h2>
<ul>
<li><strong>HD</strong> — 10 Mbps per stream</li>
<li><strong>Full HD</strong> — 15 Mbps per stream</li>
<li><strong>4K</strong> — 25 Mbps per stream</li>
</ul>
<p>Any Canadian home internet plan from Bell, Rogers, Telus, Vidéotron or a smaller ISP is usually enough. A wired Ethernet connection is the best way to avoid buffering during live sports.</p>

<h2>How many devices can I use?</h2>
<p>Install IPTVMaple on as many devices as you like. The number that can <strong>play at the same time</strong> depends on your plan — 1, 2, 3, 4 or 5 devices. See all options on the <a href="/iptv-plans-canada/">plans page</a>.</p>
""",
        faq=[
            ("What is the best device for IPTV?", "<p>For most people, an Amazon Fire TV Stick 4K or an Android TV box running TiviMate gives the best mix of price, speed and features.</p>"),
            ("Do I need a box to watch IPTV?", "<p>No. You can use a Samsung or LG smart TV app, a phone, a tablet or a computer. A box or stick just gives a smoother, remote-friendly experience.</p>"),
            ("Can I use IPTV on more than one TV?", "<p>Yes. Choose a plan with 2 to 5 simultaneous devices if several people watch at the same time.</p>"),
            ("Does IPTV work on Roku?", "<p>Roku doesn’t support most IPTV apps. See our <a href=\"/iptv-roku/\">Roku guide</a> for workarounds.</p>"),
        ],
        related=["iptv-apps", "what-is-iptv"],
        keywords=["iptv device", "iptv set top box", "set top box iptv", "iptv receiver", "tv box iptv"],
    ),
    # ------------------------------------------------------------------ FIRESTICK
    dict(
        slug="iptv-firestick", hub="devices",
        title="IPTV on Firestick: Setup Guide for Canada (2026) | IPTVMaple",
        description="How to install IPTV on Amazon Firestick step by step: Downloader, TiviMate or IPTV Smarters, and your login. Works on Fire TV 4K. Try IPTVMaple free for 24h.",
        kicker="Devices", h1='How to set up <span class="grad-text">IPTV on Firestick</span>',
        lead="The Amazon Fire TV Stick is the most popular IPTV device in Canada. Here’s the complete setup — from Downloader to your first channel.",
        crumb="Firestick", blurb="Downloader, TiviMate and login — step by step.",
        answer="<p>To get <strong>IPTV on a Firestick</strong>: install the <strong>Downloader</strong> app, allow it to install unknown apps in <em>Developer options</em>, use it to install an IPTV player such as <strong>TiviMate</strong> or <strong>IPTV Smarters Pro</strong>, then log in with the details from your IPTV provider. The whole process takes about 10 minutes.</p>",
        body="""
<h2>What you need</h2>
<ul>
<li>An Amazon Fire TV Stick (Fire TV Stick 4K or 4K Max recommended) or Fire TV Cube</li>
<li>Internet of at least 25 Mbps for 4K</li>
<li>An IPTV subscription — try IPTVMaple <a href="/try-iptv-canada/">free for 24 hours</a></li>
</ul>
<p><strong>Note:</strong> some of Amazon’s newest Fire TV models run a new operating system (Vega OS) that doesn’t allow installing apps from outside the Appstore. If Developer options are missing on your device, check the model or use an Android TV device instead.</p>

<h2>Step 1 — Enable Developer options</h2>
<ol>
<li>Go to <em>Settings → My Fire TV → About</em>.</li>
<li>Click on your device name <strong>7 times</strong> until you see “You are now a developer”.</li>
<li>Go back to <em>My Fire TV → Developer options</em>.</li>
</ol>

<h2>Step 2 — Install Downloader</h2>
<ol>
<li>From the home screen, search for <strong>Downloader</strong> (orange icon) and install it.</li>
<li>In <em>Developer options → Install unknown apps</em>, turn <strong>Downloader</strong> ON.</li>
</ol>

<h2>Step 3 — Install your IPTV player</h2>
<p>Open Downloader and enter the official download address of the player you want:</p>
<ul>
<li><a href="/tivimate/">TiviMate</a> — the best Firestick IPTV player, with a cable-style guide.</li>
<li><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> — simple and familiar.</li>
<li><a href="/xciptv/">XCIPTV</a> — lightest option for older Firesticks.</li>
</ul>
<p>Some players (like IMPlayer) are also in the Amazon Appstore — no Downloader needed.</p>

<h2>Step 4 — Log in and watch</h2>
<p>Open the app, choose Xtream Codes, and enter the server URL, username and password from IPTVMaple. Channels, movies, series and the guide load in about a minute.</p>

<h2>Firestick IPTV tips</h2>
<ul>
<li><strong>Buffering?</strong> Use Amazon’s Ethernet adapter or 5 GHz Wi-Fi.</li>
<li><strong>Running slow?</strong> Clear cache in <em>Settings → Applications → Manage installed apps</em>.</li>
<li><strong>Remote shortcut:</strong> hold Home → Apps to pin your IPTV app to the front row.</li>
</ul>
<h2>Which Fire TV device is best for IPTV?</h2>
<table>
<thead><tr><th>Model</th><th>Resolution</th><th>Good for IPTV?</th></tr></thead>
<tbody>
<tr><td>Fire TV Stick HD</td><td>1080p</td><td>OK for HD TVs and bedrooms</td></tr>
<tr><td>Fire TV Stick 4K</td><td>4K HDR</td><td>Great value for most homes</td></tr>
<tr><td>Fire TV Stick 4K Max</td><td>4K HDR, Wi-Fi 6E, more memory</td><td>Best stick for 4K sports and big channel lists</td></tr>
<tr><td>Fire TV Cube</td><td>4K HDR, Ethernet port, fastest</td><td>Best overall — wired connection built in</td></tr>
</tbody>
</table>
<p>Check Developer options on any new model before relying on sideloaded apps (see the note above about newer Fire TV models).</p>

<h2>Optimise your Firestick for IPTV</h2>
<ol>
<li><strong>Use Ethernet or 5 GHz Wi-Fi</strong> — Amazon’s Ethernet adapter is the single biggest fix for buffering.</li>
<li><strong>Turn off data collection</strong> — <em>Settings → Preferences → Privacy settings</em>: disable device usage data and app usage data.</li>
<li><strong>Match frame rate</strong> — <em>Settings → Display &amp; Sounds → Display → Match original frame rate</em> for smoother sports.</li>
<li><strong>Free up storage</strong> — uninstall apps you don’t use; keep at least 1 GB free.</li>
<li><strong>Clear the IPTV app cache</strong> once a month under <em>Manage installed applications</em>.</li>
<li><strong>Restart weekly</strong> — hold Select + Play for 5 seconds.</li>
</ol>

<h2>Firestick IPTV troubleshooting</h2>
<ul>
<li><strong>Black screen on some channels</strong> — switch the player engine in the app (ExoPlayer / VLC), or try the HD version of the channel.</li>
<li><strong>App closes by itself</strong> — low memory; clear cache and uninstall unused apps.</li>
<li><strong>“App not installed” in Downloader</strong> — delete the old APK and reinstall, or free up storage.</li>
<li><strong>Remote not working in the app</strong> — update the app; some players need “Use remote for navigation” enabled.</li>
</ul>

<h2>Firestick + IPTV vs cable box</h2>
<p>A Fire TV Stick 4K costs less than two months of a typical cable box rental, has no contract and moves with you between TVs, cottages and hotel rooms. Pair it with an <a href="/iptv-plans-canada/">IPTVMaple plan</a> and you get 50,000+ channels including the full Canadian lineup — for less than most basic cable packages.</p>
""",
        faq=[
            ("Is IPTV on Firestick easy to set up?", "<p>Yes. After enabling Developer options and installing Downloader, installing an IPTV app and logging in takes about 10 minutes. Our team can guide you on WhatsApp.</p>"),
            ("What is the best IPTV app for Firestick?", "<p>TiviMate is the favourite for its TV guide and catch-up. IPTV Smarters Pro is a good free alternative.</p>"),
            ("Which Firestick is best for IPTV?", "<p>The Fire TV Stick 4K Max has the most memory and Wi-Fi 6E, which helps with 4K sports. The standard 4K model is also excellent.</p>"),
            ("Why can’t I find Developer options on my Firestick?", "<p>Go to Settings → My Fire TV → About and click the device name 7 times. On some newer models running Vega OS, sideloading isn’t available.</p>"),
            ("Can I use one IPTV subscription on two Firesticks?", "<p>Yes, with a plan that includes 2 or more simultaneous devices.</p>"),
            ('Why does IPTV buffer on my Firestick?', '<p>Usually Wi-Fi. Use Amazon’s Ethernet adapter or 5 GHz Wi-Fi, clear the app cache, and turn on “Match original frame rate”. If only one channel buffers, try its backup version.</p>'),
            ('Is the Fire TV Cube better than the Firestick for IPTV?', '<p>Yes, it’s faster and has an Ethernet port built in, which makes it the best Fire TV device for 4K sports.</p>'),
            ('Can I take my Firestick IPTV on holiday?', '<p>Yes. Plug the Firestick into any TV with HDMI and connect it to Wi-Fi — your IPTVMaple login works anywhere with internet.</p>'),
        ],
        related=["tivimate", "iptv-smarters-pro", "iptv-box", "iptv-android-tv"],
        keywords=["iptv firestick", "iptv fire stick", "fire stick iptv", "iptv for firestick", "best iptv for firestick", "amazon fire stick iptv", "amazon fire tv stick iptv", "fire tv iptv", "fire tv stick iptv", "iptv amazon", "ip tv amazon", "iptv amazon stick", "iptv stick", "iptv sur fire stick", "firestick iptv reddit", "smart iptv firestick"],
    ),
    # ------------------------------------------------------------------ IPTV BOX
    dict(
        slug="iptv-box", hub="devices",
        title="Best IPTV Box in Canada (2026): Top Boxes Compared | IPTVMaple",
        description="Which IPTV box to buy in Canada in 2026: Formuler Z11 Pro Max, Nvidia Shield, onn 4K, Fire TV Cube, MAG and BuzzTV compared — with setup tips. Try IPTVMaple.",
        kicker="Devices", h1='Best <span class="grad-text">IPTV box</span> in Canada for 2026',
        lead="Thinking of buying an IPTV box? Here’s how the most popular Android TV boxes compare — and why you don’t need a “loaded” box.",
        crumb="IPTV box", blurb="The best Android TV boxes for IPTV, compared.",
        answer="<p>The best <strong>IPTV box</strong> in 2026 is an Android TV box with at least 2 GB of RAM and 4K HDR output. Top picks: <strong>Formuler Z11 Pro Max</strong> (dedicated IPTV box), <strong>Nvidia Shield TV Pro</strong> (most powerful), <strong>Fire TV Cube</strong> or <strong>Fire TV Stick 4K Max</strong> (best value), and the budget <strong>onn 4K Pro</strong>. Pair it with an IPTV subscription and an app like TiviMate.</p>",
        body="""
<h2>IPTV box comparison</h2>
<table>
<thead><tr><th>Box</th><th>Why buy it</th><th>Best IPTV app</th></tr></thead>
<tbody>
<tr><td><a href="/formuler-iptv/">Formuler Z11 Pro Max</a></td><td>Built for IPTV, great remote, MyTVOnline 3</td><td>MyTVOnline 3, TiviMate</td></tr>
<tr><td>Nvidia Shield TV Pro</td><td>Fastest, AI upscaling, lots of storage</td><td>TiviMate</td></tr>
<tr><td>Amazon Fire TV Cube / Stick 4K Max</td><td>Great value, easy to find in Canada</td><td>TiviMate</td></tr>
<tr><td>onn 4K Pro (Google TV)</td><td>Budget Google TV box</td><td>TiviMate, IMPlayer</td></tr>
<tr><td>BuzzTV XRS 4500 / 4900</td><td>IPTV-focused box with its own player</td><td>BuzzTV app, TiviMate</td></tr>
<tr><td><a href="/mag-box-iptv/">MAG 524 / 424</a></td><td>Simplest plug-and-play</td><td>Built-in portal</td></tr>
</tbody>
</table>

<h2>What to look for in an IPTV box</h2>
<ul>
<li><strong>At least 2 GB RAM</strong> (4 GB is better) — large channel lists need memory.</li>
<li><strong>Ethernet port or Wi-Fi 6</strong> — for stable live sports.</li>
<li><strong>Certified Android TV / Google TV</strong> — access to the Play Store and regular security updates.</li>
<li><strong>4K HDR and Dolby Vision/HDR10</strong> if your TV supports it.</li>
</ul>

<h2>Avoid “fully loaded” IPTV boxes</h2>
<p>Boxes sold pre-loaded with “free channels for life” are usually uncertified Android devices with outdated software, questionable apps and services that stop working after a few weeks. Buy a mainstream box from a regular Canadian retailer, then add a subscription you can trust — with support when you need it.</p>

<h2>IPTV box price in Canada</h2>
<p>Expect roughly $40–$80 for a Fire TV Stick or onn box, $100–$200 for Formuler or BuzzTV, and $250+ for an Nvidia Shield TV Pro, depending on sales. Your IPTVMaple subscription starts at $9/month and works on all of them.</p>
<h2>IPTV box vs Firestick vs smart TV app</h2>
<table>
<thead><tr><th></th><th>Android TV box</th><th>Firestick</th><th>Smart TV app</th></tr></thead>
<tbody>
<tr><td>Speed with big channel lists</td><td>Fastest</td><td>Good (4K Max best)</td><td>Varies by TV age</td></tr>
<tr><td>Ethernet port</td><td>Usually built in</td><td>Adapter needed</td><td>Built into most TVs</td></tr>
<tr><td>App choice</td><td>Widest (TiviMate, Smarters, IMPlayer…)</td><td>Wide</td><td>Limited (SmartOne, Flix, IBO…)</td></tr>
<tr><td>Recording</td><td>Yes, with USB storage</td><td>Limited storage</td><td>Rarely</td></tr>
<tr><td>Cost</td><td>$60–$250</td><td>$40–$80</td><td>Free (TV you own)</td></tr>
</tbody>
</table>

<h2>Which box for which home?</h2>
<ul>
<li><strong>Sports fan with a big 4K TV</strong> — Nvidia Shield TV Pro or Formuler Z11 Pro Max, wired, with TiviMate.</li>
<li><strong>Budget or second TV</strong> — onn 4K Pro or Fire TV Stick 4K.</li>
<li><strong>Less technical users / grandparents</strong> — <a href="/mag-box-iptv/">MAG box</a> or Formuler: one app, simple remote, nothing to update.</li>
<li><strong>Want to record</strong> — Nvidia Shield or Formuler with a USB drive and TiviMate Premium.</li>
<li><strong>Apple household</strong> — <a href="/iptv-apple-tv/">Apple TV 4K</a> with iPlayTV.</li>
</ul>

<h2>IPTV box setup checklist</h2>
<ol>
<li>Connect by Ethernet if the router is nearby.</li>
<li>Run all system updates before installing apps.</li>
<li>Install your IPTV app (TiviMate recommended) from Google Play.</li>
<li>Add your IPTVMaple login (Xtream Codes).</li>
<li>Set display output to your TV’s resolution (4K 60 Hz) and turn on frame-rate matching.</li>
<li>Hide unused channel groups and build a favourites list.</li>
</ol>

<h2>Should you buy a box from an IPTV seller?</h2>
<p>You don’t need to. Buying a mainstream box from a regular retailer gets you a warranty, security updates and a return policy, and you’re free to change IPTV provider any time. IPTVMaple works on the box you choose — and our team helps you set it up on WhatsApp.</p>
""",
        faq=[
            ("Do I need a special box for IPTV?", "<p>No. Any Android TV box, Firestick, smart TV or phone works. A dedicated box just makes it smoother and easier with a remote.</p>"),
            ("What is the best Android box for IPTV?", "<p>The Nvidia Shield TV Pro is the most powerful; the Formuler Z11 Pro Max is purpose-built for IPTV; the Fire TV Stick 4K Max is the best value.</p>"),
            ("Is an IPTV box a one-time purchase?", "<p>The box is a one-time purchase. The channels come from an IPTV subscription, which you renew monthly or yearly.</p>"),
            ("Can I buy an IPTV box near me?", "<p>Yes — Fire TV, onn and Nvidia Shield boxes are sold at major Canadian retailers and online. Formuler and MAG boxes are sold by specialist resellers.</p>"),
            ("Does IPTVMaple sell boxes?", "<p>No, we provide the subscription. You can use any box you already own or buy one from a retailer.</p>"),
            ('How much RAM does an IPTV box need?', '<p>At least 2 GB; 3–4 GB is better for large channel lists, fast guide scrolling and 4K playback.</p>'),
            ('Can I record TV on an IPTV box?', '<p>Yes — on Android TV boxes like the Nvidia Shield or Formuler, TiviMate Premium can record to a USB drive.</p>'),
            ('What is the best IPTV box for seniors?', '<p>A MAG box or Formuler box: one simple app, a remote with live-TV buttons, and nothing to update.</p>'),
        ],
        related=["formuler-iptv", "iptv-android-tv", "mag-box-iptv", "iptv-firestick"],
        keywords=["iptv box", "ip tv box", "iptv with box", "best iptv box", "box iptv", "best android box for iptv", "best android tv box for iptv", "iptv android tv box", "iptv box android", "box android iptv", "iptv box price", "iptv box near me", "iptv box amazon", "amazon iptv box", "ip box tv", "box iptv 4k", "iptv smart box", "meilleur box iptv", "onn tv box", "buzztv xrs4500", "buzztv xrs 4900"],
    ),
    # ------------------------------------------------------------------ FORMULER
    dict(
        slug="formuler-iptv", hub="devices",
        title="Formuler Z11 Pro Max IPTV Box: Setup & Review | IPTVMaple",
        description="Formuler Z11 Pro Max, Z11 Pro and Z8 Pro for IPTV: what they offer, how to set up MyTVOnline 3, and which model to buy in Canada. Try IPTVMaple free 24h.",
        kicker="Devices", h1='<span class="grad-text">Formuler Z11 Pro Max</span> for IPTV',
        lead="Formuler boxes are built for IPTV, with MyTVOnline pre-installed and a remote designed for live TV. Here’s which model to pick and how to set it up.",
        crumb="Formuler", blurb="Z11 Pro Max, Z11 Pro and Z8 compared.",
        answer="<p>The <strong>Formuler Z11 Pro Max</strong> is an Android TV box made specifically for IPTV. It ships with the <strong>MyTVOnline 3</strong> app, supports 4K HDR, and has a remote with live-TV buttons (guide, favourites, channel up/down). Send us its MAC address and your IPTVMaple subscription loads in MyTVOnline in minutes.</p>",
        body="""
<h2>Formuler models compared</h2>
<table>
<thead><tr><th>Model</th><th>Highlights</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>Z11 Pro Max</td><td>4 GB RAM, 32 GB storage, Android TV, Wi-Fi 6, MyTVOnline 3</td><td>Best overall</td></tr>
<tr><td>Z11 Pro</td><td>Same design, less memory</td><td>Most households</td></tr>
<tr><td>Z10 SE / Z10 Pro Max</td><td>Previous generation</td><td>Budget, second TV</td></tr>
<tr><td>Z8 / Z8 Pro</td><td>Older model, MyTVOnline 2</td><td>Already own one</td></tr>
</tbody>
</table>
<p>Specifications vary by revision — check the box before buying.</p>

<h2>How to set up IPTV on a Formuler box</h2>
<ol>
<li>Connect the box to your TV and internet (Ethernet recommended).</li>
<li>Open <strong>MyTVOnline</strong> and note the <strong>MAC address</strong> on screen.</li>
<li>Send the MAC to IPTVMaple on WhatsApp with your order or <a href="/try-iptv-canada/">free trial</a>.</li>
<li>Add the portal URL we send you (or use Xtream Codes). Full walkthrough: <a href="/mytvonline/">MyTVOnline setup guide</a>.</li>
</ol>

<h2>Formuler vs Firestick</h2>
<p>A <a href="/iptv-firestick/">Firestick</a> is cheaper and great value. A Formuler costs more but is faster with big channel lists, has a remote made for live TV, and doesn’t require sideloading. Both can run <a href="/tivimate/">TiviMate</a>.</p>
""",
        faq=[
            ("Is Formuler good for IPTV?", "<p>Yes — Formuler boxes are designed specifically for IPTV, with MyTVOnline pre-installed and a live-TV remote.</p>"),
            ("Does Formuler come with channels?", "<p>No. The box is hardware only. You add an IPTV subscription like IPTVMaple to MyTVOnline.</p>"),
            ("Can I install TiviMate on a Formuler?", "<p>Yes. Formuler Z11 models run Android TV and can install TiviMate from Google Play.</p>"),
            ("Which Formuler should I buy in 2026?", "<p>The Z11 Pro Max is the best choice for 4K and large channel lists.</p>"),
        ],
        related=["mytvonline", "iptv-box", "mag-box-iptv"],
        keywords=["formuler z11", "formuler z11 pro", "formuler z11 pro max", "box formuler", "formuler box", "formuler iptv box", "formuler tv box", "formuler z8", "formuler z8 pro", "iptv formuler", "formuler z10 se", "formuler z10 pro max 4k", "formuler z8 pro 4k", "formuler z nano", "formuler z neo", "formuler z7"],
    ),
    # ------------------------------------------------------------------ MAG
    dict(
        slug="mag-box-iptv", hub="devices",
        title="MAG Box IPTV Setup: MAG 322, 324, 424 & 524 | IPTVMaple",
        description="How to set up IPTV on an Infomir MAG box (MAG 254, 322, 324, 424, 524): portal URL, MAC address and fixes. Works with IPTVMaple — try it free for 24 hours.",
        kicker="Devices", h1='<span class="grad-text">MAG box</span> IPTV setup',
        lead="MAG boxes by Infomir are the simplest IPTV boxes: plug in, add one portal URL, done. Here’s the setup for every model.",
        crumb="MAG box", blurb="Portal setup for MAG 254, 322, 424 and 524.",
        answer="<p>A <strong>MAG box</strong> connects to IPTV with a <strong>portal URL</strong> linked to the box’s <strong>MAC address</strong> (printed on the sticker under the box). Send us the MAC, we activate it, then enter the portal URL under <em>Settings → Servers → Portals</em>. The MAG 524 and MAG 424 support 4K; the MAG 322 and 254 are HD models.</p>",
        body="""
<h2>MAG models</h2>
<ul>
<li><strong>MAG 524 / 524w3</strong> — 4K HDR, Wi-Fi, current flagship.</li>
<li><strong>MAG 424 / 424w3</strong> — 4K, Android-based.</li>
<li><strong>MAG 322 / 324</strong> — Full HD, very popular and reliable.</li>
<li><strong>MAG 254 / 256 / 250</strong> — older HD models, still supported.</li>
</ul>

<h2>MAG box setup, step by step</h2>
<ol>
<li>Find the <strong>MAC address</strong> on the sticker under the box (starts with <code>00:1A:79</code>).</li>
<li>Send it to us on WhatsApp with your order or <a href="/try-iptv-canada/">free trial</a> request.</li>
<li>On the box, open <em>Settings → System settings → Servers → Portals</em>.</li>
<li>Enter a name (e.g. “IPTVMaple”) and paste the <strong>Portal 1 URL</strong> we send you.</li>
<li>Save and restart the box. The portal loads with live TV, VOD and the guide.</li>
</ol>

<h2>MAG troubleshooting</h2>
<ul>
<li><strong>Stuck on “Loading portal”</strong> — check the URL, including <code>/c/</code> at the end.</li>
<li><strong>“Authentication failed”</strong> — the MAC we activated must match the box exactly.</li>
<li><strong>Time wrong in guide</strong> — set your time zone in <em>System settings → Time</em>.</li>
</ul>

<h2>MAG vs Android boxes</h2>
<p>MAG boxes are the easiest option for less technical users: no app store, no updates to manage. If you want other apps too (YouTube, Netflix), pick an <a href="/iptv-box/">Android TV box</a>. Want the MAG experience on Android? Use <a href="/stbemu/">STBEmu</a>.</p>
""",
        faq=[
            ("Where is the MAC address on a MAG box?", "<p>On the sticker under the box, and in Settings → System settings → Device info.</p>"),
            ("Which MAG box supports 4K?", "<p>The MAG 524, MAG 424 and their Wi-Fi variants support 4K. The MAG 322 and 254 are HD.</p>"),
            ("Can I move my subscription to a new MAG box?", "<p>Yes, send us the new MAC address and we’ll transfer it.</p>"),
            ("Does IPTVMaple work on MAG boxes?", "<p>Yes, all Infomir MAG models are supported via portal URL.</p>"),
        ],
        related=["stbemu", "formuler-iptv", "iptv-box"],
        keywords=["mag box", "mag iptv", "mag iptv box", "mag iptv boxes", "mag tv box", "tv box mag", "mag 254", "mag 322", "mag 324", "mag 424", "mag 524", "mag 250", "mag 256", "infomir mag", "infomir iptv", "im infomir", "mag box 322", "mag box 4k", "mag322w1"],
    ),
    # ------------------------------------------------------------------ SAMSUNG
    dict(
        slug="iptv-samsung-tv", hub="devices",
        title="How to Watch IPTV on a Samsung Smart TV (2026) | IPTVMaple",
        description="Set up IPTV on a Samsung smart TV (Tizen): best apps like SmartOne, Flix IPTV, IBO Player and Smart IPTV, step-by-step setup and fixes. Try IPTVMaple free.",
        kicker="Devices", h1='IPTV on a <span class="grad-text">Samsung smart TV</span>',
        lead="Watch IPTV directly on your Samsung TV with no extra box. Here are the apps that work on Tizen and how to set them up.",
        crumb="Samsung TV", blurb="Best Tizen apps and step-by-step setup.",
        answer="<p>To watch <strong>IPTV on a Samsung smart TV</strong>, install an IPTV player from the Samsung app store — <strong>SmartOne IPTV</strong>, <strong>Flix IPTV</strong>, <strong>IBO Player</strong> or <strong>Smart IPTV</strong> — note the MAC address it shows, and add your playlist on the app’s website. On older or slower Samsung TVs, a Firestick plugged into HDMI gives a smoother experience.</p>",
        body="""
<h2>Best IPTV apps for Samsung TVs</h2>
<ul>
<li><a href="/smartone-iptv/">SmartOne IPTV</a> — live TV, movies and series; MAC-based setup.</li>
<li><a href="/flix-iptv/">Flix IPTV</a> — modern design, catch-up support.</li>
<li><strong>IBO Player</strong> — popular, easy playlist upload.</li>
<li><a href="/smart-iptv/">Smart IPTV</a> — classic app focused on live channels.</li>
</ul>
<p>App availability changes by TV model year and region. If one app isn’t in your store, try another — they all work with IPTVMaple.</p>

<h2>Samsung IPTV setup</h2>
<ol>
<li>Press <strong>Home</strong> on the remote and open <strong>Apps</strong>.</li>
<li>Search for the IPTV app and install it.</li>
<li>Open the app and note the <strong>MAC address</strong> (and device key, if shown).</li>
<li>On your phone, open the app’s official website and add the M3U link or Xtream login we sent you.</li>
<li>Restart the app on the TV.</li>
</ol>
<p>Prefer help? Send us a photo of the app screen on WhatsApp — we’ll set it up for you.</p>

<h2>Why IPTV Smarters or TiviMate aren’t on Samsung</h2>
<p>Samsung TVs run Tizen, not Android, so Android apps like <a href="/tivimate/">TiviMate</a> can’t be installed. If you want those apps, plug a <a href="/iptv-firestick/">Fire TV Stick</a> into your Samsung TV.</p>

<h2>Tips for a smooth picture</h2>
<ul>
<li>Use a wired connection — many Samsung TVs have slower Wi-Fi chips.</li>
<li>Turn off Motion Plus / Auto Motion Plus for sports to avoid artifacts.</li>
<li>Keep the TV’s software updated.</li>
</ul>
""",
        faq=[
            ("Can I install IPTV Smarters on a Samsung TV?", "<p>Not the Android version. Samsung uses Tizen; use SmartOne, Flix IPTV, IBO Player or Smart IPTV instead, or plug in a Firestick.</p>"),
            ("Is there a free IPTV app for Samsung TV?", "<p>Most Samsung IPTV apps offer a free trial and then a small one-time activation paid to the app developer.</p>"),
            ("Why is IPTV buffering on my Samsung TV?", "<p>Often the TV’s Wi-Fi. Try Ethernet, or use a Firestick 4K with a stronger Wi-Fi chip.</p>"),
            ("Does IPTVMaple work on Samsung smart TVs?", "<p>Yes, with any of the apps above. We send an M3U link and Xtream login that work in all of them.</p>"),
        ],
        related=["iptv-lg-tv", "iptv-smart-tv", "smartone-iptv", "duplecast", "iptv-firestick"],
        keywords=["iptv samsung tv", "iptv for samsung tv", "iptv samsung", "iptv samsung smart tv", "iptv samsung tizen", "samsung tizen iptv", "iptv tizen", "ip tv samsung", "iptv sur samsung", "iptv sur tv samsung", "samsung iptv smarters", "iptv smasters samsung tv"],
    ),
    # ------------------------------------------------------------------ LG
    dict(
        slug="iptv-lg-tv", hub="devices",
        title="How to Watch IPTV on an LG Smart TV (webOS) | IPTVMaple",
        description="Set up IPTV on an LG smart TV running webOS: best apps (SmartOne, Flix IPTV, IBO Player, Smart IPTV), step-by-step setup and tips. Try IPTVMaple free 24h.",
        kicker="Devices", h1='IPTV on an <span class="grad-text">LG smart TV</span>',
        lead="LG TVs run webOS and support several IPTV players from the LG Content Store. Here’s how to get your channels on screen.",
        crumb="LG TV", blurb="webOS apps and setup for LG TVs.",
        answer="<p>To watch <strong>IPTV on an LG TV</strong>, open the <strong>LG Content Store</strong>, install an IPTV player such as <strong>SmartOne IPTV</strong>, <strong>Flix IPTV</strong>, <strong>IBO Player</strong> or <strong>Smart IPTV</strong>, note the MAC address, then add your playlist on the app’s website. Channels load after restarting the app.</p>",
        body="""
<h2>IPTV apps for LG webOS</h2>
<table>
<thead><tr><th>App</th><th>Live TV</th><th>Movies &amp; series</th><th>Setup</th></tr></thead>
<tbody>
<tr><td><a href="/smartone-iptv/">SmartOne IPTV</a></td><td>Yes</td><td>Yes</td><td>MAC + website</td></tr>
<tr><td><a href="/flix-iptv/">Flix IPTV</a></td><td>Yes</td><td>Yes</td><td>MAC + key + website</td></tr>
<tr><td>IBO Player</td><td>Yes</td><td>Yes</td><td>MAC + key + website</td></tr>
<tr><td><a href="/smart-iptv/">Smart IPTV</a></td><td>Yes</td><td>Limited</td><td>MAC + website</td></tr>
</tbody>
</table>

<h2>LG IPTV setup</h2>
<ol>
<li>Press <strong>Home</strong> and open the <strong>LG Content Store</strong> (Apps).</li>
<li>Search for your chosen IPTV app and install it.</li>
<li>Open the app and note the MAC address shown.</li>
<li>Add your IPTVMaple M3U link or Xtream login on the app’s official website.</li>
<li>Restart the app — your channels, movies and series appear.</li>
</ol>

<h2>LG TV tips</h2>
<ul>
<li>Turn off <em>TruMotion</em> for sports if you see artifacts.</li>
<li>Set the TV’s time zone correctly so the program guide matches.</li>
<li>For TiviMate or IPTV Smarters, add a <a href="/iptv-firestick/">Firestick</a> or <a href="/iptv-android-tv/">Android TV device</a>.</li>
</ul>
""",
        faq=[
            ("What is the best IPTV app for LG TV?", "<p>SmartOne IPTV, Flix IPTV and IBO Player are the most popular on webOS because they include live TV plus movies and series.</p>"),
            ("Can I install TiviMate on an LG TV?", "<p>No. LG TVs run webOS, not Android. Use a Firestick or Android TV box for TiviMate.</p>"),
            ("Do LG IPTV apps cost money?", "<p>Most offer a free trial, then a one-time activation paid to the app developer.</p>"),
            ("Does IPTVMaple work on LG TVs?", "<p>Yes, with any of the webOS apps above.</p>"),
        ],
        related=["iptv-samsung-tv", "iptv-smart-tv", "smartone-iptv", "ss-iptv"],
        keywords=["iptv lg", "iptv lg tv", "iptv lg smart", "iptv lg webos", "iptv for lg webos", "webos iptv", "tivimate lg", "iptv smasters lg tv"],
    ),
    # ------------------------------------------------------------------ APPLE TV
    dict(
        slug="iptv-apple-tv", hub="devices",
        title="How to Watch IPTV on Apple TV 4K (2026 Guide) | IPTVMaple",
        description="The best IPTV apps for Apple TV 4K — iPlayTV, Smarters Player Lite, IMPlayer, IPTVX — and how to set them up with your login. Try IPTVMaple free for 24 hours.",
        kicker="Devices", h1='IPTV on <span class="grad-text">Apple TV</span>',
        lead="Apple TV 4K is one of the smoothest IPTV devices available. Here are the best apps and how to set them up.",
        crumb="Apple TV", blurb="Best tvOS apps and setup for Apple TV 4K.",
        answer="<p>To watch <strong>IPTV on Apple TV</strong>, download an IPTV player from the App Store — <strong>iPlayTV</strong>, <strong>Smarters Player Lite</strong>, <strong>IMPlayer</strong> or <strong>IPTVX</strong> — then add your IPTV login (Xtream Codes or M3U). Apple TV 4K handles 4K HDR streams smoothly, especially on a wired connection.</p>",
        body="""
<h2>Best IPTV apps for Apple TV</h2>
<ul>
<li><a href="/iplaytv/">iPlayTV</a> — paid, cable-style guide, the closest to TiviMate on Apple TV.</li>
<li><a href="/smarters-player-lite/">Smarters Player Lite</a> — free and easy.</li>
<li><a href="/implayer/">IMPlayer</a> — syncs with Android devices.</li>
<li><strong>IPTVX</strong> — polished design, also on iPhone and Mac.</li>
</ul>
<p>TiviMate is not available on Apple TV.</p>

<h2>Apple TV IPTV setup</h2>
<ol>
<li>Open the <strong>App Store</strong> on your Apple TV and install your chosen app.</li>
<li>Open the app and choose <strong>Add playlist</strong> (or “Login with Xtream Codes”).</li>
<li>Enter your IPTVMaple server URL, username and password.</li>
<li>Wait for channels, movies and the guide to load.</li>
</ol>

<h2>Best settings for sports and 4K</h2>
<ul>
<li>Use <strong>Ethernet</strong> on Apple TV 4K (the Wi-Fi-only model is fine on strong 5 GHz Wi-Fi).</li>
<li>Enable <em>Settings → Video and Audio → Match Content → Match Dynamic Range and Frame Rate</em>.</li>
<li>Keep tvOS updated.</li>
</ul>
""",
        faq=[
            ("Can I use TiviMate on Apple TV?", "<p>No, TiviMate is Android only. On Apple TV, iPlayTV offers a similar cable-style experience.</p>"),
            ("What is the best free IPTV app for Apple TV?", "<p>Smarters Player Lite is free and works with IPTVMaple’s Xtream login.</p>"),
            ("Does Apple TV support 4K IPTV?", "<p>Yes, Apple TV 4K plays 4K HDR IPTV streams smoothly with a good connection.</p>"),
            ("Can I watch on my Apple TV and iPhone at once?", "<p>Yes, with a plan that includes 2 or more simultaneous devices.</p>"),
        ],
        related=["iplaytv", "smarters-player-lite", "iptv-iphone"],
        keywords=["iptv apple tv", "iptv apple tv 4k", "iptv on apple tv 4k", "iptv apple", "iptv sur apple tv", "tivimate apple tv", "iptvx apple tv", "iptv smarters apple tv", "iptv smasters pro apple tv"],
    ),
    # ------------------------------------------------------------------ ROKU
    dict(
        slug="iptv-roku", hub="devices",
        title="Can You Watch IPTV on Roku? Options for 2026 | IPTVMaple",
        description="Can you watch IPTV on a Roku TV or stick? Why most IPTV apps aren’t on Roku, the screen-mirroring workaround, and the best alternative device. Try IPTVMaple.",
        kicker="Devices", h1='Can you watch <span class="grad-text">IPTV on Roku</span>?',
        lead="Roku is popular in Canada, but it’s not built for IPTV apps. Here’s the honest answer and your best options.",
        crumb="Roku", blurb="Honest answer and workarounds for Roku.",
        answer="<p>Roku doesn’t support most IPTV players: <strong>TiviMate, IPTV Smarters and similar apps are not in the Roku Channel Store</strong>, and Roku doesn’t allow installing outside apps. Your options are <strong>screen mirroring</strong> from an Android phone or Windows PC, or adding an inexpensive <strong>Fire TV Stick or Google TV device</strong> to the Roku TV’s HDMI port — the solution we recommend.</p>",
        body="""
<h2>Why IPTV apps aren’t on Roku</h2>
<p>Roku runs its own operating system and only allows apps (“channels”) approved in its store. Full-featured IPTV players with Xtream Codes support aren’t available there, and apps that appeared in the past were often removed.</p>

<h2>Option 1 — Screen mirroring (free, basic)</h2>
<ol>
<li>On the Roku, enable <em>Settings → System → Screen mirroring</em>.</li>
<li>On an Android phone, open Quick Settings → <strong>Smart View / Cast / Screen cast</strong> and pick your Roku. On Windows, press <strong>Win + K</strong>.</li>
<li>Play IPTVMaple in <a href="/iptv-smarters-pro/">IPTV Smarters</a> on the phone or computer.</li>
</ol>
<p>Mirroring works but quality depends on your Wi-Fi, and your phone must stay on. iPhones can’t mirror to most Roku devices without AirPlay support.</p>

<h2>Option 2 — Add a streaming stick (recommended)</h2>
<p>Plug a <a href="/iptv-firestick/">Fire TV Stick 4K</a> or a Google TV device into a free HDMI port on your Roku TV. Switch inputs and you get <a href="/tivimate/">TiviMate</a>, a real TV guide and 4K — for less than one month of cable.</p>
""",
        faq=[
            ("Is there an IPTV app for Roku?", "<p>Not a full-featured one. Popular IPTV players like TiviMate and IPTV Smarters aren’t available on Roku.</p>"),
            ("Can I use IPTV Smarters on Roku?", "<p>No. You can mirror it from an Android phone or PC, or plug a Firestick into your Roku TV.</p>"),
            ("Can I watch IPTV on a Roku TV?", "<p>Yes, by plugging a Firestick or Android TV stick into one of the TV’s HDMI ports and switching input.</p>"),
            ("Does screen mirroring to Roku work for sports?", "<p>It works, but can lag or drop quality on busy Wi-Fi. A dedicated stick is much better for live sports.</p>"),
        ],
        related=["iptv-firestick", "iptv-android-tv", "iptv-devices"],
        keywords=["iptv roku", "iptv roku tv", "iptv on roku tv", "roku tv iptv", "roku express iptv", "tivimate roku", "iptv smasters pro roku", "iptv smasters on roku tv"],
    ),
    # ------------------------------------------------------------------ ANDROID TV
    dict(
        slug="iptv-android-tv", hub="devices",
        title="IPTV on Android TV & Google TV: Setup Guide | IPTVMaple",
        description="Set up IPTV on Android TV and Google TV devices — Sony, TCL, Hisense, Nvidia Shield, Chromecast, Xiaomi Mi Box — with TiviMate or Smarters. Try IPTVMaple free.",
        kicker="Devices", h1='IPTV on <span class="grad-text">Android TV</span> &amp; Google TV',
        lead="Android TV and Google TV give you the widest choice of IPTV apps, straight from the Play Store.",
        crumb="Android TV", blurb="Sony, TCL, Hisense, Shield, Mi Box & more.",
        answer="<p>On <strong>Android TV and Google TV</strong> devices — Sony, TCL, Hisense and Philips TVs, Nvidia Shield, Chromecast with Google TV, Google TV Streamer, Xiaomi Mi Box and onn boxes — install <strong>TiviMate</strong>, <strong>IPTV Smarters Pro</strong> or <strong>IMPlayer</strong> from Google Play, then add your IPTV login. No sideloading needed.</p>",
        body="""
<h2>Android TV devices that work great for IPTV</h2>
<ul>
<li><strong>Nvidia Shield TV / Shield TV Pro</strong> — the most powerful, great for 4K.</li>
<li><strong>Google TV Streamer</strong> and <strong>Chromecast with Google TV</strong> — compact and affordable (<a href="/iptv-chromecast/">Chromecast guide</a>).</li>
<li><strong>Xiaomi Mi Box S / TV Box S</strong> — budget Android TV box.</li>
<li><strong>Sony, TCL, Hisense, Philips</strong> smart TVs with Google TV built in.</li>
<li><a href="/formuler-iptv/">Formuler</a> — Android TV boxes built for IPTV.</li>
</ul>

<h2>How to set it up</h2>
<ol>
<li>Open the <strong>Google Play Store</strong> on your TV or box.</li>
<li>Install <a href="/tivimate/">TiviMate</a> (recommended), <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> or <a href="/implayer/">IMPlayer</a>.</li>
<li>Open the app → Add playlist → <strong>Xtream Codes</strong>.</li>
<li>Enter your IPTVMaple server URL, username and password.</li>
</ol>

<h2>Performance tips</h2>
<ul>
<li>Use Ethernet where possible (a USB-C Ethernet adapter works on Chromecast).</li>
<li>In TiviMate, enable “Auto frame rate” for smoother sports.</li>
<li>Uninstall unused preinstalled apps to free memory on budget boxes.</li>
</ul>
""",
        faq=[
            ("Is Android TV good for IPTV?", "<p>Yes. It supports the most IPTV apps, including TiviMate, directly from Google Play.</p>"),
            ("Do Hisense and TCL TVs support IPTV?", "<p>Models running Google TV or Android TV do — install TiviMate or Smarters from Google Play. Hisense models running VIDAA need a VIDAA-compatible app or a Firestick.</p>"),
            ("What’s the best Android TV box for IPTV?", "<p>Nvidia Shield TV Pro for power, Google TV Streamer or onn 4K for value. See our <a href=\"/iptv-box/\">IPTV box guide</a>.</p>"),
            ("Can I record IPTV on Android TV?", "<p>Yes, with TiviMate Premium and enough storage (a USB drive works on many boxes).</p>"),
        ],
        related=["tivimate", "iptv-box", "iptv-chromecast", "iptv-firestick"],
        keywords=["iptv android tv", "iptv android", "smart iptv android tv", "tivimate android tv", "iptv google tv", "nvidia shield iptv", "iptv nvidia shield", "mi box iptv", "xiaomi iptv", "xiaomi iptv box", "iptv hisense", "iptv sony", "vidaa iptv", "iptv smasters android tv"],
    ),
    # ------------------------------------------------------------------ PC / MAC
    dict(
        slug="iptv-pc-mac", hub="devices",
        title="How to Watch IPTV on PC & Mac (Windows, macOS) | IPTVMaple",
        description="Watch IPTV on a Windows PC, laptop or Mac: IPTV Smarters desktop, VLC, MyIPTV Player, Kodi and web players compared, with setup steps. Try IPTVMaple free 24h.",
        kicker="Devices", h1='How to watch <span class="grad-text">IPTV on PC &amp; Mac</span>',
        lead="Your computer is a great IPTV screen — at your desk, on a laptop, or connected to a TV by HDMI.",
        crumb="PC & Mac", blurb="Smarters, VLC, Kodi and more on computers.",
        answer="<p>To watch <strong>IPTV on a PC or Mac</strong>, install a desktop IPTV player — <strong>IPTV Smarters</strong> for Windows/macOS, <strong>MyIPTV Player</strong> (Windows), <strong>IPTVX</strong> (Mac) — or open your M3U link in <strong>VLC</strong>. Log in with your IPTV details and watch live TV, movies and series on your computer.</p>",
        body="""
<h2>Best IPTV players for computers</h2>
<table>
<thead><tr><th>App</th><th>Windows</th><th>Mac</th><th>TV guide</th></tr></thead>
<tbody>
<tr><td><a href="/iptv-smarters-pro/">IPTV Smarters</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>MyIPTV Player</td><td>Yes (Microsoft Store)</td><td>—</td><td>Yes</td></tr>
<tr><td>IPTVX</td><td>—</td><td>Yes</td><td>Yes</td></tr>
<tr><td><a href="/vlc-iptv/">VLC</a></td><td>Yes</td><td>Yes</td><td>No</td></tr>
<tr><td><a href="/kodi-iptv/">Kodi</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
</tbody>
</table>

<h2>Quickest option: VLC</h2>
<p>Open VLC → <em>Media → Open Network Stream</em> → paste your M3U link → Play. Full steps in our <a href="/vlc-iptv/">VLC IPTV guide</a>.</p>

<h2>Best option: IPTV Smarters desktop</h2>
<ol>
<li>Download IPTV Smarters for Windows or macOS from the official website.</li>
<li>Install and open it; choose <strong>Login with Xtream Codes API</strong>.</li>
<li>Enter your IPTVMaple server URL, username and password.</li>
</ol>

<h2>Watch on your TV from a laptop</h2>
<p>Connect the laptop to your TV with an HDMI cable, or cast from Chrome on Windows. For daily TV viewing, a <a href="/iptv-firestick/">Firestick</a> is more comfortable.</p>
""",
        faq=[
            ("Can I watch IPTV on my laptop?", "<p>Yes. Use IPTV Smarters, VLC, Kodi or another desktop player with your IPTV login.</p>"),
            ("What is the best IPTV player for Windows?", "<p>IPTV Smarters desktop and MyIPTV Player both offer a TV guide. VLC is the quickest for simple playback.</p>"),
            ("Can I watch IPTV on a MacBook?", "<p>Yes — IPTV Smarters for macOS, IPTVX or VLC all work on Mac.</p>"),
            ("Can I watch IPTV in a web browser?", "<p>Some players offer web versions, but a desktop app is more reliable for live TV.</p>"),
        ],
        related=["vlc-iptv", "kodi-iptv", "iptv-smarters-pro"],
        keywords=["iptv pc", "iptv player pc", "ip tv pc", "iptv laptop", "iptv macbook", "mac iptv", "iptv sur pc", "iptv sur mac", "iptv pour pc", "m3u player pc", "iptv smarter pc", "smart iptv pc", "tivimate pc", "tivimate for pc", "iptv smarters pro pc", "iptv browser", "iptv web browser", "iptv chrome"],
    ),
    # ------------------------------------------------------------------ IPHONE
    dict(
        slug="iptv-iphone", hub="devices",
        title="How to Watch IPTV on iPhone & iPad (2026) | IPTVMaple",
        description="Watch IPTV on iPhone and iPad: best App Store players (Smarters Player Lite, IPTVX, iPlayTV, GSE), setup steps and tips for mobile data. Try IPTVMaple free 24h.",
        kicker="Devices", h1='IPTV on <span class="grad-text">iPhone &amp; iPad</span>',
        lead="Take live TV and sports with you. Here’s how to set up IPTV on your iPhone or iPad in two minutes.",
        crumb="iPhone & iPad", blurb="Best App Store players for iOS.",
        answer="<p>To watch <strong>IPTV on iPhone or iPad</strong>, install a player from the App Store — <strong>Smarters Player Lite</strong> (free), <strong>IPTVX</strong>, <strong>iPlayTV</strong> or <strong>GSE Smart IPTV</strong> — and log in with your IPTV details. You can AirPlay to an Apple TV or AirPlay-compatible smart TV too.</p>",
        body="""
<h2>Best IPTV apps for iPhone and iPad</h2>
<ul>
<li><a href="/smarters-player-lite/">Smarters Player Lite</a> — free, simple, same login as Smarters Pro.</li>
<li><strong>IPTVX</strong> — beautiful interface, syncs with Apple TV and Mac.</li>
<li><a href="/iplaytv/">iPlayTV</a> — paid, excellent guide, picture-in-picture.</li>
<li><strong>GSE Smart IPTV</strong> — veteran app with Chromecast support.</li>
</ul>

<h2>Set up IPTV on iPhone</h2>
<ol>
<li>Install your chosen app from the App Store.</li>
<li>Choose <strong>Xtream Codes</strong> login.</li>
<li>Enter the server URL, username and password from IPTVMaple.</li>
<li>Browse Live TV, Movies and Series.</li>
</ol>

<h2>Watching on mobile data</h2>
<p>An HD stream uses around 1.5–3 GB per hour. On mobile data, pick SD or HD channels instead of 4K, and use Wi-Fi when you can.</p>

<h2>Send it to the big screen</h2>
<p>Use <strong>AirPlay</strong> to an <a href="/iptv-apple-tv/">Apple TV</a> or an AirPlay-compatible Samsung, LG or Sony TV. For daily TV viewing, install the app directly on the TV device instead.</p>
""",
        faq=[
            ("Is there a free IPTV app for iPhone?", "<p>Yes, Smarters Player Lite is free on the App Store and works with IPTVMaple.</p>"),
            ("Can I watch IPTV on iPad?", "<p>Yes, all the apps above run on iPad too — great for watching games in the kitchen or on the go.</p>"),
            ("How much data does IPTV use on iPhone?", "<p>About 1.5–3 GB per hour in HD, and much more in 4K. Use Wi-Fi when possible.</p>"),
            ("Can I AirPlay IPTV to my TV?", "<p>Most iOS IPTV apps support AirPlay to Apple TV and AirPlay-compatible smart TVs.</p>"),
        ],
        related=["smarters-player-lite", "iptv-apple-tv", "iplaytv"],
        keywords=["iptv iphone", "iptv sur iphone", "iptv ipad", "iptv mobile", "iptv smasters iphone", "gse iptv", "gseiptv", "iptvx", "atlas pro ontv iphone", "tivimate companion iphone"],
    ),
    # ------------------------------------------------------------------ CHROMECAST
    dict(
        slug="iptv-chromecast", hub="devices",
        title="IPTV on Chromecast & Google TV Streamer | IPTVMaple",
        description="Watch IPTV on Chromecast with Google TV and Google TV Streamer (install TiviMate) or cast from your phone with GSE and Smarters Lite. Try IPTVMaple free 24h.",
        kicker="Devices", h1='IPTV on <span class="grad-text">Chromecast</span>',
        lead="Whether you have a Chromecast with Google TV or an older cast-only Chromecast, here’s how to get IPTV on your TV.",
        crumb="Chromecast", blurb="Google TV apps or casting from your phone.",
        answer="<p>On <strong>Chromecast with Google TV</strong> and the <strong>Google TV Streamer</strong>, install an IPTV app like <strong>TiviMate</strong> directly from Google Play. On older <strong>cast-only Chromecasts</strong>, play IPTV on your phone in an app with casting support (such as GSE Smart IPTV or IPTV Smarters) and tap the Cast icon.</p>",
        body="""
<h2>Chromecast with Google TV / Google TV Streamer</h2>
<p>These are full Android TV devices with a remote. Setup is the same as any <a href="/iptv-android-tv/">Android TV</a>:</p>
<ol>
<li>Open Google Play and install <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</li>
<li>Add playlist → Xtream Codes → enter your IPTVMaple login.</li>
<li>Watch with a full TV guide.</li>
</ol>
<p>Tip: storage is limited on the Chromecast with Google TV — keep only the apps you use.</p>

<h2>Older Chromecast (cast-only)</h2>
<ol>
<li>Install an IPTV app with Chromecast support on your phone.</li>
<li>Log in with your IPTV details.</li>
<li>Start a channel and tap the <strong>Cast</strong> icon, then choose your Chromecast.</li>
</ol>
<p>Casting depends on your phone and Wi-Fi. For daily viewing, an upgrade to a Google TV device or <a href="/iptv-firestick/">Firestick</a> is worth it.</p>
""",
        faq=[
            ("Can I install TiviMate on Chromecast?", "<p>Yes, on Chromecast with Google TV and Google TV Streamer, directly from Google Play.</p>"),
            ("Can I cast IPTV from my iPhone to Chromecast?", "<p>Yes, with iOS apps that support Chromecast casting, such as GSE Smart IPTV.</p>"),
            ("Is Chromecast good for 4K IPTV?", "<p>The Chromecast with Google TV (4K) and Google TV Streamer both support 4K HDR.</p>"),
            ("Does IPTVMaple work on Chromecast?", "<p>Yes, either through an app on Google TV models or by casting from your phone.</p>"),
        ],
        related=["iptv-android-tv", "tivimate", "iptv-firestick"],
        keywords=["iptv chromecast", "chromecast iptv", "iptv google chromecast", "iptv sur chromecast", "gse iptv chromecast", "tivimate chromecast", "iptv smarters chromecast", "smarters player lite chromecast"],
    ),
]
