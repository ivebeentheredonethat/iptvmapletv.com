"""IPTV player apps cluster. Hub: /iptv-apps/"""

HOW_LOGIN = """<p>Every IPTVMaple plan works with this app. After you order (or request the <a href="/try-iptv-canada/">free 24-hour trial</a>), we send your login on WhatsApp and by email: a <strong>server URL, username and password</strong> (Xtream Codes login) and, if your app prefers it, an <strong>M3U playlist link</strong>.</p>"""

PAGES = [
    # ------------------------------------------------------------------ HUB
    dict(
        slug="iptv-apps", hub="apps", hub_page=True,
        title="Best IPTV Apps & Players in Canada (2026) | IPTVMaple",
        description="The best IPTV player apps for every device in 2026: TiviMate, IPTV Smarters Pro, IMPlayer, XCIPTV, STBEmu and more — with setup guides for Canada.",
        kicker="IPTV apps", h1='The best <span class="grad-text">IPTV apps</span> &amp; players for 2026',
        lead="The best IPTV apps and players for 2026: an IPTV player is the app that plays your subscription. Here’s which one to use on each device — and how to set it up in minutes.",
        crumb="IPTV apps", blurb="Every IPTV player compared, with setup guides.",
        answer="<p>The best IPTV app depends on your device: <strong>TiviMate</strong> for Firestick and Android TV, <strong>IPTV Smarters Pro</strong> for phones, tablets and computers, <strong>Smarters Player Lite</strong> or <strong>iPlayTV</strong> for iPhone and Apple TV, and <strong>Smart IPTV</strong>, <strong>SmartOne</strong> or <strong>Flix IPTV</strong> for Samsung and LG smart TVs. IPTVMaple works with all of them.</p>",
        body="""
<h2>What is an IPTV player?</h2>
<p>An IPTV player is an app that connects to an IPTV subscription and turns it into a TV-style experience: a channel list, an electronic program guide (EPG), catch-up and a movies &amp; series library. The player does not include any channels by itself — your <a href="/iptv-plans-canada/">IPTV subscription</a> supplies the content, and the app displays it.</p>
<p>Most players accept one of three login types:</p>
<ul>
<li><strong>Xtream Codes API</strong> — server URL + username + password. The easiest and most complete (live TV, VOD, EPG in one login).</li>
<li><strong>M3U playlist URL</strong> — one long link that contains the channel list. Works almost everywhere, including VLC and Kodi.</li>
<li><strong>MAC / portal</strong> — used by MAG boxes, STBEmu and MyTVOnline on Formuler boxes.</li>
</ul>

<h2>Best IPTV app for each device</h2>
<table>
<thead><tr><th>Device</th><th>Recommended IPTV app</th><th>Also works</th></tr></thead>
<tbody>
<tr><td>Amazon Firestick / Fire TV</td><td><a href="/tivimate/">TiviMate</a></td><td>IPTV Smarters Pro, XCIPTV, IMPlayer</td></tr>
<tr><td>Android TV box / Google TV</td><td>TiviMate</td><td>IMPlayer, OTT Navigator, STBEmu</td></tr>
<tr><td>Formuler box</td><td><a href="/mytvonline/">MyTVOnline 3</a></td><td>TiviMate</td></tr>
<tr><td>MAG box</td><td>Built-in portal</td><td>—</td></tr>
<tr><td>Samsung / LG smart TV</td><td><a href="/smart-iptv/">Smart IPTV</a>, <a href="/smartone-iptv/">SmartOne</a>, <a href="/flix-iptv/">Flix IPTV</a></td><td>IBO Player, IMPlayer</td></tr>
<tr><td>iPhone, iPad, Apple TV</td><td><a href="/smarters-player-lite/">Smarters Player Lite</a>, <a href="/iplaytv/">iPlayTV</a></td><td>IMPlayer, IPTVX</td></tr>
<tr><td>Windows / Mac</td><td><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></td><td><a href="/vlc-iptv/">VLC</a>, <a href="/kodi-iptv/">Kodi</a></td></tr>
</tbody>
</table>

<h2>How we picked these IPTV players</h2>
<p>We answer setup questions on WhatsApp every day, so we see which apps cause the fewest problems. We ranked players on stability during live sports, how good the TV guide is, catch-up support, how easy the login is, and whether the app is still maintained in 2026.</p>

<h2>Free vs paid IPTV apps</h2>
<p>Several players are free to download but charge a small fee for premium features or activation — for example TiviMate Premium, Smart IPTV’s one-time activation, or SmartOne and Flix IPTV after their trial period. These fees go to the app developer, not to IPTVMaple. Your IPTVMaple subscription works with the free versions too.</p>
""",
        faq=[
            ("What is the best IPTV app in 2026?", "<p>For Firestick and Android TV, TiviMate is the most popular IPTV player thanks to its TV-style guide and catch-up. On phones and computers, IPTV Smarters Pro is the easiest choice. On Samsung and LG TVs, Smart IPTV, SmartOne or Flix IPTV work well.</p>"),
            ("Do IPTV apps come with channels?", "<p>No. IPTV players are empty apps — they only display the channels from your IPTV subscription. With IPTVMaple you get 50,000+ live channels and 300,000+ movies and series to load into the app of your choice.</p>"),
            ("Can I use more than one IPTV app with the same subscription?", "<p>Yes. You can install your login in several apps. The number of streams you can watch at the same time depends on your plan (1 to 5 devices).</p>"),
            ("Which IPTV app works on Samsung smart TVs?", "<p>Samsung’s Tizen TVs support Smart IPTV, SmartOne IPTV, Flix IPTV, IBO Player and a few others from the Samsung app store. See our <a href=\"/iptv-samsung-tv/\">Samsung TV IPTV guide</a>.</p>"),
        ],
        related=["iptv-devices", "what-is-iptv"],
        keywords=["iptv player", "iptvapp", "best iptv app", "best iptv apps", "iptv stream player", "ip tv stream player", "android iptv player", "iptv media player", "iptv online player", "smart iptv player", "iptv viewer", "lecteur iptv", "meilleur lecteur iptv"],
    ),
    # ------------------------------------------------------------------ SMARTERS PRO
    dict(
        slug="iptv-smarters-pro", hub="apps",
        title="IPTV Smarters Pro Setup Guide & Login (2026) | IPTVMaple",
        description="How to install IPTV Smarters Pro on Firestick, Android, iPhone, PC and Mac, and log in with Xtream Codes. Works with IPTVMaple — try free for 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">IPTV Smarters Pro</span>: setup guide &amp; login',
        lead="The most widely used IPTV player — on Firestick, Android, iPhone, Windows and Mac. Install it, add your login, and start watching in five minutes.",
        crumb="IPTV Smarters Pro", blurb="Install and log in on every device.",
        answer="<p><strong>IPTV Smarters Pro</strong> is a free IPTV player app for Android, Firestick, iOS, Windows and macOS. It doesn’t include channels — you log in with your IPTV provider’s details (Xtream Codes: server URL, username, password). With an IPTVMaple subscription you get 50,000+ live channels, movies and series inside the app.</p>",
        body=f"""
<h2>What is IPTV Smarters Pro?</h2>
<p>IPTV Smarters Pro is a video player built for IPTV subscriptions. It shows live TV with a program guide, a movies and series (VOD) library, catch-up for supported channels, favourites and parental controls. It supports multiple user profiles, so one app can hold several subscriptions.</p>
<p>It is one of the most searched IPTV apps in Canada, and for good reason: the interface is simple, it runs on almost everything, and the login takes one minute.</p>

<h2>How to install IPTV Smarters Pro</h2>
<h3>On Android phones and tablets</h3>
<p>Search for IPTV Smarters Pro in the Google Play Store. If it isn’t listed in your region, download the APK from the official IPTV Smarters website and allow installation from your browser.</p>
<h3>On Amazon Firestick</h3>
<ol>
<li>Install the free <strong>Downloader</strong> app from the Amazon Appstore.</li>
<li>Go to <em>Settings → My Fire TV → Developer options</em> and allow Downloader to install unknown apps.</li>
<li>In Downloader, enter the official IPTV Smarters download link and install the APK.</li>
</ol>
<p>Full walkthrough with screenshots: <a href="/iptv-firestick/">IPTV on Firestick</a>.</p>
<h3>On iPhone, iPad and Apple TV</h3>
<p>On Apple devices the App Store version is called <a href="/smarters-player-lite/">Smarters Player Lite</a>. It uses the same login.</p>
<h3>On Windows and Mac</h3>
<p>Download the desktop version from the official IPTV Smarters website. See our <a href="/iptv-pc-mac/">IPTV on PC and Mac guide</a> for alternatives like VLC.</p>

<h2>How to log in to IPTV Smarters Pro</h2>
{HOW_LOGIN}
<ol>
<li>Open the app and choose <strong>Login with Xtream Codes API</strong>.</li>
<li>Enter any name (e.g. “IPTVMaple”), then your username, password and server URL exactly as we sent them.</li>
<li>Tap <strong>Add user</strong>. Channels, movies, series and the TV guide load automatically.</li>
</ol>

<h2>IPTV Smarters Pro not working? Quick fixes</h2>
<ul>
<li><strong>“Invalid username or password”</strong> — check for spaces and capital letters; copy-paste from our message.</li>
<li><strong>Buffering</strong> — use a wired connection or 5 GHz Wi-Fi; aim for 25 Mbps for 4K.</li>
<li><strong>Empty TV guide</strong> — open Settings → EPG and tap “Update EPG”.</li>
<li><strong>Can’t find it on Google Play</strong> — install the APK from the official site, or use <a href="/tivimate/">TiviMate</a> on Android TV.</li>
</ul>
<p>Still stuck? Message us on WhatsApp — our team sets up Smarters with customers every day.</p>
<h2>IPTV Smarters Pro features explained</h2>
<ul>
<li><strong>Live TV with EPG</strong> — channel groups on the left, program info below.</li>
<li><strong>Movies and series</strong> — posters, descriptions, ratings and “continue watching”.</li>
<li><strong>Catch-up</strong> — replay recent programs on supported channels.</li>
<li><strong>Multi-screen</strong> — watch up to four channels at once on tablets and computers (each counts as a stream on your plan).</li>
<li><strong>Parental control</strong> — lock categories behind a PIN.</li>
<li><strong>External players</strong> — send streams to VLC or MX Player if a channel doesn’t play smoothly in the built-in player.</li>
<li><strong>Multiple profiles</strong> — keep several subscriptions or family members separate.</li>
</ul>

<h2>Best settings in IPTV Smarters Pro</h2>
<ol>
<li><strong>Settings → Player selection</strong>: try the built-in player first; if you see stutter on sports, switch to “VLC” for live TV.</li>
<li><strong>Settings → Time format / Time zone</strong>: set your province’s time zone so the guide matches.</li>
<li><strong>Settings → EPG timeline</strong>: adjust by ±1 hour if programs look shifted.</li>
<li><strong>Automation</strong>: enable automatic channel and EPG refresh when the app starts.</li>
</ol>

<h2>IPTV Smarters Pro vs TiviMate</h2>
<table>
<thead><tr><th></th><th>IPTV Smarters Pro</th><th><a href="/tivimate/">TiviMate</a></th></tr></thead>
<tbody>
<tr><td>Price</td><td>Free</td><td>Free; Premium optional</td></tr>
<tr><td>Devices</td><td>Android, Firestick, iOS (Lite), Windows, Mac</td><td>Android TV, Fire TV only</td></tr>
<tr><td>Guide</td><td>Good</td><td>Excellent (cable-style grid)</td></tr>
<tr><td>Best for</td><td>Phones, tablets, computers, first-time users</td><td>Daily TV watching with a remote</td></tr>
</tbody>
</table>
<p>Many customers use both: Smarters on the phone, TiviMate on the living-room TV — with the same IPTVMaple login.</p>

<h2>Is IPTV Smarters Pro safe?</h2>
<p>The app itself is a player and is safe when downloaded from an official source: the Google Play Store, Apple’s App Store (Smarters Player Lite) or the official IPTV Smarters website. Avoid “modded” or “pro unlocked” APKs from random sites — they’re a common way to spread malware. IPTVMaple never asks you to install modified apps.</p>

<h2>How to update IPTV Smarters Pro</h2>
<p>Store versions update automatically. If you installed the APK on a Firestick, repeat the Downloader install with the latest official file — your profiles stay saved.</p>
""",
        faq=[
            ("Is IPTV Smarters Pro free?", "<p>Yes, the app is free to download. It does not include channels: you need an IPTV subscription such as IPTVMaple to watch live TV, movies and series in it.</p>"),
            ("Does IPTV Smarters Pro work on Firestick?", "<p>Yes. Install it with the Downloader app after enabling “install unknown apps” for Downloader in Developer options. Our <a href=\"/iptv-firestick/\">Firestick guide</a> shows every step.</p>"),
            ("What’s the difference between IPTV Smarters Pro and Smarters Player Lite?", "<p>Smarters Player Lite is the version published on Apple’s App Store for iPhone, iPad and Apple TV. It uses the same Xtream Codes or M3U login as Smarters Pro.</p>"),
            ("Can I use IPTV Smarters Pro on several devices?", "<p>Yes, install it on each device and use the same login. How many can play at the same time depends on your IPTVMaple plan — from 1 to 5 devices.</p>"),
            ("Why can’t I find IPTV Smarters Pro on Google Play?", "<p>Availability in app stores changes from time to time. You can install the official APK from the IPTV Smarters website, or use another player like TiviMate or IMPlayer with the same login.</p>"),
            ('Can I watch multiple channels at once in IPTV Smarters Pro?', '<p>Yes, the multi-screen feature shows up to four channels on tablets and computers. Each stream counts toward your plan’s device limit.</p>'),
            ('Is IPTV Smarters Pro safe to install?', '<p>Yes, when you install it from an official app store or the official IPTV Smarters website. Avoid modified APKs from unknown sites.</p>'),
            ('How do I fix buffering in IPTV Smarters Pro?', '<p>Switch the live TV player to VLC in Settings → Player selection, use a wired or 5 GHz connection, and restart the app after changing settings.</p>'),
        ],
        related=["smarters-player-lite", "tivimate", "iptv-firestick", "xtream-codes-iptv"],
        keywords=["ip tv smarters pro", "iptv smarters", "smarters pro", "smarterspro", "iptv smarter", "iptv smarters pro", "ip tv smarters", "iptv smarter pro", "iptv smart pro", "smarters iptv pro", "smarters pro iptv", "iptv smarters pro firestick", "iptv smarters pro android", "iptv smarters pro pc", "iptv smarters pro free", "iptv smarters downloader", "iptv smarters player", "iptv smasters pro subscription", "iptvsmarterspro", "tv smarters pro", "smarters pro firestick", "smarters pro pc"],
    ),
    # ------------------------------------------------------------------ TIVIMATE
    dict(
        slug="tivimate", hub="apps",
        title="TiviMate IPTV Player: Setup, Premium & Firestick | IPTVMaple",
        description="Set up TiviMate IPTV Player on Firestick and Android TV, what TiviMate Premium adds, and how to add your playlist. Works with IPTVMaple — try free for 24h.",
        kicker="IPTV apps", h1='<span class="grad-text">TiviMate</span> IPTV Player: setup &amp; Premium guide',
        lead="The favourite IPTV player on Firestick and Android TV — a real cable-box guide, catch-up and recording. Here’s how to set it up with your subscription.",
        crumb="TiviMate", blurb="The best IPTV player for Firestick & Android TV.",
        answer="<p><strong>TiviMate</strong> is an IPTV player for Android TV devices — Firestick, Fire TV, Nvidia Shield, Chromecast with Google TV and Android boxes. It’s free to install; <strong>TiviMate Premium</strong> is a paid upgrade that unlocks multiple playlists, catch-up, recording and more. Add your IPTVMaple login (Xtream Codes or M3U) and your channels appear with a full TV guide.</p>",
        body=f"""
<h2>Why TiviMate is so popular</h2>
<p>TiviMate looks and feels like a cable box: a grid TV guide, channel groups, a “recently watched” row and fast zapping with the remote. For Canadians switching from Bell, Rogers or Vidéotron, it’s the most familiar IPTV experience.</p>
<ul>
<li>Grid EPG (TV guide) with up to two weeks of program data</li>
<li>Catch-up on supported channels</li>
<li>Recording to device storage (Premium)</li>
<li>Multiple playlists and favourites lists (Premium)</li>
<li>Picture-in-picture and multi-view on supported devices (Premium)</li>
</ul>

<h2>Which devices support TiviMate?</h2>
<p>TiviMate runs on <strong>Android TV and Fire TV</strong> only: Amazon Firestick and Fire TV Cube, Nvidia Shield, Chromecast with Google TV, Google TV Streamer, Formuler and most Android TV boxes. It is <strong>not available</strong> on iPhone, Apple TV, Samsung, LG or Roku — on those devices, see our <a href="/iptv-apps/">IPTV apps guide</a>.</p>

<h2>How to install TiviMate on Firestick</h2>
<ol>
<li>Install <strong>Downloader</strong> from the Amazon Appstore.</li>
<li>Enable <em>Settings → My Fire TV → Developer options → Install unknown apps → Downloader</em>.</li>
<li>Open Downloader and install the TiviMate APK from the developer’s official source.</li>
<li>Open TiviMate and choose <strong>Add playlist</strong>.</li>
</ol>
<p>On Android TV and Google TV devices, TiviMate is in the Google Play Store — no sideloading needed. More detail in our <a href="/iptv-firestick/">Firestick IPTV guide</a>.</p>

<h2>How to add your IPTV playlist to TiviMate</h2>
{HOW_LOGIN}
<ol>
<li>Choose <strong>Add playlist → Xtream Codes</strong> (recommended) or <strong>M3U playlist</strong>.</li>
<li>Enter the server URL, username and password, then press <strong>Next</strong>.</li>
<li>TiviMate loads channels, movies, series and the TV guide. Name the playlist and press <strong>Done</strong>.</li>
</ol>

<h2>TiviMate Premium: is it worth it?</h2>
<p>TiviMate Premium is sold by the developer through the <em>TiviMate Companion</em> app, as a yearly or lifetime licence (check the Companion app for the current price). One purchase can be used on several devices. If you watch a lot of live TV and sports, the catch-up, recording and multi-playlist features are worth it. If you mainly watch movies and series, the free version is enough.</p>
<p>Your IPTVMaple subscription and TiviMate Premium are separate purchases — we don’t sell TiviMate accounts.</p>
<h2>TiviMate vs IPTV Smarters vs IMPlayer</h2>
<table>
<thead><tr><th></th><th>TiviMate</th><th>IPTV Smarters Pro</th><th>IMPlayer</th></tr></thead>
<tbody>
<tr><td>Devices</td><td>Android TV, Fire TV</td><td>Android, Fire TV, iOS (Lite), PC, Mac</td><td>Android TV, Fire TV, Apple</td></tr>
<tr><td>TV guide</td><td>Full grid, best in class</td><td>List + grid</td><td>Grid</td></tr>
<tr><td>Catch-up</td><td>Premium</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Recording</td><td>Premium</td><td>Limited</td><td>Premium</td></tr>
<tr><td>Multiple playlists</td><td>Premium</td><td>Yes (profiles)</td><td>Yes</td></tr>
<tr><td>Best for</td><td>Live TV and sports on the big screen</td><td>Phones, tablets, computers</td><td>Mixed Android + Apple homes</td></tr>
</tbody>
</table>

<h2>Best TiviMate settings for Canadian viewers</h2>
<ul>
<li><strong>Hide groups you don’t watch</strong> — <em>Settings → Playlists → Manage groups</em>. Keep “Canada”, “Canada Sports”, “Québec” and your favourites; big international lists feel instant once trimmed.</li>
<li><strong>EPG update interval</strong> — set to every 12 or 24 hours under <em>Settings → EPG</em> so the guide stays current without slowing startup.</li>
<li><strong>Time shift</strong> — if programs look off by an hour or more, adjust <em>EPG time shift</em> for your province (Atlantic, Eastern, Central, Mountain or Pacific).</li>
<li><strong>Auto frame rate</strong> — <em>Settings → Playback</em>: turn on for smoother hockey and soccer on 60 Hz TVs.</li>
<li><strong>Buffer size</strong> — “Medium” or “Large” reduces stutter on busy Wi-Fi.</li>
<li><strong>Favourites</strong> — long-press OK on a channel to add it; TiviMate shows favourites as the first row.</li>
</ul>

<h2>Using catch-up and recording</h2>
<p>With TiviMate Premium, channels that support catch-up show a small clock icon. Scroll back in the guide and press OK on a program that already aired to watch it from the start. To record, press OK on a future program and choose <strong>Record</strong>; set the storage folder under <em>Settings → Recording</em> (a USB drive works well on Nvidia Shield and many Android boxes).</p>

<h2>TiviMate on several TVs</h2>
<p>One TiviMate Premium purchase can activate several devices through the Companion app. Add the same IPTVMaple login on each TV — just make sure your plan covers the number of screens watching at the same time (1 to 5 on our <a href="/iptv-plans-canada/">plans page</a>).</p>

<h2>TiviMate troubleshooting</h2>
<ul>
<li><strong>“No channels” after adding the playlist</strong> — re-check the server URL includes the port; try the M3U link instead of Xtream.</li>
<li><strong>Guide shows “No information”</strong> — update EPG manually, or add the EPG link we send for M3U logins.</li>
<li><strong>Stutters on Firestick</strong> — clear TiviMate’s cache, reduce buffer to Medium, and use Ethernet or 5 GHz Wi-Fi.</li>
<li><strong>Premium not activating</strong> — sign in to the same Companion account on the device; this is handled by the TiviMate developer, not IPTVMaple.</li>
</ul>
""",
        faq=[
            ("Is TiviMate free?", "<p>TiviMate is free to download with basic features. TiviMate Premium is an optional paid upgrade from the developer that adds recording, catch-up, multiple playlists and more.</p>"),
            ("Does TiviMate work on Samsung or LG TVs?", "<p>No. TiviMate is only available for Android TV and Fire TV devices. On Samsung and LG, use Smart IPTV, SmartOne IPTV or Flix IPTV, or plug a Firestick into your TV.</p>"),
            ("Can I use TiviMate on iPhone or Apple TV?", "<p>No, there is no TiviMate app for iOS or tvOS. Use Smarters Player Lite or iPlayTV instead — see our <a href=\"/iptv-apple-tv/\">Apple TV IPTV guide</a>.</p>"),
            ("Does TiviMate include channels?", "<p>No. TiviMate is a player only. You add an IPTV subscription like IPTVMaple (via Xtream Codes or M3U) to get live channels, movies and series.</p>"),
            ("How do I get the TV guide (EPG) in TiviMate?", "<p>With an Xtream Codes login the guide loads automatically. With an M3U playlist, add the EPG link we send you under Settings → EPG.</p>"),
            ('How do I hide channel groups in TiviMate?', '<p>Go to Settings → Playlists → your playlist → Manage groups and untick the groups you don’t watch. It makes the channel list and guide much faster.</p>'),
            ('Can TiviMate record live TV?', '<p>Yes, with TiviMate Premium. Recordings are saved to the device or a USB drive you choose under Settings → Recording.</p>'),
            ('How many devices can use one TiviMate Premium?', '<p>TiviMate Premium can be activated on several devices through the Companion app. Your IPTV plan separately sets how many screens can stream at the same time.</p>'),
        ],
        related=["iptv-firestick", "iptv-smarters-pro", "iptv-android-tv", "formuler-iptv"],
        keywords=["tivimate", "tivi mate", "tivimate iptv", "tivimate firestick", "tivimate premium", "tivimate iptv player", "tivimate subscription", "tivimate premium cost", "tivimate price", "tivimate pro", "tivimate account", "tivimate for firestick", "tivimate on firestick", "tivimate apple tv", "tivimate premium subscription", "tivimate roku", "tivimate samsung", "tivimate lg", "tivimate pc"],
    ),
    # ------------------------------------------------------------------ SMARTERS LITE
    dict(
        slug="smarters-player-lite", hub="apps",
        title="Smarters Player Lite for iPhone & Apple TV Setup | IPTVMaple",
        description="Set up Smarters Player Lite on iPhone, iPad and Apple TV: download, log in with Xtream Codes or M3U and fix common errors. Try IPTVMaple free for 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">Smarters Player Lite</span> on iPhone &amp; Apple TV',
        lead="The Apple version of IPTV Smarters — free on the App Store for iPhone, iPad and Apple TV. Set it up with your IPTV login in a couple of minutes.",
        crumb="Smarters Player Lite", blurb="The Smarters app for iPhone, iPad & Apple TV.",
        answer="<p><strong>Smarters Player Lite</strong> is the free App Store version of IPTV Smarters for iPhone, iPad and Apple TV. Download it, choose “Login with Xtream Codes API”, and enter the server URL, username and password from your IPTV provider. With IPTVMaple you get live TV, sports, movies and series in HD and 4K.</p>",
        body=f"""
<h2>Smarters Player Lite vs IPTV Smarters Pro</h2>
<p>They are made by the same developer and use the same login. <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> is the Android, Firestick and desktop version; Smarters Player Lite is the one Apple approves for the App Store. The Lite version covers everything most viewers need: live TV with a guide, movies, series and favourites.</p>

<h2>How to install Smarters Player Lite</h2>
<ol>
<li>Open the <strong>App Store</strong> on your iPhone, iPad or Apple TV.</li>
<li>Search for <strong>Smarters Player Lite</strong> and tap <em>Get</em>.</li>
<li>Open the app and accept the terms.</li>
</ol>

<h2>How to log in</h2>
{HOW_LOGIN}
<ol>
<li>Choose <strong>Login with Xtream Codes API</strong>.</li>
<li>Type any profile name, then your username, password and URL.</li>
<li>Tap <strong>Add user</strong> and wait for channels and the guide to load.</li>
</ol>

<h2>Tips for Apple TV</h2>
<ul>
<li>Use a wired Ethernet connection on Apple TV 4K for the most stable 4K streams.</li>
<li>Turn on <em>Match Dynamic Range</em> and <em>Match Frame Rate</em> in Apple TV settings for smoother sports.</li>
<li>If you prefer a cable-style grid guide, try <a href="/iplaytv/">iPlayTV</a> with the same login.</li>
</ul>

<h2>Common Smarters Player Lite problems</h2>
<ul>
<li><strong>Login fails</strong> — make sure the URL includes <code>http://</code> and the port number exactly as sent.</li>
<li><strong>No TV guide</strong> — refresh EPG in the app settings.</li>
<li><strong>Video but no sound</strong> — switch the player to the native player in settings.</li>
</ul>
""",
        faq=[
            ("Is Smarters Player Lite free?", "<p>Yes, Smarters Player Lite is free on the App Store. You need an IPTV subscription such as IPTVMaple to watch content in it.</p>"),
            ("Does Smarters Player Lite work on Apple TV?", "<p>Yes. It runs on Apple TV HD and Apple TV 4K, as well as iPhone and iPad.</p>"),
            ("Is Smarters Player Lite the same as IPTV Smarters Pro?", "<p>It’s the Apple version of the same app. Both accept the same Xtream Codes and M3U login, so your IPTVMaple details work in either.</p>"),
            ("Can I watch on my iPhone and TV at the same time?", "<p>Yes, if your plan includes 2 or more devices. IPTVMaple plans cover 1 to 5 simultaneous devices.</p>"),
        ],
        related=["iptv-iphone", "iptv-apple-tv", "iptv-smarters-pro", "iplaytv"],
        keywords=["smarters players lite", "smart player lite", "smarters lite", "iptv smarters lite", "iptv smasters player lite", "smarters player lite firestick", "smarters player lite samsung tv", "smarters player lite tv", "smarters pro lite", "smasters player lite télécharger"],
    ),
    # ------------------------------------------------------------------ IMPLAYER
    dict(
        slug="implayer", hub="apps",
        title="IMPlayer IPTV App: Setup Guide & Premium (2026) | IPTVMaple",
        description="How to set up IMPlayer on Android TV, Firestick, Apple TV and smart TVs, and what IMPlayer Premium adds. Works with IPTVMaple — try it free for 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">IMPlayer</span>: setup guide for every device',
        lead="A modern IPTV player with a clean guide and cloud sync across devices. Here’s how to add your IPTVMaple login and get watching.",
        crumb="IMPlayer", blurb="Modern player with cloud sync across devices.",
        answer="<p><strong>IMPlayer</strong> is an IPTV player app available on Android TV, Fire TV, Apple devices and several smart TV platforms. It supports Xtream Codes and M3U logins, a TV guide and favourites that sync between devices. The free version works with IPTVMaple; <strong>IMPlayer Premium</strong> is a paid upgrade from the developer.</p>",
        body=f"""
<h2>Why choose IMPlayer?</h2>
<p>IMPlayer is a newer player with a polished, fast interface. Its main advantage is <strong>cloud sync</strong>: add your playlist once and it appears on your other devices signed in to the same IMPlayer account. It’s a good alternative to <a href="/tivimate/">TiviMate</a> if you use a mix of Android and Apple devices.</p>
<ul>
<li>Live TV with grid guide and channel groups</li>
<li>Movies and series with posters and descriptions</li>
<li>Favourites and watch history synced across devices</li>
<li>Catch-up on supported channels</li>
</ul>

<h2>How to install IMPlayer</h2>
<ul>
<li><strong>Android TV / Google TV</strong> — Google Play Store.</li>
<li><strong>Firestick / Fire TV</strong> — Amazon Appstore (or Downloader if it’s not listed on your model).</li>
<li><strong>iPhone, iPad, Apple TV</strong> — App Store.</li>
<li><strong>Samsung / LG</strong> — check your TV’s app store; availability varies by model year.</li>
</ul>

<h2>Add your IPTVMaple login to IMPlayer</h2>
{HOW_LOGIN}
<ol>
<li>Open IMPlayer and choose <strong>Add playlist</strong>.</li>
<li>Pick <strong>Xtream Codes</strong> and enter the server URL, username and password.</li>
<li>Save — channels, VOD and the guide load in under a minute.</li>
</ol>

<h2>IMPlayer Premium</h2>
<p>IMPlayer Premium is sold by the developer and unlocks extra features such as more playlists and advanced guide options. It’s optional — your IPTVMaple channels play fine in the free version.</p>
""",
        faq=[
            ("Is IMPlayer free?", "<p>Yes, IMPlayer can be used for free. IMPlayer Premium is an optional paid upgrade sold by the app developer.</p>"),
            ("Does IMPlayer work with IPTVMaple?", "<p>Yes. Use the Xtream Codes login we send after you order or start your free trial.</p>"),
            ("Is IMPlayer better than TiviMate?", "<p>TiviMate has more advanced recording and guide features on Android TV. IMPlayer is a strong choice if you also use Apple devices, because it runs on both and syncs your favourites.</p>"),
            ("Can I use IMPlayer on Apple TV?", "<p>Yes, IMPlayer is available on the App Store for Apple TV, iPhone and iPad.</p>"),
        ],
        related=["tivimate", "iptv-apple-tv", "iptv-android-tv"],
        keywords=["implayer", "implayer premium", "implayer tv"],
    ),
    # ------------------------------------------------------------------ XCIPTV
    dict(
        slug="xciptv", hub="apps",
        title="XCIPTV Player: Firestick & Android Setup Guide | IPTVMaple",
        description="Install XCIPTV (XC IPTV) player on Firestick and Android, log in with Xtream Codes and fix common errors. Works with IPTVMaple — try free for 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">XCIPTV</span> player: Firestick &amp; Android setup',
        lead="XCIPTV is a lightweight IPTV player built around the Xtream Codes login. Fast on older Firesticks and Android boxes.",
        crumb="XCIPTV", blurb="Lightweight Xtream Codes player for Firestick.",
        answer="<p><strong>XCIPTV</strong> (also written “XC IPTV”) is a free IPTV player for Android devices and Firestick designed for the <strong>Xtream Codes</strong> login: server URL, username and password. It’s lightweight, which makes it a good choice for older Firesticks and budget Android boxes. Your IPTVMaple login works in it straight away.</p>",
        body=f"""
<h2>What makes XCIPTV different?</h2>
<p>Where <a href="/tivimate/">TiviMate</a> focuses on a cable-style guide, XCIPTV focuses on speed. It uses little memory, opens quickly and supports live TV, movies, series and catch-up from one Xtream Codes login. It also includes a built-in VPN field and multiple player engines (ExoPlayer and VLC) you can switch between if a channel stutters.</p>

<h2>How to install XCIPTV on Firestick</h2>
<ol>
<li>Install <strong>Downloader</strong> from the Amazon Appstore.</li>
<li>Allow Downloader to install unknown apps in <em>Developer options</em>.</li>
<li>Download the XCIPTV APK from its official source and install it.</li>
</ol>
<p>On Android phones and boxes, install the same APK or find XCIPTV in the Play Store if it’s listed in your region.</p>

<h2>Log in to XCIPTV</h2>
{HOW_LOGIN}
<ol>
<li>Open XCIPTV and enter your <strong>username</strong>, <strong>password</strong> and <strong>server URL</strong>.</li>
<li>Tap <strong>Sign in</strong>. Live TV, VOD and EPG load automatically.</li>
</ol>

<h2>XCIPTV troubleshooting</h2>
<ul>
<li><strong>Channel freezes</strong> — in Settings → Player, switch between ExoPlayer and VLC.</li>
<li><strong>Guide empty</strong> — Settings → EPG → refresh.</li>
<li><strong>Wrong time in guide</strong> — set the EPG time offset for your province’s time zone.</li>
</ul>
""",
        faq=[
            ("Is XCIPTV the same as Xtream Codes?", "<p>No. Xtream Codes is the login format (server URL + username + password) used by most IPTV providers. XCIPTV is a player app built to use that login. Learn more in our <a href=\"/xtream-codes-iptv/\">Xtream Codes guide</a>.</p>"),
            ("Is XCIPTV free?", "<p>Yes, the XCIPTV player is free to use. You need an IPTV subscription like IPTVMaple for the channels.</p>"),
            ("Does XCIPTV work on Firestick?", "<p>Yes. Install it with the Downloader app after enabling unknown apps in Developer options.</p>"),
            ("Is XCIPTV good for old Firesticks?", "<p>Yes — it’s one of the lightest IPTV players, so it runs smoothly on older Fire TV Sticks with less memory.</p>"),
        ],
        related=["xtream-codes-iptv", "iptv-firestick", "tivimate"],
        keywords=["xc iptv", "xciptv firestick", "xciptv for firestick", "xciptv pro", "xciptv tv"],
    ),
    # ------------------------------------------------------------------ STBEMU
    dict(
        slug="stbemu", hub="apps",
        title="STBEmu Pro IPTV Setup: Portal & MAC Address | IPTVMaple",
        description="How to set up STBEmu Pro on Android and Firestick: add your portal URL, set the MAC address and fix errors. Works with IPTVMaple — try free for 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">STBEmu Pro</span>: portal &amp; MAC setup',
        lead="STBEmu turns an Android device into a MAG-style set-top box. Here’s how to set up the portal and MAC address.",
        crumb="STBEmu Pro", blurb="MAG box emulator for Android & Firestick.",
        answer="<p><strong>STBEmu</strong> (free) and <strong>STBEmu Pro</strong> (paid) are Android apps that emulate a MAG set-top box. Instead of a username and password, they connect with a <strong>portal URL</strong> and a <strong>MAC address</strong>. Send us the MAC address shown in the app, we activate it, and you enter the portal URL we give you.</p>",
        body="""
<h2>When should you use STBEmu?</h2>
<p>STBEmu is ideal if you like the classic MAG box interface, or if you’re moving from a MAG box to an Android device and want the same look. For most people, <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> is simpler — but STBEmu is fully supported by IPTVMaple.</p>

<h2>How to set up STBEmu Pro</h2>
<ol>
<li>Install <strong>STBEmu</strong> or <strong>STBEmu Pro</strong> from the Google Play Store (or with Downloader on Firestick).</li>
<li>Open the app. On first launch it shows a <strong>MAC address</strong> (it starts with <code>00:1A:79</code>). Write it down.</li>
<li>Send us that MAC address on WhatsApp with your order or <a href="/try-iptv-canada/">free trial</a> request. We activate it and send you a portal URL.</li>
<li>In STBEmu go to <em>Settings → Profiles → your profile → Portal settings</em> and paste the <strong>Portal URL</strong>.</li>
<li>Under <em>STB configuration</em>, choose model <strong>MAG 250</strong> or <strong>MAG 254</strong>, then restart the app.</li>
</ol>

<h2>Fixing common STBEmu errors</h2>
<ul>
<li><strong>“Loading portal” forever</strong> — check the portal URL ends with <code>/c/</code> exactly as sent.</li>
<li><strong>“STB blocked” or authentication failed</strong> — the MAC address in the app must match the one we activated.</li>
<li><strong>Buttons don’t work with the remote</strong> — enable “Use remote control” mapping in STBEmu’s keyboard settings.</li>
</ul>

<h2>STBEmu vs a real MAG box</h2>
<p>A <a href="/mag-box-iptv/">MAG box</a> is dedicated hardware that does one thing well. STBEmu gives you the same portal experience on a device you already own, plus access to every other Android app.</p>
""",
        faq=[
            ("What is the difference between STBEmu and STBEmu Pro?", "<p>STBEmu Pro is the paid, ad-free version with extra profiles and features. Both connect to IPTVMaple the same way, with a portal URL and MAC address.</p>"),
            ("Where do I find my MAC address in STBEmu?", "<p>It’s shown on the first screen after install, and under Settings → Profiles → STB configuration → MAC address.</p>"),
            ("Does STBEmu work on Firestick?", "<p>Yes, install it with the Downloader app. Remote navigation works, though TiviMate is usually easier on Firestick.</p>"),
            ("Can I change the MAC address later?", "<p>Yes, but tell us the new one so we can move your subscription to it.</p>"),
        ],
        related=["mag-box-iptv", "iptv-android-tv", "tivimate"],
        keywords=["stb emu pro", "stbemu pro", "stbemu iptv", "iptv stbemu", "stbemu 4k", "stbemu pro firestick", "iptv stb", "smart stb tv"],
    ),
    # ------------------------------------------------------------------ MYTVONLINE
    dict(
        slug="mytvonline", hub="apps",
        title="MyTVOnline 3 Setup on Formuler Boxes (2026) | IPTVMaple",
        description="Set up MyTVOnline 2 and MyTVOnline 3 on Formuler Z11 Pro Max, Z11 and Z8: add a portal or Xtream Codes login. Works with IPTVMaple — try free 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">MyTVOnline 3</span> setup on Formuler',
        lead="MyTVOnline is the IPTV app built into Formuler boxes. Here’s how to connect it to your IPTVMaple subscription.",
        crumb="MyTVOnline", blurb="Formuler’s built-in IPTV app, set up in minutes.",
        answer="<p><strong>MyTVOnline</strong> (MyTVOnline 2 and MyTVOnline 3) is the IPTV player pre-installed on Formuler boxes like the Z11 Pro Max, Z11 Pro and Z8 Pro. It connects with a <strong>portal URL</strong> tied to your box’s MAC address, or with an <strong>Xtream Codes</strong> login. Send us your box’s MAC address and we’ll activate it.</p>",
        body="""
<h2>MyTVOnline 2 vs MyTVOnline 3</h2>
<p>MyTVOnline 3 ships on the newer Formuler Z11 series. It adds a redesigned guide, faster channel switching and better VOD browsing. Older boxes such as the Z8 run MyTVOnline 2. Both work with IPTVMaple.</p>

<h2>Set up MyTVOnline with a portal (MAC)</h2>
<ol>
<li>Open MyTVOnline and note the <strong>MAC address</strong> shown on the first screen.</li>
<li>Send the MAC address to us on WhatsApp with your order or <a href="/try-iptv-canada/">free trial</a>.</li>
<li>We activate it and send you a <strong>portal URL</strong>.</li>
<li>In MyTVOnline choose <em>Add portal</em>, enter a name and paste the portal URL. Press <em>Connect</em>.</li>
</ol>

<h2>Set up MyTVOnline with Xtream Codes</h2>
<p>MyTVOnline 3 also accepts an Xtream Codes login. Choose <em>Add portal → Xtream Codes</em>, then enter the server URL, username and password we send you.</p>

<h2>MyTVOnline tips</h2>
<ul>
<li>Use the <strong>Guide</strong> button for the full grid EPG.</li>
<li>Press and hold OK on a channel to add it to favourites.</li>
<li>Prefer TiviMate? Formuler boxes run Android, so you can install <a href="/tivimate/">TiviMate</a> too.</li>
</ul>
<p>Looking for a box? Read our <a href="/formuler-iptv/">Formuler Z11 Pro Max guide</a>.</p>
""",
        faq=[
            ("Is MyTVOnline free?", "<p>Yes, it comes pre-installed on Formuler boxes at no extra cost. You add your IPTV subscription to it.</p>"),
            ("Where do I find the MAC address on a Formuler box?", "<p>It’s displayed when you open MyTVOnline, and also under Settings → About → Network on the box.</p>"),
            ("Can I install MyTVOnline on a Firestick?", "<p>No, MyTVOnline is exclusive to Formuler boxes. On Firestick use TiviMate or IPTV Smarters Pro.</p>"),
            ("Does IPTVMaple work with MyTVOnline 3?", "<p>Yes, via a MAC-based portal or an Xtream Codes login.</p>"),
        ],
        related=["formuler-iptv", "mag-box-iptv", "tivimate"],
        keywords=["mytvonline", "mytvonline 3"],
    ),
    # ------------------------------------------------------------------ SMART IPTV
    dict(
        slug="smart-iptv", hub="apps",
        title="Smart IPTV (SIPTV) Setup for Samsung & LG TVs | IPTVMaple",
        description="How to set up Smart IPTV (SIPTV) on Samsung and LG smart TVs: activation, uploading your M3U playlist by MAC address, and fixes. Try IPTVMaple free 24h.",
        kicker="IPTV apps", h1='<span class="grad-text">Smart IPTV</span> (SIPTV) setup for smart TVs',
        lead="The classic IPTV app for Samsung and LG TVs. Upload your playlist once from your phone and your channels appear on the TV.",
        crumb="Smart IPTV", blurb="The classic SIPTV app for Samsung & LG.",
        answer="<p><strong>Smart IPTV</strong> (SIPTV) is a player app for Samsung and LG smart TVs. You install it on the TV, note the TV’s <strong>MAC address</strong>, then upload your <strong>M3U playlist link</strong> on the Smart IPTV website. After a 7-day trial the app needs a one-time activation fee paid to its developer. It works with IPTVMaple.</p>",
        body="""
<h2>How Smart IPTV works</h2>
<p>Unlike most players, you don’t type your login on the TV. Instead, the app identifies your TV by its MAC address, and you link a playlist to that MAC on the official Smart IPTV website (siptv.app). This saves typing long URLs with a TV remote.</p>

<h2>Step-by-step: Smart IPTV setup</h2>
<ol>
<li>On your Samsung or LG TV, open the app store and install <strong>Smart IPTV</strong>.</li>
<li>Open it and write down the <strong>MAC address</strong> shown on screen.</li>
<li>On your phone or computer, go to the <em>My List</em> page of the official Smart IPTV website.</li>
<li>Enter the MAC address and paste the <strong>M3U link</strong> we sent you. Submit.</li>
<li>Restart the app on the TV. Your channel list loads.</li>
</ol>

<h2>Activation</h2>
<p>Smart IPTV includes a free trial, then asks for a one-time activation per TV, paid directly to the developer on their website. IPTVMaple doesn’t charge for this and doesn’t sell activations.</p>

<h2>Smart IPTV alternatives</h2>
<p>Many viewers now prefer <a href="/smartone-iptv/">SmartOne IPTV</a>, <a href="/flix-iptv/">Flix IPTV</a> or IBO Player, which support Xtream Codes (with movies and series sections) and more modern interfaces. For the smoothest experience on any TV, a <a href="/iptv-firestick/">Firestick with TiviMate</a> is hard to beat.</p>
""",
        faq=[
            ("Is Smart IPTV free?", "<p>Smart IPTV offers a free trial, then requires a one-time activation fee per TV paid to the app developer.</p>"),
            ("Why can’t I find Smart IPTV on my Samsung TV?", "<p>The app’s availability in Samsung’s store has changed over the years. If it isn’t listed, use SmartOne IPTV, Flix IPTV or IBO Player instead — they work the same way with IPTVMaple.</p>"),
            ("What is the SIPTV MAC address?", "<p>It’s the identifier the Smart IPTV app shows on your TV. You use it on the Smart IPTV website to attach your M3U playlist to that TV.</p>"),
            ("Does Smart IPTV show movies and series?", "<p>Smart IPTV focuses on live channels from an M3U list. For a full movies and series library, SmartOne, Flix IPTV or IBO Player are better.</p>"),
        ],
        related=["iptv-samsung-tv", "iptv-lg-tv", "set-iptv", "smartone-iptv"],
        keywords=["smart iptv", "siptv", "my sip tv", "my siptv", "sip tv", "siptv list", "siptv my list", "smart iptv my list", "smart iptv samsung", "smart iptv com", "smart iptv list", "smart iptv m3u"],
    ),
    # ------------------------------------------------------------------ SMARTONE
    dict(
        slug="smartone-iptv", hub="apps",
        title="SmartOne IPTV Setup on Samsung, LG & Android | IPTVMaple",
        description="Set up SmartOne IPTV on Samsung, LG and Android TVs: find your MAC, add your playlist on the SmartOne website and activate. Try IPTVMaple free 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">SmartOne IPTV</span> setup guide',
        lead="A popular smart-TV IPTV app with live TV, movies and series. Here’s how to add your IPTVMaple playlist.",
        crumb="SmartOne IPTV", blurb="Smart TV player with live TV, movies & series.",
        answer="<p><strong>SmartOne IPTV</strong> is an IPTV player for Samsung, LG and Android TVs. Install it on the TV, note the <strong>MAC address</strong>, then add your playlist on the official SmartOne website. It offers a free trial period followed by a one-time activation paid to the developer.</p>",
        body="""
<h2>Why SmartOne?</h2>
<p>SmartOne IPTV runs natively on Samsung Tizen and LG webOS TVs, so you don’t need an extra device. It organises content into Live TV, Movies and Series and supports a TV guide.</p>

<h2>SmartOne IPTV setup</h2>
<ol>
<li>Install <strong>SmartOne IPTV</strong> from your TV’s app store.</li>
<li>Open it and write down the <strong>MAC address</strong>.</li>
<li>On the official SmartOne IPTV website, go to the playlist / “generate” page, enter your MAC and paste the <strong>M3U link</strong> or Xtream details we sent you.</li>
<li>Restart the app on the TV — your channels appear.</li>
</ol>
<p>Prefer we do it? Send us your MAC address on WhatsApp and we’ll help you add the playlist.</p>

<h2>Tips</h2>
<ul>
<li>Only upload your playlist on the <strong>official</strong> SmartOne website.</li>
<li>If the guide is empty, re-upload the playlist including the EPG link.</li>
<li>For the fastest channel switching on older TVs, consider a <a href="/iptv-firestick/">Firestick</a>.</li>
</ul>
""",
        faq=[
            ("Is SmartOne IPTV free?", "<p>It has a free trial period, then a one-time activation fee per device paid to the developer.</p>"),
            ("Which TVs support SmartOne IPTV?", "<p>Samsung (Tizen), LG (webOS) and Android TVs. Check your TV’s app store for availability.</p>"),
            ("How do I add a playlist to SmartOne?", "<p>Enter your TV’s MAC address on the official SmartOne website and paste your M3U link. Restart the app to load it.</p>"),
            ("Does SmartOne IPTV work with IPTVMaple?", "<p>Yes. We send you an M3U link and Xtream details that work in SmartOne.</p>"),
        ],
        related=["iptv-samsung-tv", "iptv-lg-tv", "smart-iptv", "flix-iptv"],
        keywords=["smartone iptv", "smartone iptv com", "smartone iptv generate", "smartone iptv com generate"],
    ),
    # ------------------------------------------------------------------ FLIX IPTV
    dict(
        slug="flix-iptv", hub="apps",
        title="Flix IPTV Setup on Samsung, LG & Firestick | IPTVMaple",
        description="How to set up Flix IPTV on Samsung, LG, Android and Firestick: MAC address, playlist upload and activation. Works with IPTVMaple — try free for 24 hours.",
        kicker="IPTV apps", h1='<span class="grad-text">Flix IPTV</span> setup guide',
        lead="Flix IPTV is a sleek player for smart TVs and Android devices with live TV, movies and series. Here’s how to add your playlist.",
        crumb="Flix IPTV", blurb="Sleek player for Samsung, LG and Android.",
        answer="<p><strong>Flix IPTV</strong> is an IPTV player for Samsung, LG, Android TV, Firestick and Apple devices. You install it, note the <strong>MAC address</strong> and <strong>device key</strong>, then upload your playlist on the official Flix IPTV website. It has a free trial and then a one-time activation paid to the developer.</p>",
        body="""
<h2>What Flix IPTV offers</h2>
<ul>
<li>Live TV, movies and series in separate sections</li>
<li>TV guide and catch-up support</li>
<li>Multiple themes and subtitle options</li>
<li>Runs on Samsung, LG, Android, Fire TV and Apple devices</li>
</ul>

<h2>Flix IPTV setup in 4 steps</h2>
<ol>
<li>Install <strong>Flix IPTV</strong> from your TV or device app store.</li>
<li>Open the app and note the <strong>MAC address</strong> and <strong>device key</strong> in Settings → User account.</li>
<li>On the official Flix IPTV website, open the playlist upload page, enter the MAC and key, and paste your <strong>M3U link</strong> from IPTVMaple.</li>
<li>Restart Flix IPTV on the TV.</li>
</ol>

<h2>Flix IPTV vs SmartOne and Smart IPTV</h2>
<p>All three work by MAC address. Flix IPTV has the most modern look and the best movie and series browsing; <a href="/smartone-iptv/">SmartOne</a> is simpler; <a href="/smart-iptv/">Smart IPTV</a> is the oldest and focuses on live channels. All three work with IPTVMaple.</p>
""",
        faq=[
            ("Is Flix IPTV free?", "<p>Flix IPTV has a free trial, then a one-time activation paid to its developer.</p>"),
            ("Where is the MAC address in Flix IPTV?", "<p>Open Settings → User account inside the app. You’ll see the MAC address and device key.</p>"),
            ("Does Flix IPTV work on Firestick?", "<p>Yes, Flix IPTV is available for Fire TV devices as well as Samsung, LG and Android.</p>"),
            ("Can IPTVMaple upload the playlist for me?", "<p>Yes — send us your MAC address and device key on WhatsApp and our team will help.</p>"),
        ],
        related=["smartone-iptv", "smart-iptv", "iptv-samsung-tv"],
        keywords=["flix iptv", "flix ip tv", "flixiptv", "flix iptv player", "flixtv iptv"],
    ),
    # ------------------------------------------------------------------ IPLAYTV
    dict(
        slug="iplaytv", hub="apps",
        title="iPlayTV for Apple TV & iPhone: IPTV Setup | IPTVMaple",
        description="Set up iPlayTV on Apple TV, iPhone and iPad with your IPTV login: M3U or Xtream Codes, TV guide and favourites. Works with IPTVMaple — try it free 24h.",
        kicker="IPTV apps", h1='<span class="grad-text">iPlayTV</span> on Apple TV &amp; iPhone',
        lead="A premium IPTV player for Apple TV with a cable-style guide. Here’s how to set it up with IPTVMaple.",
        crumb="iPlayTV", blurb="Premium cable-style player for Apple TV.",
        answer="<p><strong>iPlayTV</strong> is a paid IPTV player on the App Store for Apple TV, iPhone and iPad. It supports M3U playlists and Xtream Codes, shows a grid TV guide and syncs favourites through iCloud. Add your IPTVMaple login and your channels appear with a full guide.</p>",
        body="""
<h2>Why Apple TV owners choose iPlayTV</h2>
<p>On Apple TV, iPlayTV is the closest thing to <a href="/tivimate/">TiviMate</a>: a fast, clean, cable-box style interface designed for the Siri Remote. It’s a one-time paid app on the App Store.</p>
<ul>
<li>Grid EPG with channel logos</li>
<li>Favourites synced between Apple devices</li>
<li>Picture-in-picture on iPhone and iPad</li>
<li>M3U and Xtream Codes support</li>
</ul>

<h2>Setting up iPlayTV</h2>
<ol>
<li>Buy and install <strong>iPlayTV</strong> from the App Store.</li>
<li>Open it and choose <strong>Add playlist</strong>.</li>
<li>Select <strong>Xtream Codes</strong> and enter server URL, username and password — or paste the <strong>M3U link</strong>.</li>
<li>Add the EPG link if you used M3U. Your guide appears within a minute.</li>
</ol>

<h2>Free alternative</h2>
<p>Don’t want to pay for a player? <a href="/smarters-player-lite/">Smarters Player Lite</a> is free on the App Store and works with the same IPTVMaple login.</p>
""",
        faq=[
            ("Is iPlayTV free?", "<p>No, iPlayTV is a paid app on the App Store. Smarters Player Lite is a free alternative.</p>"),
            ("Does iPlayTV work on Android?", "<p>No, it’s only for Apple TV, iPhone and iPad.</p>"),
            ("Does iPlayTV support Xtream Codes?", "<p>Yes, along with M3U playlists and external EPG links.</p>"),
            ("Can I use iPlayTV with IPTVMaple?", "<p>Yes — enter the Xtream Codes login or M3U link we send after your order or free trial.</p>"),
        ],
        related=["iptv-apple-tv", "smarters-player-lite", "iptv-iphone"],
        keywords=["iplaytv", "iplaytv apple tv", "iplaytv android", "iplay iptv"],
    ),
    # ------------------------------------------------------------------ KODI
    dict(
        slug="kodi-iptv", hub="apps",
        title="How to Watch IPTV on Kodi with PVR Simple Client | IPTVMaple",
        description="Set up IPTV on Kodi with the PVR IPTV Simple Client add-on: add your M3U playlist and EPG for live TV with a guide. Works with IPTVMaple — try free 24h.",
        kicker="IPTV apps", h1='How to watch <span class="grad-text">IPTV on Kodi</span>',
        lead="Kodi can play your IPTV subscription with a full TV guide using its official PVR IPTV Simple Client add-on.",
        crumb="Kodi IPTV", blurb="Live TV and guide in Kodi via PVR Simple Client.",
        answer="<p>To watch IPTV on <strong>Kodi</strong>, install the official <strong>PVR IPTV Simple Client</strong> add-on, paste your <strong>M3U playlist URL</strong> and <strong>EPG (XMLTV) URL</strong>, and enable it. Your live channels then appear under <em>TV</em> with a full guide. It works on Windows, Mac, Android, Firestick and Nvidia Shield.</p>",
        body="""
<h2>Before you start</h2>
<p>You need Kodi installed (free, from the official Kodi website or your device’s app store) and an IPTV subscription with an M3U link. IPTVMaple sends you the M3U link and EPG link with your login.</p>

<h2>Set up PVR IPTV Simple Client</h2>
<ol>
<li>In Kodi go to <em>Add-ons → Install from repository → Kodi Add-on repository → PVR clients</em>.</li>
<li>Select <strong>PVR IPTV Simple Client</strong> and install it.</li>
<li>Open <em>Configure</em>. Under <strong>General</strong>, set Location to <em>Remote path</em> and paste your <strong>M3U playlist URL</strong>.</li>
<li>Under <strong>EPG</strong>, paste the <strong>XMLTV URL</strong>.</li>
<li>Enable the add-on and restart Kodi. Open <strong>TV</strong> from the home menu.</li>
</ol>

<h2>Only use official add-ons</h2>
<p>Stick to add-ons from the official Kodi repository. Unofficial “free TV” add-ons are often unreliable and can contain malware. The official Simple Client is maintained by the Kodi team — see the <a href="https://kodi.wiki/view/Add-on:PVR_IPTV_Simple_Client" target="_blank" rel="noopener">Kodi wiki</a>.</p>

<h2>Kodi vs a dedicated IPTV player</h2>
<p>Kodi is powerful but slower to set up. If you mainly want live TV and movies with a remote, <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> is easier. Kodi is great if you already use it for your local media library.</p>
""",
        faq=[
            ("Is Kodi IPTV free?", "<p>Kodi and the PVR IPTV Simple Client add-on are free. You still need an IPTV subscription for the channels.</p>"),
            ("Does Kodi support Xtream Codes?", "<p>The Simple Client uses M3U playlists. Convert your Xtream login into the M3U link we provide — or ask us for it.</p>"),
            ("Why does Kodi show no channels?", "<p>Check the M3U URL is set under “Remote path”, the add-on is enabled, and restart Kodi. Clearing the add-on cache also helps.</p>"),
            ("Can I watch IPTV on Kodi on a Firestick?", "<p>Yes. Install Kodi on the Firestick, then set up the Simple Client as above.</p>"),
        ],
        related=["m3u-playlist", "vlc-iptv", "iptv-pc-mac"],
        keywords=["kodi iptv", "kodi ip tv", "iptv sur kodi", "kodi iptv m3u", "kodi m3u", "kodi live tv", "m3u kodi"],
    ),
    # ------------------------------------------------------------------ VLC
    dict(
        slug="vlc-iptv", hub="apps",
        title="How to Watch IPTV on VLC Media Player (M3U) | IPTVMaple",
        description="Watch IPTV on VLC media player on Windows, Mac and Android by opening your M3U playlist URL. Simple steps and fixes. Try IPTVMaple free for 24 hours.",
        kicker="IPTV apps", h1='How to watch <span class="grad-text">IPTV on VLC</span>',
        lead="VLC can play your IPTV channels on any computer in under a minute — no extra app needed.",
        crumb="VLC IPTV", blurb="Play your M3U playlist in VLC in one minute.",
        answer="<p>To watch IPTV on <strong>VLC</strong>, open VLC, go to <em>Media → Open Network Stream</em> (Windows) or <em>File → Open Network</em> (Mac), paste your <strong>M3U playlist URL</strong> and press Play. Your channels load as a playlist. VLC is free, but it has no TV guide — for that use IPTV Smarters or Kodi.</p>",
        body="""
<h2>Play IPTV in VLC on Windows</h2>
<ol>
<li>Install VLC from the official VideoLAN website.</li>
<li>Open VLC and click <strong>Media → Open Network Stream</strong>.</li>
<li>Paste your IPTVMaple <strong>M3U link</strong> and click <strong>Play</strong>.</li>
<li>Press <strong>Ctrl + L</strong> to show the playlist and pick a channel.</li>
</ol>

<h2>Play IPTV in VLC on Mac</h2>
<ol>
<li>Open VLC and choose <strong>File → Open Network</strong>.</li>
<li>Paste the M3U URL and click <strong>Open</strong>.</li>
<li>Use <strong>Window → Playlist</strong> to browse channels.</li>
</ol>

<h2>VLC on Android and iPhone</h2>
<p>The VLC mobile app can open a network stream the same way (<em>More → New stream</em>). For a better mobile experience with a guide, use <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> or <a href="/smarters-player-lite/">Smarters Player Lite</a>.</p>

<h2>Limitations of VLC for IPTV</h2>
<ul>
<li>No electronic program guide (EPG)</li>
<li>Large playlists (tens of thousands of channels) load slowly</li>
<li>No separate movies/series library</li>
</ul>
<p>VLC is perfect for a quick test or occasional viewing on a laptop. For daily use see our <a href="/iptv-pc-mac/">IPTV on PC &amp; Mac guide</a>.</p>
""",
        faq=[
            ("Can VLC play IPTV?", "<p>Yes. VLC can open an M3U playlist URL as a network stream and play your IPTV channels.</p>"),
            ("Does VLC show a TV guide?", "<p>No. VLC has no EPG. Use IPTV Smarters, Kodi or MyIPTV Player if you want a guide on your computer.</p>"),
            ("Why is my playlist slow to load in VLC?", "<p>Full IPTV playlists contain tens of thousands of entries. Ask us for a smaller playlist with only the channel groups you want.</p>"),
            ("Is VLC free?", "<p>Yes, VLC media player is free and open source.</p>"),
        ],
        related=["m3u-playlist", "iptv-pc-mac", "kodi-iptv"],
        keywords=["iptv vlc", "vlc ip tv", "ip tv vlc", "iptv vlc media player", "iptv vlc player", "iptv sur vlc"],
    ),
    # ------------------------------------------------------------------ M3U
    dict(
        slug="m3u-playlist", hub="apps",
        title="What Is an M3U Playlist? IPTV M3U Guide (2026) | IPTVMaple",
        description="What an IPTV M3U playlist is, M3U vs M3U8 vs Xtream Codes, how to use an M3U list in VLC, Kodi, TiviMate and smart TVs, and how to stay safe. Try IPTVMaple.",
        kicker="IPTV apps", h1='What is an <span class="grad-text">M3U playlist</span>?',
        lead="M3U is the file format behind most IPTV channel lists. Here’s what it is and how to use one in any player.",
        crumb="M3U playlists", blurb="How M3U lists work and how to use them.",
        answer="<p>An <strong>M3U playlist</strong> is a plain-text file (or URL) that lists streams: each entry has a channel name, a logo and group tags, and the stream address. IPTV players read the M3U to build your channel list. <strong>M3U8</strong> is the same format saved in UTF-8. Your IPTV provider gives you a private M3U URL linked to your subscription.</p>",
        body="""
<h2>What’s inside an M3U file?</h2>
<p>An IPTV M3U starts with <code>#EXTM3U</code>, followed by one entry per channel:</p>
<pre><code>#EXTM3U
#EXTINF:-1 tvg-id="cbc.ca" tvg-logo="…" group-title="Canada",CBC Toronto
http://server:port/username/password/12345</code></pre>
<p>The <code>tvg-id</code> links the channel to the TV guide (EPG), <code>group-title</code> sorts it into a category, and the last line is the stream address.</p>

<h2>M3U vs M3U8 vs Xtream Codes</h2>
<table>
<thead><tr><th></th><th>M3U / M3U8</th><th><a href="/xtream-codes-iptv/">Xtream Codes</a></th></tr></thead>
<tbody>
<tr><td>Login</td><td>One long URL</td><td>Server URL + username + password</td></tr>
<tr><td>Movies &amp; series</td><td>Mixed into the channel list</td><td>Separate VOD sections</td></tr>
<tr><td>TV guide</td><td>Separate EPG (XMLTV) link</td><td>Built in</td></tr>
<tr><td>Works in</td><td>Almost every player, VLC, Kodi</td><td>Most IPTV apps</td></tr>
</tbody>
</table>

<h2>How to use an M3U list</h2>
<ul>
<li><strong>VLC</strong> — <em>Open Network Stream</em>, paste the URL (<a href="/vlc-iptv/">guide</a>).</li>
<li><strong>Kodi</strong> — PVR IPTV Simple Client (<a href="/kodi-iptv/">guide</a>).</li>
<li><strong>TiviMate / Smarters</strong> — <em>Add playlist → M3U</em>.</li>
<li><strong>Samsung / LG</strong> — upload it by MAC address in <a href="/smart-iptv/">Smart IPTV</a>, SmartOne or Flix IPTV.</li>
</ul>

<h2>Are free M3U lists safe?</h2>
<p>“Free IPTV M3U list” links shared on forums usually stop working within hours, are full of dead channels, and can expose you to malware or shady websites. There are legitimate free, legal lists of public channels (such as the open-source <a href="https://github.com/iptv-org/iptv" target="_blank" rel="noopener">iptv-org</a> project), but they don’t include premium sports and movies. A private playlist from a paid service is far more stable — try ours <a href="/try-iptv-canada/">free for 24 hours</a>.</p>
""",
        faq=[
            ("What is an M3U link?", "<p>It’s a URL that points to an M3U playlist file. IPTV apps download it to build your channel list.</p>"),
            ("What’s the difference between M3U and M3U8?", "<p>The format is the same; M3U8 is saved with UTF-8 encoding, which supports accented characters in channel names (useful for French channels).</p>"),
            ("How do I get the TV guide with an M3U playlist?", "<p>Add the EPG (XMLTV) link from your provider to your player. IPTVMaple sends it with your login.</p>"),
            ("Can I edit my M3U playlist?", "<p>Yes, but it’s easier to ask us for a filtered playlist with only the countries and categories you want.</p>"),
            ("Does IPTVMaple provide an M3U link?", "<p>Yes, every subscription and free trial includes both an M3U link and an Xtream Codes login.</p>"),
        ],
        related=["xtream-codes-iptv", "iptv-server", "vlc-iptv", "kodi-iptv"],
        keywords=["m3u", "iptv m3u", "m3u iptv", "m3u list", "iptv m3u list", "iptv list", "ip tv list", "iptv play list", "iptv player m3u", "player m3u", "m3u ip tv", "liste m3u iptv", "m3u8 iptv", "iptv m3u8", "m3u8 list", "m3u player online", "list iptv", "play list iptv", "liste iptv m3u fr"],
    ),
    # ------------------------------------------------------------------ XTREAM
    dict(
        slug="xtream-codes-iptv", hub="apps",
        title="Xtream Codes IPTV Login: URL, User & Pass | IPTVMaple",
        description="What an Xtream Codes IPTV login is, how to enter the server URL, username and password in TiviMate, Smarters and more, and how to fix errors. Try IPTVMaple.",
        kicker="IPTV apps", h1='<span class="grad-text">Xtream Codes</span> IPTV login explained',
        lead="Server URL, username, password — the login most IPTV apps use. Here’s how it works and where to type it.",
        crumb="Xtream Codes login", blurb="The login format most IPTV apps use.",
        answer="<p>An <strong>Xtream Codes</strong> (or “Xtream IPTV”) login is three pieces of information: a <strong>server URL</strong> (with port), a <strong>username</strong> and a <strong>password</strong>. Apps like TiviMate, IPTV Smarters, XCIPTV and IMPlayer use it to load live TV, movies, series and the TV guide in one step. It’s the recommended way to use your IPTVMaple subscription.</p>",
        body="""
<h2>Where does the name come from?</h2>
<p>Xtream Codes was originally software used by IPTV providers to run their servers. The company behind it shut down in 2019, but its login standard — the “Xtream Codes API” — became the norm, and players still label the option “Xtream Codes” today.</p>

<h2>Where to enter your Xtream Codes login</h2>
<table>
<thead><tr><th>App</th><th>Menu</th></tr></thead>
<tbody>
<tr><td><a href="/tivimate/">TiviMate</a></td><td>Add playlist → Xtream Codes</td></tr>
<tr><td><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></td><td>Login with Xtream Codes API</td></tr>
<tr><td><a href="/xciptv/">XCIPTV</a></td><td>Main login screen</td></tr>
<tr><td><a href="/implayer/">IMPlayer</a></td><td>Add playlist → Xtream Codes</td></tr>
<tr><td><a href="/mytvonline/">MyTVOnline 3</a></td><td>Add portal → Xtream Codes</td></tr>
</tbody>
</table>

<h2>Common Xtream Codes errors</h2>
<ul>
<li><strong>Invalid credentials</strong> — usernames and passwords are case-sensitive; copy-paste them.</li>
<li><strong>Can’t connect to server</strong> — include <code>http://</code> and the port (e.g. <code>:8080</code>) exactly as sent.</li>
<li><strong>Account expired</strong> — renew your plan on our <a href="/iptv-plans-canada/">pricing page</a>.</li>
<li><strong>Max connections reached</strong> — too many devices are playing at once for your plan; stop one or upgrade.</li>
</ul>

<h2>Keep your login private</h2>
<p>Your Xtream login is personal. Sharing it beyond your plan’s device limit can get the account locked. Need more screens? Our plans go up to 5 simultaneous devices.</p>
""",
        faq=[
            ("What is an Xtream Codes URL?", "<p>It’s the server address your app connects to, usually in the form http://domain:port. IPTVMaple sends it with your username and password.</p>"),
            ("Is Xtream Codes better than M3U?", "<p>For most apps, yes: it loads live TV, movies, series and the guide separately and more reliably. M3U is useful for players like VLC and Kodi.</p>"),
            ("Is Xtream IPTV a provider?", "<p>No — “Xtream IPTV” refers to the login format, not a specific service. Many providers, including IPTVMaple, support it.</p>"),
            ("Can I use the same Xtream login on two devices?", "<p>Yes, up to the number of simultaneous devices included in your plan.</p>"),
        ],
        related=["m3u-playlist", "iptv-server", "iptv-smarters-pro", "xciptv"],
        keywords=["xtream iptv", "xtream iptv m3u", "xtream tv", "xtreamtv", "lxtream", "lxtream player"],
    ),
]
