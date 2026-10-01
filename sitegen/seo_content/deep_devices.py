"""Depth pass, part 2: hardware and device pages. See deep.py for how entries are applied."""

DATA = {}

DATA["formuler-iptv"] = dict(
    meta=dict(title="Formuler Z-Series IPTV Box Guide (2026) | IPTVMaple"),
    add="""
<h2>Which Formuler should you buy?</h2>
<table>
<thead><tr><th>You want…</th><th>Choose</th><th>Why</th></tr></thead>
<tbody>
<tr><td>The best box, with room to grow</td><td>Z11 Pro Max</td><td>The most memory and the newest MyTVOnline 3</td></tr>
<tr><td>A great box for most homes</td><td>Z11 Pro or Z11</td><td>Same design and software, less memory</td></tr>
<tr><td>A bargain or a second-room TV</td><td>Z10 SE / Z10 Pro Max, if on sale</td><td>Previous generation, still works well</td></tr>
<tr><td>To keep what you own</td><td>Z8 / Z8 Pro and older</td><td>Still supported through MyTVOnline 2 and portals</td></tr>
</tbody>
</table>
<p>Model names, memory and sale prices change often, so confirm the specs on the retailer’s page before buying.</p>

<h2>Formuler vs Nvidia Shield vs Firestick</h2>
<table>
<thead><tr><th></th><th>Formuler</th><th>Nvidia Shield</th><th>Firestick 4K Max</th></tr></thead>
<tbody>
<tr><td>Built for IPTV</td><td>Yes, remote and portal app</td><td>General media player</td><td>General streaming stick</td></tr>
<tr><td>Setup</td><td>Easy (portal or Xtream)</td><td>Easy (Google Play)</td><td>Needs Downloader for TiviMate</td></tr>
<tr><td>Power with big channel lists</td><td>Very good</td><td>Excellent</td><td>Good</td></tr>
<tr><td>Price</td><td>Higher</td><td>Highest</td><td>Lowest</td></tr>
<tr><td>Best IPTV app</td><td>MyTVOnline 3 or <a href="/tivimate/">TiviMate</a></td><td><a href="/tivimate/">TiviMate</a></td><td><a href="/tivimate-firestick/">TiviMate</a></td></tr>
</tbody>
</table>
<p>For the broader comparison see the <a href="/iptv-box/">IPTV box guide</a>.</p>

<h2>Formuler troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Portal error or “not authorized”</td><td>Send us the MAC shown on the MyTVOnline start screen so we can match it, then re-enter the portal URL</td></tr>
<tr><td>Sluggish guide</td><td>Hide channel groups you don’t watch and restart the box</td></tr>
<tr><td>Wi-Fi drops</td><td>Use the Ethernet port. See the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
<tr><td>Want a nicer guide</td><td>Install <a href="/tivimate/">TiviMate</a> from Google Play and use your Xtream login</td></tr>
</tbody>
</table>
""",
    faq=[
        ("Can I use my old Formuler Z8 with IPTVMaple?",
         "<p>Yes. Older Formuler boxes work through MyTVOnline 2 and the portal method: send us the MAC address shown in the app and we will activate it.</p>"),
        ("Should I use MyTVOnline or TiviMate on a Formuler?",
         "<p>MyTVOnline is the simplest start and made for the Formuler remote. TiviMate has a more polished guide and extra Premium features. You can install both and use the same login.</p>"),
    ],
    related=["tivimate-devices", "iptv-buffering-fix"],
)

DATA["mag-box-iptv"] = dict(
    add="""
<h2>Find your MAG box’s MAC address</h2>
<p>The MAC address is printed on the sticker under the box and starts with <code>00:1A:79</code>. It also appears in the box’s settings or on the start-up screen. Send us exactly what you see, including the colons, so we can activate it.</p>

<h2>MAG box troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>“Loading portal” never finishes</td><td>Check the portal URL ends with <code>/c/</code> as sent; check the cable or Wi-Fi</td></tr>
<tr><td>Authentication failed</td><td>The MAC we activated must match the sticker exactly</td></tr>
<tr><td>Picture freezes</td><td>Use Ethernet and see the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
<tr><td>Guide is off by hours</td><td>Set your time zone in the box’s System settings</td></tr>
<tr><td>Box behaves oddly after a firmware update</td><td>Re-enter the portal URL in Settings and restart. Update options are in the Settings menu (names vary by model)</td></tr>
</tbody>
</table>

<h2>Moving to a new MAG box</h2>
<p>A subscription is tied to the box’s MAC address. If you replace the box, send us the new MAC address and we will move the activation. Want the MAG experience without the hardware? See <a href="/stbemu/">STBEmu</a>, or compare the options in the <a href="/iptv-box/">IPTV box guide</a>.</p>
""",
    faq=[
        ("Do MAG boxes need an app store?",
         "<p>No. A MAG box runs its own portal software, so you simply enter the portal address. If you want other apps, such as YouTube, choose an Android TV box instead.</p>"),
    ],
    related=["iptv-box", "iptv-buffering-fix"],
)

DATA["iptv-samsung-tv"] = dict(
    add="""
<h2>Which Samsung TVs support IPTV apps?</h2>
<p>Samsung’s smart TVs use the Tizen system. Models from roughly 2017 onwards have the widest choice of apps, and very old models may not list newer ones. App stores differ by country, so an app can be available on one TV and missing on another. If your TV’s store lacks the app you want, add a Fire TV Stick instead of replacing the TV.</p>

<h2>Samsung IPTV apps compared</h2>
<table>
<thead><tr><th>App</th><th>Login</th><th>Movies and series</th><th>Guide</th></tr></thead>
<tbody>
<tr><td><a href="/iptv-smarters-pro-samsung-lg/">Smarters Player Lite</a></td><td>Xtream Codes on the TV</td><td>Yes</td><td>Yes</td></tr>
<tr><td><a href="/smartone-iptv/">SmartOne IPTV</a></td><td>MAC address + website</td><td>Yes</td><td>Yes</td></tr>
<tr><td><a href="/flix-iptv/">Flix IPTV</a></td><td>MAC address + website</td><td>Yes</td><td>Yes</td></tr>
<tr><td><a href="/smart-iptv/">Smart IPTV</a></td><td>MAC address + website</td><td>Limited</td><td>Basic</td></tr>
</tbody>
</table>

<h2>Samsung IPTV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>App not in the store</td><td>Update the TV, try another app, or use a Firestick</td></tr>
<tr><td>Playlist won’t load</td><td>Re-enter the MAC address on the app’s official site; restart the app</td></tr>
<tr><td>App crashes</td><td>Unplug the TV for a minute; reinstall the app</td></tr>
<tr><td>Stutters</td><td>Connect Ethernet to the TV; see the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>
<p>Prefer French? <a href="/iptv-sur-samsung/">IPTV sur Samsung et LG</a>.</p>
""",
    faq=[
        ("Which Samsung TV models work with IPTV apps?",
         "<p>Tizen smart TVs from roughly 2017 onwards have the widest app support, depending on your country’s store. Older models may not list newer apps; a Firestick is an easy fix.</p>"),
    ],
    related=["iptv-smarters-pro-samsung-lg", "tivimate-devices"],
)

DATA["iptv-lg-tv"] = dict(
    add="""
<h2>Which LG TVs support IPTV apps?</h2>
<p>LG’s webOS smart TVs from roughly 2018 onwards usually have the widest choice in the LG Content Store. Availability varies by country and model year. If the app you want is missing, the quickest fix is a Fire TV Stick or Google TV Streamer on an HDMI port.</p>

<h2>LG IPTV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>App not found in the Content Store</td><td>Update webOS, check your region setting, or try another app</td></tr>
<tr><td>Playlist not loading</td><td>Re-enter the MAC address (and device key, if shown) on the app’s official website</td></tr>
<tr><td>Slow menus</td><td>Hide channel groups you don’t watch or add a stick</td></tr>
<tr><td>Buffering</td><td>Connect Ethernet to the TV; see the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>
<p>The Smarters app is also available on many LG TVs as Smarters Player Lite: see <a href="/iptv-smarters-pro-samsung-lg/">IPTV Smarters on Samsung and LG</a>. En français: <a href="/iptv-sur-samsung/">IPTV sur Samsung et LG</a>.</p>
""",
    related=["iptv-smarters-pro-samsung-lg", "tivimate-devices"],
)

DATA["iptv-apple-tv"] = dict(
    add="""
<h2>Apple TV or Firestick for IPTV?</h2>
<table>
<thead><tr><th></th><th>Apple TV 4K</th><th>Fire TV Stick 4K Max</th></tr></thead>
<tbody>
<tr><td>Price</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Best IPTV app</td><td>iPlayTV, Smarters Player Lite</td><td><a href="/tivimate-firestick/">TiviMate</a></td></tr>
<tr><td>Guide quality</td><td>Excellent in iPlayTV</td><td>Excellent in TiviMate</td></tr>
<tr><td>Ecosystem</td><td>AirPlay, iPhone remote</td><td>Alexa, Amazon apps</td></tr>
<tr><td>Setup</td><td>App Store only</td><td>Sideloading with Downloader</td></tr>
</tbody>
</table>

<h2>Apple TV IPTV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Login fails</td><td>Re-enter without spaces; include http:// and the port</td></tr>
<tr><td>No guide</td><td>Use Xtream Codes, or add the EPG link with M3U</td></tr>
<tr><td>Video stutters</td><td>Ethernet; turn on Match Frame Rate; see the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>
<p>TiviMate is not on Apple TV: see <a href="/tivimate-devices/">where TiviMate runs</a>. En français: <a href="/iptv-sur-apple-tv-iphone/">IPTV sur Apple TV et iPhone</a>.</p>
""",
    related=["tivimate-devices", "iptv-smarters-pro-download"],
)

DATA["iptv-roku"] = dict(
    add="""
<h2>Be careful with “IPTV channels” on Roku</h2>
<p>You may see guides that tell you to add a “private channel” to Roku using a code. Private channels aren’t reviewed by Roku, many stop working without notice, and some are scams that ask for payment. A Roku device doesn’t have an official, full-featured IPTV player for Xtream Codes logins, so we recommend the streaming-stick approach below.</p>

<h2>Roku options compared</h2>
<table>
<thead><tr><th>Option</th><th>Quality</th><th>Effort</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Add a Fire TV Stick or Google TV device</td><td>Best (4K, full guide)</td><td>Low</td><td>Recommended</td></tr>
<tr><td>Screen mirroring from a phone or PC</td><td>Basic, depends on Wi-Fi</td><td>Medium</td><td>Fine for a quick test</td></tr>
<tr><td>Private “IPTV” channels</td><td>Unreliable</td><td>Medium</td><td>Avoid</td></tr>
</tbody>
</table>
<p>See the stick guides: <a href="/tivimate-firestick/">TiviMate on Firestick</a>, <a href="/iptv-smarters-pro-firestick/">IPTV Smarters on Firestick</a>, and <a href="/tivimate-devices/">why TiviMate doesn’t run on Roku</a>.</p>
""",
    faq=[
        ("Are private IPTV channels on Roku safe?",
         "<p>They aren’t reviewed by Roku, often stop working and are sometimes used for scams. Use a Fire TV or Google TV stick on the same TV instead.</p>"),
    ],
    related=["tivimate-devices", "iptv-smarters-pro-firestick"],
)

DATA["iptv-android-tv"] = dict(
    add="""
<h2>Android TV, Google TV and Fire TV: what’s the difference?</h2>
<table>
<thead><tr><th></th><th>Android TV / Google TV</th><th>Fire TV (Fire OS)</th></tr></thead>
<tbody>
<tr><td>App store</td><td>Google Play</td><td>Amazon Appstore (sideload others)</td></tr>
<tr><td>TiviMate</td><td>Install from Google Play</td><td>Install with Downloader</td></tr>
<tr><td>Devices</td><td>Nvidia Shield, Google TV Streamer, Sony, TCL, Hisense TVs, boxes</td><td>Fire TV sticks and cubes, Fire TV smart TVs</td></tr>
<tr><td>Best IPTV app</td><td><a href="/tivimate/">TiviMate</a></td><td><a href="/tivimate-firestick/">TiviMate</a></td></tr>
</tbody>
</table>

<h2>Installing an app that isn’t in Google Play</h2>
<ol>
<li>Install the free <strong>Downloader</strong> app from Google Play.</li>
<li>Open <em>Settings → Device Preferences → Security &amp; restrictions → Unknown sources</em> (menu names vary by TV) and allow Downloader.</li>
<li>Enter the app developer’s official download address in Downloader and install the file.</li>
</ol>
<p>Only use official addresses. Details for each app are in <a href="/iptv-smarters-pro-download/">IPTV Smarters Pro download</a> and <a href="/tivimate-firestick/">TiviMate install</a>.</p>

<h2>Android TV troubleshooting</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Storage full</td><td>Remove unused apps; clear app caches</td></tr>
<tr><td>Lag after hours of use</td><td>Restart the device; reduce channel groups in the player</td></tr>
<tr><td>Wi-Fi unstable</td><td>Ethernet or 5 GHz. See the <a href="/iptv-buffering-fix/">buffering fixes</a></td></tr>
</tbody>
</table>
""",
    related=["tivimate-firestick", "tivimate-devices"],
)

DATA["iptv-pc-mac"] = dict(
    add="""
<h2>Guides for computers</h2>
<ul>
<li><a href="/iptv-smarters-pro-pc-mac/">IPTV Smarters Pro for Windows and Mac</a>: install, log in, troubleshoot.</li>
<li><a href="/vlc-iptv/">VLC</a> and <a href="/kodi-iptv/">Kodi</a>: the lightweight and full-featured alternatives.</li>
<li><a href="/watch-iptv-online/">Watch IPTV online in a browser</a>: why it often fails and what is safe.</li>
<li><a href="/tivimate-devices/">Does TiviMate run on PC and Mac?</a> No, and what to use instead.</li>
</ul>

<h2>Performance tips for laptops</h2>
<ul>
<li>Plug in the charger during live sports; some laptops reduce performance on battery.</li>
<li>Use Ethernet or 5 GHz Wi-Fi. Close heavy browser tabs.</li>
<li>For HEVC 4K channels, make sure hardware decoding is enabled in the player.</li>
</ul>
<p>En français: <a href="/iptv-sur-pc-mac/">IPTV sur PC et Mac</a>.</p>
""",
    related=["iptv-smarters-pro-pc-mac", "watch-iptv-online"],
)

DATA["iptv-iphone"] = dict(
    add="""
<h2>iPhone IPTV tips</h2>
<ul>
<li><strong>Picture-in-picture:</strong> apps that support it let a channel float over other apps while you work.</li>
<li><strong>Cellular data:</strong> pick HD instead of 4K and use Wi-Fi when you can. Check your plan’s data allowance.</li>
<li><strong>Cast to a TV:</strong> use AirPlay to an Apple TV or compatible TV for the big screen.</li>
<li><strong>Low Power Mode</strong> can reduce video quality; turn it off for live sports.</li>
</ul>
<p>For the full list of Apple apps and a table comparing them, see <a href="/iplaytv/">iPlayTV</a>, <a href="/smarters-player-lite/">Smarters Player Lite</a> and <a href="/iptv-apple-tv/">IPTV on Apple TV</a>. TiviMate is not on iPhone: <a href="/tivimate-devices/">why and what to use</a>. En français: <a href="/iptv-sur-apple-tv-iphone/">IPTV sur iPhone</a>.</p>
""",
    related=["tivimate-devices", "iptv-sur-apple-tv-iphone"],
)

DATA["iptv-chromecast"] = dict(
    add="""
<h2>Which Chromecast do you have?</h2>
<table>
<thead><tr><th>Device</th><th>Runs apps like TiviMate?</th><th>How to watch IPTV</th></tr></thead>
<tbody>
<tr><td>Google TV Streamer</td><td>Yes (Android TV based)</td><td>Install <a href="/tivimate/">TiviMate</a> or Smarters from Google Play</td></tr>
<tr><td>Chromecast with Google TV</td><td>Yes</td><td>Same as above</td></tr>
<tr><td>Older Chromecast (no remote)</td><td>No, cast only</td><td>Cast from a phone app; quality depends on Wi-Fi</td></tr>
</tbody>
</table>
<p>For a Google TV device, follow the steps in the <a href="/iptv-android-tv/">Android TV guide</a>. If you only have a cast-only Chromecast, a Firestick is a better long-term choice: see <a href="/tivimate-firestick/">TiviMate on Firestick</a>. More: <a href="/tivimate-devices/">which devices TiviMate supports</a>.</p>
""",
    related=["tivimate-devices"],
)

DATA["iptv-devices"] = dict(
    add="""
<h2>Guides for every device</h2>
<table>
<thead><tr><th>Device</th><th>Setup guide</th><th>App guide</th></tr></thead>
<tbody>
<tr><td>Amazon Firestick</td><td><a href="/iptv-firestick/">IPTV on Firestick</a></td><td><a href="/tivimate-firestick/">TiviMate</a>, <a href="/iptv-smarters-pro-firestick/">Smarters Pro</a></td></tr>
<tr><td>Android TV, Google TV, Chromecast</td><td><a href="/iptv-android-tv/">Android TV</a>, <a href="/iptv-chromecast/">Chromecast</a></td><td><a href="/tivimate/">TiviMate</a></td></tr>
<tr><td>Samsung and LG TVs</td><td><a href="/iptv-samsung-tv/">Samsung</a>, <a href="/iptv-lg-tv/">LG</a></td><td><a href="/iptv-smarters-pro-samsung-lg/">Smarters</a>, <a href="/smartone-iptv/">SmartOne</a></td></tr>
<tr><td>Apple TV, iPhone, iPad</td><td><a href="/iptv-apple-tv/">Apple TV</a>, <a href="/iptv-iphone/">iPhone</a></td><td><a href="/iplaytv/">iPlayTV</a>, <a href="/smarters-player-lite/">Smarters Lite</a></td></tr>
<tr><td>Windows, Mac</td><td><a href="/iptv-pc-mac/">PC and Mac</a></td><td><a href="/iptv-smarters-pro-pc-mac/">Smarters Pro</a>, <a href="/vlc-iptv/">VLC</a></td></tr>
<tr><td>Roku</td><td><a href="/iptv-roku/">Roku options</a></td><td>Use a stick</td></tr>
<tr><td>Formuler, MAG boxes</td><td><a href="/formuler-iptv/">Formuler</a>, <a href="/mag-box-iptv/">MAG</a></td><td><a href="/mytvonline/">MyTVOnline</a>, <a href="/stbemu/">STBEmu</a></td></tr>
</tbody>
</table>
<p>Not sure which box to buy? Read the <a href="/iptv-box/">IPTV box guide</a>. If anything buffers, use the <a href="/iptv-buffering-fix/">buffering fixes</a>. Prefer French? <a href="/iptv-sur-smart-tv/">IPTV sur votre appareil</a>.</p>
""",
    faq=[
        ("Can I use IPTV on a TV that isn’t smart?",
         "<p>Yes. Plug a Fire TV Stick, Google TV Streamer or an Android TV box into the TV’s HDMI port and install an IPTV app on it.</p>"),
    ],
    related=["iptv-box", "iptv-buffering-fix", "tivimate-devices"],
)

DATA["iptv-firestick"] = dict(
    add="""
<h2>Firestick IPTV guides</h2>
<ul>
<li><a href="/tivimate-firestick/">TiviMate on Firestick</a>: the best-looking guide, with step-by-step install.</li>
<li><a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro on Firestick</a>: free and simple.</li>
<li><a href="/tivimate-premium/">TiviMate Premium</a>: cost and features of the paid upgrade.</li>
<li><a href="/iptv-buffering-fix/">Fix buffering</a> on a stick that stutters.</li>
</ul>

<h2>Which Firestick for IPTV?</h2>
<table>
<thead><tr><th>Model type</th><th>Good for</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Fire TV Stick 4K Max</td><td>4K sports, long channel lists</td><td>Best stick for IPTV</td></tr>
<tr><td>Fire TV Stick 4K</td><td>4K on a budget</td><td>Good all-rounder</td></tr>
<tr><td>Fire TV Stick (HD) / Lite</td><td>HD on a second TV</td><td>Trim channel groups to keep it fast</td></tr>
<tr><td>Fire TV Cube</td><td>Fastest Fire TV</td><td>Has an Ethernet port</td></tr>
<tr><td>Newer models running Vega OS</td><td>Not for sideloading</td><td>Check that the model supports Android apps</td></tr>
</tbody>
</table>
""",
    related=["tivimate-firestick", "iptv-smarters-pro-firestick", "tivimate-premium"],
)
