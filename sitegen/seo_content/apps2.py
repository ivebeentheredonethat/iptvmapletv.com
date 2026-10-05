"""App long-tail: TiviMate (Premium, Firestick, device support), IPTV Smarters per device, Plex / Jellyfin / Stremio.

Where an app's behaviour varies by region or version we say so and point to the developer, rather than guessing.
"""
D = dict(published="2026-10-01", updated="2026-10-01")

LOGIN_STEPS = """<p>After you order, or request the <a href="/try-iptv-canada/">free 24-hour trial</a>, IPTVMaple sends your login by email and WhatsApp: a <strong>server URL, username and password</strong> (an Xtream Codes login) and an <strong>M3U link</strong> if your app prefers it.</p>"""

PAGES = [
    # ------------------------------------------------------------------ TIVIMATE PREMIUM
    dict(
        slug="tivimate-premium", hub="apps", **D,
        title="TiviMate Premium: Cost, Features & Activation | IPTVMaple",
        description="What TiviMate Premium costs, what it adds over the free app, how to buy and activate it with the Companion app, and whether it’s worth it. Works with IPTVMaple.",
        kicker="App guide", h1='TiviMate Premium: <span class="grad-text">cost, features and activation</span>',
        lead="TiviMate Premium is an optional upgrade from the app’s developer. Here is what it adds, how to buy it and how to decide if you need it.",
        crumb="TiviMate Premium", blurb="Cost, features and activation of TiviMate Premium.",
        answer="<p><strong>TiviMate Premium is an optional paid upgrade sold by the TiviMate developer, not by IPTVMaple.</strong> It unlocks features such as multiple playlists, catch-up, recording and favourites groups on top of the free app. The current price and plan options (yearly or lifetime) are shown in the <em>TiviMate Companion</em> app and can change, so check there before you buy. Your IPTVMaple subscription is a separate purchase.</p>",
        body="""
<h2>What TiviMate Premium adds</h2>
<p><a href="/tivimate/">TiviMate</a> is free to install and plays any IPTV login with a clean grid TV guide. Premium adds the features most people who watch a lot of live TV end up wanting:</p>
<table>
<thead><tr><th>Feature</th><th>Free TiviMate</th><th>TiviMate Premium</th></tr></thead>
<tbody>
<tr><td>Live TV with grid guide</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Multiple playlists</td><td>Limited</td><td>Yes</td></tr>
<tr><td>Favourites and custom channel groups</td><td>Limited</td><td>Yes</td></tr>
<tr><td>Catch-up on supported channels</td><td>No</td><td>Yes</td></tr>
<tr><td>Recording (to device or USB)</td><td>No</td><td>Yes</td></tr>
<tr><td>Picture-in-picture and multi-view</td><td>No</td><td>On supported devices</td></tr>
<tr><td>Reminders and extra guide options</td><td>Basic</td><td>Yes</td></tr>
</tbody>
</table>
<p>Feature lists change as the developer updates the app. The TiviMate Companion app and the developer’s website show the current list.</p>

<h2>How much does TiviMate Premium cost?</h2>
<p>The price is set by the TiviMate developer and shown in the Companion app, so we don’t quote a number here that could be out of date. It has been offered as a yearly subscription and as a lifetime option, and the amounts have changed over time. Look for the plan that matches how long you expect to use the app.</p>
<ul>
<li><strong>Yearly plan</strong> — a smaller payment, renewed each year.</li>
<li><strong>Lifetime option</strong>, when offered — a larger one-time payment.</li>
<li>One Premium account can normally be used on several of your devices.</li>
</ul>
<p>Compare that with your IPTV costs on our <a href="/iptv-price/">IPTV price</a> page. For many households the app upgrade is a small extra next to the subscription itself.</p>

<h2>How to buy and activate TiviMate Premium</h2>
<ol>
<li>Install <strong>TiviMate Companion</strong> on an Android phone or tablet and create or sign in to your account with your email address.</li>
<li>Choose a Premium plan in the Companion app and complete the purchase.</li>
<li>On your TV, open TiviMate and go to <strong>Settings</strong> to find the Premium or account option, then sign in with the same account.</li>
<li>Premium features unlock on that device. Repeat step 3 on your other TVs.</li>
</ol>
<p>Menu names can differ between versions. If something doesn’t match, follow the developer’s on-screen prompts or help pages.</p>

<h2>What is a “TiviMate account”?</h2>
<p>People searching for a “TiviMate account” or “TiviMate premium account” are usually looking for one of two different things:</p>
<ul>
<li><strong>The Premium account</strong> you create in the Companion app. It stores your Premium licence. It is not a login for channels.</li>
<li><strong>Your IPTV login</strong> (server URL, username and password) from your provider. This is what actually gives you channels, movies and series. IPTVMaple sends it when you <a href="/iptv-plans-canada/">subscribe</a> or start the <a href="/try-iptv-canada/">free trial</a>.</li>
</ul>
<p>IPTVMaple does not sell TiviMate accounts or licences.</p>

<h2>Beware of cracked or resold Premium</h2>
<p>Sites that advertise “TiviMate Premium cracked”, “free Premium” or cheap resold accounts are risky. Modified apps can carry malware, and a resold licence can stop working without warning. Buy only through the developer’s own Companion app.</p>

<h2>Is TiviMate Premium worth it?</h2>
<table>
<thead><tr><th>You mostly…</th><th>Do you need Premium?</th></tr></thead>
<tbody>
<tr><td>Watch live TV and sports on the big screen</td><td>Probably yes: catch-up, recording and favourites help a lot</td></tr>
<tr><td>Watch movies and series on demand</td><td>No: the free app is enough</td></tr>
<tr><td>Have several TVs or several playlists</td><td>Yes: multiple playlists and the shared account</td></tr>
<tr><td>Prefer not to pay for an app</td><td>Use a free player such as <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>, <a href="/xciptv/">XCIPTV</a> or <a href="/implayer/">IMPlayer</a></td></tr>
</tbody>
</table>

<h2>Activation not working?</h2>
<ul>
<li>Confirm you signed in to the <em>same</em> account on the Companion app and the TV.</li>
<li>Check the TV’s date, time and internet connection.</li>
<li>Restart TiviMate and try again.</li>
<li>Activation is handled by the TiviMate developer. If these steps don’t help, use the developer’s support. We are happy to help with the IPTV login side.</li>
</ul>

<h2>Set up TiviMate with IPTVMaple</h2>
<p>If you’re ready to install, follow the <a href="/tivimate-firestick/">TiviMate on Firestick guide</a>. On a smart TV or Apple device, check <a href="/tivimate-devices/">which devices TiviMate supports</a> first.</p>
""",
        faq=[
            ("Is TiviMate Premium free?",
             "<p>No. TiviMate itself is free to install, but Premium is a paid upgrade sold by the app’s developer. IPTVMaple does not sell it. You can use the free version or another free player such as IPTV Smarters Pro with every IPTVMaple plan.</p>"),
            ("How much is TiviMate Premium?",
             "<p>The developer sets the price and shows it in the TiviMate Companion app. It has been offered as a yearly subscription and a lifetime option, and the amounts change over time, so check the Companion app for the current price before you buy.</p>"),
            ("Do I need TiviMate Premium to watch IPTVMaple?",
             "<p>No. Every IPTVMaple plan works with the free TiviMate app and with free players such as IPTV Smarters Pro. Premium only adds convenience features like catch-up, recording and multiple playlists.</p>"),
            ("Can one TiviMate Premium account be used on several TVs?",
             "<p>Yes, a Premium account can normally be used on several of your devices by signing in with the same account. Each TV still needs your IPTV login, and your IPTV plan limits how many screens can watch at the same time.</p>"),
            ("Does IPTVMaple sell TiviMate accounts?",
             "<p>No. TiviMate Premium is bought from the developer through the Companion app. Be careful with anyone selling accounts or cracked versions.</p>"),
            ("What is the difference between a TiviMate account and an IPTV login?",
             "<p>The TiviMate account stores your Premium licence. The IPTV login (server URL, username and password) comes from your IPTV provider and gives you the channels. You need the second one in either case.</p>"),
        ],
        related=["tivimate", "tivimate-firestick", "tivimate-devices", "iptv-smarters-pro"],
        keywords=["tivimate premium", "tivimate premium cost", "tivimate premium subscription", "tivimate price", "tivimate premium price", "tivimate premium prix",
                  "tivimate pro", "tivimate account", "tivimate account premium", "tivimate premium account", "tivimate subscription", "tivimate website", "tivimate com",
                  "tivimate iptv player premium", "tivimate companion iphone", "tivimate player"],
    ),

    # ------------------------------------------------------------------ TIVIMATE FIRESTICK
    dict(
        slug="tivimate-firestick", hub="apps", **D,
        title="TiviMate on Firestick: Step-by-Step Install | IPTVMaple",
        description="How to install TiviMate on a Firestick or Fire TV with Downloader, add your IPTV login, set up the guide and fix common problems. Works with IPTVMaple.",
        kicker="Install guide", h1='TiviMate on Firestick: <span class="grad-text">install and set up in 10 minutes</span>',
        lead="TiviMate is not in the Amazon Appstore, so it is installed with the free Downloader app. Here is every step, plus fixes for the usual problems.",
        crumb="TiviMate on Firestick", blurb="Install TiviMate on a Firestick with Downloader and add your login.",
        answer="<p><strong>To install TiviMate on a Firestick:</strong> install the free Downloader app, allow it to install unknown apps in <em>Settings → My Fire TV → Developer options</em>, enter the official TiviMate download address from tivimate.com in Downloader, install the APK, then open TiviMate and add your IPTV login with <em>Add playlist → Xtream Codes</em>. It takes about ten minutes and works on Fire OS Firesticks and Fire TV devices.</p>",
        body="""
<h2>Which Firestick works best with TiviMate?</h2>
<p>TiviMate needs a Fire TV device that runs Fire OS, the Android-based system that can install Android apps. The common models work well; a few cautions:</p>
<ul>
<li><strong>Fire TV Stick 4K, 4K Max and Fire TV Cube</strong> — best choice. Fast enough for 4K channels and a large channel list.</li>
<li><strong>Fire TV Stick Lite and older sticks</strong> — work for HD, but they can be slow with long channel lists. Hide the groups you don’t watch.</li>
<li><strong>Newer Fire TV models running Amazon’s Vega OS</strong> — some recent devices don’t run Android apps at all, so TiviMate can’t be installed on them. Check the product page for “Android apps” support before you buy.</li>
</ul>
<p>Not sure which device to buy? Read the <a href="/iptv-box/">IPTV box guide</a> and our general <a href="/iptv-firestick/">Firestick IPTV guide</a>.</p>

<h2>Step 1: allow apps from unknown sources</h2>
<ol>
<li>On the Firestick home screen, go to <strong>Settings → My Fire TV</strong>.</li>
<li>Select <strong>Developer options</strong>. If you don’t see it, go to <em>About</em>, select the device name seven times, then go back.</li>
<li>Open <strong>Install unknown apps</strong> and turn on <strong>Downloader</strong> (install Downloader first if it isn’t listed).</li>
</ol>

<h2>Step 2: install Downloader</h2>
<p>Search for <strong>Downloader</strong> in the Fire TV search, choose the app by AFTVnews with the orange icon, and select <strong>Get</strong>. Open it and allow file access when asked.</p>

<h2>Step 3: download and install TiviMate</h2>
<ol>
<li>In Downloader, select the address bar and enter the official TiviMate download address from <strong>tivimate.com</strong>.</li>
<li>Select <strong>Go</strong> and wait for the file to download.</li>
<li>Choose <strong>Install</strong>, then <strong>Done</strong>. You can delete the downloaded file afterwards to save space.</li>
</ol>
<p>Only use the developer’s official website. Modified TiviMate files from other sites are a common way to spread malware.</p>

<h2>Step 4: add your IPTVMaple login</h2>
""" + LOGIN_STEPS + """
<ol>
<li>Open TiviMate and choose <strong>Add playlist</strong>.</li>
<li>Select <strong>Xtream Codes</strong> and enter the server URL, username and password exactly as sent.</li>
<li>Press <strong>Next</strong>. TiviMate loads channels, movies, series and the TV guide.</li>
<li>Name the playlist (for example “IPTVMaple”) and press <strong>Done</strong>.</li>
</ol>

<h2>Step 5: tune it for Canadian viewing</h2>
<ul>
<li><strong>Hide groups you don’t watch</strong> in <em>Settings → Playlists → Manage groups</em>. Keep your Canadian, Québec and sports groups.</li>
<li><strong>Set the guide time</strong> in <em>Settings → EPG</em>. If programs look an hour off, adjust the time shift for your province.</li>
<li><strong>Turn on auto frame rate</strong> in <em>Settings → Playback</em> for smoother hockey.</li>
<li><strong>Add favourites</strong> by long-pressing OK on a channel.</li>
</ul>

<h2>Should you buy TiviMate Premium?</h2>
<p>Premium is optional and is sold by the developer. See <a href="/tivimate-premium/">TiviMate Premium: cost, features and activation</a> to decide. You can also use a free player such as <a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro on Firestick</a>.</p>

<h2>TiviMate on Firestick: common problems</h2>
<table>
<thead><tr><th>Problem</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>“App not installed”</td><td>Free up storage space, then try again. Remove old files from Downloader.</td></tr>
<tr><td>Developer options missing</td><td>Select the device name seven times under <em>Settings → My Fire TV → About</em>.</td></tr>
<tr><td>No channels after adding the playlist</td><td>Check the server URL includes the port and has no spaces; try the M3U link instead.</td></tr>
<tr><td>Guide shows “No information”</td><td>Update the EPG manually; for M3U logins add the EPG link we send.</td></tr>
<tr><td>Stutters or freezes</td><td>Use an Ethernet adapter or 5 GHz Wi-Fi and raise the buffer. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</td></tr>
</tbody>
</table>
<p>New here? Start with the <a href="/try-iptv-canada/">free 24-hour trial</a> and follow the steps above.</p>
""",
        faq=[
            ("How do I install TiviMate on a Firestick?",
             "<p>Install Downloader from the Amazon Appstore, allow it to install unknown apps in Developer options, enter the official TiviMate download address from tivimate.com in Downloader, install the file, then open TiviMate and add your Xtream Codes login.</p>"),
            ("Is TiviMate in the Amazon Appstore?",
             "<p>No. On Fire TV devices TiviMate is installed with the Downloader app. On Android TV and Google TV devices it can be installed from the Google Play Store.</p>"),
            ("Why can’t I find Developer options on my Firestick?",
             "<p>It is hidden until you enable it. Go to Settings, My Fire TV, About, then select the device name seven times. Go back and Developer options will appear in My Fire TV.</p>"),
            ("Does TiviMate work on every Firestick?",
             "<p>It works on Fire OS Firesticks and Fire TV devices. Some newer Fire TV models run Amazon’s Vega OS and don’t support Android apps, so TiviMate can’t be installed on them. Check the product description before buying.</p>"),
            ("Which Firestick is best for TiviMate?",
             "<p>A Fire TV Stick 4K Max, Fire TV Stick 4K or Fire TV Cube. They have enough memory for long channel lists and handle 4K sports channels more smoothly than entry-level sticks.</p>"),
            ("Do I need TiviMate Premium on Firestick?",
             "<p>No. The free version plays your IPTV login. Premium adds catch-up, recording and multiple playlists and is sold separately by the developer.</p>"),
            ("TiviMate shows no channels. What should I check?",
             "<p>Re-enter the server URL, username and password without spaces, make sure the URL includes the port number, and try the M3U playlist link instead of Xtream Codes. If it still fails, message our support team with a screenshot.</p>"),
        ],
        related=["tivimate", "tivimate-premium", "iptv-firestick", "iptv-smarters-pro-firestick"],
        keywords=["tivimate firestick", "tivimate for firestick", "tivimate on firestick", "firestick tivimate", "tivimate premium firestick", "troypoint tivimate",
                  "tivimate android tv", "stbemu pro firestick", "firestick ly73pr", "amazon fire stick iptv", "amazon fire tv stick iptv"],
    ),

    # ------------------------------------------------------------------ TIVIMATE DEVICES
    dict(
        slug="tivimate-devices", hub="apps", **D,
        title="TiviMate on Samsung, LG, Apple TV, Roku & PC? | IPTVMaple",
        description="Does TiviMate work on Samsung, LG, Apple TV, iPhone, Roku, Chromecast, Windows or Mac? The honest answer for each device and the best alternative to use.",
        kicker="Compatibility", h1='Does TiviMate work on <span class="grad-text">Samsung, LG, Apple TV, Roku and PC?</span>',
        lead="TiviMate is built for Android TV and Fire TV. Here is exactly where it runs, where it doesn’t, and what to use instead on every other screen.",
        crumb="TiviMate devices", blurb="Where TiviMate runs, and the best alternative on every other device.",
        answer="<p><strong>TiviMate runs only on Android TV and Fire TV devices</strong>, including Firestick, Nvidia Shield, Chromecast with Google TV, Google TV Streamer, Formuler and most Android boxes. It does <em>not</em> run on Samsung (Tizen) or LG (webOS) TVs, Apple TV, iPhone or iPad, Roku, or natively on Windows and Mac. On those devices, use a compatible IPTV app, or plug a Firestick into the TV.</p>",
        body="""
<h2>TiviMate compatibility at a glance</h2>
<table>
<thead><tr><th>Device</th><th>TiviMate?</th><th>Use this instead</th></tr></thead>
<tbody>
<tr><td>Amazon Firestick / Fire TV</td><td>Yes</td><td><a href="/tivimate-firestick/">TiviMate install guide</a></td></tr>
<tr><td>Android TV / Google TV boxes</td><td>Yes</td><td><a href="/iptv-android-tv/">Android TV guide</a></td></tr>
<tr><td>Chromecast with Google TV</td><td>Yes</td><td><a href="/iptv-chromecast/">Chromecast guide</a></td></tr>
<tr><td>Nvidia Shield, Formuler</td><td>Yes</td><td><a href="/formuler-iptv/">Formuler guide</a></td></tr>
<tr><td>Samsung Smart TV</td><td>No</td><td><a href="/smart-iptv/">Smart IPTV</a>, <a href="/smartone-iptv/">SmartOne</a>, <a href="/flix-iptv/">Flix IPTV</a></td></tr>
<tr><td>LG Smart TV (webOS)</td><td>No</td><td><a href="/iptv-lg-tv/">LG guide</a></td></tr>
<tr><td>Apple TV, iPhone, iPad</td><td>No</td><td><a href="/iplaytv/">iPlayTV</a>, <a href="/smarters-player-lite/">Smarters Player Lite</a></td></tr>
<tr><td>Roku</td><td>No</td><td><a href="/iptv-roku/">Roku options</a></td></tr>
<tr><td>Windows and Mac</td><td>No</td><td><a href="/iptv-smarters-pro-pc-mac/">IPTV Smarters Pro</a>, <a href="/vlc-iptv/">VLC</a></td></tr>
<tr><td>Original Chromecast (no Google TV)</td><td>No</td><td>Cast from a phone app, or use a Firestick</td></tr>
</tbody>
</table>

<h2>TiviMate on Samsung TV</h2>
<p>Samsung TVs run Tizen, not Android, so TiviMate can’t be installed. You have two good routes: use a Tizen IPTV app such as Smart IPTV, SmartOne IPTV or Flix IPTV (see <a href="/iptv-samsung-tv/">IPTV on Samsung TV</a>), or plug a Firestick or Google TV streamer into an HDMI port and run TiviMate on that. Many people choose the second option because a stick is quicker and gets regular app updates.</p>

<h2>TiviMate on LG TV</h2>
<p>LG TVs run webOS, which can’t run Android apps. Use an IPTV app from the LG Content Store (see <a href="/iptv-lg-tv/">IPTV on LG TV</a>) or add a Firestick. The result with an external stick is usually faster than a TV’s built-in apps.</p>

<h2>TiviMate on Apple TV, iPhone and iPad</h2>
<p>There is no TiviMate app for iOS, iPadOS or tvOS. On Apple devices use <a href="/iplaytv/">iPlayTV</a> or <a href="/smarters-player-lite/">Smarters Player Lite</a>. Both accept the same IPTVMaple login. See <a href="/iptv-apple-tv/">IPTV on Apple TV</a> for the step-by-step guide.</p>

<h2>TiviMate on Roku</h2>
<p>TiviMate is not available on Roku, and Roku devices have no official IPTV player for this kind of login. Read <a href="/iptv-roku/">can you watch IPTV on Roku?</a> for the options, or use a Firestick or Android TV streamer on the same TV.</p>

<h2>TiviMate on PC and Mac</h2>
<p>TiviMate is a TV app and has no Windows or Mac version. You can run Android apps in an emulator, but the experience isn’t designed for it and we don’t recommend it. A desktop app does the job better: <a href="/iptv-smarters-pro-pc-mac/">IPTV Smarters Pro for PC and Mac</a>, <a href="/vlc-iptv/">VLC</a> or <a href="/kodi-iptv/">Kodi</a>. More options are in the <a href="/iptv-pc-mac/">PC and Mac guide</a>.</p>

<h2>What is the TiviMate Companion app?</h2>
<p>TiviMate Companion is a separate app used to buy and manage <a href="/tivimate-premium/">TiviMate Premium</a>. It doesn’t play TV and doesn’t run TiviMate on a phone. Check the developer’s website for which platforms it supports.</p>

<h2>The easiest setup if your TV isn’t Android</h2>
<ol>
<li>Buy or borrow a Fire TV Stick 4K or a Google TV streamer.</li>
<li>Plug it into your TV’s HDMI port.</li>
<li>Install TiviMate and add your IPTVMaple login.</li>
</ol>
<p>It works on every TV with an HDMI input and keeps your smart TV’s own apps untouched. Start with the <a href="/try-iptv-canada/">free 24-hour trial</a> to test it first.</p>
""",
        faq=[
            ("Does TiviMate work on Samsung TV?",
             "<p>No. Samsung TVs run Tizen, which can’t run Android apps like TiviMate. Use a Samsung IPTV app such as Smart IPTV, SmartOne IPTV or Flix IPTV, or plug a Firestick into the TV and run TiviMate on it.</p>"),
            ("Does TiviMate work on LG TV?",
             "<p>No. LG TVs run webOS and don’t support Android apps. Use an IPTV app from the LG Content Store, or add a Firestick or Google TV streamer.</p>"),
            ("Is there a TiviMate app for Apple TV or iPhone?",
             "<p>No. TiviMate is not available for iOS, iPadOS or tvOS. On Apple devices use iPlayTV or Smarters Player Lite, which both accept the same IPTV login.</p>"),
            ("Can I use TiviMate on Roku?",
             "<p>No. TiviMate isn’t available on Roku. Use a Firestick or Android TV device, or see our Roku IPTV guide for what is possible on Roku itself.</p>"),
            ("Can I use TiviMate on a PC or Mac?",
             "<p>There is no native Windows or Mac version. A desktop app such as IPTV Smarters Pro or VLC is a better choice for a computer.</p>"),
            ("Does TiviMate work on Chromecast?",
             "<p>Yes on Chromecast with Google TV and the Google TV Streamer, because they run Android TV. It doesn’t run on older Chromecasts without the Google TV interface.</p>"),
        ],
        related=["tivimate", "tivimate-firestick", "iptv-apps", "iptv-devices"],
        keywords=["tivimate samsung", "tivimate samsung tv", "tivimate lg", "tivimate apple tv", "tivimate roku", "tivimate pc", "tivimate for pc", "tivimate mac",
                  "tivimate chromecast", "tivimate iphone", "tivimate companion iphone"],
    ),

    # ------------------------------------------------------------------ SMARTERS FIRESTICK
    dict(
        slug="iptv-smarters-pro-firestick", hub="apps", **D,
        title="IPTV Smarters Pro on Firestick: Install & Login | IPTVMaple",
        description="Install IPTV Smarters Pro on a Firestick or Fire TV with Downloader, log in with Xtream Codes, set the guide and fix buffering. Works with IPTVMaple.",
        kicker="Install guide", h1='IPTV Smarters Pro on Firestick: <span class="grad-text">install and log in</span>',
        lead="Smarters Pro is a free player that runs on Fire TV. Here is how to install it and log in, and when TiviMate is the better choice on the same stick.",
        crumb="Smarters Pro on Firestick", blurb="Install IPTV Smarters Pro on Fire TV and log in with Xtream Codes.",
        answer="<p><strong>To install IPTV Smarters Pro on a Firestick:</strong> turn on <em>Install unknown apps</em> for Downloader in <em>Settings → My Fire TV → Developer options</em>, open Downloader, enter the official IPTV Smarters download address from the developer’s website, install the APK, then open the app and choose <em>Login with Xtream Codes API</em>. Enter any name, then your username, password and server URL.</p>",
        body="""
<h2>Before you start</h2>
<p>You need a Firestick or Fire TV that runs Fire OS, an internet connection and your IPTV login. If you don’t have a login yet, start the <a href="/try-iptv-canada/">free 24-hour trial</a> or <a href="/iptv-plans-canada/">choose a plan</a>.</p>
<p>First check the Fire TV search for “IPTV Smarters”. If the app is listed for your region you can install it directly. If it isn’t, use the Downloader steps below.</p>

<h2>Install IPTV Smarters Pro with Downloader</h2>
<ol>
<li>Install <strong>Downloader</strong> from the Amazon Appstore.</li>
<li>Go to <strong>Settings → My Fire TV → Developer options → Install unknown apps</strong> and turn on Downloader. If Developer options is missing, select the device name seven times under <em>About</em>.</li>
<li>Open Downloader and enter the official IPTV Smarters download address from the developer’s website (iptvsmarters.com).</li>
<li>Select <strong>Go</strong>, wait for the download, and choose <strong>Install</strong>.</li>
<li>Open the app and accept the terms.</li>
</ol>
<p>Avoid “modded”, “pro unlocked” or “free subscription” versions from other websites. They are a common source of malware. See <a href="/iptv-smarters-pro-download/">IPTV Smarters Pro download: where to get it safely</a>.</p>

<h2>Log in with your Xtream Codes details</h2>
""" + LOGIN_STEPS + """
<ol>
<li>Choose <strong>Login with Xtream Codes API</strong>.</li>
<li>Enter any name, for example “IPTVMaple”.</li>
<li>Enter the <strong>username</strong>, <strong>password</strong> and <strong>server URL</strong> exactly as we sent them. Copy and paste if possible; stray spaces cause “invalid username or password”.</li>
<li>Choose <strong>Add user</strong>. Channels, movies and series load, and the guide fills in.</li>
</ol>

<h2>Best settings on Fire TV</h2>
<ul>
<li><strong>Player selection</strong> — try the built-in player first. If live sports stutter, switch to an external player.</li>
<li><strong>EPG</strong> — set the time zone for your province and enable automatic guide updates.</li>
<li><strong>Hide categories</strong> you never watch to speed up browsing.</li>
<li><strong>Parental control</strong> — lock categories behind a PIN if children use the TV.</li>
</ul>

<h2>Smarters Pro or TiviMate on a Firestick?</h2>
<table>
<thead><tr><th></th><th>IPTV Smarters Pro</th><th><a href="/tivimate-firestick/">TiviMate</a></th></tr></thead>
<tbody>
<tr><td>Price</td><td>Free</td><td>Free; Premium is optional</td></tr>
<tr><td>Guide</td><td>Good</td><td>Cable-style grid, very polished</td></tr>
<tr><td>Setup</td><td>Very simple</td><td>Slightly more steps</td></tr>
<tr><td>Best for</td><td>First-time users, mixed live and on-demand</td><td>Daily live TV with a remote</td></tr>
</tbody>
</table>
<p>You can install both on the same stick and use the same login. The full comparison is on the <a href="/iptv-smarters-pro/">IPTV Smarters Pro guide</a> and the <a href="/tivimate/">TiviMate guide</a>.</p>

<h2>Smarters Pro on Firestick: common problems</h2>
<ul>
<li><strong>“Invalid username or password”</strong> — re-enter without spaces and check capital letters.</li>
<li><strong>Buffering</strong> — use Ethernet or 5 GHz Wi-Fi. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>Empty guide</strong> — open the app’s Settings and update the EPG.</li>
<li><strong>App closes on start</strong> — clear its cache in <em>Settings → Applications → Manage installed applications</em>, or reinstall.</li>
</ul>
<p>More about the whole stick is in our <a href="/iptv-firestick/">Firestick IPTV guide</a>.</p>
""",
        faq=[
            ("How do I install IPTV Smarters Pro on a Firestick?",
             "<p>Install Downloader, allow it to install unknown apps in Developer options, enter the official IPTV Smarters download address from the developer’s website, install the APK, and open the app. Then log in with your Xtream Codes details.</p>"),
            ("Is IPTV Smarters Pro free on Firestick?",
             "<p>The app is free to download and use. It doesn’t include channels, so you still need an IPTV subscription such as IPTVMaple to get live TV, movies and series.</p>"),
            ("Why does IPTV Smarters say invalid username or password?",
             "<p>Usually a typo or a stray space. Copy the details from your email or WhatsApp message, check capital letters, and make sure the server URL starts with http:// or https:// and includes the port if one was given.</p>"),
            ("Which is better on Firestick, Smarters Pro or TiviMate?",
             "<p>TiviMate has the nicer live TV guide and works best with a remote. Smarters Pro is simpler to set up and free. Many people install both and use the same login.</p>"),
            ("Can I use IPTV Smarters Pro on several Fire TVs?",
             "<p>Yes, with the same login on each, as long as the number of screens watching at the same time stays within your plan (1 to 5).</p>"),
            ("Is it safe to sideload IPTV Smarters Pro?",
             "<p>It is safe when you download the app from the developer’s official website. Avoid modified or “unlocked” versions from other sites.</p>"),
        ],
        related=["iptv-smarters-pro", "tivimate-firestick", "iptv-firestick", "iptv-smarters-pro-download"],
        keywords=["iptv smarters pro firestick", "iptv smasters pro fire stick", "iptv smasters pro firestick", "iptv smasters firestick", "iptv smasters fire stick",
                  "iptv smasters for firestick", "iptv smasters on firestick", "smarters pro firestick", "smarters iptv firestick", "smarters player lite firestick",
                  "iptv smasters pro downloader", "iptv smasters pro android tv", "iptv smasters android tv", "xciptv firestick"],
    ),

    # ------------------------------------------------------------------ SMARTERS SAMSUNG / LG
    dict(
        slug="iptv-smarters-pro-samsung-lg", hub="apps", **D,
        title="IPTV Smarters on Samsung & LG TV: Setup Guide | IPTVMaple",
        description="Set up IPTV Smarters (Smarters Player Lite) on Samsung Tizen and LG webOS TVs: where to find the app, how to log in, and what to do if it’s missing.",
        kicker="Smart TV guide", h1='IPTV Smarters on <span class="grad-text">Samsung and LG TV</span>',
        lead="Smart TVs have their own app stores, and the Smarters app is named slightly differently there. Here is how to find it, log in and fix the usual problems.",
        crumb="Smarters on Samsung & LG", blurb="Find and set up the Smarters app on Samsung and LG smart TVs.",
        answer="<p><strong>On Samsung and LG TVs the Smarters app is usually listed as “Smarters Player Lite”</strong> in the Samsung Smart Hub or the LG Content Store. Search for “Smarters”, install it, open it and choose <em>Login with Xtream Codes API</em> to enter your username, password and server URL. If your TV model or region doesn’t list it, use Smart IPTV, SmartOne IPTV or Flix IPTV, or plug in a Firestick.</p>",
        body="""
<h2>Will it work on my TV?</h2>
<p>Availability depends on your TV’s age, operating system and region:</p>
<ul>
<li><strong>Samsung</strong> — Tizen smart TVs from roughly 2017 onwards have the widest app support. Older models may not list newer apps.</li>
<li><strong>LG</strong> — webOS TVs from roughly 2018 onwards usually work. Very old webOS versions may not.</li>
<li><strong>Regional stores</strong> — an app can appear in one country’s store and not another’s.</li>
</ul>
<p>If the Smarters app isn’t available on your TV, you have good alternatives in the same store: see <a href="/iptv-samsung-tv/">IPTV on Samsung TV</a> and <a href="/iptv-lg-tv/">IPTV on LG TV</a>.</p>

<h2>Install on a Samsung Smart TV</h2>
<ol>
<li>Press <strong>Home</strong> on the remote and open <strong>Apps</strong>.</li>
<li>Select the search icon and type <strong>Smarters</strong>.</li>
<li>Choose <strong>Smarters Player Lite</strong> and select <strong>Install</strong>.</li>
<li>Open the app and accept the terms.</li>
</ol>

<h2>Install on an LG Smart TV</h2>
<ol>
<li>Press the <strong>Home</strong> button and open the <strong>LG Content Store</strong>.</li>
<li>Search for <strong>Smarters</strong> and open the result.</li>
<li>Select <strong>Install</strong>, then <strong>Launch</strong>.</li>
</ol>

<h2>Log in to your IPTV service</h2>
""" + LOGIN_STEPS + """
<ol>
<li>Select <strong>Add User</strong> and choose <strong>Login with Xtream Codes API</strong>.</li>
<li>Type any name, then the username, password and server URL. A phone keyboard app or a USB keyboard makes typing faster.</li>
<li>Confirm. Your channels and the guide load.</li>
</ol>
<p>Prefer to use the M3U link instead? Choose the playlist option and enter the link we sent.</p>

<h2>If you can’t find the app</h2>
<table>
<thead><tr><th>Option</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Another IPTV app in the same store</td><td>Try <a href="/smart-iptv/">Smart IPTV</a>, <a href="/smartone-iptv/">SmartOne IPTV</a> or <a href="/flix-iptv/">Flix IPTV</a></td></tr>
<tr><td>Add a streaming stick</td><td>Plug a Firestick into the HDMI port and use <a href="/tivimate-firestick/">TiviMate</a> or <a href="/iptv-smarters-pro-firestick/">Smarters Pro</a></td></tr>
<tr><td>Cast from a phone</td><td>Use Smarters on your phone and cast to the TV (quality depends on your Wi-Fi)</td></tr>
</tbody>
</table>

<h2>Samsung and LG troubleshooting</h2>
<ul>
<li><strong>Login failed</strong> — retype carefully; a stray space is the most common cause.</li>
<li><strong>No guide data</strong> — update the EPG in the app’s Settings and check the TV’s date and time zone.</li>
<li><strong>Playback stutters</strong> — a wired Ethernet connection to the TV helps. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>App crashes after a TV update</strong> — reinstall the app or restart the TV by unplugging it for a minute.</li>
</ul>
<p>Need a login first? Start the <a href="/try-iptv-canada/">free trial</a>. Parlez français? Voir <a href="/iptv-smarters-pro-francais/">IPTV Smarters Pro en français</a>.</p>
""",
        faq=[
            ("Is IPTV Smarters Pro available on Samsung TV?",
             "<p>In the Samsung Smart Hub the Smarters app is usually listed as Smarters Player Lite. Availability depends on your TV’s age and region. If you can’t find it, use Smart IPTV, SmartOne IPTV or Flix IPTV, or plug in a Firestick.</p>"),
            ("Is IPTV Smarters available on LG webOS?",
             "<p>It is usually listed in the LG Content Store as Smarters Player Lite for webOS TVs from about 2018 onwards. Search for Smarters. If it isn’t listed for your model or country, use another IPTV app or a streaming stick.</p>"),
            ("How do I log in on a smart TV?",
             "<p>Choose Login with Xtream Codes API, enter any name, then your username, password and server URL. Copy the details from your email or WhatsApp message to avoid typing mistakes.</p>"),
            ("Why is the Smarters app missing on my TV?",
             "<p>Usually because the TV model is too old, the TV’s software isn’t updated or the app isn’t offered in your country’s store. Update the TV, try another app from the same store, or add a Firestick.</p>"),
            ("Is a Firestick better than the TV’s own app?",
             "<p>Often yes. A stick is faster, receives frequent updates and can run TiviMate. Your TV’s built-in apps remain untouched.</p>"),
        ],
        related=["iptv-smarters-pro", "iptv-samsung-tv", "iptv-lg-tv", "smart-iptv"],
        keywords=["iptv smarters pro samsung tv", "iptv smarters pro lg", "iptv smasters lg", "iptv smasters lg tv", "iptv smasters samsung", "iptv smasters samsung tv",
                  "iptv smasters pro samsung tv", "iptv smasters pro lg", "samsung iptv smarters", "iptv smasters player samsung", "smarters player lite samsung tv",
                  "iptv smarters pro smart tv", "iptv smasters smart tv", "iptv smasters pro smart tv", "iptv smasters tv", "iptv smasters pro tv", "smarters pro tv",
                  "smarters tv pro", "tv smarters pro", "tv smarters", "smarterstv", "smarters player tv", "smarters player lite tv", "smarters lite", "smarters pro lite",
                  "smarters player pro", "smarter player pro", "samsung tizen iptv", "iptv samsung tizen", "iptv tizen", "webos iptv", "iptv for lg webos"],
    ),

    # ------------------------------------------------------------------ SMARTERS PC / MAC
    dict(
        slug="iptv-smarters-pro-pc-mac", hub="apps", **D,
        title="IPTV Smarters Pro for PC & Mac: Install Guide | IPTVMaple",
        description="Install IPTV Smarters Pro on Windows or Mac, log in with Xtream Codes, and see the best alternatives (VLC, Kodi) for watching IPTV on a computer.",
        kicker="Computer guide", h1='IPTV Smarters Pro for <span class="grad-text">PC and Mac</span>',
        lead="A computer is a great IPTV screen. Here is how to install Smarters Pro on Windows or macOS, log in and pick the right alternative if you prefer VLC or Kodi.",
        crumb="Smarters Pro on PC & Mac", blurb="Install IPTV Smarters Pro on Windows and Mac and log in.",
        answer="<p><strong>IPTV Smarters Pro has desktop versions for Windows and macOS.</strong> Download the installer from the official IPTV Smarters website (or the Mac App Store listing, where available), install it, choose <em>Login with Xtream Codes API</em> and enter your name, username, password and server URL. If you prefer something simpler, open your M3U link in VLC.</p>",
        body="""
<h2>Which version do you need?</h2>
<table>
<thead><tr><th>Computer</th><th>How to get Smarters Pro</th></tr></thead>
<tbody>
<tr><td>Windows 10 / 11</td><td>Official installer from the IPTV Smarters website, or the Microsoft Store listing where available</td></tr>
<tr><td>Mac (macOS)</td><td>Mac App Store listing where available, or the macOS download on the official website</td></tr>
<tr><td>Chromebook</td><td>Android version from Google Play, if your Chromebook supports Android apps</td></tr>
</tbody>
</table>
<p>Stores and download pages change, so use the developer’s official website to find the current version, and avoid any other site that offers “free pro” files.</p>

<h2>Install on Windows</h2>
<ol>
<li>Download the Windows installer from the official website.</li>
<li>Run the installer and follow the prompts.</li>
<li>Open <strong>IPTV Smarters Pro</strong> from the Start menu.</li>
</ol>

<h2>Install on Mac</h2>
<ol>
<li>Open the Mac App Store and search for “IPTV Smarters Pro”, or download the macOS version from the official website.</li>
<li>Install it and open it from Launchpad.</li>
<li>If macOS blocks a downloaded app, open <em>System Settings → Privacy &amp; Security</em> and allow it, but only for a file you downloaded from the official site.</li>
</ol>

<h2>Log in with Xtream Codes</h2>
""" + LOGIN_STEPS + """
<ol>
<li>Click <strong>Add User</strong> and choose <strong>Login with Xtream Codes API</strong>.</li>
<li>Enter any name, then the username, password and server URL.</li>
<li>Click <strong>Add User</strong>. Live TV, movies, series and the guide appear.</li>
</ol>

<h2>Alternatives to Smarters Pro on a computer</h2>
<table>
<thead><tr><th>App</th><th>Best for</th><th>Guide</th></tr></thead>
<tbody>
<tr><td>VLC</td><td>Quick playback of an M3U link, no account</td><td><a href="/vlc-iptv/">VLC IPTV guide</a></td></tr>
<tr><td>Kodi</td><td>A full media centre with a TV guide</td><td><a href="/kodi-iptv/">Kodi IPTV guide</a></td></tr>
<tr><td>Browser</td><td>Not recommended for most logins</td><td><a href="/watch-iptv-online/">Watch IPTV online</a></td></tr>
</tbody>
</table>

<h2>Send a computer to the TV</h2>
<p>Connect the computer to your TV with an HDMI cable, or use a Chromecast or Firestick for a wireless setup. For a permanent living-room solution, a <a href="/iptv-firestick/">Firestick</a> with <a href="/tivimate/">TiviMate</a> is usually more comfortable than a laptop.</p>

<h2>Troubleshooting on Windows and Mac</h2>
<ul>
<li><strong>Black screen</strong> — update your graphics driver, or switch the player in Smarters’ settings.</li>
<li><strong>Login fails</strong> — re-copy the credentials; check for spaces.</li>
<li><strong>Stutters</strong> — use Ethernet and close other apps. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>App not opening on Mac</strong> — re-download from the official source and allow it in Privacy &amp; Security.</li>
</ul>
<p>Overview of all computer options: <a href="/iptv-pc-mac/">IPTV on PC and Mac</a>. Need a login? Start the <a href="/try-iptv-canada/">free trial</a>.</p>
""",
        faq=[
            ("Is there an IPTV Smarters Pro for PC?",
             "<p>Yes. There are desktop versions for Windows and macOS. Download them from the developer’s official website or the store listing where available, then log in with your Xtream Codes details.</p>"),
            ("How do I install IPTV Smarters Pro on a Mac?",
             "<p>Search for IPTV Smarters Pro in the Mac App Store or download the macOS version from the official website. Install it, open it and choose Login with Xtream Codes API.</p>"),
            ("Is VLC better than Smarters Pro on a computer?",
             "<p>VLC is simpler for playing one M3U link. Smarters Pro gives you a channel list, a TV guide and a movies and series library. Choose by how much interface you want.</p>"),
            ("Can I watch IPTV on a MacBook?",
             "<p>Yes. Use IPTV Smarters Pro for macOS or open your M3U link in VLC. Both work on any recent MacBook.</p>"),
            ("Why is my screen black in Smarters Pro on Windows?",
             "<p>Try switching to a different player in the settings and update your graphics driver. A VPN or a very slow connection can also cause a black screen.</p>"),
        ],
        related=["iptv-smarters-pro", "iptv-pc-mac", "vlc-iptv", "kodi-iptv"],
        keywords=["iptv smarters pro pc", "iptv smarters pc", "iptv smasters pc", "iptv smasters for pc", "iptv smasters pro for pc", "iptv smasters mac", "iptv smasters pro mac",
                  "iptv smasters pro macbook", "iptv macbook", "iptv smarter pc", "smarters pro pc", "mac iptv", "iptv laptop", "ip tv pc", "iptv pc", "iptv smasters pc",
                  "iptv smasters pour pc", "iptv smasters pro sur pc", "iptv smasters pro pc", "iptv smasters pro mac", "iptv smasters pro for pc", "smart iptv pc", "smart iptv mac",
                  "smarters pro pc", "strymtv for pc", "iptv player pc", "iptv player m3u pc", "m3u player pc"],
    ),

    # ------------------------------------------------------------------ SMARTERS DOWNLOAD
    dict(
        slug="iptv-smarters-pro-download", hub="apps", **D,
        title="IPTV Smarters Pro Download: Android & APK Safety | IPTVMaple",
        description="Where to download IPTV Smarters Pro safely: Google Play, the official APK, Downloader on Fire TV and the App Store. Is it free, and how to avoid fake versions.",
        kicker="Download guide", h1='IPTV Smarters Pro download: <span class="grad-text">where to get it safely</span>',
        lead="Dozens of sites offer an “IPTV Smarters Pro APK”. Only a few are safe. Here is where the real app lives on every device and how to spot a fake.",
        crumb="Smarters Pro download", blurb="Where to download IPTV Smarters Pro safely on Android, Fire TV, iPhone and PC.",
        answer="<p><strong>Download IPTV Smarters Pro only from official sources</strong>: Google Play or the official IPTV Smarters website for Android, the Downloader app with the official address on Fire TV, the App Store for iPhone and iPad (as Smarters Player Lite), and the developer’s website for Windows and Mac. The app is free; the channels come from your IPTV subscription. Avoid “modded”, “premium unlocked” and “free IPTV” versions.</p>",
        body="""
<h2>Is IPTV Smarters Pro free?</h2>
<p>Yes. The app itself is free to download and use. It is a player: it doesn’t contain channels. To watch live TV, movies and series you add the login from an IPTV provider. With IPTVMaple that login arrives by email and WhatsApp after you <a href="/iptv-plans-canada/">subscribe</a> or start the <a href="/try-iptv-canada/">free trial</a>.</p>
<p>Anyone who offers “free IPTV Smarters Pro with 20,000 channels” is selling something else, and the channels they promise are usually unauthorized or unreliable. See <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> for the risks.</p>

<h2>Where to download it, by device</h2>
<table>
<thead><tr><th>Device</th><th>Where to get it</th></tr></thead>
<tbody>
<tr><td>Android phone or tablet</td><td>Google Play, if listed in your region; otherwise the APK from the official IPTV Smarters website</td></tr>
<tr><td>Android TV and Google TV</td><td>Google Play on the TV, or the official APK</td></tr>
<tr><td>Amazon Firestick / Fire TV</td><td>Amazon Appstore if listed, otherwise Downloader with the <a href="/iptv-smarters-pro-firestick/">official address</a></td></tr>
<tr><td>iPhone, iPad, Apple TV</td><td>The App Store, as <a href="/smarters-player-lite/">Smarters Player Lite</a></td></tr>
<tr><td>Windows and Mac</td><td>The developer’s website; see the <a href="/iptv-smarters-pro-pc-mac/">PC and Mac guide</a></td></tr>
<tr><td>Samsung and LG TV</td><td>Samsung Smart Hub / LG Content Store: <a href="/iptv-smarters-pro-samsung-lg/">TV guide</a></td></tr>
</tbody>
</table>

<h2>How to install the APK on Android</h2>
<ol>
<li>Download the APK from the official IPTV Smarters website in your phone’s browser.</li>
<li>When asked, allow your browser to install apps (<em>Settings → Apps → Special access → Install unknown apps</em>, menu names vary by phone).</li>
<li>Open the downloaded file and tap <strong>Install</strong>.</li>
<li>After installing, turn the “install unknown apps” permission back off.</li>
</ol>

<h2>The “Downloader” app on Fire TV</h2>
<p>People searching for “IPTV downloader” often mean the free Downloader app on Fire TV. It opens a web address and installs the file it downloads. It isn’t a source of channels: it only installs apps. Our step-by-step guides are <a href="/iptv-smarters-pro-firestick/">Smarters Pro on Firestick</a> and <a href="/tivimate-firestick/">TiviMate on Firestick</a>.</p>

<h2>Why can’t I find it on Google Play?</h2>
<p>Availability changes by country, device and over time. If you can’t find it, install the APK from the official website, or use another player that is on Google Play: <a href="/tivimate/">TiviMate</a> on Android TV, <a href="/xciptv/">XCIPTV</a> or <a href="/implayer/">IMPlayer</a>.</p>

<h2>How to avoid fake or modified versions</h2>
<ul>
<li>Use the developer’s official website or an official store, never a random file-sharing link.</li>
<li>Be suspicious of “pro unlocked”, “mod”, “cracked”, “lifetime free” or “no subscription needed”.</li>
<li>Check what permissions the app asks for. A TV player doesn’t need your contacts or SMS.</li>
<li>Never enter your IPTV login on a website that isn’t your provider’s.</li>
</ul>

<h2>After you download: log in</h2>
""" + LOGIN_STEPS + """
<p>Open the app, choose <strong>Login with Xtream Codes API</strong> and enter your name, username, password and server URL. Full guide: <a href="/iptv-smarters-pro/">IPTV Smarters Pro setup and login</a>.</p>
""",
        faq=[
            ("Where can I download IPTV Smarters Pro?",
             "<p>From Google Play or the official IPTV Smarters website on Android, via Downloader on Fire TV, from the App Store as Smarters Player Lite on Apple devices, and from the developer’s website on Windows and Mac.</p>"),
            ("Is IPTV Smarters Pro free?",
             "<p>The app is free. It doesn’t include channels, so you need an IPTV subscription, such as IPTVMaple, to get live TV, movies and series.</p>"),
            ("Is the IPTV Smarters Pro APK safe?",
             "<p>The official APK from the developer’s website is safe. Modified, unlocked or re-uploaded files from other sites are risky and can contain malware. Download only from the official source.</p>"),
            ("Why is IPTV Smarters Pro not on Google Play?",
             "<p>Availability varies by country and over time. If you can’t find it, install the official APK from the developer’s website, or use another player from Google Play such as TiviMate on Android TV.</p>"),
            ("What does ‘IPTV Downloader’ mean?",
             "<p>It usually refers to the free Downloader app on Fire TV, which installs apps from a web address. It doesn’t provide channels or a subscription.</p>"),
            ("Can I get IPTV Smarters Pro for free with channels included?",
             "<p>No. The app is free but contains no channels. Offers of free channels are unreliable and often unauthorized. Test a real service with a free trial instead.</p>"),
        ],
        related=["iptv-smarters-pro", "iptv-smarters-pro-firestick", "smarters-player-lite", "iptv-apps"],
        keywords=["iptv smarters pro android", "iptv smarters android", "iptv smarters downloader", "iptv smarters pro downloader", "iptv smarters pro free", "iptv smasters free",
                  "iptv smasters google play", "iptv smasters pro com", "iptv smarters com", "iptv smasters player android", "iptv smasters pro introuvable google play",
                  "iptv downloader", "smart iptv downloader", "m3u downloader online", "iptv smarters pro price", "iptv smasters pro price", "iptv smasters premium",
                  "iptv smarters customer service", "iptv customer service", "iptv smasters pro live", "iptv smasters google play", "ip smarters pro", "ip smarter pro",
                  "smarters iptv pro", "iptv smarters pro downloader", "iptv smasters m3u", "iptv smasters pro m3u", "smarters pro iptv"],
    ),

    # ------------------------------------------------------------------ PLEX
    dict(
        slug="plex-iptv", hub="apps", **D,
        title="IPTV on Plex: Can Plex Play M3U Live TV? (2026) | IPTVMaple",
        description="Can you watch IPTV on Plex? Plex has no native M3U import. How Live TV & DVR works, the community workaround, its limits, and easier alternatives.",
        kicker="Media server guide", h1='IPTV on Plex: <span class="grad-text">what works and what doesn’t</span>',
        lead="Plex is a media server, not an IPTV player. It can show live TV, but not straight from an M3U link. Here is the honest picture and the options.",
        crumb="IPTV on Plex", blurb="Can Plex play IPTV and M3U playlists? The honest answer and options.",
        answer="<p><strong>Plex does not natively accept IPTV M3U playlists or Xtream Codes logins.</strong> Its Live TV and DVR feature is built for supported tuner hardware and antenna or cable sources. People get IPTV into Plex with a community tool that imitates a tuner (such as Threadfin or xTeVe). This is unofficial, takes some technical setup, and is not supported by Plex. For simpler IPTV viewing, use a dedicated player app, or use Jellyfin, which accepts M3U directly.</p>",
        body="""
<h2>Does Plex support IPTV?</h2>
<p>Plex has a <em>Live TV &amp; DVR</em> feature, but it expects a network tuner, such as an HDHomeRun, or a supported antenna or cable source. It doesn’t have an option to paste an M3U link or an Xtream Codes login. Plex also offers its own free, ad-supported channels; those aren’t your IPTV subscription.</p>

<h2>The community workaround</h2>
<p>A small server program such as <strong>Threadfin</strong> or <strong>xTeVe</strong> can take an M3U playlist and an XMLTV guide and present them to Plex as if they came from a tuner. In outline:</p>
<ol>
<li>Install Threadfin or xTeVe on the same machine as Plex, or on a NAS or Docker host.</li>
<li>Add your IPTV playlist (the M3U link from your provider) and, if you have one, the guide (XMLTV) link.</li>
<li>Filter the channel list down to the groups you really watch. Plex copes better with a few hundred channels than with tens of thousands.</li>
<li>In Plex go to <strong>Settings → Live TV &amp; DVR → Set up Plex DVR</strong> and pick the emulated tuner.</li>
<li>Match the channels to the guide and finish the setup.</li>
</ol>
<p>Plex DVR may require a Plex Pass subscription. Details change, so check Plex’s own support pages.</p>

<h2>Limits you should know about</h2>
<ul>
<li><strong>Not supported by Plex or by your IPTV provider.</strong> If something breaks, you’re on your own.</li>
<li><strong>Connections.</strong> Each channel watched through Plex uses a connection from your IPTV plan, and Plex may open streams in the background for guide data or recording.</li>
<li><strong>Server load.</strong> Plex may transcode, which needs a capable computer.</li>
<li><strong>Channel and guide limits.</strong> Huge playlists make the Plex guide slow.</li>
</ul>

<h2>Easier ways to watch IPTV</h2>
<table>
<thead><tr><th>Goal</th><th>Better tool</th></tr></thead>
<tbody>
<tr><td>Just watch live TV on a TV</td><td><a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></td></tr>
<tr><td>Live TV in a self-hosted server</td><td><a href="/jellyfin-iptv/">Jellyfin</a>, which accepts M3U directly</td></tr>
<tr><td>Free media centre on a computer</td><td><a href="/kodi-iptv/">Kodi</a></td></tr>
<tr><td>Quick test on a computer</td><td><a href="/vlc-iptv/">VLC</a></td></tr>
</tbody>
</table>

<h2>Be careful with “Plex M3U” lists</h2>
<p>“Plex M3U” and “Plex IPTV” searches often lead to free playlists shared on forums. These are typically unreliable and can be unauthorized or unsafe. See <a href="/m3u-playlist/">what an M3U playlist is</a> and <a href="/is-iptv-legal-in-canada/">is IPTV legal in Canada?</a> before using one.</p>
<p>Want a reliable source to test with? Start the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>
""",
        faq=[
            ("Can Plex play IPTV M3U playlists?",
             "<p>Not directly. Plex has no option to import an M3U playlist or Xtream Codes login. A community tool such as Threadfin or xTeVe can present your playlist to Plex as a tuner, but this is unofficial and not supported by Plex.</p>"),
            ("Do I need Plex Pass for IPTV?",
             "<p>Plex’s Live TV and DVR features may require Plex Pass. Plex’s support pages list the current requirements, which can change.</p>"),
            ("Is there an easier way than Plex?",
             "<p>Yes. A dedicated IPTV app like TiviMate or IPTV Smarters Pro is much simpler, and Jellyfin accepts M3U playlists and XMLTV guides directly.</p>"),
            ("Why is my Plex IPTV guide slow?",
             "<p>Plex struggles with very large channel lists. Filter your playlist to the groups you watch before adding it to the tuner emulator.</p>"),
            ("Will Plex use more of my IPTV connections?",
             "<p>It can. Each channel streamed through Plex counts as a connection on your plan, and background tasks such as recording or guide scans may open streams too.</p>"),
        ],
        related=["jellyfin-iptv", "m3u-playlist", "kodi-iptv", "iptv-apps"],
        keywords=["plex iptv", "m3u plex", "plex m3u", "plex iptv m3u", "iptv plex"],
    ),

    # ------------------------------------------------------------------ JELLYFIN / EMBY
    dict(
        slug="jellyfin-iptv", hub="apps", **D,
        title="IPTV on Jellyfin & Emby: Add an M3U Tuner | IPTVMaple",
        description="How to watch IPTV on Jellyfin: add an M3U tuner and XMLTV guide in Live TV settings, watch on Android TV, Fire TV, Apple and web. Emby notes included.",
        kicker="Media server guide", h1='IPTV on Jellyfin and Emby: <span class="grad-text">add an M3U tuner</span>',
        lead="Unlike Plex, Jellyfin has a built-in M3U tuner. Add your IPTV playlist and guide, and watch live TV on every device that runs Jellyfin.",
        crumb="IPTV on Jellyfin", blurb="Add an M3U tuner and TV guide to Jellyfin or Emby.",
        answer="<p><strong>Jellyfin can play IPTV directly.</strong> In the Jellyfin dashboard open <em>Live TV</em>, choose <em>Add tuner device</em>, select <em>M3U Tuner</em>, paste your M3U link, then add an XMLTV guide under <em>TV guide data providers</em>. Emby works the same way but requires an Emby Premiere subscription for Live TV. Both use one connection from your IPTV plan per channel watched.</p>",
        body="""
<h2>What you need</h2>
<ul>
<li>A Jellyfin server (on a PC, NAS or home server). Install it from <a href="https://jellyfin.org/" rel="noopener">jellyfin.org</a>.</li>
<li>Your IPTV <strong>M3U playlist link</strong> and, if available, the <strong>XMLTV guide link</strong> from your provider.</li>
<li>A Jellyfin app on your viewing device: Android TV, Fire TV, Apple devices and the web browser are supported.</li>
</ul>
<p>IPTVMaple customers receive an M3U link with their login. Ask our team on WhatsApp for the guide link if you need it. New to IPTV? Start the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>

<h2>Add your IPTV playlist to Jellyfin</h2>
<ol>
<li>Sign in to the Jellyfin web dashboard as an administrator.</li>
<li>Open <strong>Dashboard → Live TV</strong>.</li>
<li>Under <strong>Tuner Devices</strong>, select <strong>Add</strong> and choose <strong>M3U Tuner</strong>.</li>
<li>Paste the M3U link (or choose a file), set the number of simultaneous streams to match your plan, and save.</li>
<li>Under <strong>TV Guide Data Providers</strong>, add <strong>XMLTV</strong> with your guide link and save.</li>
<li>Open the Live TV section of the Jellyfin app, refresh the guide data, and your channels appear.</li>
</ol>
<p>Menus can differ slightly between Jellyfin versions. The official documentation at jellyfin.org has the current screens.</p>

<h2>Tips for a smooth experience</h2>
<ul>
<li><strong>Match the stream limit to your plan.</strong> If you have a 2-screen plan, don’t allow more than two simultaneous streams.</li>
<li><strong>Trim the playlist.</strong> Remove channel groups you never watch before importing; the guide loads faster.</li>
<li><strong>Use direct play.</strong> Set client apps to play without transcoding when possible, to avoid server load.</li>
<li><strong>Wired connections.</strong> Put the server and TV on Ethernet if you can. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
</ul>

<h2>Emby</h2>
<p>Emby offers a similar M3U tuner in its server settings under <em>Live TV</em>, but Live TV and DVR in Emby require an <strong>Emby Premiere</strong> subscription. The steps are close to Jellyfin: add a tuner of type M3U, then an XMLTV guide source. Check Emby’s own help pages for current requirements.</p>

<h2>Jellyfin or a dedicated IPTV app?</h2>
<table>
<thead><tr><th></th><th>Jellyfin / Emby</th><th>TiviMate / Smarters</th></tr></thead>
<tbody>
<tr><td>Setup effort</td><td>Higher: needs a server</td><td>Low: install and log in</td></tr>
<tr><td>Best for</td><td>One library for your own media and live TV</td><td>Watching IPTV on the TV</td></tr>
<tr><td>Guide quality</td><td>Good</td><td>TiviMate is excellent</td></tr>
<tr><td>Devices</td><td>Most platforms via Jellyfin apps</td><td>Depends on the app</td></tr>
</tbody>
</table>
<p>If you only want to watch IPTV, <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> is the simpler route. Compare more apps in our <a href="/iptv-apps/">IPTV apps guide</a>. Using Plex? Read <a href="/plex-iptv/">IPTV on Plex</a>.</p>
""",
        faq=[
            ("Can Jellyfin play IPTV?",
             "<p>Yes. Jellyfin includes an M3U tuner. Add your M3U link under Dashboard, Live TV, Tuner Devices, then add an XMLTV guide under TV Guide Data Providers.</p>"),
            ("Does Emby support IPTV?",
             "<p>Yes, with an M3U tuner and an XMLTV guide, but Live TV and DVR in Emby require an Emby Premiere subscription.</p>"),
            ("How many streams should I allow in Jellyfin?",
             "<p>No more than your IPTV plan allows. IPTVMaple plans cover 1 to 5 simultaneous screens, and each channel watched through Jellyfin uses one connection.</p>"),
            ("Where do I get an XMLTV guide link?",
             "<p>Ask your provider. With IPTVMaple, contact support on WhatsApp or email and we will send the guide link that matches your playlist.</p>"),
            ("Is Jellyfin better than TiviMate?",
             "<p>They do different jobs. Jellyfin is a media server that can also show live TV. TiviMate is a dedicated IPTV player with a polished TV guide. If you just want live TV on your television, TiviMate is simpler.</p>"),
        ],
        related=["plex-iptv", "kodi-iptv", "m3u-playlist", "iptv-apps"],
        keywords=["jellyfin iptv", "emby iptv", "iptv emby", "iptv jellyfin"],
    ),

    # ------------------------------------------------------------------ STREMIO
    dict(
        slug="stremio-iptv", hub="apps", **D,
        title="IPTV on Stremio: Add-ons, Limits & Options | IPTVMaple",
        description="Can Stremio play IPTV? Stremio has no built-in live TV. How community M3U/EPG add-ons work, the risks, and simpler apps for live channels.",
        kicker="App guide", h1='IPTV on Stremio: <span class="grad-text">what is possible</span>',
        lead="Stremio is a streaming hub for movies and series. Live IPTV channels aren’t part of the core app, but community add-ons can fill the gap.",
        crumb="IPTV on Stremio", blurb="Stremio and IPTV: community add-ons, limits and simpler options.",
        answer="<p><strong>Stremio has no built-in IPTV or live TV support.</strong> Third-party community add-ons can load an M3U playlist and a TV guide, but they are not made or supported by Stremio and their quality varies. For live channels with a proper TV guide, a dedicated player such as TiviMate or IPTV Smarters Pro is more reliable.</p>",
        body="""
<h2>What Stremio is, and isn’t</h2>
<p>Stremio gathers movies and series from add-ons into one interface. Its focus is on-demand video. It was not designed as a live TV player with a grid guide, channel groups and catch-up, which is what IPTV viewers usually want.</p>

<h2>How IPTV add-ons work</h2>
<p>Some independent developers publish Stremio add-ons that read an IPTV M3U playlist and, optionally, an XMLTV guide, then list the channels in Stremio. To use one:</p>
<ol>
<li>Open Stremio and go to the <strong>Add-ons</strong> section.</li>
<li>Install the add-on you chose from its page, or by entering its address.</li>
<li>Configure it with your M3U link (and guide link, if supported).</li>
<li>Channels appear under the add-on’s catalogue.</li>
</ol>
<p>We don’t endorse any specific add-on. Their behaviour depends on the developer.</p>

<h2>Risks and limits</h2>
<ul>
<li><strong>Your playlist link contains your login.</strong> If you enter it into a hosted add-on configuration page, the add-on’s server sees it. Only use add-ons you trust, and ask your provider to change your password if you’re unsure.</li>
<li><strong>No official support</strong> from Stremio or from your IPTV provider.</li>
<li><strong>Weak guide features.</strong> No full grid guide, recording or catch-up like in a dedicated player.</li>
<li><strong>Add-ons come and go</strong> and can break after an update.</li>
</ul>

<h2>Better ways to watch IPTV</h2>
<table>
<thead><tr><th>Device</th><th>Recommended app</th></tr></thead>
<tbody>
<tr><td>Firestick, Android TV</td><td><a href="/tivimate-firestick/">TiviMate</a></td></tr>
<tr><td>Phone, tablet, computer</td><td><a href="/iptv-smarters-pro/">IPTV Smarters Pro</a></td></tr>
<tr><td>Apple TV, iPhone</td><td><a href="/iplaytv/">iPlayTV</a> or <a href="/smarters-player-lite/">Smarters Player Lite</a></td></tr>
<tr><td>Self-hosted server</td><td><a href="/jellyfin-iptv/">Jellyfin</a></td></tr>
</tbody>
</table>
<p>See all options in the <a href="/iptv-apps/">IPTV apps guide</a>. To test with a real login, start the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>
""",
        faq=[
            ("Does Stremio support IPTV?",
             "<p>Not natively. Stremio has no built-in live TV. Community add-ons can load M3U playlists, but they are not made or supported by Stremio.</p>"),
            ("Is it safe to put my IPTV link into a Stremio add-on?",
             "<p>Your playlist link contains your username and password, so only use add-ons you trust. If you’re unsure, ask your provider to reset your password.</p>"),
            ("What is the best app for IPTV instead of Stremio?",
             "<p>TiviMate on Firestick and Android TV, IPTV Smarters Pro on phones and computers, and iPlayTV or Smarters Player Lite on Apple devices.</p>"),
            ("Can I use Stremio and IPTVMaple together?",
             "<p>You can try a community add-on with your M3U link, but we recommend a dedicated IPTV app for live TV. The free trial lets you test both.</p>"),
        ],
        related=["iptv-apps", "tivimate", "iptv-smarters-pro", "jellyfin-iptv"],
        keywords=["stremio iptv", "iptv stremio"],
    ),
]
