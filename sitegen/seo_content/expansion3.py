"""Expansion pass 3 (2026-10-05): the two keyword clusters still without a page after expansion passes 1 and 2.

- MyIPTV Player ("my iptv", "my ip tv", "myiptv player"): a free Windows player that the PC page only listed in a table.
- IPTV on 5G and mobile data ("5g iptv", "5giptv", "iptv sim"): 5G home internet and phone data plans, which the Starlink and
  iPhone pages touch only in passing.
Third-party app facts were checked on the Microsoft Store listing and established reviews on 2026-10-05. Speed and data figures
match the rest of the site (10 Mbps HD / 25 Mbps 4K per screen; 1 to 3 GB per hour for HD) and the 4K figure is plain
arithmetic from the stream bitrate.
"""
from ._util import price_range

D = dict(published="2026-10-05", updated="2026-10-05")
LOW, PER_MONTH = price_range()

PAGES = [
    # ------------------------------------------------------------------ MyIPTV Player (Windows)
    dict(
        slug="myiptv-player", hub="apps", **D,
        title="MyIPTV Player Setup on Windows: M3U & EPG Guide | IPTVMaple",
        description="Set up MyIPTV Player on a Windows PC: add your M3U link and EPG, turn on the VLC engine, use favourites and the PIN lock, and fix common errors. Free 24h trial.",
        kicker="IPTV apps", h1='<span class="grad-text">MyIPTV Player</span> setup on Windows',
        lead="A free IPTV player from the Microsoft Store that turns a Windows PC or laptop into a TV with a guide. Here is how to load your channels.",
        crumb="MyIPTV Player", blurb="Free Windows player with a TV guide and VLC engine.",
        answer="<p><strong>MyIPTV Player</strong> is a free, ad-supported IPTV player for <strong>Windows</strong>, installed from the Microsoft Store. It reads an <strong>M3U playlist</strong> (a link or a file) and an <strong>EPG</strong> link for the TV guide, and it can switch to a built-in VLC engine for streams that won’t play. It contains no channels: add the M3U link IPTVMaple sends after your order or <a href=\"/try-iptv-canada/\">free trial</a>.</p>",
        body="""
<h2>What MyIPTV Player does well</h2>
<table>
<thead><tr><th>Feature</th><th>MyIPTV Player</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Price</td><td>Free, with ads in the sidebar</td><td>No purchase needed to test your service</td></tr>
<tr><td>Playlist</td><td>M3U from a link or a local file; several playlists</td><td>Paste the M3U link from our welcome message</td></tr>
<tr><td>TV guide</td><td>EPG support</td><td>See what is on now and next</td></tr>
<tr><td>Playback</td><td>Built-in player, with VLC as a fallback engine</td><td>Switch to VLC if a channel stays black</td></tr>
<tr><td>Favourites</td><td>Right-click a channel to add it</td><td>Keep your daily channels at the top</td></tr>
<tr><td>Recording</td><td>Record from live channels</td><td>Save a programme to watch later</td></tr>
<tr><td>Parental control</td><td>Hide adult channels, or lock the app with a PIN</td><td>Safe on a family computer</td></tr>
</tbody>
</table>
<p>What it doesn’t do: it doesn’t take an Xtream Codes login (server, username, password) directly, and it runs on Windows only. On a Mac, use <a href="/iptvx/">IPTVX</a> or IPTV Smarters; see <a href="/iptv-pc-mac/">IPTV on PC and Mac</a>.</p>

<h2>Step-by-step: MyIPTV Player with IPTVMaple</h2>
<ol>
<li>Open the <strong>Microsoft Store</strong> on your PC, search for <strong>MyIPTV Player</strong> and install it.</li>
<li>Open the app and go to <strong>Settings</strong>, then <strong>Add new playlist and EPG source</strong>.</li>
<li>Under <strong>Remote channel list</strong>, type a name (for example “IPTVMaple”), paste the <strong>M3U link</strong> from our message and choose <strong>Add remote list</strong>.</li>
<li>On the same screen, add the <strong>EPG link</strong> we sent you as the guide source.</li>
<li>Back in Settings, pick your new playlist under <strong>Select channel playlist</strong> and press <strong>Refresh</strong>. Channels appear in the Channels view, grouped by category.</li>
</ol>
<p>Menu names can shift a little between versions; the order is always the same: add the source, select it, refresh.</p>

<h2>Smooth playback on a PC</h2>
<ul>
<li><strong>Turn on the VLC engine</strong> in Settings if a channel shows a black screen or no sound. With VLC on, you can also raise the <strong>network caching</strong> value (in milliseconds) to absorb short drops.</li>
<li><strong>Use a cable or 5 GHz Wi-Fi.</strong> Laptops on the far side of the house are the usual cause of freezing; see our <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li><strong>Refresh after a renewal.</strong> If channels disappear, open Settings and press Refresh to reload the playlist.</li>
<li><strong>Plug the laptop into the TV</strong> with an HDMI cable to watch on the big screen.</li>
</ul>

<h2>MyIPTV Player, VLC or IPTV Smarters?</h2>
<table>
<thead><tr><th>You want…</th><th>Use</th></tr></thead>
<tbody>
<tr><td>A free Windows player with a guide and favourites</td><td>MyIPTV Player</td></tr>
<tr><td>To open the playlist in seconds, no guide needed</td><td><a href="/vlc-iptv/">VLC</a></td></tr>
<tr><td>Live TV, movies and series in separate sections, with an Xtream login</td><td><a href="/iptv-smarters-pro-pc-mac/">IPTV Smarters for PC</a></td></tr>
<tr><td>To watch in a browser without installing anything</td><td><a href="/watch-iptv-online/">Watch IPTV online</a></td></tr>
</tbody>
</table>
<p>IPTVMaple plans start at <strong>${LOW}</strong> for one month, or about <strong>${PER_MONTH:.2f} a month</strong> on a 12-month plan, and every plan works in MyIPTV Player. Test it on your own PC first with the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>
""".replace("${LOW}", f"${LOW}").replace("${PER_MONTH:.2f}", f"${PER_MONTH:.2f}"),
        faq=[
            ("Is MyIPTV Player free?", "<p>Yes. It is free in the Microsoft Store and shows ads in the sidebar. It includes no channels; you add your own M3U playlist.</p>"),
            ("Does MyIPTV Player work with IPTVMaple?", "<p>Yes. Paste the M3U link and EPG link from your IPTVMaple welcome message. The same link works in every M3U player.</p>"),
            ("Can I use an Xtream Codes login in MyIPTV Player?", "<p>Not directly: it reads M3U playlists. Use the M3U link we send with your Xtream details, or use IPTV Smarters for PC if you prefer to log in with server, username and password.</p>"),
            ("Is “My IPTV” the same as MyIPTV Player?", "<p>Usually, yes: people searching for “my IPTV” or “my IP TV” on Windows mean this player. A few providers use similar names, but the app in the Microsoft Store is MyIPTV Player.</p>"),
            ("Is MyIPTV Player available on Mac?", "<p>No, it is a Windows app. On a Mac, use IPTVX, IPTV Smarters or VLC.</p>"),
            ("Why is a channel black in MyIPTV Player?", "<p>Turn on the VLC engine in Settings and try again. If it still doesn’t play, check the channel in another player and tell us its name on WhatsApp.</p>"),
        ],
        related=["iptv-pc-mac", "vlc-iptv", "iptv-smarters-pro-pc-mac", "m3u-playlist", "watch-iptv-online"],
        keywords=["myiptv player", "myiptv", "my iptv", "my ip tv", "my iptv player", "myiptv player windows"],
    ),
    # ------------------------------------------------------------------ IPTV on 5G and mobile data
    dict(
        slug="iptv-5g-mobile-data", hub="guides", **D,
        title="IPTV on 5G Home Internet & Mobile Data | IPTVMaple",
        description="Can you watch IPTV on 5G home internet or your phone’s mobile data? Speed needed per screen, data used per hour in HD and 4K, and settings that save data.",
        kicker="Guides", h1='IPTV on <span class="grad-text">5G and mobile data</span>',
        lead="5G home internet and phone plans can carry IPTV well. The two things to check are signal stability and how much data your plan includes.",
        crumb="IPTV on 5G", blurb="5G home internet and phone data: speed and data use.",
        answer="<p><strong>Yes, IPTV works on 5G</strong>, both on 5G home internet and on a phone’s mobile data. Each screen needs about <strong>10 Mbps for HD</strong> and <strong>25 Mbps for 4K</strong>, which a good 5G signal provides. The real limit is data: an HD stream uses roughly <strong>1 to 3 GB per hour</strong>, so check that your plan is unlimited, or lower the quality on mobile data.</p>",
        body="""
<h2>5G home internet vs a phone plan</h2>
<table>
<thead><tr><th></th><th>5G home internet</th><th>Phone on mobile data (SIM)</th></tr></thead>
<tbody>
<tr><td>Typical use</td><td>Replaces cable or DSL for the whole home</td><td>Watching on the go, or a cottage without internet</td></tr>
<tr><td>Data</td><td>Often unlimited; check your plan</td><td>Usually capped, or slowed after a set amount</td></tr>
<tr><td>Devices</td><td>Fire TV, Android box, smart TV through the 5G router</td><td>The phone itself, or other devices through a hotspot</td></tr>
<tr><td>Main risk</td><td>Signal changes through the day and indoors</td><td>Running out of data mid-game</td></tr>
</tbody>
</table>

<h2>How much data does IPTV use on 5G?</h2>
<p>Data depends on picture quality, not on the network. These are the figures to plan with:</p>
<table>
<thead><tr><th>Quality</th><th>Speed per screen</th><th>Data per hour (approx.)</th><th>A 3-hour hockey game</th></tr></thead>
<tbody>
<tr><td>SD (phone screen)</td><td>3 to 5 Mbps</td><td>1 to 2 GB</td><td>3 to 6 GB</td></tr>
<tr><td>HD / Full HD</td><td>about 10 Mbps</td><td>1 to 3 GB</td><td>3 to 9 GB</td></tr>
<tr><td>4K</td><td>about 25 Mbps</td><td>7 to 10 GB</td><td>20 to 30 GB</td></tr>
</tbody>
</table>
<p>The speed column is the headroom we recommend per screen; the stream itself usually runs below it, which is where the data figures come from. The arithmetic is simple: a stream of 5 megabits per second uses 5 × 3,600 ÷ 8 = 2,250 MB, or about 2.25 GB, in an hour. A family watching four hours of HD a day uses roughly 120 to 360 GB a month, which is fine on an unlimited 5G home plan and far too much for most phone plans.</p>

<h2>Getting a stable picture on 5G home internet</h2>
<ol>
<li><strong>Place the 5G router by a window</strong> facing the nearest tower, and use its app’s signal meter to find the best spot. Indoor walls weaken 5G more than older 4G.</li>
<li><strong>Connect the TV device by Ethernet</strong> to the 5G router, or use its 5 GHz Wi-Fi.</li>
<li><strong>Raise the buffer</strong> in <a href="/tivimate/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters</a>, so a short dip in signal doesn’t freeze the picture.</li>
<li><strong>Prefer HD to 4K</strong> on a busy evening if your signal varies; HD needs well under half the bandwidth.</li>
</ol>
<p>If the signal drops for a few seconds every few minutes, the cause is the radio link, not the IPTV service: see <a href="/iptv-buffering-fix/">IPTV buffering fixes</a>. The same advice applies to satellite internet in our <a href="/iptv-starlink/">Starlink guide</a>.</p>

<h2>Saving data on your phone</h2>
<ul>
<li><strong>Pick the SD or HD version</strong> of a channel when several are listed, instead of the 4K one.</li>
<li><strong>Use Wi-Fi when you have it</strong> and keep mobile data for when you are out.</li>
<li><strong>Watch the data meter</strong> in your phone’s settings after the first game, to see what your viewing really costs.</li>
<li><strong>Use a hotspot carefully</strong>: a TV on a phone hotspot streams at TV quality and can use a month of phone data in an evening.</li>
</ul>
<p>Setup on the phone itself is covered in <a href="/iptv-iphone/">IPTV on iPhone</a> and our <a href="/iptv-apps/">IPTV apps guide</a> for Android.</p>

<h2>Test it on your own connection</h2>
<p>Coverage varies street by street, so the only real test is your own signal. The <a href="/try-iptv-canada/">free 24-hour trial</a> needs no card: watch a live game on your 5G connection, check the data meter afterwards, and decide. Plans start at <strong>${LOW}</strong> for one month; see <a href="/iptv-plans-canada/">all plans</a>.</p>
""".replace("${LOW}", f"${LOW}"),
        faq=[
            ("Does IPTV work on 5G home internet?", "<p>Yes. A good 5G home connection gives far more than the 10 Mbps an HD stream needs. Place the router where the signal is strongest and connect the TV device by Ethernet or 5 GHz Wi-Fi.</p>"),
            ("Can I watch IPTV on my phone’s mobile data?", "<p>Yes, on 4G LTE or 5G. Watch your data: an HD stream uses about 1 to 3 GB per hour, so an unlimited plan or a lower quality setting is wise.</p>"),
            ("How much data does IPTV use per month?", "<p>It depends on hours and quality. Four hours of HD a day is roughly 120 to 360 GB a month; 4K uses about three times as much.</p>"),
            ("Why does IPTV freeze on 5G but not on cable?", "<p>The 5G signal changes with weather, time of day and how busy the tower is. Move the router to a window, use a cable to the TV device and raise the player’s buffer size.</p>"),
            ("Is 5G better than 4G for IPTV?", "<p>5G usually has more capacity, which helps in the evening when towers are busy. 4G LTE with a strong signal can also carry an HD stream comfortably.</p>"),
        ],
        related=["iptv-starlink", "iptv-buffering-fix", "iptv-iphone", "what-is-iptv", "4k-iptv"],
        keywords=["5g iptv", "5giptv", "iptv 5g", "iptv sim", "iptv mobile data", "iptv on mobile data", "iptv 5g home internet"],
    ),
]

# Existing pages that should link to the new ones (added to their "Related guides").
LINK_IN = {
    "iptv-pc-mac": ["myiptv-player"],
    "vlc-iptv": ["myiptv-player"],
    "iptv-smarters-pro-pc-mac": ["myiptv-player"],
    "iptv-starlink": ["iptv-5g-mobile-data"],
    "iptv-iphone": ["iptv-5g-mobile-data"],
    "iptv-buffering-fix": ["iptv-5g-mobile-data"],
}


def link_in(pages):
    by = {p["slug"]: p for p in pages}
    for src, targets in LINK_IN.items():
        rel = by[src].setdefault("related", [])
        rel.extend(t for t in targets if t not in rel)
