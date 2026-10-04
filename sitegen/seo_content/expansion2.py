"""Expansion pass 2 (2026-10-04, SEO master prompt v3): pages for protected keyword classes (apps, devices, tools) that v2 had
filed under "other brands" or lumped into a broader page.

New pages: GSE Smart IPTV, IPTVX, OTT Navigator, Purple IPTV players (apps); onn 4K box (devices); IPTV vs Netflix and the
M3U playlist checker (guides). Third-party facts were checked on the developers' own store listings or websites on 2026-10-04;
app prices are not quoted because they change. IPTVMaple facts (trial, refund, login delivery, prices) come from the site data.
"""
from ._util import price_range

D = dict(published="2026-10-04", updated="2026-10-04")
LOW, PER_MONTH = price_range()

APPS = [
    # ------------------------------------------------------------------ GSE Smart IPTV
    dict(
        slug="gse-smart-iptv", hub="apps", **D,
        title="GSE Smart IPTV Setup: iPhone, Apple TV & Android | IPTVMaple",
        description="GSE Smart IPTV setup guide: add your Xtream login or M3U link on iPhone, iPad, Apple TV or Android, load the EPG, cast to Chromecast and fix common errors.",
        kicker="IPTV apps", h1='<span class="grad-text">GSE Smart IPTV</span> setup guide',
        lead="One of the longest-running IPTV players, with versions for Apple and Android devices. Here is how to set it up with your login.",
        crumb="GSE Smart IPTV", blurb="Veteran player for iPhone, Apple TV and Android.",
        answer="<p><strong>GSE Smart IPTV</strong> is an IPTV player from GSE Technology, available on iPhone, iPad, Apple TV and Android. It doesn’t include any channels: you add your provider’s <strong>Xtream Codes login</strong> (server, username, password) or <strong>M3U playlist link</strong>, plus an <strong>XMLTV EPG</strong> link for the guide. It works with the login IPTVMaple sends by email and WhatsApp after your order or free trial.</p>",
        body="""
<h2>Which GSE app do you need?</h2>
<p>Search the store for “GSE” and you will see more than one listing, which is the main source of confusion with this app. The developer publishes separate apps per platform: an iPhone/iPad app, a <strong>GSE Smart IPTV Pro</strong> app for Apple TV (a one-time purchase on the App Store), and Android versions on Google Play. They share the same idea and menus, so the steps below apply to all of them. Install the one listed for your device.</p>
<p>Every GSE listing says the same thing: the app ships with no media apart from a sample video, and it has no link to any TV provider. You bring the content; we provide the channels.</p>

<h2>What GSE Smart IPTV supports</h2>
<table>
<thead><tr><th>Feature</th><th>GSE Smart IPTV</th><th>What it means for you</th></tr></thead>
<tbody>
<tr><td>Xtream Codes API</td><td>Yes</td><td>Log in with server, username and password: live TV, movies and series load in separate sections</td></tr>
<tr><td>M3U playlists</td><td>Local file or remote link</td><td>Paste the M3U link from your welcome message</td></tr>
<tr><td>TV guide</td><td>XMLTV EPG</td><td>Add our EPG link if the guide is empty</td></tr>
<tr><td>Recording</td><td>Live stream recording (Apple TV Pro listing)</td><td>Record a programme to watch later</td></tr>
<tr><td>Parental control</td><td>PIN lock</td><td>Hide adult or late-night categories</td></tr>
<tr><td>Casting</td><td>Chromecast and AirPlay on mobile</td><td>Send a channel from your phone to the TV</td></tr>
<tr><td>Languages</td><td>31 interface languages</td><td>Including English and French</td></tr>
</tbody>
</table>

<h2>Step-by-step: GSE Smart IPTV with IPTVMaple</h2>
<ol>
<li>Install <strong>GSE Smart IPTV</strong> from the App Store or Google Play (on Apple TV, <strong>GSE Smart IPTV Pro</strong>).</li>
<li>Open the app and go to <strong>Xtream-Codes API</strong> (on some versions under the menu → <em>Xtream-Codes API</em>).</li>
<li>Tap <strong>+</strong> and enter any name, then the <strong>server URL</strong>, <strong>username</strong> and <strong>password</strong> from our message, exactly as written.</li>
<li>Save and open the new entry. Live TV, movies and series appear as separate sections.</li>
<li>If you prefer M3U, use <strong>Remote playlists</strong> instead and paste the M3U link. Then add our EPG link under <strong>EPG sources</strong>.</li>
</ol>
<p>On Apple TV, typing a long password with the remote is slow. The Pro listing mentions a web interface for managing playlists, which lets you paste the details from a computer on the same network instead.</p>

<h2>Casting from your phone</h2>
<p>If your TV has no app store, GSE on a phone can cast to a Chromecast or AirPlay to an Apple TV. Casting is handy for a bedroom TV but depends on your phone staying on the same Wi-Fi. For a main TV, an app running on the TV itself is smoother: see <a href="/iptv-chromecast/">IPTV on Chromecast</a> and <a href="/iptv-apple-tv/">IPTV on Apple TV</a>.</p>

<h2>Common GSE Smart IPTV problems</h2>
<ul>
<li><strong>“Login failed” or empty list</strong>: check the server URL includes <code>http://</code> and the port, with no space at the end.</li>
<li><strong>Guide shows nothing</strong>: an M3U playlist doesn’t always carry the guide. Switch to the Xtream Codes login, or add the EPG link.</li>
<li><strong>Channels buffer</strong>: change the player engine in GSE’s player settings, then see our <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>App keeps the old list</strong>: pull down to refresh, or delete and re-add the entry after a renewal.</li>
</ul>

<h2>GSE vs other players</h2>
<p>GSE is a solid all-rounder on Apple devices. If you want a cable-style grid guide on Android TV or Fire TV, <a href="/tivimate/">TiviMate</a> is better. On iPhone and Apple TV, <a href="/iptvx/">IPTVX</a> has the most polished interface and <a href="/iplaytv/">iPlayTV</a> is simpler. Our <a href="/iptv-apps/">IPTV apps guide</a> compares them all.</p>
""",
        faq=[
            ("Is GSE Smart IPTV free?", "<p>It depends on the platform. The Apple TV app, GSE Smart IPTV Pro, is a one-time purchase on the App Store; other versions are free to install with optional purchases. Check the listing on your device. The app never includes channels.</p>"),
            ("Does GSE Smart IPTV work with IPTVMaple?", "<p>Yes. Add your IPTVMaple Xtream Codes login or M3U link. Start with our free 24-hour trial to test it on your device first.</p>"),
            ("Is GSE Smart IPTV on Apple TV?", "<p>Yes, as GSE Smart IPTV Pro on the tvOS App Store. It supports Xtream Codes logins, M3U playlists and XMLTV guides.</p>"),
            ("Can GSE Smart IPTV cast to Chromecast?", "<p>The mobile apps can cast to Chromecast and AirPlay. On a Chromecast with Google TV you can also install an Android player directly.</p>"),
            ("Why are there several GSE apps in the store?", "<p>The developer publishes separate apps per platform, such as the Pro version for Apple TV. Install the one listed for your device; setup is the same.</p>"),
        ],
        related=["iptv-iphone", "iptv-apple-tv", "iptv-chromecast", "iptvx", "iplaytv"],
        keywords=["gseiptv", "gse iptv", "gse smart iptv", "gse smart iptv pro", "gse iptv player"],
    ),
    # ------------------------------------------------------------------ IPTVX
    dict(
        slug="iptvx", hub="apps", **D,
        title="IPTVX App Setup: Apple TV, iPhone, iPad & Mac | IPTVMaple",
        description="IPTVX setup for Apple TV, iPhone, iPad and Mac: add your Xtream or M3U login, get the TV guide and catch-up working, and what the subscription unlocks.",
        kicker="IPTV apps", h1='<span class="grad-text">IPTVX</span> setup on Apple TV, iPhone & Mac',
        lead="IPTVX is the most polished IPTV player on Apple devices. Here is how to add your login and get the guide, catch-up and multi-screen working.",
        crumb="IPTVX", blurb="Polished player for Apple TV, iPhone, iPad and Mac.",
        answer="<p><strong>IPTVX</strong> is an IPTV player for <strong>iPhone, iPad, Apple TV, Mac and Apple Vision</strong>, made by Bending X. It plays your own sources (<strong>Xtream Codes API, M3U/M3U8</strong>, Plex and SMB shares) and does not provide channels. It is free to download, with an in-app subscription for the full feature set. Add the Xtream login IPTVMaple sends you and the guide, movies and series load automatically.</p>",
        body="""
<h2>Why Apple users pick IPTVX</h2>
<ul>
<li><strong>One app, every Apple screen</strong>: iPhone, iPad, Apple TV, Mac and Vision Pro, with your sources synced through iCloud.</li>
<li><strong>Proper TV guide</strong>: EPG with search, so you can find a game by team name.</li>
<li><strong>Catch-up (TV archive)</strong>: replay recent programmes on channels that offer it.</li>
<li><strong>Multi-screen</strong>: watch several channels at once, useful for game nights.</li>
<li><strong>Picture-in-picture and AirPlay 2</strong> on iPhone and iPad.</li>
<li><strong>Dolby Vision, HDR10 and HLG</strong> playback where the stream supports it.</li>
</ul>
<p>The developer’s App Store listing is explicit that IPTVX “does not provide content”. It is a player, the same way Safari is a browser.</p>

<h2>Step-by-step: IPTVX with IPTVMaple</h2>
<ol>
<li>Install <strong>IPTVX</strong> from the App Store on your Apple TV, iPhone, iPad or Mac.</li>
<li>Open it and choose to add a source, then pick <strong>Xtream Codes</strong> (or <strong>M3U</strong> if you prefer the playlist link).</li>
<li>Enter the <strong>server URL, username and password</strong> from our email or WhatsApp message.</li>
<li>Let the first sync finish; large libraries take a minute. Live TV, the guide, movies and series then appear.</li>
<li>Sign in with the same Apple ID on your other devices: iCloud sync brings the source across, so you only type it once.</li>
</ol>
<p>Each device that plays at the same time counts as one connection on your IPTV plan. If two people watch on two screens at once, choose a 2-device plan; see <a href="/iptv-plans-canada/">all plans</a>.</p>

<h2>Free version vs subscription</h2>
<p>IPTVX is free to download, and the developer sells monthly, yearly and family-sharing subscriptions in the app. The subscription is paid to the app developer through Apple, separately from your channel subscription with us. Use the free version and our <a href="/try-iptv-canada/">24-hour trial</a> together before paying for either.</p>

<h2>Fixing common IPTVX issues</h2>
<ul>
<li><strong>Guide empty after adding an M3U link</strong>: add the EPG link we sent, or use the Xtream Codes login, which brings the guide automatically.</li>
<li><strong>Catch-up icon missing</strong>: catch-up only appears on channels whose stream offers an archive.</li>
<li><strong>Apple TV stutters on 4K</strong>: use Ethernet on Apple TV 4K models that have a port, and see our <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>Login rejected after renewal</strong>: edit the source and re-enter the password from your renewal message.</li>
</ul>

<h2>IPTVX or another Apple player?</h2>
<p>IPTVX is the pick if you want the best-looking interface across all your Apple devices. <a href="/iplaytv/">iPlayTV</a> is simpler, <a href="/smarters-player-lite/">Smarters Player Lite</a> is free, and <a href="/gse-smart-iptv/">GSE Smart IPTV</a> adds Chromecast casting. TiviMate isn’t available on Apple devices. For Mac users, see <a href="/iptv-pc-mac/">IPTV on PC and Mac</a>.</p>
""",
        faq=[
            ("Is IPTVX free?", "<p>IPTVX is free to download, with optional in-app subscriptions sold by the developer through Apple. It doesn’t include channels: you add an IPTV subscription such as IPTVMaple.</p>"),
            ("Does IPTVX work on Apple TV?", "<p>Yes. IPTVX runs on Apple TV, iPhone, iPad, Mac and Apple Vision, and can sync your sources between them with iCloud.</p>"),
            ("Is there an IPTVX app for Android?", "<p>The IPTVX App Store app is for Apple devices. On Android phones, Android TV and Fire TV, use TiviMate or IPTV Smarters Pro with the same IPTVMaple login.</p>"),
            ("Does IPTVX support Xtream Codes?", "<p>Yes. It supports Xtream Codes API logins as well as M3U and M3U8 playlists, Plex and SMB sources.</p>"),
            ("Can I watch on my iPhone and Apple TV at the same time?", "<p>Yes, if your plan covers two devices. Each screen playing at the same time uses one connection.</p>"),
        ],
        related=["iptv-apple-tv", "iptv-iphone", "iptv-pc-mac", "gse-smart-iptv", "iplaytv"],
        keywords=["iptvx", "iptvx apple tv", "iptvx android", "iptvx app", "iptv x app"],
    ),
    # ------------------------------------------------------------------ OTT Navigator
    dict(
        slug="ott-navigator", hub="apps", **D,
        title="OTT Navigator IPTV Setup on Android TV & Firestick | IPTVMaple",
        description="OTT Navigator IPTV setup on Android TV, Google TV and Fire TV: add your provider, enable catch-up, what Premium adds and the OttNav Companion app.",
        kicker="IPTV apps", h1='<span class="grad-text">OTT Navigator</span> IPTV setup',
        lead="A powerful Android player with catch-up, timeshift and a media library. Here is how to set it up and what Premium really means.",
        crumb="OTT Navigator", blurb="Android TV player with catch-up and timeshift.",
        answer="<p><strong>OTT Navigator IPTV</strong> is an Android player by SIA Scillarium Studio for phones, tablets, Android TV and TV boxes. It “does not provide any video by itself”: you add your provider’s playlist or login. It supports live TV with <strong>timeshift and catch-up</strong> where your provider has an archive, picture-in-picture, multi-stream viewing and a movies library. Premium features are bought per device, managed with the <strong>OttNav Companion</strong> app on devices without Google Play.</p>",
        body="""
<h2>What OTT Navigator does well</h2>
<ul>
<li><strong>Catch-up and timeshift</strong>: rewind live TV or replay recent programmes on channels with an archive.</li>
<li><strong>Media library</strong>: movies and series filtered by category, genre, season and year, with resume where you stopped.</li>
<li><strong>Picture-in-picture and multi-stream</strong>: keep a game in a corner while browsing.</li>
<li><strong>AFR (auto frame rate)</strong>: switches your TV’s refresh rate to match the channel, which smooths motion on sports.</li>
<li><strong>Local network files</strong> via UPnP/DLNA.</li>
</ul>

<h2>Free vs Premium</h2>
<p>The app is free to install and play with. Premium unlocks extra features and is tied to devices: you buy device slots, and the developer’s <strong>OttNav Companion</strong> app lets you add or remove devices and buy more slots for boxes that don’t have Google Play, such as a Fire TV Stick. Premium is paid to the developer, not to IPTVMaple, and is separate from your channel subscription.</p>
<p>Avoid “Premium unlocked” APK downloads from third-party sites. Modified apps can carry malware and they cut off the developer who maintains the player.</p>

<h2>Step-by-step: OTT Navigator with IPTVMaple</h2>
<ol>
<li>Install <strong>OTT Navigator IPTV</strong> from Google Play on your Android TV, Google TV or phone. On a Fire TV Stick, use the developer’s official download through the Downloader app (see our <a href="/iptv-firestick/">Firestick guide</a>).</li>
<li>Open the app. When asked for a provider, choose the <strong>Xtream Codes</strong> option and enter the <strong>server URL, username and password</strong> from our message. You can also choose a playlist and paste the <strong>M3U link</strong>.</li>
<li>Wait for channels, guide and the movie library to load.</li>
<li>Open a channel with a catch-up icon to test the archive, then set the guide to your time zone in the settings.</li>
</ol>

<h2>Common OTT Navigator problems</h2>
<ul>
<li><strong>Guide one hour off</strong>: set the EPG time shift in the provider settings, or check your box’s time zone.</li>
<li><strong>Catch-up missing</strong>: only channels with an archive on the provider side show it.</li>
<li><strong>Stutter on 4K or sports</strong>: try the other player engine in the playback settings, use Ethernet, and see <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>Premium not recognised on a new box</strong>: add the device in OttNav Companion or remove an old one to free a slot.</li>
</ul>

<h2>OTT Navigator vs TiviMate</h2>
<table>
<thead><tr><th></th><th>OTT Navigator</th><th><a href="/tivimate/">TiviMate</a></th></tr></thead>
<tbody>
<tr><td>Platforms</td><td>Android phone, tablet, Android TV, boxes</td><td>Android TV, Fire TV, boxes (TV-focused)</td></tr>
<tr><td>Guide</td><td>Full EPG</td><td>Cable-style grid, the reference for this</td></tr>
<tr><td>Catch-up / timeshift</td><td>Yes</td><td>Catch-up yes; recording with Premium</td></tr>
<tr><td>Movies &amp; series library</td><td>Strong, with filters</td><td>Basic</td></tr>
<tr><td>Paid tier</td><td>Premium per device</td><td><a href="/tivimate-premium/">TiviMate Premium</a> per account</td></tr>
</tbody>
</table>
<p>Choose TiviMate for the classic TV-guide experience and OTT Navigator if you watch a lot of on-demand content or want it on a phone too. Both work with the same IPTVMaple login.</p>
""",
        faq=[
            ("Is OTT Navigator free?", "<p>The app is free to install and use. Premium features are an in-app purchase tied to devices. Channels always come from your IPTV subscription.</p>"),
            ("What is OttNav Companion?", "<p>An app from the same developer, SIA Scillarium Studio, that manages Premium on devices without Google Play: adding or removing devices and buying more slots.</p>"),
            ("Does OTT Navigator work on Firestick?", "<p>Yes, it runs on Fire TV, but it isn’t in the Amazon Appstore, so it is installed with the Downloader app. Premium on Fire TV is managed with OttNav Companion.</p>"),
            ("Does OTT Navigator work with IPTVMaple?", "<p>Yes, with your Xtream Codes login or M3U link. Try it with our free 24-hour trial first.</p>"),
            ("Should I download OTT Navigator Premium APKs?", "<p>No. “Premium unlocked” APKs are modified apps from unofficial sites and can contain malware. Install the official app and buy Premium from the developer if you need it.</p>"),
        ],
        related=["tivimate", "iptv-android-tv", "iptv-firestick", "iptv-recording-catch-up", "iptv-apps"],
        keywords=["ott navigator", "ott navigator premium", "ottnavigator", "ott navigator iptv", "ott navigator firestick"],
    ),
    # ------------------------------------------------------------------ Purple players
    dict(
        slug="purple-iptv", hub="apps", **D,
        title="Purple IPTV Player Setup: Samsung & Android | IPTVMaple",
        description="Purple IPTV players explained: IPTV Smart Purple Player and the Purple Smart TV app for Samsung. Add your Xtream login or M3U link and fix common errors.",
        kicker="IPTV apps", h1='<span class="grad-text">Purple IPTV</span> player setup',
        lead="“Purple IPTV” usually means one of the Purple Smart players. Here is which one you have and how to add your login.",
        crumb="Purple IPTV", blurb="IPTV Smart Purple Player and the Samsung TV app.",
        answer="<p>“<strong>Purple IPTV</strong>” refers to the Purple Smart family of players: <strong>IPTV Smart Purple Player</strong> for Android devices and the <strong>Purple Smart TV</strong> app, which the developer lists on the <strong>Samsung</strong> store. They are players only: the developer states the apps “do not come with any media content”. You add your IPTV login, such as the Xtream Codes details or M3U link IPTVMaple sends you.</p>",
        body="""
<h2>Which Purple app is which</h2>
<table>
<thead><tr><th>App</th><th>Where you find it</th><th>Typical use</th></tr></thead>
<tbody>
<tr><td>IPTV Smart Purple Player</td><td>Android phones, Android TV boxes (check the store on your device)</td><td>Phone or TV box player with live TV, movies and series</td></tr>
<tr><td>Purple Smart TV app</td><td>Samsung Smart TVs (Tizen), per the developer’s site</td><td>A player that runs on the TV itself</td></tr>
<tr><td>LG version</td><td>Listed as “coming soon” by the developer at the time of writing</td><td>Use another LG player meanwhile</td></tr>
</tbody>
</table>
<p>Store listings for IPTV players come and go, and copies with similar names appear often. Install only the listing published by Purple Smart, and never one that promises channels: a real player never includes them.</p>

<h2>Step-by-step: a Purple player with IPTVMaple</h2>
<ol>
<li>Install the Purple app from your device’s store.</li>
<li>On first launch, choose the option to log in with <strong>Xtream Codes API</strong> (or add an <strong>M3U URL</strong>).</li>
<li>Type any name, then the <strong>server URL, username and password</strong> from our email or WhatsApp message.</li>
<li>Wait for the channels, guide and on-demand sections to download, then open Live TV.</li>
<li>Add channels to favourites so the ones you watch most open first.</li>
</ol>

<h2>Common Purple player issues</h2>
<ul>
<li><strong>“Invalid credentials”</strong>: retype the password; capitals and zeros versus the letter O are the usual culprits.</li>
<li><strong>Guide empty</strong>: use the Xtream login rather than M3U, which carries the guide automatically.</li>
<li><strong>App not in your TV’s store</strong>: Samsung and LG stores vary by model year and country. Try <a href="/duplecast/">Duplecast</a>, <a href="/smartone-iptv/">SmartOne</a> or <a href="/set-iptv/">SET IPTV</a> instead.</li>
<li><strong>Freezing</strong>: restart the TV and router, then see <a href="/iptv-buffering-fix/">IPTV buffering fixes</a>.</li>
</ul>

<h2>Is a Purple player the right choice?</h2>
<p>Purple players are a reasonable option on Samsung TVs and Android devices. If your TV runs Google TV or Android TV, or you use a Fire TV Stick, <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> remain the most widely used players. The <a href="/iptv-smart-tv/">smart TV guide</a> lists the best app for each TV brand.</p>
""",
        faq=[
            ("What is Purple IPTV?", "<p>Usually the Purple Smart IPTV players: IPTV Smart Purple Player for Android and the Purple Smart TV app for Samsung. They are players, not channel providers.</p>"),
            ("Does Purple IPTV include channels?", "<p>No. The developer states the apps come with no media content. You add your own IPTV subscription, such as IPTVMaple.</p>"),
            ("Is the Purple player on LG TVs?", "<p>The developer lists the LG version as coming soon at the time of writing. On LG, use Duplecast, SmartOne or SS IPTV.</p>"),
            ("Does the Purple player work with IPTVMaple?", "<p>Yes, with your Xtream Codes login or M3U link. Test it with our free 24-hour trial.</p>"),
        ],
        related=["iptv-samsung-tv", "iptv-smart-tv", "iptv-smarters-pro", "duplecast"],
        keywords=["purple iptv", "iptv purple", "iptv smart purple player", "purple iptv player", "purple smart tv"],
    ),
]

DEVICES = [
    # ------------------------------------------------------------------ onn 4K box
    dict(
        slug="onn-tv-box-iptv", hub="devices", **D,
        title="onn TV Box IPTV: Set Up the onn 4K Pro for Live TV | IPTVMaple",
        description="Use an onn TV box (Walmart onn 4K and 4K Pro, Google TV) for IPTV: install TiviMate or Smarters, add your login, Ethernet tips and buying advice for Canada.",
        kicker="Devices", h1='<span class="grad-text">onn TV box</span> for IPTV: setup guide',
        lead="Walmart’s onn boxes run Google TV, which makes them one of the cheapest good IPTV boxes. Here is how to set one up.",
        crumb="onn TV box", blurb="Walmart’s Google TV box: TiviMate in minutes.",
        answer="<p>An <strong>onn TV box</strong> is Walmart’s own-brand streaming device running <strong>Google TV</strong>. Because it has Google Play, you can install <strong>TiviMate</strong> or <strong>IPTV Smarters Pro</strong> directly and log in with your IPTV details. The <strong>onn 4K Pro</strong> is the better pick for IPTV: reviewers list <strong>3 GB of RAM, 32 GB of storage, an Ethernet port</strong> and a USB port, plus Dolby Vision and Atmos.</p>",
        body="""
<h2>onn 4K vs onn 4K Pro for IPTV</h2>
<table>
<thead><tr><th></th><th>onn 4K Pro</th><th>onn 4K streaming box / stick</th></tr></thead>
<tbody>
<tr><td>System</td><td>Google TV</td><td>Google TV</td></tr>
<tr><td>Memory &amp; storage</td><td>3 GB RAM, 32 GB</td><td>Less memory and storage</td></tr>
<tr><td>Ethernet</td><td>Built in</td><td>Wi-Fi only on most models (USB adapter possible)</td></tr>
<tr><td>Best for</td><td>Main TV, sports, 4K channels, large channel lists</td><td>Second TV, lighter use</td></tr>
</tbody>
</table>
<p>For IPTV the two numbers that matter are memory and the wired port. Large channel lists and a full TV guide use RAM, and Ethernet removes most buffering caused by Wi-Fi. That is why we recommend the Pro.</p>

<h2>Buying an onn box in Canada</h2>
<p>onn is a Walmart brand. Some Walmart.com listings carry a “U.S. compatible only” note, and model availability differs between Walmart US and Walmart Canada, so check the listing before you order. If you can’t get one, a <a href="/iptv-firestick/">Fire TV Stick 4K</a>, a <a href="/iptv-chromecast/">Google TV Streamer</a> or an <a href="/iptv-android-tv/">Android TV box</a> does the same job with the same apps.</p>

<h2>Step-by-step: IPTV on an onn box</h2>
<ol>
<li>Connect the box, sign in with your Google account, and plug in Ethernet if you have the Pro.</li>
<li>Open <strong>Google Play</strong> on the box and install <a href="/tivimate/">TiviMate</a> (best TV guide) or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> (simplest login).</li>
<li>Open the app and choose <strong>Xtream Codes</strong>. Enter the server URL, username and password from our email or WhatsApp message.</li>
<li>Let the channels and guide load, then add your favourite channels to a favourites group.</li>
<li>In the box’s display settings, turn on <strong>match frame rate</strong> if available; sports look smoother.</li>
</ol>
<p>You don’t need to sideload anything: both apps are on Google Play for Google TV. If you want an app that isn’t, install <strong>Downloader</strong> from Google Play and allow it under <em>Settings → System → About</em> (developer options) and <em>Apps → Security → Unknown sources</em>.</p>

<h2>Getting the most from the onn box</h2>
<ul>
<li><strong>Free up space</strong>: uninstall pre-installed apps you don’t use; TiviMate’s guide data likes storage.</li>
<li><strong>Use the remote’s input button</strong> to switch to the box quickly, and set TiviMate to open on startup.</li>
<li><strong>Restart weekly</strong>: Google TV boxes keep apps in memory; a restart clears it.</li>
<li><strong>Buffering on Wi-Fi?</strong> Move the router closer, use 5 GHz, or see our <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
</ul>
""",
        faq=[
            ("Is the onn TV box good for IPTV?", "<p>Yes. It runs Google TV, so TiviMate and IPTV Smarters Pro install from Google Play. The onn 4K Pro, with 3 GB of RAM and Ethernet, is the better choice for live TV and sports.</p>"),
            ("Can I buy an onn box in Canada?", "<p>onn is a Walmart brand and availability differs between Walmart US and Walmart Canada. Some US listings are marked “U.S. compatible only”, so check before ordering, or use a Fire TV Stick or Google TV Streamer instead.</p>"),
            ("Do I need to jailbreak an onn box for IPTV?", "<p>No. There is nothing to unlock: install an IPTV player from Google Play and add your login.</p>"),
            ("Which IPTV app is best on the onn 4K Pro?", "<p>TiviMate for a cable-style guide, IPTV Smarters Pro for the simplest setup. Both work with IPTVMaple.</p>"),
            ("How many onn boxes can I use with one subscription?", "<p>One per connection on your plan. For two TVs watching at the same time, choose a 2-device plan.</p>"),
        ],
        related=["iptv-box", "iptv-android-tv", "tivimate", "iptv-firestick"],
        keywords=["onn tv box", "onn 4k pro", "onn box iptv", "onn tv box iptv", "onn 4k box", "walmart onn box"],
    ),
]

GUIDES = [
    # ------------------------------------------------------------------ IPTV vs Netflix
    dict(
        slug="iptv-vs-netflix", hub="guides", **D,
        title="IPTV vs Netflix: Live TV vs On-Demand Streaming | IPTVMaple",
        description="IPTV vs Netflix compared: live channels and sports vs on-demand originals, how each works, devices, and why many households in Canada keep both. Try IPTV free.",
        kicker="IPTV guides", h1='IPTV vs <span class="grad-text">Netflix</span>: what’s the difference?',
        lead="People search “IPTV Netflix” for two reasons: to compare them, or to find Netflix inside an IPTV app. Here is a clear answer to both.",
        crumb="IPTV vs Netflix", blurb="Live channels vs on-demand originals.",
        answer="<p><strong>Netflix</strong> is an on-demand service: you choose a film or series from its own catalogue and watch whenever you like. <strong>IPTV</strong> delivers <strong>live TV channels</strong> over the internet, with a channel guide, live sports and news, often plus a movies and series library. They solve different problems, so many households keep both. Netflix is not a channel inside an IPTV subscription; you use the official Netflix app for it.</p>",
        body="""
<h2>Side-by-side comparison</h2>
<table>
<thead><tr><th></th><th>IPTV (IPTVMaple)</th><th>Netflix</th></tr></thead>
<tbody>
<tr><td>What you get</td><td>Live TV channels with a guide, plus movies and series on demand</td><td>On-demand films, series and Netflix originals</td></tr>
<tr><td>Live sports</td><td>Yes: NHL, NFL, NBA, soccer, UFC on their usual channels</td><td>Occasional live events only</td></tr>
<tr><td>News</td><td>Live news channels</td><td>No live news channels</td></tr>
<tr><td>Local Canadian channels</td><td>Yes</td><td>No</td></tr>
<tr><td>International channels</td><td>UK, French, Italian, Polish and many more</td><td>Foreign-language films and series, not channels</td></tr>
<tr><td>How you watch</td><td>An IPTV player app with your login</td><td>The Netflix app</td></tr>
<tr><td>Free trial</td><td>24 hours free</td><td>See Netflix’s own site</td></tr>
</tbody>
</table>

<h2>When IPTV is the better fit</h2>
<p>If you mainly want <strong>live TV</strong>, IPTV replaces cable: hockey on Saturday night, the news at six, a Premier League match in the morning. You browse by channel and time, the way you did with cable, and you can add international channels from home. See <a href="/what-is-iptv/">what IPTV is</a> and <a href="/iptv-sports/">IPTV for sports</a>.</p>

<h2>When Netflix is the better fit</h2>
<p>If you mostly binge series and films and never watch live, an on-demand service is simpler. Netflix’s originals are only on Netflix, and its app is built into almost every smart TV.</p>

<h2>Why “IPTV Netflix” confuses people</h2>
<ul>
<li><strong>Netflix runs on the same devices</strong>: a Fire TV Stick or Android TV box can run Netflix and an IPTV player side by side. Switching takes one button.</li>
<li><strong>“Netflix-style” apps</strong>: some IPTV players, such as <a href="/flix-iptv/">Flix IPTV</a>, borrow the look of a streaming app. They are still IPTV players, unrelated to Netflix.</li>
<li><strong>VOD sections</strong>: IPTV subscriptions often include movies and series, but that isn’t Netflix and doesn’t include Netflix originals.</li>
</ul>

<h2>Cost: replacing cable vs adding a service</h2>
<p>IPTVMaple plans start at <strong>${LOW}</strong> for one month, or about <strong>${PER_MONTH:.2f} a month</strong> on a 12-month plan for one screen. Netflix pricing depends on the plan you pick on its site. Compare IPTV with what you pay for cable or satellite rather than with Netflix: see <a href="/iptv-price/">IPTV prices</a> and our <a href="/cord-cutting-guide/">cord-cutting guide</a>.</p>

<h2>Using both on one TV</h2>
<ol>
<li>Get a device with an app store, such as a <a href="/iptv-firestick/">Fire TV Stick</a> or an <a href="/onn-tv-box-iptv/">onn 4K Pro</a>.</li>
<li>Install Netflix and an IPTV player (<a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>).</li>
<li>Log in to each with its own account. Pin both to the home screen.</li>
</ol>
""".replace("${LOW}", f"${LOW}").replace("${PER_MONTH:.2f}", f"${PER_MONTH:.2f}"),
        faq=[
            ("Is IPTV better than Netflix?", "<p>They do different jobs. IPTV is for live TV, sports and news channels; Netflix is for on-demand originals. If you want to replace cable, IPTV is the closer match.</p>"),
            ("Does IPTV include Netflix?", "<p>No. Netflix is a separate service with its own app and account. An IPTV subscription gives you live channels and an on-demand library, not Netflix originals.</p>"),
            ("Can I watch Netflix and IPTV on the same device?", "<p>Yes. Fire TV, Android TV and Google TV devices run both apps side by side.</p>"),
            ("What is Flix IPTV, is it Netflix?", "<p>Flix IPTV is an IPTV player app with a streaming-style design. It has no connection to Netflix.</p>"),
            ("Can I try IPTV before cancelling anything?", "<p>Yes. IPTVMaple has a free 24-hour trial and a 7-day refund policy on paid plans.</p>"),
        ],
        related=["what-is-iptv", "pluto-tv-vs-iptv", "iptv-vs-satellite", "iptv-price", "flix-iptv"],
        keywords=["iptv netflix", "ip tv netflix", "iptv vs netflix", "netflix vs iptv"],
    ),
    # ------------------------------------------------------------------ M3U checker
    dict(
        slug="iptv-checker", hub="guides", **D,
        title="IPTV Checker: Free M3U Playlist Checker Online | IPTVMaple",
        description="Free IPTV checker: paste an M3U playlist to count channels, groups and VOD, find duplicates and the EPG link. Runs in your browser; nothing is uploaded.",
        kicker="IPTV tools", h1='<span class="grad-text">IPTV checker</span>: test your M3U playlist',
        lead="Paste a playlist to see what is inside it before you load it on a TV. The check runs in your browser; nothing is sent to us.",
        crumb="IPTV checker", blurb="Free M3U playlist checker in your browser.",
        answer="<p>An <strong>IPTV checker</strong> reads an <strong>M3U playlist</strong> and reports what it contains. Paste your playlist text below to count <strong>channels, groups, movies and series</strong>, find <strong>duplicates</strong>, entries with no logo or guide ID, and the <strong>EPG link</strong>. It works offline in your browser. It can’t confirm that each stream plays, because browsers block direct stream tests; open the playlist in an IPTV player for that.</p>",
        body="""
<h2>Check a playlist</h2>
<div class="m3u-check card" data-m3u-check>
  <div class="field">
    <label for="m3u-input">Paste the contents of an M3U file <em>(starts with #EXTM3U)</em></label>
    <textarea id="m3u-input" class="input m3u-input" rows="8" spellcheck="false" placeholder="#EXTM3U&#10;#EXTINF:-1 tvg-id=&quot;cbc.ca&quot; group-title=&quot;Canada&quot;,CBC Toronto&#10;http://example.com/live/user/pass/1.ts"></textarea>
  </div>
  <div class="btn-row m3u-actions">
    <button type="button" class="btn btn--primary btn--sm" data-m3u-run>Check playlist</button>
    <label class="btn btn--ghost btn--sm m3u-file">Open .m3u file<input type="file" accept=".m3u,.m3u8,.txt,audio/x-mpegurl" data-m3u-file hidden></label>
  </div>
  <div class="m3u-out" data-m3u-out aria-live="polite"></div>
</div>
<p>Your playlist never leaves this page: the check is plain JavaScript running on your device. Even so, a playlist contains your login, so don’t paste it into checkers that upload it to a server.</p>

<h2>What the checker reports</h2>
<table>
<thead><tr><th>Check</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Valid header</td><td>A playlist must start with <code>#EXTM3U</code>; otherwise most apps reject it.</td></tr>
<tr><td>Entries and groups</td><td>How many channels and categories the list holds, and the biggest groups.</td></tr>
<tr><td>Live vs movies vs series</td><td>Guessed from the stream URLs (<code>/movie/</code>, <code>/series/</code>), the pattern Xtream Codes servers use.</td></tr>
<tr><td>EPG link</td><td>The <code>url-tvg</code> or <code>x-tvg-url</code> in the header. Without it, add the guide link separately.</td></tr>
<tr><td>Missing tvg-id</td><td>Channels without a guide ID show no programme information.</td></tr>
<tr><td>Missing logos</td><td>Cosmetic, but a sign of a hastily built list.</td></tr>
<tr><td>Duplicates</td><td>The same stream URL listed twice makes the list longer, not better.</td></tr>
<tr><td>Catch-up tags</td><td>Entries with <code>catchup</code> or <code>tvg-rec</code> attributes support replay in players such as TiviMate.</td></tr>
</tbody>
</table>

<h2>Why an online checker can’t test every stream</h2>
<p>Testing whether a stream plays means opening a connection to the provider’s server. Browsers block a web page from reading streams on other servers, and many IPTV servers only allow a limited number of connections per login, so mass-testing every channel could get a login temporarily blocked. The reliable test is simple: load the playlist in <a href="/vlc-iptv/">VLC</a> or an IPTV player and open a few channels from each group.</p>

<h2>Reading an M3U entry</h2>
<p>Each channel is two lines. The first holds the details, the second the stream address:</p>
<pre><code>#EXTINF:-1 tvg-id="cbc.ca" tvg-logo="https://…/cbc.png" group-title="Canada",CBC Toronto
http://server:port/live/username/password/12345.ts</code></pre>
<p><code>tvg-id</code> links the channel to the guide, <code>group-title</code> sets the category, and the text after the comma is the name you see. Our <a href="/m3u-playlist/">M3U playlist guide</a> explains every field.</p>

<h2>Checking your IPTVMaple playlist</h2>
<p>With an IPTVMaple subscription you rarely need a checker: logging in with Xtream Codes loads channels, guide, movies and series automatically. If a channel won’t play, send us its name on WhatsApp and we’ll check it from our side. Not a customer yet? Start the <a href="/try-iptv-canada/">free 24-hour trial</a> and check our playlist yourself.</p>
""",
        faq=[
            ("Is this IPTV checker safe?", "<p>Yes. The check runs entirely in your browser and the playlist is never uploaded. Still, treat your playlist like a password and don’t paste it into tools that send it to a server.</p>"),
            ("Can the checker tell me if channels are working?", "<p>No. Browsers block web pages from testing streams on other servers. Open the playlist in VLC or an IPTV player to confirm playback.</p>"),
            ("Can I check an M3U link instead of the file?", "<p>Open the link in your browser to download the file, then use “Open .m3u file” or paste its contents. The page doesn’t fetch links itself, so your login isn’t sent anywhere.</p>"),
            ("Why does my playlist have no EPG?", "<p>Many playlists don’t include the guide link in the header. Add the separate EPG link from your provider in your player, or use an Xtream Codes login, which loads the guide automatically.</p>"),
            ("What is an M3U8 file?", "<p>An M3U playlist saved as UTF-8. Players treat .m3u and .m3u8 playlists the same way, and this checker reads both.</p>"),
        ],
        related=["m3u-playlist", "watch-iptv-online", "xtream-codes-iptv", "vlc-iptv", "iptv-buffering-fix"],
        keywords=["iptv checker", "iptv checker online", "m3u checker", "m3u playlist checker", "iptv tester online"],
    ),
]

PAGES = APPS + DEVICES + GUIDES

# Existing pages that should link to the new ones (added to their "Related guides").
LINK_IN = {
    "iptv-iphone": ["gse-smart-iptv", "iptvx"],
    "iptv-apple-tv": ["iptvx", "gse-smart-iptv"],
    "iptv-chromecast": ["gse-smart-iptv"],
    "iptv-pc-mac": ["iptvx"],
    "tivimate": ["ott-navigator"],
    "iptv-recording-catch-up": ["ott-navigator"],
    "iptv-android-tv": ["ott-navigator", "onn-tv-box-iptv"],
    "iptv-samsung-tv": ["purple-iptv"],
    "iptv-smart-tv": ["purple-iptv"],
    "iptv-box": ["onn-tv-box-iptv"],
    "iptv-firestick": ["onn-tv-box-iptv"],
    "what-is-iptv": ["iptv-vs-netflix"],
    "flix-iptv": ["iptv-vs-netflix"],
    "pluto-tv-vs-iptv": ["iptv-vs-netflix"],
    "iptv-vs-satellite": ["iptv-vs-netflix"],
    "m3u-playlist": ["iptv-checker"],
    "watch-iptv-online": ["iptv-checker"],
    "liste-iptv-m3u": ["iptv-checker"],
    "vlc-iptv": ["iptv-checker"],
}


def link_in(pages):
    by = {p["slug"]: p for p in pages}
    for src, targets in LINK_IN.items():
        rel = by[src].setdefault("related", [])
        rel.extend(t for t in targets if t not in rel)
