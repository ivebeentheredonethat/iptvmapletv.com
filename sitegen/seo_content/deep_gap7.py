"""Gap pass, part 7 (2026-10-05): what was still left after expansion passes 1 and 2 when both keyword files were re-checked.

Mostly device model numbers (MAG, Formuler, BuzzTV), player names (Smart STB) and generic queries that the keyword map had
filed with "other brands" because no rule matched them ("paid iptv", "isp iptv", "iptv wifi", "xtream iptv pc").
Box facts were checked on Infomir's and Formuler's own product pages and on retailer listings on 2026-10-05.
"""

UPDATED = "2026-10-05"
DATA = {}

DATA["mag-box-iptv"] = dict(updated=UPDATED, add="""
<h2>Every MAG model, by generation</h2>
<p>Infomir (the “IM Infomir” logo on the box) has made MAG set-top boxes for years, and most generations still work with IPTV portals. The model number tells you whether the box is Linux or Android, and whether it does 4K:</p>
<table>
<thead><tr><th>Model</th><th>System</th><th>Picture</th><th>How to connect IPTVMaple</th></tr></thead>
<tbody>
<tr><td>MAG540w3 / MAG544w3</td><td>Linux</td><td>4K, AV1, Wi-Fi</td><td>Portal URL + MAC address (steps above)</td></tr>
<tr><td>MAG520 / MAG520w3</td><td>Linux</td><td>4K HDR, HEVC; Wi-Fi on the w3</td><td>Portal URL + MAC address</td></tr>
<tr><td>MAG524 / MAG524w3</td><td>Linux</td><td>4K HDR, HEVC; dual-band Wi-Fi on the w3</td><td>Portal URL + MAC address</td></tr>
<tr><td>MAG424 / MAG424w3</td><td>Linux</td><td>4K, HEVC; Wi-Fi on the w3</td><td>Portal URL + MAC address</td></tr>
<tr><td>MAG425A</td><td>Android TV (Google certified)</td><td>4K, HEVC, Chromecast built in</td><td>Install TiviMate or IPTV Smarters from Google Play and log in</td></tr>
<tr><td>MAG555</td><td>Google TV</td><td>4K, HEVC and AV1</td><td>Install TiviMate or IPTV Smarters from Google Play and log in</td></tr>
<tr><td>MAG322 / MAG322w1 / MAG324</td><td>Linux</td><td>Full HD</td><td>Portal URL + MAC address</td></tr>
<tr><td>MAG254 / MAG256 / MAG250</td><td>Linux</td><td>HD</td><td>Portal URL + MAC address</td></tr>
</tbody>
</table>
<p>The “w” models (w1, w3) are the same box with built-in Wi-Fi. Infomir lists the 520, 524 and 424 families as discontinued, but they are still sold second-hand and work the same way. On the two Android models the portal method does not apply: you use an <a href="/iptv-apps/">IPTV app</a> as on any <a href="/iptv-android-tv/">Android TV box</a>.</p>
""", faq=[
    ("Is the MAG 524w3 good for IPTV?", "<p>Yes. It is a 4K HDR Linux box with HEVC support and dual-band Wi-Fi. Send us its MAC address, enter the portal URL we give you, and it loads live TV, the guide and on-demand video.</p>"),
    ("What is the difference between MAG 520 and MAG 524?", "<p>Both are 4K Linux boxes on the same Amlogic chip with the same portal setup. For IPTV they behave the same; buy whichever is cheaper and in good condition, ideally the w3 version if you need Wi-Fi.</p>"),
    ("Is the MAG 425A Android?", "<p>Yes. The MAG425A runs Android TV with Google Play, so you install an IPTV app such as TiviMate or IPTV Smarters instead of using a portal.</p>"),
], keywords_add=["mag520", "mag 520", "mag520w3", "mag 520w3", "mag524", "mag524w3", "mag 524w3", "mag424w3", "mag 424w3",
                 "mag425a", "mag 425a", "mag 540", "mag 544", "mag555"])

DATA["formuler-iptv"] = dict(updated=UPDATED, add="""
<h2>Older Formuler boxes: Z+ Neo and ZX</h2>
<p>Two compact models are still common in Canadian homes. Both are 4K Android boxes with Formuler’s MyTVOnline app preinstalled, and both work with IPTVMaple through the portal (MAC address) or an Xtream Codes login.</p>
<table>
<thead><tr><th>Model</th><th>System</th><th>Memory</th><th>Network</th><th>IPTV app</th></tr></thead>
<tbody>
<tr><td>Formuler Z+ Neo</td><td>Android, 4K HDR10 / HLG</td><td>1 GB RAM, 4 GB storage</td><td>Ethernet and 2.4 GHz Wi-Fi</td><td>MyTVOnline 2</td></tr>
<tr><td>Formuler ZX</td><td>Android 7, 4K HDR10 / HLG</td><td>1 GB RAM, 8 GB storage</td><td>Ethernet</td><td>MyTVOnline</td></tr>
</tbody>
</table>
<p>With 1 GB of memory, these boxes are slower with very large channel lists. Hide the channel groups you never watch in MyTVOnline, use the Ethernet port, and they remain perfectly usable for a second TV. For a main TV, a current Z11 model is a big step up.</p>
""", faq=[
    ("Does the Formuler Z+ work with IPTVMaple?", "<p>Yes. Open MyTVOnline 2, send us the MAC address shown on screen, and add the portal we send you, or log in with Xtream Codes. Use Ethernet: the Z+ Neo’s Wi-Fi is 2.4 GHz only.</p>"),
    ("Is the Formuler ZX still good for IPTV?", "<p>It still works, with MyTVOnline and 4K output. It is an older Android 7 box with 1 GB of memory, so large channel lists load more slowly than on a Z11.</p>"),
], keywords_add=["formuler z+", "formuler z plus", "formuler z+ neo", "formuler zx"])

DATA["stbemu"] = dict(updated=UPDATED, add="""
<h2>Smart STB: the MAG portal on Samsung and LG TVs</h2>
<p>STBEmu runs on Android only. If your TV is a Samsung (Tizen) or LG (webOS) and your login is a MAG-style portal, the app people use is <strong>Smart STB</strong>. It does the same job as STBEmu: it imitates a MAG box in software.</p>
<ol>
<li>Install Smart STB from your TV’s app store (it is also on Android TV and Fire TV).</li>
<li>Open it and note the virtual <strong>MAC address</strong> it shows. Send it to us so we can activate it.</li>
<li>In the app’s settings, enter the <strong>portal URL</strong> we send you and restart the app.</li>
</ol>
<p>Smart STB is a paid app with a trial; the fee goes to its developer, not to IPTVMaple. If you don’t specifically want the MAG look, you don’t need it: on a Samsung or LG TV, an app that takes an Xtream Codes login, such as <a href="/iptv-smarters-pro-samsung-lg/">IPTV Smarters</a>, is simpler and free to try.</p>
""", faq=[
    ("What is Smart STB?", "<p>A paid app for Samsung, LG, Android TV and Fire TV that emulates a MAG set-top box. It shows a virtual MAC address and connects to a portal URL, like STBEmu does on Android.</p>"),
], keywords_add=["smart stb", "smart stb app", "smart stb samsung", "smart stb lg"])

DATA["iptv-box"] = dict(updated=UPDATED, add="""
<h2>Buying an IPTV box on Amazon, AliExpress, Alibaba or eBay</h2>
<p>Marketplaces sell three very different things under the words “IPTV box”, and only one is worth buying:</p>
<table>
<thead><tr><th>Listing</th><th>What it is</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Branded device (Fire TV, onn, Nvidia Shield, Formuler, MAG, BuzzTV XRS 4500)</td><td>A known box with updates and support from the maker</td><td>Good buy; add your own IPTV subscription</td></tr>
<tr><td>Unbranded Android box on AliExpress or Alibaba</td><td>Cheap hardware, often without Google certification or updates; specs on the listing are not always accurate</td><td>Works for some, but expect slower menus and no Google Play</td></tr>
<tr><td>“Fully loaded” or “lifetime channels” box on eBay or Facebook</td><td>A box with an unknown service pre-installed</td><td>Avoid: the channels usually stop and there is no one to contact</td></tr>
</tbody>
</table>
<p>For reference, the BuzzTV XRS 4500 is an Android 9 box on an Amlogic S905X3 chip with 4 GB of memory and 64 GB of storage, sold through Canadian retailers. If you buy an unbranded box, check that it shows the Android version and Google Play in its settings, and keep the receipt in case it can’t install the player you want.</p>
""", faq=[
    ("Is it safe to buy an IPTV box on AliExpress?", "<p>The box itself is usually just an Android device. The risk is accuracy and support: specs can be overstated and updates rare. A branded box from a Canadian retailer costs a bit more but installs IPTV apps without trouble.</p>"),
    ("What is a fully loaded IPTV box?", "<p>A box sold with channels already installed from a service you don’t choose or know. When that service stops, the box shows nothing and the seller can’t help. Buy a plain device and pick your own subscription instead.</p>"),
], keywords_add=["buzztv xrs4500", "buzztv xrs 4500", "iptv aliexpress", "aliexpress iptv box", "alibaba iptv", "ebay iptv",
                 "iptv box fully loaded", "fully loaded iptv box"])

DATA["4k-iptv"] = dict(updated=UPDATED, add="""
<h2>4K OTT IPTV, IP TV 4K, IPTV 8K: same thing, different labels</h2>
<p>“OTT” (over the top) just means the stream reaches you over the open internet instead of a cable company’s private network, which is how all independent IPTV works. So “4K OTT IPTV”, “IP TV 4K” and “IPTV 4K OTT” describe the same service: 4K channels streamed over your normal internet connection. Searches for “IPTV 8K” or “iptv8k” are mostly provider names; there are no regular 8K live channels to stream, and 4K is the top quality on any IPTV service today, including ours.</p>
""", keywords_add=["4k ott iptv", "iptv 4k ott", "ip tv 4k", "iptv 8k", "iptv8k"])

DATA["what-is-iptv"] = dict(updated=UPDATED, add="""
<h2>ISP IPTV vs internet IPTV</h2>
<p>When an internet provider delivers TV over its own network, as Bell Fibe TV and Telus Optik TV do, that is <strong>ISP IPTV</strong>: it works only on that company’s connection and set-top box. Independent services such as IPTVMaple are <strong>internet (OTT) IPTV</strong>: the stream travels over any internet connection, so it works with whichever provider you already have and on devices you choose. Both are “IPTV live TV”; the difference is who owns the network and how many devices you can use.</p>
""", keywords_add=["isp iptv", "iptv live tv", "ip tv live"])

DATA["iptv-buffering-fix"] = dict(updated=UPDATED, faq=[
    ("Does IPTV work well over Wi-Fi?", "<p>Yes, if the signal is strong. IPTV over Wi-Fi is the most common cause of freezing when the device is far from the router or on the crowded 2.4 GHz band. Use 5 GHz Wi-Fi, move the router closer or add a mesh point, or connect by Ethernet for the most stable picture.</p>"),
], keywords_add=["iptv wifi", "iptv over wifi"])

DATA["best-iptv-canada"] = dict(updated=UPDATED, faq=[
    ("Is paid IPTV better than free IPTV?", "<p>Free IPTV lists are usually collected from public links that stop working, with no guide and no support. The best paid IPTV gives you a stable server, a TV guide, on-demand video and someone to contact. Test that with a free trial before paying, as with our <a href=\"/try-iptv-canada/\">24-hour trial</a>.</p>"),
], keywords_add=["paid iptv", "best paid iptv"])

DATA["xtream-codes-iptv"] = dict(updated=UPDATED, add="""
<h2>Xtream IPTV on a PC</h2>
<p>To use an Xtream login on a Windows PC or Mac, install a desktop player that accepts it: <a href="/iptv-smarters-pro-pc-mac/">IPTV Smarters for Windows and macOS</a> takes the server, username and password directly. Players that only read playlists, such as <a href="/myiptv-player/">MyIPTV Player</a> or <a href="/vlc-iptv/">VLC</a>, use the M3U link we send alongside the Xtream details; it carries the same channels.</p>
""", keywords_add=["xtream iptv pc", "xtream iptv for pc"])

DATA["xciptv"] = dict(updated=UPDATED, faq=[
    ("Can I install XCIPTV on a Samsung TV?", "<p>No. XCIPTV is an Android app, and Samsung TVs run Tizen, which can’t install Android apps. Use a Samsung app such as <a href=\"/iptv-smarters-pro-samsung-lg/\">IPTV Smarters</a> or <a href=\"/smartone-iptv/\">SmartOne</a>, or plug a Fire TV Stick into the TV and install XCIPTV there.</p>"),
], keywords_add=["xciptv samsung"])

DATA["iptvx"] = dict(updated=UPDATED, faq=[
    ("Is “IPTV X” the same app as IPTVX?", "<p>Yes. The app is written IPTVX in the App Store, but people often search for it as “IPTV X” or “X IPTV”. Look for the listing from Bending X.</p>"),
], keywords_add=["iptv x", "x iptv"])

DATA["ss-iptv"] = dict(updated=UPDATED, faq=[
    ("Is SSIPTV the same as SS IPTV?", "<p>Yes. SSIPTV, SS IPTV and Simple Smart IPTV are the same app. The setup above applies whichever name your TV’s store shows.</p>"),
])

DATA["set-iptv"] = dict(updated=UPDATED, faq=[
    ("Is “SET IP TV” a different app?", "<p>No. SET IP TV and SET IPTV are the same player; only the spelling differs. Follow the MAC-address steps above.</p>"),
])

DATA["gse-smart-iptv"] = dict(updated=UPDATED, faq=[
    ("What is GSEIPTV?", "<p>Just GSE Smart IPTV written as one word. It is the same player from GSE Technology, and the setup steps on this page apply.</p>"),
])

# Spelling variants the keyword map sent to the general Smarters page although a dedicated page answers them.
DATA["iptv-smarters-pro-firestick"] = dict(updated=UPDATED, keywords_add=["iptv smarters fire stick", "iptv smarters pro fire stick"])
DATA["iptv-smarters-pro-pc-mac"] = dict(updated=UPDATED, keywords_add=["iptv smarters pro macbook"])
