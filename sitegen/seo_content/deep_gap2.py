"""Gap pass, part 2: boxes, devices, comparison and trust pages."""

DATA = {}

DATA["iptv-box"] = dict(
    add="""
<h2>IPTV box, IP TV box, Android TV box: the differences</h2>
<p>“<strong>IPTV box</strong>”, “ip tv box”, “box iptv”, “tv ip box” and “iptv smart box” all describe a small set-top device that plugs into your TV and plays IPTV. There are two families:</p>
<table>
<thead><tr><th>Type</th><th>Examples</th><th>How it works</th></tr></thead>
<tbody>
<tr><td>Android TV / Google TV boxes</td><td>Nvidia Shield, Xiaomi Mi Box, Onn 4K (Walmart), generic Android boxes</td><td>You install an app such as <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">Smarters</a>. The most flexible choice. See <a href="/iptv-android-tv/">Android TV guide</a></td></tr>
<tr><td>Linux “portal” boxes</td><td><a href="/mag-box-iptv/">MAG (Infomir)</a>, <a href="/formuler-iptv/">Formuler</a> (Android, with a portal app), BuzzTV, Dreamlink</td><td>Built around a portal or app that you set up with a link or MAC address</td></tr>
<tr><td>Streaming sticks</td><td><a href="/iptv-firestick/">Amazon Firestick and Fire TV Cube</a></td><td>Cheapest and easiest; our recommendation for most people</td></tr>
</tbody>
</table>

<h2>Buying tips: Amazon, Onn, BuzzTV, Dreamlink</h2>
<ul>
<li><strong>Amazon IPTV box</strong> searches (“iptv box amazon”, “amazon iptv box”) usually lead to Fire TV devices or to generic Android boxes. A Fire TV Stick 4K or Cube is the safest buy.</li>
<li><strong>Best Android TV box for IPTV:</strong> an Nvidia Shield or a current Google TV streamer; for a budget pick the Walmart <em>Onn 4K</em> box. Look for a 4K output, 2 GB or more of RAM and Ethernet.</li>
<li><strong>BuzzTV</strong> (XRS 4500, XRS 4900), <strong>Dreamlink</strong> and “DLTA 4K” or “Global TV Box” style units are specialised set-top boxes sold to IPTV users. They can work well, but check that they are supported before buying and keep the receipt.</li>
<li><strong>Avoid</strong> any box sold with “lifetime free channels” already loaded. It is a sign of a risky seller (see <a href="/iptv-lifetime/">lifetime IPTV deals</a>).</li>
<li>Best <strong>IPTV box 4K</strong>: any box that supports HEVC and 60 fps. Read <a href="/4k-iptv/">4K IPTV requirements</a>.</li>
</ul>
<p>French speakers asking for le meilleur box IPTV: l’appareil le plus simple est la <a href="/iptv-sur-firestick/">clé Fire TV</a>. Not sure which device? Our <a href="/iptv-devices/">device comparison</a> helps you choose.</p>
""",
    faq=[("What is the best IPTV box in Canada?",
          "<p>For most people a Fire TV Stick 4K or an Nvidia Shield running <a href=\"/tivimate/\">TiviMate</a>. Portal boxes such as MAG or Formuler suit people who already own one. We test new hardware regularly and update this page.</p>")],
    related=["iptv-lifetime", "iptv-android-tv"],
)

DATA["iptv-devices"] = dict(
    add="""
<h2>Set-top box, receiver, device: what to call it</h2>
<p>An <strong>IPTV set-top box</strong> (also searched as “iptv set top box”, “set top box iptv”, “iptv receiver” and “iptv device”) is any hardware that decodes IPTV and sends it to your TV. A Firestick, an Apple TV and a MAG box are all “IPTV devices”. Your own smart TV counts too if it can run a player app. Details on specific hardware: <a href="/iptv-box/">IPTV boxes</a>, <a href="/mag-box-iptv/">MAG</a>, <a href="/formuler-iptv/">Formuler</a>, <a href="/iptv-firestick/">Firestick</a>.</p>
""",
)

DATA["mag-box-iptv"] = dict(
    add="""
<h2>MAG box models</h2>
<p>MAG boxes are made by <strong>Infomir</strong> and run a Linux-based portal system. Searches for “mag iptv”, “mag iptv box”, “mag tv box” and “infomir iptv” all point to this family. Common models:</p>
<table>
<thead><tr><th>Model</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>MAG 250, MAG 254, MAG 256</td><td>Older HD boxes, still widely used; MAG 254 is the most common</td></tr>
<tr><td>MAG 322 (and 322w1, with built-in Wi-Fi)</td><td>HD with HEVC support; “MAG 322w1” adds Wi-Fi</td></tr>
<tr><td>MAG 324, MAG 410, MAG 420</td><td>Newer generations</td></tr>
<tr><td>MAG 524, MAG 544 (“MAG box 4K”)</td><td>4K UHD models</td></tr>
</tbody>
</table>
<p>To use a MAG box you enter a portal URL into the box’s settings and give the provider the box’s MAC address, which is printed on the label. Not sure a given model is supported? <a href="/go/wa">Ask us</a> before buying. If you are choosing new hardware, a <a href="/iptv-firestick/">Firestick</a> is usually simpler and cheaper; compare in the <a href="/iptv-box/">IPTV box guide</a>.</p>
""",
)

DATA["formuler-iptv"] = dict(
    add="""
<h2>Formuler box models</h2>
<p>Formuler boxes (“box formuler”, “formuler tv box”, “formuler iptv box”) are Android-based IPTV boxes with the MyTVOnline portal app preinstalled. The line-up:</p>
<table>
<thead><tr><th>Model</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Formuler Z7 and Z7+</td><td>Older generation, 4K</td></tr>
<tr><td>Formuler Z8 and Z8 Pro (4K)</td><td>Popular middle option; Z8 Pro adds more memory</td></tr>
<tr><td>Formuler Z10 SE, Z10 Pro Max (4K)</td><td>Newest, fastest</td></tr>
<tr><td>Formuler Z Nano, Z Neo</td><td>Small and compact</td></tr>
</tbody>
</table>
<p>Because they run Android you can also install <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">Smarters</a> on them instead of the portal app. The portal route is described in <a href="/mytvonline/">MyTVOnline setup</a>.</p>
""",
)

DATA["iptv-android-tv"] = dict(
    add="""
<h2>Nvidia Shield, Mi Box, Google TV</h2>
<p>“<strong>IPTV Android TV</strong>”, “iptv google tv”, “nvidia shield iptv”, “mi box iptv” and “xiaomi iptv box” are the same job: install a player app on an Android-based device.</p>
<table>
<thead><tr><th>Device</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Nvidia Shield TV / Shield Pro</td><td>The most powerful; handles 4K and big channel lists easily</td></tr>
<tr><td>Xiaomi Mi Box S / Mi TV Stick</td><td>Cheaper; fine for HD, 4K on the Mi Box S</td></tr>
<tr><td>Google TV Streamer, Chromecast with Google TV</td><td>Works; see <a href="/iptv-chromecast/">Chromecast guide</a></td></tr>
<tr><td>Sony, Philips, TCL, Hisense Google TV sets</td><td>Install apps right on the TV, no extra box</td></tr>
</tbody>
</table>
<p>The setup is the same on all of them: <a href="/tivimate-firestick/">TiviMate</a> (the Firestick steps work unchanged) or <a href="/iptv-smarters-pro-firestick/">Smarters</a>. Android phones: <a href="/iptv-smarters-pro-download/">download guide</a>.</p>
""",
)

DATA["iptv-firestick"] = dict(
    add="""
<h2>Fire TV, Fire Stick, Amazon stick: the same device</h2>
<p>“<strong>IPTV firestick</strong>”, “iptv fire stick”, “fire tv stick iptv”, “iptv for firestick”, “iptv stick”, “iptv amazon” and “ip tv amazon” all refer to using an Amazon Fire TV device as your IPTV player. The Fire TV Stick (Lite, standard, 4K, 4K Max) and the Fire TV Cube can all do it. Pick the Stick 4K or 4K Max if you can: they handle <a href="/4k-iptv/">4K channels</a> smoothly.</p>
<h3>What is the best IPTV app for Firestick?</h3>
<p>For daily use choose <a href="/tivimate-firestick/">TiviMate</a>. Alternatives: <a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro</a>, <a href="/xciptv/">XCIPTV</a> and <a href="/smart-iptv/">Smart IPTV</a>. The old <a href="/stbemu/">STBEmu Pro</a> works too.</p>
<h3>Reddit-style advice</h3>
<p>Threads like “IPTV on Firestick reddit” mostly agree on three things: use an Ethernet adapter, don’t clog the stick with unused apps, and pick a provider with a free trial. That is also our approach. For a fair look at the forum noise see <a href="/iptv-reddit/">IPTV Reddit</a>.</p>
<p>French: <a href="/iptv-sur-firestick/">IPTV sur Fire Stick</a> (clé Amazon).</p>
""",
)

DATA["iptv-roku"] = dict(
    add="""
<h2>IPTV on Roku TV: what actually works</h2>
<p>People ask for “iptv roku”, “iptv on roku tv”, “roku tv iptv” and “roku express iptv”. Roku’s system is closed: there is no IPTV Smarters or TiviMate app on it, and Roku does not let you sideload apps the way Android does. The reliable options are:</p>
<ol>
<li><strong>Cast or mirror from a phone</strong> (Android screen mirroring to Roku, or iPhone via AirPlay on Roku models that support it).</li>
<li><strong>Add a Fire TV Stick</strong> (about the price of a lunch) to the same TV for a proper app: <a href="/iptv-firestick/">Firestick guide</a>.</li>
<li><strong>Use the TV’s own platform</strong> if your Roku is built into a TCL or Hisense TV that also offers other apps; see the <a href="/iptv-devices/">device comparison</a>.</li>
</ol>
<p>Smarters on Roku does not exist (“iptv smasters roku” searches are mixed up with the phone app): read <a href="/iptv-smarters-pro/">Smarters Pro</a> for the real device list.</p>
""",
)

DATA["iptv-iphone"] = dict(
    add="""
<h2>IPTV on iPhone and iPad</h2>
<p>Searches for “iptv iphone”, “iptv mobile” and “iptv smasters iphone” all lead to the same answer: install a player from the App Store. Good choices are <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>, GSE Smart IPTV (“gseiptv”) and Atlas Pro ONTV. Then log in with Xtream Codes (<a href="/xtream-codes-iptv/">guide</a>) or paste an M3U link (<a href="/liste-iptv-m3u/">M3U explained</a>). To watch on a big screen, use AirPlay or an <a href="/iptv-apple-tv/">Apple TV</a>. On the move, mobile data uses roughly 1 to 3 GB per hour in HD, so use Wi-Fi when you can.</p>
""",
)

DATA["iptv-chromecast"] = dict(
    add="""
<h2>Chromecast IPTV in short</h2>
<p>“Chromecast iptv”, “iptv google chromecast” and “gse iptv chromecast” differ by device. A Chromecast with Google TV is an Android TV device and can run <a href="/tivimate/">TiviMate</a> directly. An older Chromecast has no apps: you cast from a phone using an app that supports casting, such as GSE Smart IPTV or <a href="/smarters-player-lite/">Smarters Player Lite</a>. Casting uses your phone as the remote, and the phone has to stay on.</p>
""",
)

DATA["iptv-apple-tv"] = dict(
    add="""
<h2>Apple TV 4K and HD</h2>
<p>If you searched “iptv apple tv 4k”, “iptv smarters apple tv” or “iptvx apple tv”: Apple TV runs tvOS apps from the App Store. IPTV Smarters Pro, iPlayTV (<a href="/iplaytv/">iPlayTV guide</a>) and IPTVX are the usual options. TiviMate does not run on Apple TV (<a href="/tivimate-devices/">why</a>). Use a wired connection on the 4K model for best stability.</p>
""",
)

DATA["iptv-samsung-tv"] = dict(
    add="""
<h2>IPTV for Samsung TV</h2>
<p>For “iptv samsung tv” and “iptv for samsung tv”: Samsung sets use the Tizen system. Search the app store for Smarters Player Lite (<a href="/iptv-smarters-pro-samsung-lg/">full steps</a>) or Smart IPTV (<a href="/smart-iptv/">Smart IPTV guide</a>). If your TV is older than about 2017 the apps might not be available: use a <a href="/iptv-firestick/">Firestick</a> instead. French: <a href="/iptv-sur-samsung/">IPTV sur Samsung</a>.</p>
""",
)

DATA["kodi-iptv"] = dict(
    add="""
<h2>Kodi IP TV and live TV on Kodi</h2>
<p>“Kodi iptv”, “kodi ip tv”, “kodi live tv” and “kodi iptv m3u” mean setting up the <strong>PVR IPTV Simple Client</strong> add-on. In Kodi: Add-ons, My add-ons, PVR clients, PVR IPTV Simple Client, Configure, then paste your M3U link and the XMLTV guide address. Restart Kodi and Live TV appears in the main menu. For other computer options see <a href="/iptv-pc-mac/">IPTV on PC and Mac</a> and <a href="/vlc-iptv/">VLC</a>.</p>
""",
)

DATA["vlc-iptv"] = dict(
    add="""
<h2>VLC for IPTV: the quick version</h2>
<p>“Iptv vlc”, “vlc ip tv”, “iptv vlc media player” and “iptv vlc player” all describe the same trick: VLC can open an M3U link directly. Open VLC, choose Media, then Open Network Stream, paste your link, and press Play. Press Ctrl+L (Cmd+L on Mac) to show the channel list. VLC has no TV guide, so for daily viewing choose a proper player (<a href="/iptv-apps/">IPTV apps</a>). More about links: <a href="/m3u-playlist/">M3U playlists</a>.</p>
""",
)

DATA["stbemu"] = dict(
    add="""
<h2>STB Emu, STB Emu Pro and “iptv stb”</h2>
<p>“Stb emu pro”, “stbemu iptv” and “iptv stbemu” are the same Android app. It imitates a MAG box (see <a href="/mag-box-iptv/">MAG</a>) so you can use a portal link and MAC address on a phone, Android TV or Firestick. It’s a good fallback for people who already have a portal-style setup; most new users are better off with <a href="/tivimate-firestick/">TiviMate</a> or <a href="/iptv-smarters-pro-firestick/">Smarters</a>. Search “stbemu pro firestick” is answered in our <a href="/iptv-firestick/">Firestick guide</a>. The 4K stb emu version needs a 4K device.</p>
""",
)

DATA["flix-iptv"] = dict(
    add="""
<h2>Flix IPTV, FlixIPTV and “flix ip tv”</h2>
<p>These all refer to the same player app (not Netflix, despite searches such as “iptv netflix”). It logs in by code or portal and plays your subscription. Setup steps are the same as for <a href="/xciptv/">XCIPTV</a> and <a href="/iptv-smarters-pro/">Smarters</a>. See also <a href="/iptv-apps/">all IPTV apps</a>.</p>
""",
)

DATA["xciptv"] = dict(
    add="""
<h2>XCIPTV on Firestick and TV</h2>
<p>XCIPTV (also XCIPTV Pro or “xciptv tv”) runs on Android phones, Android TV and Firestick. Install it with Downloader as described in the <a href="/iptv-smarters-pro-firestick/">Firestick guide</a> and log in with Xtream Codes (<a href="/xtream-codes-iptv/">guide</a>). “XCIPTV for Firestick” is the most-searched version, and the process is just the same as for Smarters.</p>
""",
)

DATA["xtream-codes-iptv"] = dict(
    add="""
<h2>Xtream, Xtream TV and Lxtream</h2>
<p>“Xtream iptv m3u”, “xtream tv”, “xtreamtv” and “Lxtream” are names of apps and login systems built on the Xtream Codes API. An Xtream login is made of three parts: server URL, username and password. Apps like <a href="/iptv-smarters-pro/">Smarters</a> and <a href="/tivimate/">TiviMate</a> turn those into a channel list with a TV guide. Lxtream Player is one more app on Android TV that accepts the same login. If an app wants an M3U instead, see <a href="/liste-iptv-m3u/">M3U links</a>.</p>
""",
)

DATA["smartone-iptv"] = dict(
    add="""
<h2>SmartOne IPTV: generate a playlist</h2>
<p>SmartOne IPTV (searched as “smartone iptv com”, “smartone iptv generate”) is a player app that uses a code instead of a password. The app shows a MAC-address-style code on screen; you register it on the app’s website and add your playlist. If you are stuck at the generate step, check the app’s help page or <a href="/go/wa">message us</a> with the code. Other apps with simpler login: <a href="/iptv-apps/">IPTV apps</a>.</p>
""",
)

DATA["iplaytv"] = dict(
    add="""
<h2>iPlayTV on iPhone, Apple TV and Android</h2>
<p>iPlayTV (“iplay iptv”) began on Apple devices; “iplaytv android” refers to its Android version. It loads M3U links and Xtream logins. For Apple TV and iPhone setup see <a href="/iptv-apple-tv/">IPTV on Apple TV</a> and <a href="/iptv-iphone/">iPhone</a>. French: <a href="/iptv-sur-apple-tv-iphone/">IPTV sur Apple TV et iPhone</a>.</p>
""",
)

DATA["implayer"] = dict(
    add="""
<h2>IMPlayer</h2>
<p>IMPlayer (“implayer tv”) is a free IPTV player for Android TV, Firestick and Samsung. If it isn’t working or can’t find a playlist, the usual cause is a mistyped login. Compare with other <a href="/iptv-apps/">IPTV apps</a>.</p>
""",
)

DATA["plex-iptv"] = dict(
    add="""
<h2>M3U on Plex</h2>
<p>Plex does not read an M3U link on its own. Searches for “m3u plex” and “plex iptv m3u” are normally answered by a bridge tool that converts the M3U into a tuner Plex can see, or by using Plex only for your own library and a normal player for IPTV. Keep it simple: use <a href="/tivimate/">TiviMate</a> for live TV. Prefer an open-source server? See <a href="/jellyfin-iptv/">Jellyfin</a>, which also covers Emby.</p>
""",
)

DATA["jellyfin-iptv"] = dict(
    add="""
<h2>Jellyfin and Emby with IPTV</h2>
<p>“Jellyfin iptv” and “emby iptv” both use the server’s Live TV feature: you add an M3U tuner and an XMLTV guide in the admin dashboard. Emby needs Emby Premiere for Live TV; Jellyfin includes it free. For a simpler setup see <a href="/stremio-iptv/">Stremio</a> or a standard <a href="/iptv-apps/">IPTV app</a>.</p>
""",
)

DATA["stremio-iptv"] = dict(
    add="""
<h2>Stremio IPTV in brief</h2>
<p>“Stremio iptv” means loading an M3U playlist as an add-on so live channels appear beside movies and series. It works but with a rough channel experience. For live TV daily, use <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">Smarters</a>.</p>
""",
)
