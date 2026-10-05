"""Official sources: a short closing section on long app, device and how-to guides that link out to the developer,
manufacturer or reference page a reader needs (download from the official source, check a spec, read the definition).

Only official or reference sites, each checked on 2026-10-05. Commercial pages (home, plans, prices, trial, channel
list, city pages) deliberately get none. Links open in a new tab with rel="noopener". The page's "Updated" date is
not changed: these are reference links, not new content.
"""


def _a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


TIVIMATE = _a("https://tivimate.com/", "TiviMate’s official website")
SMARTERS = _a("https://www.iptvsmarters.com/", "the official IPTV Smarters website")
DOWNLOADER = _a("https://www.aftvnews.com/downloader/", "the Downloader app page by AFTVnews")
FORMULER = _a("https://www.formuler.tv/", "Formuler’s official site")
INFOMIR = _a("https://www.infomir.eu/", "Infomir, the maker of MAG boxes")
SSIPTV = _a("https://ss-iptv.com/en/", "the official SS IPTV website")
ANDROID_TV = _a("https://www.android.com/tv/", "Google’s Android TV page")
SAMSUNG = _a("https://www.samsung.com/ca/support/", "Samsung Canada support")
LG = _a("https://www.lg.com/ca_en/support/", "LG Canada support")
VLC = _a("https://www.videolan.org/vlc/", "VLC from VideoLAN")
WIKI_IPTV = _a("https://en.wikipedia.org/wiki/Internet_Protocol_television", "Wikipedia’s overview of IPTV")
WIKI_M3U = _a("https://en.wikipedia.org/wiki/M3U", "the M3U format on Wikipedia")
WIKI_M3U_FR = _a("https://fr.wikipedia.org/wiki/M3U", "le format M3U sur Wikipédia")
CRTC = _a("https://crtc.gc.ca/eng/home-accueil.htm", "the CRTC")
SPEEDTEST = _a("https://www.speedtest.net/", "Speedtest")
REDDIT = _a("https://www.reddit.com/r/IPTV/", "r/IPTV")


def _en(text):
    return f'<h2>Official sources</h2>\n<p>{text}</p>'


def _fr(text):
    return f'<h2>Sources officielles</h2>\n<p>{text}</p>'


SOURCES = {
    # apps
    "tivimate": _en(f"Install TiviMate from Google Play or the Amazon Appstore and check features and Premium pricing on {TIVIMATE}. Avoid modified APKs from other sites: they can crash, lose your settings or carry malware."),
    "tivimate-premium": _en(f"Premium is bought from the developer through the TiviMate Companion app. Current pricing and what Premium unlocks are listed on {TIVIMATE}."),
    "tivimate-firestick": _en(f"Downloader is published by AFTVnews; see {DOWNLOADER} for the official code and instructions. TiviMate itself is documented on {TIVIMATE}."),
    "tivimate-devices": _en(f"Supported devices and system requirements are listed on {TIVIMATE}. For Android TV and Google TV hardware in general, see {ANDROID_TV}."),
    "iptv-smarters-pro": _en(f"Download IPTV Smarters Pro only from your device’s app store or from {SMARTERS}. Copies of the app on file-sharing sites are often outdated or modified."),
    "iptv-smarters-pro-download": _en(f"The safe download sources are the Google Play Store, the Apple App Store and {SMARTERS}. On Fire TV, the Downloader app is documented on {DOWNLOADER}."),
    "iptv-smarters-pro-firestick": _en(f"For the Downloader app and its codes, see {DOWNLOADER}. App versions and release notes are on {SMARTERS}."),
    "iptv-smarters-pro-pc-mac": _en(f"Desktop versions of the app are listed on {SMARTERS}. If you prefer a lightweight player for an M3U link, {VLC} is free on Windows and macOS."),
    "iptv-smarters-pro-samsung-lg": _en(f"App availability depends on your TV model and region. Check {SMARTERS} for supported platforms, and {SAMSUNG} or {LG} to update your TV’s firmware before installing."),
    "iptv-smarters-pro-francais": _fr(f"Téléchargez IPTV Smarters Pro uniquement depuis la boutique d’applications de votre appareil ou depuis {SMARTERS.replace('the official IPTV Smarters website', 'le site officiel d’IPTV Smarters')}."),
    "ss-iptv": _en(f"Playlist upload, the connection code and supported TV models are documented on {SSIPTV}."),
    "stbemu": _en(f"StbEmu emulates the portal interface of MAG set-top boxes. The original hardware and its portal system are described by {INFOMIR}."),
    "iptv-apps": _en(f"Get apps from your device’s official store or the developer’s own site: {TIVIMATE}, {SMARTERS} and {VLC}. Unofficial APK mirrors are a common source of malware on streaming devices."),
    "lecteur-iptv": _fr(f"Installez vos lecteurs depuis la boutique officielle de l’appareil ou le site de l’éditeur : {TIVIMATE.replace('TiviMate’s official website', 'le site de TiviMate')}, {SMARTERS.replace('the official IPTV Smarters website', 'IPTV Smarters')} et {VLC.replace('VLC from VideoLAN', 'VLC (VideoLAN)')}."),
    "watch-iptv-online": _en(f"To open an M3U link on a computer without installing an IPTV app, {VLC} plays most playlists. The playlist format itself is explained in {WIKI_M3U}."),
    "gse-smart-iptv": _en(f"GSE Smart IPTV reads standard M3U and M3U8 playlists; the format is explained in {WIKI_M3U}."),
    "myiptv-player": _en(f"MyIPTV Player loads standard M3U playlists and XMLTV guides; the playlist format is explained in {WIKI_M3U}. For a quick test of the same link, {VLC} works on Windows too."),
    "liste-iptv-m3u": _fr(f"Pour comprendre la structure d’un fichier (#EXTM3U, #EXTINF), voyez {WIKI_M3U_FR}. Pour tester un lien sur ordinateur, {VLC.replace('VLC from VideoLAN', 'VLC (VideoLAN)')} lit la plupart des listes."),
    # devices
    "formuler-iptv": _en(f"Model specifications and support for each box are published on {FORMULER}."),
    "mag-box-iptv": _en(f"Model specifications, firmware updates and portal setup for MAG boxes are published by {INFOMIR}."),
    "iptv-box": _en(f"Check specs on the makers’ own sites before you buy: {FORMULER}, {INFOMIR} and {ANDROID_TV} for certified Android TV and Google TV boxes."),
    "iptv-firestick": _en(f"The Downloader app used in these steps is published by AFTVnews; see {DOWNLOADER} for its official code."),
    "iptv-samsung-tv": _en(f"Before installing an IPTV app, update your TV’s software. Model-specific manuals and firmware are on {SAMSUNG}."),
    "iptv-smart-tv": _en(f"Firmware updates and manuals are on {SAMSUNG} and {LG}; for Sony, TCL and other TVs running Google TV or Android TV, see {ANDROID_TV}."),
    # how-to and reference
    "4k-iptv": _en(f"Before you pick a 4K plan, run {SPEEDTEST} on the device you will watch on (not your phone) to check you have about 25 Mbps per 4K screen."),
    "iptv-5g-mobile-data": _en(f"Run {SPEEDTEST} at the time of day you usually watch: 5G home internet speeds change with network load. Wireless service rules in Canada are set by {CRTC}."),
    "iptv-ne-fonctionne-plus": _fr(f"Mesurez votre débit avec {SPEEDTEST} sur l’appareil qui lit l’IPTV, idéalement à l’heure où le problème se produit."),
    "iptv-server": _en(f"For background on how IPTV delivery works, multicast and unicast included, see {WIKI_IPTV}. The playlist format servers hand out is described in {WIKI_M3U}."),
    "iptv-quebec": _en(f"Broadcasting in Quebec and the rest of Canada is regulated by {CRTC}, which publishes the rules for TV distributors."),
    "iptv-providers": _en(f"Canadian TV distribution is regulated by {CRTC}. For how IPTV works as a technology, see {WIKI_IPTV}."),
    "iptv-reddit": _en(f"The main community is {REDDIT}. Read its rules before posting: many IPTV communities restrict naming or asking for providers."),
}


def apply(pages):
    by = {p["slug"]: p for p in pages}
    missing = [s for s in SOURCES if s not in by]
    assert not missing, f"outbound.py refers to pages that do not exist: {missing}"
    for slug, html in SOURCES.items():
        by[slug]["body"] = by[slug]["body"].rstrip() + "\n" + html
    return pages
