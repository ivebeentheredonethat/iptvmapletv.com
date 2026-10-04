"""Expansion pass (2026-10-04): pages for keyword clusters from the worldwide keyword file that had no page of their own.

Smart TV player apps (SS IPTV, SET IPTV, Duplecast, Nanomid, Lazy IPTV), an English smart TV pillar, buying/comparison guides
(Pluto TV, satellite, Starlink, your IPTV account, recording and catch-up, HBO and premium movie channels) and German IPTV.
Facts about third-party apps come from their own websites; IPTVMaple facts (prices, trial, refund, login delivery) from the site.
"""
from ._util import price_range
from .international import community

D = dict(published="2026-10-04", updated="2026-10-04")
LOW, PER_MONTH = price_range()

APPS = [
    # ------------------------------------------------------------------ SS IPTV
    dict(
        slug="ss-iptv", hub="apps", **D,
        title="SS IPTV Setup Guide: Load Your Playlist on a Smart TV | IPTVMaple",
        description="SS IPTV (Simple Smart IPTV) setup for LG, Samsung and other smart TVs: external playlist links, the connection code, limits and fixes. Try IPTVMaple free 24h.",
        kicker="IPTV apps", h1='<span class="grad-text">SS IPTV</span> setup guide for smart TVs',
        lead="SS IPTV is one of the oldest free players for smart TVs. Here is how to load your playlist the right way, and when another app is the better pick.",
        crumb="SS IPTV", blurb="Simple Smart IPTV: playlist link or connection code.",
        answer="<p><strong>SS IPTV</strong> (Simple Smart IPTV) is a free IPTV player for smart TVs such as LG and Samsung. It does not include channels: you add your provider’s <strong>M3U playlist</strong>, either as an <strong>external playlist link</strong> in the app’s settings or by uploading a file with a temporary <strong>connection code</strong> on the SS IPTV website. It works with the M3U link IPTVMaple sends after your order or free trial.</p>",
        body="""
<h2>What SS IPTV is (and isn’t)</h2>
<p>SS IPTV is a player app. Like every IPTV player, it shows channels from a playlist you supply; it never comes with TV channels of its own. The developer documents installation on LG, Samsung, Sony and Philips smart TVs, and the app is also found on Android. It reads M3U playlists, which is exactly what we send you, so there is nothing extra to buy from us to use it.</p>

<h2>Two ways to add your IPTV playlist</h2>
<table>
<thead><tr><th></th><th>External playlist (link)</th><th>Internal playlist (connection code)</th></tr></thead>
<tbody>
<tr><td>What you enter</td><td>The M3U URL we send you</td><td>An M3U file uploaded on the SS IPTV website</td></tr>
<tr><td>Where</td><td>Settings → Content → External playlists</td><td>Settings → General → Get code, then the website’s playlist page</td></tr>
<tr><td>How many</td><td>As many as you like</td><td>One for live TV and one for video on demand</td></tr>
<tr><td>Formats</td><td>m3u, xspf, asx, pls</td><td>m3u only (UTF-8)</td></tr>
<tr><td>Best for</td><td>IPTV subscriptions: the list updates itself</td><td>A fixed file you edited yourself</td></tr>
</tbody>
</table>
<p>For a subscription, always use the <strong>external playlist link</strong>. A link stays up to date when channels change; an uploaded file is a snapshot that goes stale.</p>

<h2>Step-by-step: SS IPTV with IPTVMaple</h2>
<ol>
<li>Install <strong>SS IPTV</strong> from your TV’s app store and open it.</li>
<li>Go to <strong>Settings → Content → External playlists</strong> and choose <strong>Add</strong>.</li>
<li>Give it a name (for example “IPTVMaple”) and paste the <strong>M3U link</strong> from our email or WhatsApp message. Typing it with the remote is fiddly, so take your time with capitals and symbols.</li>
<li>Save. A new tile appears on the home screen; open it to load your channels.</li>
<li>Add the EPG link we send you in the app’s settings if the TV guide is empty.</li>
</ol>
<p>On some TV models the external playlist is fetched through the SS IPTV server, so the link must be reachable from the internet. Our links are, so this needs no change on your side.</p>

<h2>Using the connection code</h2>
<p>The code shown under <em>Settings → General → Get code</em> links your TV to the SS IPTV website for uploading a file. It is not permanent: the developer says it works for 24 hours, or until you generate a new one. If the website rejects your code, generate a fresh one on the TV and try again.</p>

<h2>Common SS IPTV problems</h2>
<ul>
<li><strong>“Playlist can’t be loaded”</strong>: re-check the link character by character, or send us a photo of the screen on WhatsApp.</li>
<li><strong>Channels load but don’t play</strong>: restart the TV and router; if it persists, see our <a href="/iptv-buffering-fix/">buffering and playback fixes</a>.</li>
<li><strong>No movies or series section</strong>: SS IPTV is built mainly for live channels. For a full on-demand library, try <a href="/smartone-iptv/">SmartOne IPTV</a> or <a href="/duplecast/">Duplecast</a>.</li>
</ul>

<h2>SS IPTV vs other smart TV players</h2>
<p>SS IPTV is a sensible free starting point. If you want a cable-style guide, catch-up and a movies section, the paid players such as <a href="/set-iptv/">SET IPTV</a>, <a href="/duplecast/">Duplecast</a> or <a href="/smart-iptv/">Smart IPTV</a> are usually smoother, and a <a href="/iptv-firestick/">Fire TV Stick</a> with TiviMate is smoother still. Our <a href="/iptv-smart-tv/">smart TV IPTV guide</a> compares the options by TV brand.</p>
""",
        faq=[
            ("Is SS IPTV free?", "<p>The SS IPTV app itself is free to install. It doesn’t include channels: you add the playlist from your IPTV subscription, such as the M3U link IPTVMaple sends you.</p>"),
            ("Does SS IPTV work with IPTVMaple?", "<p>Yes. Add the M3U link we send you as an external playlist under Settings → Content. Our free 24-hour trial lets you test it on your TV first.</p>"),
            ("How long is the SS IPTV connection code valid?", "<p>According to the developer, the code works for 24 hours or until you generate a new one. You only need it to upload a playlist file, not for a playlist link.</p>"),
            ("Can SS IPTV use Xtream Codes logins?", "<p>SS IPTV works with playlist links and files (M3U and similar formats). Use the M3U link from your IPTVMaple welcome message.</p>"),
            ("Why does SS IPTV show only one playlist tile?", "<p>Each external playlist becomes its own tile. If you added the link as an internal playlist instead, it replaces the previous one; use External playlists to keep several.</p>"),
        ],
        related=["smart-iptv", "set-iptv", "iptv-lg-tv", "iptv-smart-tv"],
        keywords=["ssiptv", "ss iptv", "ssiptv android", "ssiptv list", "ssiptv com", "ss iptv app", "simple smart iptv"],
    ),
    # ------------------------------------------------------------------ SET IPTV
    dict(
        slug="set-iptv", hub="apps", **D,
        title="SET IPTV Setup: Upload Your Playlist by MAC Address | IPTVMaple",
        description="Set up SET IPTV on a Samsung, LG or Android TV: find the MAC address, upload your M3U or Xtream login on the SET IPTV website and fix common errors. Try free.",
        kicker="IPTV apps", h1='<span class="grad-text">SET IPTV</span>: setup by MAC address',
        lead="SET IPTV skips typing on the TV: you send your playlist to the TV from a phone or computer. Here is the full process.",
        crumb="SET IPTV", blurb="Upload your playlist to the TV by MAC address.",
        answer="<p><strong>SET IPTV</strong> is a paid IPTV player for smart TVs and Android devices. You install it on the TV, note the <strong>MAC address</strong> it shows, then enter that MAC with your <strong>M3U link or Xtream Codes login</strong> on the official SET IPTV upload page. After a 7-day trial the app needs a one-time activation paid to its developer. It doesn’t include channels; it plays the IPTVMaple playlist you add.</p>",
        body="""
<h2>How SET IPTV works</h2>
<p>SET IPTV identifies your TV by its MAC address. Instead of typing a long link with the remote, you link your playlist to that MAC on the SET IPTV website (setsysteme.com) from any browser. The TV downloads it the next time the app starts. The approach is the same as <a href="/smart-iptv/">Smart IPTV</a>, which is why the two names are often confused.</p>

<h2>Step-by-step: SET IPTV with IPTVMaple</h2>
<ol>
<li>Install <strong>SET IPTV</strong> from your TV’s app store (on Android devices, from the developer’s link).</li>
<li>Open it and write down the <strong>MAC address</strong> on screen.</li>
<li>On your phone or computer, open the playlist upload page on the official SET IPTV website.</li>
<li>Enter the MAC address, then either paste the <strong>M3U link</strong> or fill in the <strong>Xtream Codes</strong> server, username and password we sent you.</li>
<li>Complete the captcha, send, and restart the app on the TV.</li>
</ol>

<h2>M3U link or Xtream Codes?</h2>
<table>
<thead><tr><th></th><th>M3U link</th><th>Xtream Codes login</th></tr></thead>
<tbody>
<tr><td>Setup</td><td>One URL to paste</td><td>Server, username, password</td></tr>
<tr><td>TV guide (EPG)</td><td>May not load the full guide</td><td>Loads the guide automatically</td></tr>
<tr><td>Movies and series</td><td>Mixed into the list</td><td>Separate sections</td></tr>
</tbody>
</table>
<p>We recommend the Xtream Codes option when SET IPTV offers it: the guide and the movies and series sections come out cleaner.</p>

<h2>Trial and activation</h2>
<p>SET IPTV gives you a 7-day trial, then asks for a one-time activation per device, paid on the developer’s website. That fee goes to the app developer, not to IPTVMaple, and is separate from your channel subscription. Test the app during the trial together with our <a href="/try-iptv-canada/">free 24-hour IPTV trial</a> before paying for either.</p>

<h2>Fixing common SET IPTV errors</h2>
<ul>
<li><strong>“No playlist”</strong> after uploading: restart the app fully, or switch the TV off at the wall for a minute.</li>
<li><strong>Wrong MAC</strong>: some TVs show different MACs for Wi-Fi and Ethernet. Use the one the app displays.</li>
<li><strong>Channels freeze</strong>: SET IPTV runs on the TV’s own processor and Wi-Fi. A wired connection helps; see <a href="/iptv-buffering-fix/">IPTV buffering fixes</a>.</li>
</ul>

<h2>Alternatives to SET IPTV</h2>
<p>If SET IPTV isn’t in your TV’s store, <a href="/duplecast/">Duplecast</a>, <a href="/smartone-iptv/">SmartOne IPTV</a> and <a href="/flix-iptv/">Flix IPTV</a> work the same way. For the full list by TV brand, see <a href="/iptv-smart-tv/">IPTV on a smart TV</a>.</p>
""",
        faq=[
            ("Is SET IPTV free?", "<p>It has a 7-day free trial. After that the developer charges a one-time activation per device on its website. IPTVMaple doesn’t sell or charge for the activation.</p>"),
            ("Where do I upload my playlist for SET IPTV?", "<p>On the playlist upload page of the official SET IPTV website (setsysteme.com). Enter the MAC address shown on your TV, then your M3U link or Xtream login.</p>"),
            ("Does SET IPTV provide channels?", "<p>No. SET IPTV is only a player. Channels come from your IPTV subscription, such as IPTVMaple.</p>"),
            ("Why is the TV guide empty in SET IPTV?", "<p>An M3U upload may not bring the full guide. Re-upload using the Xtream Codes option, or add the EPG link we sent you.</p>"),
            ("Is SET IPTV the same as Smart IPTV?", "<p>No. They are different apps from different developers, but both link your playlist to the TV’s MAC address on a website.</p>"),
        ],
        related=["smart-iptv", "ss-iptv", "duplecast", "iptv-samsung-tv"],
        keywords=["set iptv", "set ip tv", "setiptv", "set iptv app", "set iptv mac"],
    ),
    # ------------------------------------------------------------------ Duplecast
    dict(
        slug="duplecast", hub="apps", **D,
        title="Duplecast IPTV Player: Setup, Activation & Devices | IPTVMaple",
        description="Duplecast IPTV player setup on Samsung, LG, VIDAA, Android TV and Fire TV: add your playlist, the 15-day trial, Device ID and key activation. Try IPTVMaple free.",
        kicker="IPTV apps", h1='<span class="grad-text">Duplecast</span> IPTV player setup',
        lead="One player for almost every TV, including Hisense VIDAA models that few IPTV apps support. Here is how to set it up.",
        crumb="Duplecast", blurb="A player for Samsung, LG, VIDAA and Android TVs.",
        answer="<p><strong>Duplecast</strong> is an IPTV media player for Samsung, LG, Hisense VIDAA, Android TV, Google TV and Amazon Fire TV. You add your playlist as an <strong>M3U link or Xtream Codes login</strong>, try every feature free for <strong>15 days</strong>, then activate a licence on the Duplecast website with the <strong>Device ID and Device Key</strong> shown in the app. Duplecast doesn’t provide channels; it plays the IPTVMaple login you add.</p>",
        body="""
<h2>Why people choose Duplecast</h2>
<ul>
<li><strong>Wide device support</strong>: the developer lists Samsung, LG, VIDAA, Android TV, Google TV and Fire TV, so one app can cover a mixed household.</li>
<li><strong>Hisense VIDAA</strong>: many IPTV players aren’t available on VIDAA, which makes Duplecast one of the few direct options for those TVs.</li>
<li><strong>Xtream Codes support</strong>: live TV, movies and series appear in separate sections.</li>
<li><strong>Free trial</strong>: 15 days with every feature, no credit card.</li>
</ul>

<h2>Step-by-step: Duplecast with IPTVMaple</h2>
<ol>
<li>Install <strong>Duplecast</strong> from your TV’s app store (or Google Play / Amazon Appstore).</li>
<li>Open the app and choose <strong>Add a playlist</strong>.</li>
<li>Pick <strong>Xtream Codes</strong> and enter the server URL, username and password we sent you, or choose M3U and paste the link.</li>
<li>Wait for channels, guide and on-demand content to load, then add favourites.</li>
</ol>

<h2>Activating Duplecast after the trial</h2>
<ol>
<li>In the app, open <strong>Settings → License</strong> and note the <strong>Device ID</strong> and <strong>Device Key</strong>.</li>
<li>Buy a licence on the official Duplecast website and enter those two values.</li>
<li>Restart the app.</li>
</ol>
<p>The licence is paid to Duplecast, not to IPTVMaple, and is separate from your IPTV subscription. Buy it only from the official website.</p>

<h2>Duplecast vs SET IPTV vs Smart IPTV</h2>
<table>
<thead><tr><th></th><th>Duplecast</th><th>SET IPTV</th><th>Smart IPTV</th></tr></thead>
<tbody>
<tr><td>Trial</td><td>15 days</td><td>7 days</td><td>7 days</td></tr>
<tr><td>Playlist entry</td><td>In the app</td><td>Website, by MAC</td><td>Website, by MAC</td></tr>
<tr><td>Xtream Codes</td><td>Yes</td><td>Yes</td><td>M3U-based</td></tr>
<tr><td>VIDAA TVs</td><td>Listed by developer</td><td>Not listed</td><td>Not listed</td></tr>
</tbody>
</table>
<p>Details change as apps update, so check the developer’s site before paying. For more choices, see the <a href="/iptv-apps/">best IPTV apps</a>.</p>

<h2>If Duplecast stutters</h2>
<p>Smart TV processors and Wi-Fi chips are modest. Use Ethernet if you can, keep the TV updated, and read our <a href="/iptv-buffering-fix/">buffering checklist</a>. If your TV still struggles, a <a href="/iptv-firestick/">Fire TV Stick 4K</a> in the HDMI port is an inexpensive fix.</p>
""",
        faq=[
            ("Is Duplecast free?", "<p>Duplecast offers a 15-day free trial with every feature. After that you buy a licence on the Duplecast website.</p>"),
            ("Does Duplecast work on Hisense VIDAA TVs?", "<p>Duplecast lists VIDAA among its supported platforms, along with Samsung, LG, Android TV, Google TV and Fire TV.</p>"),
            ("Does Duplecast include channels?", "<p>No. Duplecast is a player only. Add your IPTVMaple Xtream login or M3U link to watch channels.</p>"),
            ("Where do I find my Duplecast Device ID and key?", "<p>In the app under Settings → License. You enter both on the Duplecast website when activating.</p>"),
        ],
        related=["set-iptv", "nanomid", "iptv-smart-tv", "iptv-samsung-tv"],
        keywords=["duplecast", "duplecast iptv", "duplecast player", "duplecast activation"],
    ),
    # ------------------------------------------------------------------ Nanomid
    dict(
        slug="nanomid", hub="apps", **D,
        title="Nanomid IPTV Player: Setup With OTP Code & Devices | IPTVMaple",
        description="How to use the Nanomid IPTV player on Samsung, LG, Android, Fire TV and iPhone: the OTP code, adding your playlist link, licence and tips. Try IPTVMaple free 24h.",
        kicker="IPTV apps", h1='<span class="grad-text">Nanomid</span> player setup',
        lead="Nanomid runs on TVs, phones and Fire TV, and you add your playlist from a browser with a one-time code.",
        crumb="Nanomid", blurb="Player for Samsung, LG, Android, Fire TV and iOS.",
        answer="<p><strong>Nanomid Player</strong> is an IPTV player for Samsung (2014+, except J series) and LG (webOS 3.0+) smart TVs, Android and Android TV, Fire TV and iPhone/iPad (iOS 16+). To add your playlist, open the app, press the green button to see your <strong>OTP code</strong>, then enter a name, your <strong>playlist link</strong> and the code on the Nanomid website. It doesn’t include channels; it plays the IPTVMaple M3U link we send you.</p>",
        body="""
<h2>Supported devices</h2>
<table>
<thead><tr><th>Platform</th><th>Requirement (per Nanomid)</th></tr></thead>
<tbody>
<tr><td>Samsung smart TV</td><td>2014 and later, J series excluded</td></tr>
<tr><td>LG smart TV</td><td>2016 and later, webOS 3.0+</td></tr>
<tr><td>Android, Android TV</td><td>Android 5.0+</td></tr>
<tr><td>Amazon Fire TV</td><td>Fire TV Stick and Fire TV Cube</td></tr>
<tr><td>iPhone, iPad</td><td>iOS / iPadOS 16+</td></tr>
</tbody>
</table>

<h2>Step-by-step: Nanomid with IPTVMaple</h2>
<ol>
<li>Install <strong>Nanomid</strong> from your device’s app store and open it.</li>
<li>Press the <strong>green button</strong> on the remote (or the on-screen option) to show your <strong>OTP code</strong>.</li>
<li>On your phone or computer, open the <em>Manage app</em> section of the official Nanomid website.</li>
<li>Enter a playlist name, paste the <strong>M3U link</strong> from our welcome message, and type the OTP code.</li>
<li>Return to the TV and reload. Your channels appear.</li>
</ol>

<h2>Things to know before you start</h2>
<ul>
<li><strong>Links only</strong>: Nanomid accepts a playlist link, not an uploaded m3u file. That suits IPTV subscriptions, because the link stays current.</li>
<li><strong>No separate username field</strong>: use the full M3U link we send, which already includes your login.</li>
<li><strong>Licence</strong>: Nanomid sells its player licence on its own website for a multi-year term. Check the current price there; it is paid to Nanomid, not IPTVMaple.</li>
<li><strong>Playlist support</strong>: Nanomid doesn’t see or support your playlist content, so for channel questions contact us, not Nanomid.</li>
</ul>

<h2>Nanomid or another player?</h2>
<p>Nanomid is handy when you want the same player on an older Samsung or LG TV and on your phone. If you prefer entering an Xtream login with separate movies and series sections, <a href="/duplecast/">Duplecast</a> or <a href="/smartone-iptv/">SmartOne IPTV</a> may suit you better. On Fire TV and Android TV, <a href="/tivimate/">TiviMate</a> remains the most complete option.</p>
<p>Not sure which app your TV supports? Our <a href="/iptv-smart-tv/">smart TV IPTV guide</a> lists the options for every brand.</p>
""",
        faq=[
            ("What is the Nanomid OTP code?", "<p>A one-time code shown in the app (press the green button). You enter it on the Nanomid website with your playlist link to send the playlist to that device.</p>"),
            ("Can I upload an m3u file to Nanomid?", "<p>No. Nanomid accepts playlist links only. Use the M3U link IPTVMaple sends you.</p>"),
            ("Does Nanomid work on Samsung TVs?", "<p>Yes, on Samsung smart TVs from 2014 onward, except the J series, according to Nanomid’s technical specifications.</p>"),
            ("Does Nanomid include TV channels?", "<p>No. It’s a player. You need an IPTV subscription such as IPTVMaple to watch channels.</p>"),
        ],
        related=["duplecast", "ss-iptv", "iptv-lg-tv", "iptv-smart-tv"],
        keywords=["nanomid", "nanomid iptv", "nanomid com", "nanomid player"],
    ),
    # ------------------------------------------------------------------ Lazy IPTV
    dict(
        slug="lazy-iptv", hub="apps", **D,
        title="Lazy IPTV: What Happened and the Best Alternatives | IPTVMaple",
        description="LazyIPTV Deluxe was removed from Google Play in 2023. What that means if you still use it, and the best Android IPTV players to switch to. Try IPTVMaple free 24h.",
        kicker="IPTV apps", h1='<span class="grad-text">Lazy IPTV</span>: status and alternatives',
        lead="Lazy IPTV was a favourite playlist manager on Android. If you are looking for it today, here is what changed and what to use instead.",
        crumb="Lazy IPTV", blurb="What happened to LazyIPTV Deluxe and what to use now.",
        answer="<p><strong>LazyIPTV Deluxe</strong>, the Android playlist and TV-guide manager by LC-Soft, was <strong>removed from Google Play in September 2023</strong>. If it’s still installed it may keep working, but it no longer gets updates from the store. For a maintained alternative, use <a href=\"/tivimate/\">TiviMate</a> on Android TV and Fire TV, or <a href=\"/iptv-smarters-pro/\">IPTV Smarters Pro</a> on phones and tablets. Both work with the IPTVMaple login.</p>",
        body="""
<h2>What Lazy IPTV did</h2>
<p>Lazy IPTV was a manager for playlists and TV guides rather than a full-screen player. Users liked it because it could:</p>
<ul>
<li>hold several M3U playlists and XMLTV/JTV guides in one place;</li>
<li>open streams in its own player or in an external player such as VLC or MX Player;</li>
<li>sync playlists across devices through Google Drive or Dropbox;</li>
<li>show catch-up archives where the provider supported them;</li>
<li>switch between a phone layout and a TV layout.</li>
</ul>

<h2>Should you keep using it?</h2>
<p>Apps that leave Google Play stop receiving updates there. Over time that can mean crashes on new Android versions, and copies offered on third-party sites may be modified. We don’t recommend installing it from unofficial APK sites. If your existing install still works, it will keep playing our M3U link, but plan a switch.</p>

<h2>Best Lazy IPTV alternatives</h2>
<table>
<thead><tr><th>If you used Lazy IPTV for…</th><th>Switch to</th><th>Why</th></tr></thead>
<tbody>
<tr><td>TV-style guide on Android TV / Fire TV</td><td><a href="/tivimate/">TiviMate</a></td><td>Best guide, catch-up and recording (Premium)</td></tr>
<tr><td>Phone or tablet</td><td><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></td><td>Free, simple Xtream login</td></tr>
<tr><td>Several playlists and profiles</td><td><a href="/tivimate-premium/">TiviMate Premium</a></td><td>Multiple playlists in one app</td></tr>
<tr><td>Opening streams in an external player</td><td><a href="/vlc-iptv/">VLC</a></td><td>Plays M3U links directly</td></tr>
<tr><td>Fast, modern player</td><td><a href="/implayer/">iMPlayer</a></td><td>Clean interface, Xtream support</td></tr>
</tbody>
</table>

<h2>Moving your IPTVMaple login</h2>
<ol>
<li>Install TiviMate or IPTV Smarters Pro.</li>
<li>Choose <strong>Xtream Codes</strong> and enter the server, username and password from our welcome message (or paste the M3U link).</li>
<li>Re-create your favourites. Most players let you mark favourites from the channel list in a few clicks.</li>
</ol>
<p>Lost your login details? Message us on WhatsApp and we will resend them. Our guide to the <a href="/iptv-apps/">best IPTV apps</a> compares the full range.</p>
""",
        faq=[
            ("Is Lazy IPTV still available?", "<p>LazyIPTV Deluxe was removed from Google Play in September 2023, so it’s no longer available or updated there.</p>"),
            ("Is IPTV# the same as LazyIPTV Deluxe?", "<p>IPTV# is a separate app from the same developer, LC-Soft. App stores list it as a different app rather than a renamed one.</p>"),
            ("What is the best replacement for Lazy IPTV?", "<p>TiviMate on Android TV and Fire TV, and IPTV Smarters Pro on phones and tablets. Both are maintained and work with IPTVMaple.</p>"),
            ("Can I still use my Lazy IPTV playlists?", "<p>Yes. A playlist is just a link or file; add the same IPTVMaple M3U link or Xtream login to any other player.</p>"),
        ],
        related=["tivimate", "iptv-smarters-pro", "iptv-apps", "vlc-iptv"],
        keywords=["lazy iptv", "lazyiptv", "lazyiptv deluxe", "lazy iptv deluxe"],
    ),
]

DEVICES = [
    dict(
        slug="iptv-smart-tv", hub="devices", **D,
        title="IPTV on a Smart TV: Apps for Every Brand (2026) | IPTVMaple",
        description="How to watch IPTV on any smart TV: the right app for Samsung, LG, Sony, Hisense VIDAA, TCL, Philips, Panasonic and Roku TVs, plus when to add a Fire TV Stick.",
        kicker="Devices", h1='IPTV on a <span class="grad-text">smart TV</span>: every brand',
        lead="The app you need depends on the system your TV runs, not the logo on the front. Find your TV below.",
        crumb="Smart TV", blurb="Which IPTV app to use on every TV brand.",
        answer="<p>To watch <strong>IPTV on a smart TV</strong>, install an IPTV player from the TV’s app store and add your IPTV login. Which app depends on the TV’s system: <strong>Samsung (Tizen)</strong> and <strong>LG (webOS)</strong> use players like SmartOne, Duplecast or SET IPTV; <strong>Sony, TCL, Hisense and Philips TVs with Google TV or Android TV</strong> can run TiviMate or IPTV Smarters; <strong>Hisense VIDAA</strong> and <strong>Roku TVs</strong> have few options, so a Fire TV Stick is usually the easier route.</p>",
        body="""
<h2>Find your TV’s system first</h2>
<p>Open your TV’s settings and look under <em>About</em> or <em>System</em>. You will see Tizen (Samsung), webOS (LG), Google TV or Android TV, VIDAA, Roku TV, Fire TV, or the maker’s own system. That name decides which IPTV apps you can install.</p>

<h2>Which IPTV app for which TV</h2>
<table>
<thead><tr><th>TV brand</th><th>Usual system</th><th>IPTV apps to use</th><th>Full guide</th></tr></thead>
<tbody>
<tr><td>Samsung</td><td>Tizen</td><td>SmartOne, Flix IPTV, Duplecast, SET IPTV, Nanomid, Smart IPTV</td><td><a href="/iptv-samsung-tv/">Samsung</a></td></tr>
<tr><td>LG</td><td>webOS</td><td>SmartOne, Flix IPTV, Duplecast, SS IPTV, Nanomid</td><td><a href="/iptv-lg-tv/">LG</a></td></tr>
<tr><td>Sony</td><td>Google TV / Android TV</td><td>TiviMate, IPTV Smarters Pro</td><td><a href="/iptv-android-tv/">Android TV</a></td></tr>
<tr><td>TCL</td><td>Google TV or Roku TV</td><td>TiviMate (Google TV); Fire TV Stick (Roku TV)</td><td><a href="/iptv-android-tv/">Android TV</a></td></tr>
<tr><td>Hisense</td><td>VIDAA, Google TV or Roku TV</td><td>Duplecast on VIDAA; TiviMate on Google TV</td><td>See below</td></tr>
<tr><td>Philips</td><td>Android/Google TV on many models</td><td>TiviMate, IPTV Smarters Pro</td><td><a href="/iptv-android-tv/">Android TV</a></td></tr>
<tr><td>Panasonic</td><td>Own system; some recent models Fire TV</td><td>Fire TV models: TiviMate, Smarters</td><td><a href="/iptv-firestick/">Fire TV</a></td></tr>
<tr><td>Roku TV (any brand)</td><td>Roku OS</td><td>No dedicated IPTV player; add a Fire TV Stick</td><td><a href="/iptv-roku/">Roku</a></td></tr>
</tbody>
</table>
<p>App stores change by model year and country. If an app isn’t listed on your TV, pick another from the same row; all of them work with IPTVMaple.</p>

<h2>Samsung and LG smart TVs</h2>
<p>Samsung and LG don’t run Android, so TiviMate and the Android version of IPTV Smarters aren’t available. Their players use one of two setups: you type your login in the app (<a href="/duplecast/">Duplecast</a>, SmartOne), or the app shows a MAC address and you send your playlist from a phone (<a href="/set-iptv/">SET IPTV</a>, <a href="/smart-iptv/">Smart IPTV</a>). <a href="/ss-iptv/">SS IPTV</a> is a free option, and <a href="/nanomid/">Nanomid</a> covers older Samsung and LG models. Most paid TV players have a free trial, then a one-time or multi-year activation paid to the app developer.</p>

<h2>Google TV and Android TV sets (Sony, TCL, Hisense, Philips)</h2>
<p>These TVs use Google Play, which gives you the best IPTV apps: <a href="/tivimate/">TiviMate</a> for a cable-style guide, or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> for a simple login. Setup is the same as on any <a href="/iptv-android-tv/">Android TV device</a>.</p>

<h2>Hisense VIDAA TVs</h2>
<p>VIDAA is Hisense’s own system and its app store is small. Duplecast lists VIDAA support, so check for it first. If you can’t find a player you like, plug a <a href="/iptv-firestick/">Fire TV Stick</a> into the HDMI port; it costs less than most TV apps’ multi-year licences over time and gives you TiviMate.</p>

<h2>Roku TVs</h2>
<p>Roku TVs (sold by TCL, Hisense and others) don’t offer a proper IPTV player that loads Xtream or M3U logins well. The simple answer is a Fire TV Stick or an Android TV box. Our <a href="/iptv-roku/">IPTV on Roku</a> page explains the options.</p>

<h2>Built-in app or streaming stick?</h2>
<table>
<thead><tr><th></th><th>App on the TV</th><th>Fire TV Stick 4K or Android box</th></tr></thead>
<tbody>
<tr><td>Extra hardware</td><td>None</td><td>One small device in HDMI</td></tr>
<tr><td>Best apps (TiviMate)</td><td>Only on Google/Android TV</td><td>Yes</td></tr>
<tr><td>Speed and Wi-Fi</td><td>Depends on the TV, often modest</td><td>Usually faster</td></tr>
<tr><td>App activation fees</td><td>Common on Samsung/LG players</td><td>TiviMate Premium optional</td></tr>
</tbody>
</table>
<p>Whichever you choose, plan on about 10 Mbps per screen for HD and 25 Mbps for 4K, and use Ethernet when the TV is near the router.</p>

<h2>Start watching</h2>
<p>Request the <a href="/try-iptv-canada/">free 24-hour trial</a>, install the app for your TV, and enter the login we send by email and WhatsApp. If you get stuck, send us a photo of the TV screen and we will walk you through it. When you are happy, plans start at $""" + str(LOW) + """ a month; see <a href="/iptv-plans-canada/">all IPTV plans</a>.</p>
""",
        faq=[
            ("Can I watch IPTV on a smart TV without a box?", "<p>Yes. Install an IPTV player from the TV’s app store and add your login. Samsung and LG use players like SmartOne or Duplecast; Google TV and Android TV sets can use TiviMate or IPTV Smarters.</p>"),
            ("What is the best IPTV app for a smart TV?", "<p>On Google TV and Android TV sets, TiviMate. On Samsung and LG, SmartOne IPTV, Duplecast or SET IPTV are popular. On VIDAA and Roku TVs, a Fire TV Stick usually gives the best result.</p>"),
            ("Does IPTV work on a Hisense TV?", "<p>Yes. On Hisense Google TV models install TiviMate. On VIDAA models look for Duplecast, or add a Fire TV Stick.</p>"),
            ("Does IPTV work on Sony and Philips TVs?", "<p>Most Sony TVs and many Philips TVs run Google TV or Android TV, so you can install TiviMate or IPTV Smarters Pro from Google Play.</p>"),
            ("Why do smart TV IPTV apps charge an activation fee?", "<p>Players on Samsung and LG are made by independent developers who charge after a free trial. The fee goes to them, not to your IPTV provider.</p>"),
        ],
        related=["iptv-samsung-tv", "iptv-lg-tv", "iptv-android-tv", "iptv-firestick", "duplecast"],
        keywords=["iptv smart tv", "ip tv smart tv", "smart tv iptv", "iptv hisense", "iptv hisense vidaa", "smart iptv hisense vidaa", "vidaa iptv", "iptv sony", "smart iptv sony",
                  "iptv philips", "smart iptv philips", "iptv panasonic", "iptv tcl", "iptv smasters smart tv", "iptv smasters pro smart tv"],
    ),
]

GUIDES = [
    # ------------------------------------------------------------------ Pluto TV vs IPTV
    dict(
        slug="pluto-tv-vs-iptv", hub="guides", **D,
        title="Pluto TV vs IPTV: Free Streaming or Paid Live TV? | IPTVMaple",
        description="Pluto TV is free, ad-supported streaming; IPTV gives you the real live channels. Compare channels, sports, ads, price and devices in Canada.",
        kicker="Comparison", h1='<span class="grad-text">Pluto TV vs IPTV</span>: what’s the difference?',
        lead="Both stream TV over the internet, but they are very different products. Here is what each one really gives you.",
        crumb="Pluto TV vs IPTV", blurb="Free ad-supported channels vs full live TV.",
        answer="<p><strong>Pluto TV</strong> is a free, ad-supported streaming service owned by Paramount. It offers its own themed channels and on-demand titles, not the live cable networks. A paid <strong>IPTV subscription</strong> such as IPTVMaple streams the actual live channels, including CBC, CTV, Global, TSN, Sportsnet and US networks, with live sports, a TV guide and catch-up. Pluto TV costs nothing; IPTV gives you live TV that Pluto TV doesn’t carry.</p>",
        body="""
<h2>Quick comparison</h2>
<table>
<thead><tr><th></th><th>Pluto TV</th><th>IPTV (IPTVMaple)</th></tr></thead>
<tbody>
<tr><td>Price</td><td>Free</td><td>From $""" + str(LOW) + """ a month, about $""" + f"{PER_MONTH:.2f}" + """/month on a 12-month plan</td></tr>
<tr><td>Ads</td><td>Yes, inside programs</td><td>Only the ads the channel itself broadcasts</td></tr>
<tr><td>Channel type</td><td>Curated themed channels (FAST)</td><td>Live broadcast and cable networks</td></tr>
<tr><td>Canadian networks live</td><td>No</td><td>CBC, CTV, Global, City, TVA and more</td></tr>
<tr><td>Live NHL, NFL, NBA, soccer</td><td>No</td><td>On TSN, Sportsnet, ESPN and others</td></tr>
<tr><td>TV guide and catch-up</td><td>Guide for Pluto’s channels</td><td>Full EPG; catch-up on supported channels</td></tr>
<tr><td>Account</td><td>Optional</td><td>Login sent after order or free trial</td></tr>
</tbody>
</table>

<h2>What Pluto TV is good at</h2>
<p>Pluto TV runs “FAST” channels: free, ad-supported streams built around a show, a genre or a back catalogue, such as classic sitcoms, crime dramas, movies or news clips. It launched in Canada in late 2023 and has its own apps for smart TVs, phones and streaming sticks. If you want something on in the background and don’t mind ads, it’s a decent free extra.</p>

<h2>What Pluto TV doesn’t do</h2>
<ul>
<li><strong>No live cable networks</strong>: you won’t find TSN, Sportsnet, CTV or CNN as they air.</li>
<li><strong>No live major sports</strong>: Hockey Night in Canada, the Super Bowl or the Champions League aren’t on Pluto TV.</li>
<li><strong>Limited choice</strong>: the lineup is what Pluto chooses, and it changes.</li>
</ul>

<h2>Can you watch Pluto TV through an IPTV app?</h2>
<p>People search for a “Pluto TV M3U” to load Pluto channels into TiviMate or another IPTV player. Pluto TV doesn’t publish an official M3U playlist; lists shared online are made by third parties and tend to break when Pluto changes its streams. The reliable way is Pluto TV’s own app, which you can install alongside your IPTV player on the same <a href="/iptv-firestick/">Fire TV Stick</a> or <a href="/iptv-android-tv/">Android TV</a>.</p>

<h2>Which one should you choose?</h2>
<ul>
<li><strong>Pluto TV</strong>: you only watch reruns and movies casually and want to spend nothing.</li>
<li><strong>IPTV</strong>: you want live Canadian and US channels, <a href="/iptv-sports/">live sports</a>, news as it happens, or channels from <a href="/iptv-international/">your home country</a>.</li>
<li><strong>Both</strong>: many cord-cutters keep a free app like Pluto TV and add IPTV for live TV and sports.</li>
</ul>
<p>You can test the difference yourself with our <a href="/try-iptv-canada/">free 24-hour IPTV trial</a>. To understand the technology, read <a href="/what-is-iptv/">what is IPTV</a>.</p>
""",
        faq=[
            ("Is Pluto TV a form of IPTV?", "<p>Technically yes: it delivers TV over the internet. But it’s a free, ad-supported service with its own channels, not a subscription to live cable networks.</p>"),
            ("Is Pluto TV available in Canada?", "<p>Yes. Pluto TV launched in Canada in late 2023 and is free on most smart TVs, phones and streaming devices.</p>"),
            ("Does Pluto TV have live sports?", "<p>Not the major live leagues. For live NHL, NFL, NBA, UFC and soccer you need channels such as TSN, Sportsnet and ESPN, which IPTV includes.</p>"),
            ("Is there an official Pluto TV M3U playlist?", "<p>No. Pluto TV doesn’t publish one. Use the official Pluto TV app; third-party M3U lists often stop working.</p>"),
            ("Which is cheaper, Pluto TV or IPTV?", "<p>Pluto TV is free. IPTVMaple starts at $" + str(LOW) + " for a month, and the price includes live Canadian, US and international channels that Pluto TV doesn’t offer.</p>"),
        ],
        related=["what-is-iptv", "best-iptv-canada", "watch-iptv-online", "iptv-price"],
        keywords=["pluto tv iptv", "iptv pluto tv", "pluto iptv", "pluto tv m3u", "pluto tv vs iptv"],
    ),
    # ------------------------------------------------------------------ IPTV vs satellite
    dict(
        slug="iptv-vs-satellite", hub="guides", **D,
        title="IPTV vs Satellite TV in Canada: Cost, Setup & Picture | IPTVMaple",
        description="IPTV vs satellite TV in Canada: compare cost, installation, weather, channels and contracts, and how IPTV runs on an Enigma2 receiver. Try IPTV free for 24h.",
        kicker="Comparison", h1='<span class="grad-text">IPTV vs satellite TV</span> in Canada',
        lead="A dish on the roof or an app on your TV? Here is how the two compare for Canadian homes, condos and cottages.",
        crumb="IPTV vs satellite", blurb="Dish vs internet: cost, setup and reliability.",
        answer="<p><strong>Satellite TV</strong> sends channels from a satellite to a dish on your home, so it needs installation, a clear view of the southern sky and a receiver, and heavy rain or snow can interrupt it. <strong>IPTV</strong> streams the same kind of live channels over your internet connection to apps on your TV, phone or computer, with no dish, no installer and no contract. Satellite still makes sense where internet is very slow; elsewhere IPTV is usually cheaper and more flexible.</p>",
        body="""
<h2>Side-by-side</h2>
<table>
<thead><tr><th></th><th>Satellite TV</th><th>IPTV</th></tr></thead>
<tbody>
<tr><td>What you need</td><td>Dish, cabling, receiver per TV</td><td>Internet and an app or streaming stick</td></tr>
<tr><td>Installation</td><td>Technician visit, mounting on the building</td><td>Install an app and enter a login</td></tr>
<tr><td>Weather</td><td>Rain fade and snow on the dish</td><td>Not affected by weather at your home</td></tr>
<tr><td>Condos and rentals</td><td>Often not allowed or no line of sight</td><td>Works anywhere with internet</td></tr>
<tr><td>Watch on phone or laptop</td><td>Limited</td><td>Yes, on every device</td></tr>
<tr><td>International channels</td><td>Add-on packages or a second dish</td><td>Included in every IPTVMaple plan</td></tr>
<tr><td>Contract</td><td>Usually</td><td>None: monthly, 6- or 12-month plans</td></tr>
<tr><td>Needs internet</td><td>No</td><td>Yes, about 10 Mbps per HD screen</td></tr>
</tbody>
</table>

<h2>Satellite TV in Canada today</h2>
<p>Two satellite services cover Canada: Bell Satellite TV and Shaw Direct, which became part of Rogers after the Rogers–Shaw merger in 2023. Both serve many rural homes where cable never arrived. Their strength is that they work without internet; their weaknesses are the dish, the hardware rental and the price of channel packages.</p>

<h2>When satellite is still the better choice</h2>
<ul>
<li>Your home has no internet, or less than about 10 Mbps.</li>
<li>You use a capped mobile data plan as your only internet.</li>
</ul>
<p>Rural internet has changed fast, though. Many cottages and farms now use fibre, fixed wireless or <a href="/iptv-starlink/">Starlink</a>, all of which carry IPTV well.</p>

<h2>When IPTV wins</h2>
<ul>
<li>You live in a condo or rental where you can’t mount a dish.</li>
<li>You want TV on several devices, including phones and tablets.</li>
<li>Your family wants channels from <a href="/iptv-international/">Italy, Poland, the UK or other countries</a> without a second package.</li>
<li>You want to stop paying for receivers and contracts. Compare costs on our <a href="/iptv-price/">IPTV prices page</a>.</li>
</ul>

<h2>Using IPTV on an Enigma2 satellite receiver</h2>
<p>If you already own a Linux satellite receiver running Enigma2 (such as models from Vu+, Dreambox or Zgemma), you don’t have to throw it away. Enigma2 can play IPTV streams from an M3U playlist, usually through a plugin that turns the list into channel bouquets. Plugins and steps differ between images, so send us your receiver model on WhatsApp and we will help with the M3U link. For a simpler setup, a <a href="/iptv-box/">dedicated IPTV box</a> or a <a href="/iptv-firestick/">Fire TV Stick</a> is plug-and-play.</p>

<h2>Try before you cancel</h2>
<p>Keep your dish for a day and run our <a href="/try-iptv-canada/">free 24-hour IPTV trial</a> side by side. If IPTV covers your channels and your internet keeps up, switch to an <a href="/iptv-plans-canada/">IPTV plan</a>.</p>
""",
        faq=[
            ("Is IPTV better than satellite TV?", "<p>For most homes with decent internet, yes: no dish, no installer, no contract, and it works on every device. Satellite is better only where internet is very slow or unavailable.</p>"),
            ("Does weather affect IPTV like satellite?", "<p>Weather at your home doesn’t affect IPTV, because it arrives over your internet connection. Satellite signals can drop during heavy rain or when snow covers the dish.</p>"),
            ("Can I use IPTV on my Enigma2 satellite receiver?", "<p>Usually, yes. Enigma2 can load an M3U playlist through a plugin. Send us your model and we will help with the setup.</p>"),
            ("What internet speed do I need to replace satellite with IPTV?", "<p>About 10 Mbps per screen for HD and 25 Mbps per screen for 4K.</p>"),
        ],
        related=["iptv-starlink", "what-is-iptv", "iptv-box", "iptv-price"],
        keywords=["iptv satellite", "iptv vs satellite", "sat iptv", "iptv enigma2", "enigma2 iptv", "satellite vs iptv"],
    ),
    # ------------------------------------------------------------------ Starlink
    dict(
        slug="iptv-starlink", hub="guides", **D,
        title="IPTV on Starlink: Does It Work in Rural Canada? | IPTVMaple",
        description="Yes, IPTV works on Starlink. The speed you need, why obstructions cause brief drops, buffer settings, wired setup and data use for rural Canadian homes.",
        kicker="Guide", h1='IPTV on <span class="grad-text">Starlink</span>',
        lead="Starlink has brought fast internet to farms, cottages and remote towns across Canada. Here is how to get smooth IPTV on it.",
        crumb="IPTV on Starlink", blurb="Smooth IPTV on satellite internet in rural Canada.",
        answer="<p><strong>Yes, IPTV works on Starlink.</strong> Streaming needs about <strong>10 Mbps per screen for HD</strong> and 25 Mbps for 4K, which most Starlink connections exceed. The main issue is short dropouts when trees or buildings block the dish’s view of the sky. Fix obstructions with the Starlink app’s check, use a wired connection to the TV device, and raise the buffer in your IPTV player.</p>",
        body="""
<h2>Why Starlink works for IPTV</h2>
<p>Starlink satellites orbit much closer to Earth than older internet satellites, so latency is low enough for live streaming. IPTV only downloads a video stream, so Starlink’s shared (CGNAT) addressing, which can bother gamers and people running servers, doesn’t matter for watching TV.</p>

<h2>Starlink vs older satellite internet and satellite TV</h2>
<table>
<thead><tr><th></th><th>Starlink + IPTV</th><th>Older satellite internet</th><th>Satellite TV</th></tr></thead>
<tbody>
<tr><td>Live streaming</td><td>Works well</td><td>High latency, often data caps</td><td>Not streaming; dish TV</td></tr>
<tr><td>Devices</td><td>TV, phone, tablet, laptop</td><td>Limited by speed</td><td>Receiver per TV</td></tr>
<tr><td>International channels</td><td>Included with IPTVMaple</td><td>—</td><td>Extra packages</td></tr>
</tbody>
</table>
<p>For a wider comparison, read <a href="/iptv-vs-satellite/">IPTV vs satellite TV</a>.</p>

<h2>Setting up for smooth streaming</h2>
<ol>
<li><strong>Clear the view of the sky.</strong> Run the obstruction check in the Starlink app and move the dish if trees or a roof edge block it. Even small obstructions cause a few seconds of freezing every few minutes.</li>
<li><strong>Wire the TV device.</strong> Connect your Fire TV, Android box or smart TV to the Starlink router by Ethernet. Some router versions need Starlink’s Ethernet adapter.</li>
<li><strong>Raise the buffer.</strong> In <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters</a>, choose a larger buffer size so short drops are covered.</li>
<li><strong>Use the right stream quality.</strong> HD channels are more forgiving than 4K on a busy evening.</li>
</ol>

<h2>How much data does IPTV use on Starlink?</h2>
<p>Roughly 1 to 3 GB per hour for an HD stream, and more for 4K. A household watching a few hours a day can use several hundred gigabytes a month. Check whether your Starlink plan includes unlimited data or lower priority after a threshold, and pick HD over 4K if you are on a limited plan.</p>

<h2>Snow, rain and northern winters</h2>
<p>Heavy rain or wet snow can reduce Starlink speeds briefly. The dish has a snow-melt mode, and a short drop is usually covered by a larger player buffer. Mount the dish where snow won’t pile up around it.</p>

<h2>Try it on your connection</h2>
<p>Every rural setup is different. Use the <a href="/try-iptv-canada/">free 24-hour trial</a> during your normal evening viewing to see how your Starlink handles it. If you see buffering, our <a href="/iptv-buffering-fix/">buffering fixes</a> walk through the next steps, or message us on WhatsApp.</p>
""",
        faq=[
            ("Does IPTV work with Starlink?", "<p>Yes. IPTV needs about 10 Mbps per HD screen and 25 Mbps for 4K, which most Starlink connections provide. Clear obstructions and use a wired connection for the best results.</p>"),
            ("Why does IPTV freeze every few minutes on Starlink?", "<p>Usually an obstruction: trees or buildings briefly block the dish. Run the obstruction check in the Starlink app, move the dish, and raise the buffer in your IPTV app.</p>"),
            ("Does Starlink’s CGNAT affect IPTV?", "<p>No. CGNAT affects incoming connections like game hosting, not streaming TV to your devices.</p>"),
            ("Is Starlink plus IPTV cheaper than satellite TV?", "<p>If you already pay for Starlink for internet, adding IPTV from $" + str(LOW) + " a month is usually far cheaper than a separate satellite TV package with receivers.</p>"),
        ],
        related=["iptv-vs-satellite", "iptv-buffering-fix", "iptv-near-me", "iptv-firestick"],
        keywords=["starlink iptv", "iptv starlink", "iptv on starlink", "iptv rural canada"],
    ),
    # ------------------------------------------------------------------ IPTV account
    dict(
        slug="iptv-account", hub="guides", **D,
        title="Your IPTV Account Explained: Login, M3U, Screens | IPTVMaple",
        description="What an IPTV account includes: the Xtream login, M3U and EPG links, how many screens you can use, renewals and login safety. Get a free 24h trial.",
        kicker="Guide", h1='Your <span class="grad-text">IPTV account</span>, explained',
        lead="After you order, you receive a few lines of login details. This is what each one does and how to use them on any device.",
        crumb="IPTV account", blurb="Login, M3U link, screens and renewals.",
        answer="<p>An <strong>IPTV account</strong> is the login that unlocks your subscription in an IPTV app. With IPTVMaple it comes as an <strong>Xtream Codes login</strong> (server URL, username, password), an <strong>M3U playlist link</strong> and an <strong>EPG (TV guide) link</strong>, sent by email and WhatsApp after your order or free trial. Your plan sets how many screens can watch at once, from 1 to 5.</p>",
        body="""
<h2>What’s in your IPTVMaple account</h2>
<table>
<thead><tr><th>Detail</th><th>What it does</th><th>Used in</th></tr></thead>
<tbody>
<tr><td>Server URL</td><td>The address your app connects to</td><td>Xtream Codes login</td></tr>
<tr><td>Username and password</td><td>Identify your subscription</td><td>Xtream Codes login</td></tr>
<tr><td>M3U link</td><td>Your full channel list in one URL</td><td>Apps that take a playlist link</td></tr>
<tr><td>EPG link</td><td>The TV guide for those channels</td><td>Apps that need a separate guide</td></tr>
</tbody>
</table>
<p>The Xtream Codes login is the one to use whenever an app offers it: it loads live TV, the guide, movies and series in separate sections. Use the M3U link for apps that only accept a playlist, such as <a href="/ss-iptv/">SS IPTV</a>, <a href="/vlc-iptv/">VLC</a> or <a href="/nanomid/">Nanomid</a>. Our <a href="/m3u-playlist/">M3U playlist guide</a> and <a href="/xtream-codes-iptv/">Xtream Codes guide</a> go deeper.</p>

<h2>Your account vs your app account</h2>
<p>Your IPTV account and your player app are separate things. Apps such as <a href="/tivimate-premium/">TiviMate Premium</a>, <a href="/set-iptv/">SET IPTV</a> or <a href="/duplecast/">Duplecast</a> may have their own account or activation, paid to the app developer. That never replaces your IPTV login, and we don’t charge for it.</p>

<h2>How many screens can use one account?</h2>
<p>Each plan allows a set number of devices to watch at the same time. You can install the apps on as many devices as you like, but only that number can play at once.</p>
<table>
<thead><tr><th>Plan</th><th>Watch at the same time</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>1 device</td><td>1 screen</td><td>One TV or one person</td></tr>
<tr><td>2–3 devices</td><td>2–3 screens</td><td>Couples, small families</td></tr>
<tr><td>4–5 devices</td><td>4–5 screens</td><td>Larger households</td></tr>
</tbody>
</table>
<p>Extra screens cost less per screen than a second account. See the prices on our <a href="/iptv-plans-canada/">plans page</a>.</p>

<h2>Getting an account</h2>
<ol>
<li>Start with the <a href="/try-iptv-canada/">free 24-hour trial</a>: a full account, no credit card.</li>
<li>Pick a plan length (1, 6 or 12 months) and a number of screens.</li>
<li>Receive your login by email and WhatsApp, and enter it in your app.</li>
</ol>

<h2>Renewing and changing your plan</h2>
<p>When your plan is about to end, renew it and keep the same login, so you don’t have to set up your apps again. If you need more screens, ask us on WhatsApp to move you to a bigger plan.</p>

<h2>Keeping your account safe</h2>
<ul>
<li>Don’t share your login outside your household; extra simultaneous streams can stop playback on your own screens.</li>
<li>Install apps only from official stores or the developer’s website.</li>
<li>If you think your login was exposed, contact us and we will help.</li>
</ul>
""",
        faq=[
            ("What do I get when I create an IPTV account?", "<p>An Xtream Codes login (server, username, password), an M3U playlist link and an EPG link, sent by email and WhatsApp.</p>"),
            ("Can I use my IPTV account on several devices?", "<p>Yes. Install it on as many devices as you like; your plan sets how many can watch at the same time, from 1 to 5.</p>"),
            ("Is my IPTV account the same as my TiviMate account?", "<p>No. TiviMate Premium and other app activations are separate purchases from the app developers. Your IPTV login is what brings the channels.</p>"),
            ("Can I try an IPTV account for free?", "<p>Yes, IPTVMaple gives a full 24-hour trial account with no credit card.</p>"),
            ("Do I keep the same login when I renew?", "<p>Yes. Renewing extends your existing account, so your apps keep working without new setup.</p>"),
        ],
        related=["xtream-codes-iptv", "m3u-playlist", "iptv-price", "iptv-for-beginners"],
        keywords=["iptv account", "iptv login", "iptv account login", "iptv credentials"],
    ),
    # ------------------------------------------------------------------ Recording / catch-up
    dict(
        slug="iptv-recording-catch-up", hub="guides", **D,
        title="IPTV DVR, Recording & Catch-Up: How to Watch Later | IPTVMaple",
        description="Can you record IPTV? How catch-up, TiviMate recording and cloud DVR differ, which devices and apps support each, and storage tips. Try it free for 24h.",
        kicker="Guide", h1='IPTV <span class="grad-text">recording, DVR and catch-up</span>',
        lead="Missed the game or tonight’s episode? IPTV gives you two ways to watch later. Here is how each works.",
        crumb="Recording & catch-up", blurb="Record shows and replay recent programs.",
        answer="<p>Yes, you can watch IPTV later in two ways. <strong>Catch-up</strong> replays recent programs on supported channels straight from the TV guide, with nothing to set up. <strong>Recording (DVR)</strong> saves a program to your own device’s storage; on Fire TV and Android TV, <strong>TiviMate Premium</strong> can schedule recordings. Unlike cable, there’s no rented DVR box.</p>",
        body="""
<h2>Catch-up vs recording</h2>
<table>
<thead><tr><th></th><th>Catch-up</th><th>Recording (DVR)</th></tr></thead>
<tbody>
<tr><td>Where it’s stored</td><td>On the provider’s side</td><td>On your device or USB drive</td></tr>
<tr><td>Setup</td><td>None: pick a past program in the guide</td><td>Schedule the program in your app</td></tr>
<tr><td>Which channels</td><td>Channels that offer catch-up</td><td>Any channel you can play</td></tr>
<tr><td>How long it’s kept</td><td>A limited window (varies by channel)</td><td>Until you delete it</td></tr>
<tr><td>App support</td><td>TiviMate, IPTV Smarters and others</td><td>Mainly TiviMate Premium on Android</td></tr>
</tbody>
</table>

<h2>How to use catch-up</h2>
<ol>
<li>Log in with your <strong>Xtream Codes</strong> details: catch-up works best with this login type.</li>
<li>Open the TV guide and go back in time on a channel marked with a catch-up or rewind icon.</li>
<li>Select the program and press play.</li>
</ol>
<p>If you don’t see past programs, the channel may not offer catch-up, or your app doesn’t support it. <a href="/tivimate/">TiviMate</a> and <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> both show it in the guide.</p>

<h2>How to record IPTV with TiviMate</h2>
<ol>
<li>Get <a href="/tivimate-premium/">TiviMate Premium</a> on a <a href="/iptv-firestick/">Fire TV Stick</a> or <a href="/iptv-android-tv/">Android TV</a> device.</li>
<li>Set a recording folder in Settings. A USB drive gives far more room than a stick’s built-in storage.</li>
<li>In the guide, select a program and choose <strong>Record</strong>, or set a series recording.</li>
</ol>
<p>An hour of HD video can take 1 to 3 GB, so a Fire TV Stick’s internal storage fills quickly. An Android box with a USB port, like those on our <a href="/iptv-box/">IPTV box page</a>, is a better DVR.</p>

<h2>Recording on smart TVs, iPhone and PC</h2>
<ul>
<li><strong>Samsung and LG apps</strong>: most players focus on live TV and catch-up rather than recording.</li>
<li><strong>iPhone and iPad</strong>: use catch-up; iOS apps rarely record.</li>
<li><strong>PC and Mac</strong>: <a href="/vlc-iptv/">VLC</a> can save a stream to a file while you watch it.</li>
</ul>

<h2>Why this beats a cable DVR</h2>
<p>A cable PVR is a rented box tied to one TV. With IPTV, catch-up follows you to every device on your account, and recording is optional. Test both on your favourite channels with the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>
""",
        faq=[
            ("Can you record IPTV?", "<p>Yes. On Fire TV and Android TV, TiviMate Premium can record programs to the device or a USB drive. On other devices, use catch-up to watch recent programs later.</p>"),
            ("What is IPTV catch-up?", "<p>A replay of recently aired programs on supported channels, picked from the TV guide. Nothing needs to be recorded in advance.</p>"),
            ("Does every channel have catch-up?", "<p>No, only channels that offer it. Your app’s guide marks them with a rewind or catch-up icon.</p>"),
            ("Is there a cloud DVR with IPTV?", "<p>Catch-up works like a short-term cloud replay for supported channels. For long-term storage, record locally with TiviMate Premium.</p>"),
            ("How much storage do IPTV recordings need?", "<p>Roughly 1 to 3 GB per hour in HD, more for 4K. Use a USB drive for regular recording.</p>"),
        ],
        related=["tivimate-premium", "tivimate", "iptv-box", "iptv-apps"],
        keywords=["iptv dvr", "iptv recording", "record iptv", "iptv catch up", "iptv catchup", "iptv cloud dvr"],
    ),
    # ------------------------------------------------------------------ HBO / premium movie channels
    dict(
        slug="hbo-iptv", hub="guides", **D,
        title="HBO on IPTV in Canada: HBO, Crave & Movie Channels | IPTVMaple",
        description="Watch HBO channels live on IPTV in Canada: HBO East and West, HBO 2, Crave, Cinemax, Showtime, Starz and Super Écran in one plan. HBO Max vs live channels explained.",
        kicker="Channels", h1='<span class="grad-text">HBO on IPTV</span>: live premium movie channels',
        lead="HBO, Crave, Cinemax, Showtime and Starz without stacking premium add-ons. Here is what’s included and how it differs from HBO Max.",
        crumb="HBO IPTV", blurb="HBO, Crave, Showtime, Starz and more.",
        answer="<p><strong>IPTVMaple includes HBO channels live</strong>: HBO East and West, HBO 2, HBO Comedy, HBO Family, HBO Signature and HBO Zone, plus Canada’s Crave 1–4 and Super Écran, and Cinemax, Showtime and Starz. These are the live linear channels, shown with a TV guide. HBO Max is a different product: an on-demand app with its own subscription. In Canada, HBO’s series have long streamed on Crave.</p>",
        body="""
<h2>Premium movie channels included</h2>
<table>
<thead><tr><th>Group</th><th>Channels</th></tr></thead>
<tbody>
<tr><td>HBO (US)</td><td>HBO East, HBO West, HBO 2, HBO Comedy, HBO Family, HBO Signature, HBO Zone</td></tr>
<tr><td>Canada</td><td>Crave 1, Crave 2, Crave 3, Crave 4, HBO 1, HBO 2, Super Écran 1–4, Super Channel Fuse, Heart &amp; Home, Vault</td></tr>
<tr><td>Cinemax</td><td>Cinemax East and West, ActionMax, MovieMax, ThrillerMax, 5StarMax, OuterMax</td></tr>
<tr><td>Showtime</td><td>Showtime East and West, Showtime 2, Showcase, Extreme, Next, Beyond, Women, Family Zone</td></tr>
<tr><td>Starz</td><td>Starz East and West, Starz Edge, Cinema, Comedy, Kids &amp; Family, Encore channels</td></tr>
<tr><td>UK</td><td>Sky Cinema Premiere, Hits, Action, Comedy, Drama, Thriller, Family, Greats</td></tr>
</tbody>
</table>
<p>Lineups change from time to time. Search “HBO” or “Crave” on the <a href="/channels-list/">full channels list</a> for the current list.</p>

<h2>Live HBO channels vs HBO Max</h2>
<table>
<thead><tr><th></th><th>Live HBO channels (IPTV)</th><th>HBO Max app</th></tr></thead>
<tbody>
<tr><td>How you watch</td><td>Scheduled, like cable</td><td>On demand, any episode any time</td></tr>
<tr><td>New episodes</td><td>At the scheduled air time</td><td>When released in the app</td></tr>
<tr><td>Other channels</td><td>Hundreds of live channels in the same plan</td><td>HBO and Max content only</td></tr>
<tr><td>Watch later</td><td>Catch-up on supported channels</td><td>Built in</td></tr>
</tbody>
</table>
<p>Many viewers like the live channels because a new episode airs at a set time on HBO East, then again three hours later on HBO West, which is handy across Canadian time zones.</p>

<h2>Crave and Super Écran for Canadian viewers</h2>
<p>Crave is the Canadian home of HBO programming and other premium series, and Super Écran is the French-language premium movie service in Québec. Both are in the Canadian group of your channel list, next to CTV, CBC and TVA. Prefer French? See <a href="/iptv-quebec/">IPTV in Québec</a>.</p>

<h2>Best way to watch</h2>
<ul>
<li>Use <a href="/tivimate/">TiviMate</a> and add the premium channels to a “Movies” favourites group.</li>
<li>Pick a <a href="/4k-iptv/">4K-capable device</a> for the 4K versions of these channels.</li>
<li>Use catch-up to replay a premiere you missed; see <a href="/iptv-recording-catch-up/">IPTV recording and catch-up</a>.</li>
</ul>
<p>Check the HBO channels on your own TV with the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>
""",
        faq=[
            ("Can I watch HBO on IPTV?", "<p>Yes. IPTVMaple includes live HBO channels (East, West, HBO 2, Comedy, Family, Signature and Zone) as well as Crave, Cinemax, Showtime and Starz.</p>"),
            ("Is HBO Max included with IPTV?", "<p>No. HBO Max is a separate on-demand app. IPTV gives you the live HBO channels as they air, with catch-up on supported channels.</p>"),
            ("Is Crave included?", "<p>Yes, Crave 1 to 4 are in the Canadian channel group, along with Super Écran for French-language viewers.</p>"),
            ("Do I pay extra for HBO and movie channels?", "<p>No. Premium movie channels are part of every IPTVMaple plan, with no add-on packages.</p>"),
        ],
        related=["4k-iptv", "iptv-recording-catch-up", "best-iptv-canada", "iptv-quebec"],
        keywords=["iptv hbo", "iptv hbo max", "hbo max iptv", "hbo iptv", "iptv crave", "iptv series"],
    ),
]

GERMAN = community(
    "german-iptv", "German", "Germany", "🇩🇪", "Willkommen!",
    "Kitchener–Waterloo, Toronto, Vancouver, Calgary, Edmonton and Winnipeg",
    [("General", ["Das Erste (ARD)", "ZDF", "RTL", "Sat.1", "ProSieben", "VOX", "kabel eins", "RTLZWEI"]),
     ("News", ["n-tv", "WELT", "phoenix", "ZDFinfo"]),
     ("Sport", ["Sky Sport Bundesliga", "Sky Sport", "Sport1", "Eurosport 1", "DAZN 1"]),
     ("Documentary &amp; kids", ["Discovery", "National Geographic", "History", "DMAX", "Spiegel Geschichte", "KiKA", "Super RTL"]),
     ("Austria &amp; Switzerland", ["ORF 1", "ORF 2", "ServusTV", "SRF 1", "SRF zwei"])],
    "Follow the Bundesliga on Sky Sport Bundesliga, the national team and the DFB-Pokal, plus winter sports on Eurosport and Sport1.",
    "Germany is 6 hours ahead of Toronto and 9 hours ahead of Vancouver, so a Saturday 15:30 Bundesliga kick-off is 9:30 in the morning in Ontario.",
    [("Can I watch the Bundesliga in Canada with German commentary?", "<p>Yes, on the Sky Sport Bundesliga and Sky Sport channels in the German lineup.</p>"),
     ("Are Austrian and Swiss channels included?", "<p>Yes. ORF, ServusTV and SRF channels are listed next to the German channels.</p>")],
    ["polish-iptv", "uk-iptv", "canada/ontario/kitchener"], ["german iptv", "iptv germany", "iptv deutsch", "deutsches iptv"],
    title="German IPTV in Canada: ARD, ZDF, RTL & Bundesliga | IPTVMaple",
)

GERMAN.update(D)

PAGES = APPS + DEVICES + GUIDES + [GERMAN]

# Existing pages that link to the new ones from their "Related guides" list (contextual inbound links, so no new page is orphaned).
LINK_IN = {
    "what-is-iptv": ["pluto-tv-vs-iptv", "iptv-vs-satellite"],
    "watch-iptv-online": ["pluto-tv-vs-iptv"],
    "iptv-near-me": ["iptv-starlink"],
    "iptv-buffering-fix": ["iptv-starlink"],
    "xtream-codes-iptv": ["iptv-account"],
    "m3u-playlist": ["iptv-account"],
    "iptv-for-beginners": ["iptv-account"],
    "tivimate-premium": ["iptv-recording-catch-up"],
    "4k-iptv": ["hbo-iptv"],
    "best-iptv-canada": ["hbo-iptv"],
    "tivimate": ["lazy-iptv"],
    "vlc-iptv": ["lazy-iptv"],
    "polish-iptv": ["german-iptv"],
    "uk-iptv": ["german-iptv"],
    "iptv-android-tv": ["iptv-smart-tv"],
}


def link_in(pages):
    by = {p["slug"]: p for p in pages}
    for src, targets in LINK_IN.items():
        rel = by[src].setdefault("related", [])
        rel.extend(t for t in targets if t not in rel)
