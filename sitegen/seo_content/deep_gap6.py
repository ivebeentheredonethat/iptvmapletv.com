"""Gap pass, part 6 (2026-10-04, SEO master prompt v3): device models and Balkan search terms that the v2 keyword map had
filed as "other brands". Box facts were checked on the makers' or established retailers' pages on 2026-10-04."""

UPDATED = "2026-10-04"
DATA = {}

DATA["iptv-box"] = dict(updated=UPDATED, add="""
<h2>IPTV box models people ask about</h2>
<p>Box names come up in searches far more often than the systems they run. What matters for IPTV is the system: an <strong>Android or Google TV</strong> box takes the same apps as any Android TV device, while a <strong>Linux</strong> box uses its own built-in player or a portal linked to its MAC address, like a <a href="/mag-box-iptv/">MAG box</a>.</p>
<table>
<thead><tr><th>Model</th><th>System</th><th>How to use it with IPTVMaple</th></tr></thead>
<tbody>
<tr><td>onn 4K / 4K Pro (Walmart)</td><td>Google TV</td><td>TiviMate or Smarters from Google Play: see the <a href="/onn-tv-box-iptv/">onn TV box guide</a></td></tr>
<tr><td>Homatics Box Q</td><td>Android TV with Google certification</td><td>Install TiviMate or Smarters from Google Play</td></tr>
<tr><td>Ugoos AM7</td><td>Android TV 11 (Amlogic S905X4, Wi-Fi 6)</td><td>Install TiviMate or Smarters from Google Play</td></tr>
<tr><td>Dreamlink T2 / T3</td><td>Android</td><td>Install an Android player such as <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> and add your Xtream login</td></tr>
<tr><td>Formuler Z11 / Z11 Pro Max</td><td>Android with MyTVOnline</td><td><a href="/mytvonline/">MyTVOnline 3</a> with your Xtream login: see <a href="/formuler-iptv/">Formuler</a></td></tr>
<tr><td>TVIP S-Box v.605</td><td>Dual system: Linux and Android</td><td>Linux mode: portal linked to the box’s MAC address (send us the MAC); Android mode: an Android player</td></tr>
<tr><td>Xsarius Sniper 4K</td><td>Linux</td><td>Built-in IPTV player; ask us on WhatsApp which login type to enter</td></tr>
<tr><td>Amiko A9 range</td><td>Android</td><td>Install an Android player and add your Xtream login</td></tr>
<tr><td>MAG 322 / 424 / 524</td><td>Linux (Infomir)</td><td>Portal URL + MAC address: see <a href="/mag-box-iptv/">MAG box IPTV</a></td></tr>
</tbody>
</table>
<p>If your box isn’t listed, check its settings for the system name. Android boxes that aren’t Google-certified may lack Google Play; install the player from the developer’s website with the Downloader app instead. Avoid boxes sold “fully loaded” with channels: you are paying for an unknown service you can’t contact when it stops.</p>
""", faq=[
    ("Which IPTV box should I buy in Canada?", "<p>A Google-certified Android TV or Google TV box with Ethernet, such as an Nvidia Shield, Homatics Box Q or Google TV Streamer, gives you Google Play and TiviMate. A Fire TV Stick 4K is the cheapest good option.</p>"),
    ("Does a TVIP box work with IPTVMaple?", "<p>Yes. In Linux mode it connects with a portal linked to the box’s MAC address, which we activate; in Android mode you install an Android player and log in.</p>"),
], keywords_add=["tvip s box", "tvip s box 605", "tvip 605", "tvip s box v 605", "tvip s box v 525", "ugoos am7", "homatics box q",
                 "dreamlink t2", "dreamlink t3", "dreamlink box", "xsarius sniper", "xsarius sniper 4k", "amiko a9 green", "amiko a6n",
                 "global tv box", "dlta 4k", "dlta 4k iptv", "box tv iptv", "tv ip box"])

DATA["ex-yu-iptv"] = dict(updated=UPDATED, add="""
<h2>IPTV ponuda: what the subscription includes</h2>
<p>Searching for an <strong>IPTV ponuda</strong> (IPTV offer) or <strong>IPTV televizija</strong> from Canada? With IPTVMaple one subscription carries the Ex-YU channels listed above together with Canadian, US and other international channels. There is no separate Balkan package to add.</p>
<ul>
<li><strong>IPTV kanali</strong>: the Ex-YU group in our channel list holds the Serbian, Croatian, Bosnian and regional sports channels; the full list is on the <a href="/channels-list/">channels page</a>.</li>
<li><strong>Uređaji (devices)</strong>: a <a href="/iptv-firestick/">Fire TV Stick</a>, an Android TV box, a <a href="/iptv-samsung-tv/">Samsung</a> or LG smart TV, a phone or a computer.</li>
<li><strong>Probni period (trial)</strong>: 24 hours free, no card needed: <a href="/try-iptv-canada/">start the trial</a>.</li>
<li><strong>Cijene (prices)</strong>: the same plans as every customer, from 1 to 12 months: <a href="/iptv-plans-canada/">see plans</a>.</li>
</ul>
""", faq=[
    ("Koliko košta IPTV ponuda?", "<p>Ex-YU kanali su uključeni u svaki IPTVMaple paket, bez doplate. Cijene za 1, 6 i 12 mjeseci su na stranici s paketima, a probni period od 24 sata je besplatan.</p>"),
], keywords_add=["iptv ponuda", "iptv televizija", "ip televizija iptv", "balkan iptv canada"])

DATA["iptv-iphone"] = dict(updated=UPDATED, add="""
<h2>Full guides for the main iPhone players</h2>
<p>Two of the players above now have their own step-by-step pages: <a href="/iptvx/">IPTVX</a> (iPhone, iPad, Apple TV and Mac, synced with iCloud) and <a href="/gse-smart-iptv/">GSE Smart IPTV</a> (with Chromecast and AirPlay casting).</p>
""")

DATA["iptv-apps"] = dict(updated=UPDATED, add="""
<h2>More player guides</h2>
<ul>
<li><a href="/ott-navigator/">OTT Navigator</a>: Android player with catch-up, timeshift and a strong movies library.</li>
<li><a href="/iptvx/">IPTVX</a>: the most polished player across Apple devices.</li>
<li><a href="/gse-smart-iptv/">GSE Smart IPTV</a>: veteran player on iPhone, Apple TV and Android.</li>
<li><a href="/purple-iptv/">Purple IPTV players</a>: Android and Samsung TV players.</li>
<li><a href="/iptv-checker/">IPTV checker</a>: see what an M3U playlist contains before loading it.</li>
</ul>
""")
