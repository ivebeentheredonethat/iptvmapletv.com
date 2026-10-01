"""Gap pass, part 4: question-style FAQ entries that answer high-volume phrasings directly."""

DATA = {}

def _q(slug, *items):
    DATA[slug] = dict(faq=[(q, f"<p>{a}</p>") for q, a in items])

_q("best-iptv-canada",
   ("What is the best IPTV 2026?", "There is no single winner for everyone. The best IPTV 2026 is one that is stable on game nights, carries your channels, offers a no-card trial and a refund policy, and answers support quickly. Test that with our <a href=\"/try-iptv-canada/\">free trial</a>."),
   ("Which are the best IPTV services?", "Compare the best IPTV services using the checklist in this guide: stability, channels, trial, pricing and support. See also <a href=\"/iptv-providers/\">how to compare providers</a>."),
   ("Is great IPTV the same as expensive IPTV?", "No. Great IPTV is reliable and honest about what it offers; price alone says little. A longer plan can make IPTV best value: see <a href=\"/iptv-price/\">prices</a>."))
_q("iptv-providers",
   ("What is the best IPTV service provider?", "The best IPTV service provider is the one that passes a real trial, publishes prices and has support that answers. Use our scorecard above."),
   ("Is a provider IPTV the same as a reseller?", "Not always. A provider IPTV business can run its own servers or resell another’s. Read <a href=\"/iptv-resellers/\">IPTV resellers explained</a> to tell the difference."))
_q("what-is-iptv",
   ("What does IPTV TV mean?", "IPTV TV is television delivered over the internet instead of cable or satellite. It covers live channels and on-demand video."),
   ("What is live IPTV and what is IPTV stream?", "Live IPTV means channels broadcast in real time. An IPTV stream is the video data your app receives for a channel or movie."))
_q("iptv-box",
   ("What is the best Android IPTV box?", "An Nvidia Shield or a current Google TV box for power, the Onn 4K box for budget. Any IPTV box Android model should have 4K, HEVC support and Ethernet."),
   ("Is an IPTV android TV box better than a Firestick?", "They do the same job. Android TV boxes offer more storage and ports; a Firestick is cheaper and simpler. See <a href=\"/iptv-firestick/\">Firestick IPTV</a>."),
   ("What is an IPTV box 4K?", "A box that can decode 4K video (HEVC) at 60 fps with an HDMI 2.0 output. See <a href=\"/4k-iptv/\">4K IPTV</a>."),
   ("Is the Onn TV box good for IPTV?", "Yes. The Onn 4K box from Walmart runs Google TV, so you can install TiviMate or Smarters on it."))
_q("iptv-firestick",
   ("What is the best IPTV for Firestick?", "The best IPTV for Firestick is a service with an app you can install quickly and a trial. Pair it with TiviMate: see <a href=\"/tivimate-firestick/\">TiviMate on Firestick</a>."),
   ("How do I get Fire TV IPTV working?", "Install Downloader, install a player app, log in with Xtream Codes details and open a channel. Steps are in the <a href=\"/iptv-smarters-pro-firestick/\">Smarters Firestick guide</a>."))
_q("iptv-roku", ("Does IPTV Roku TV work?", "Not with a dedicated app. Roku TV doesn’t offer the common IPTV players, so use screen mirroring or add a Fire TV Stick."))
_q("iptv-smarters-pro-download",
   ("Where is the IPTV Smarters downloader?", "Use the Downloader app on Firestick or Android TV to install the APK, or install from your phone’s store. See the table above."),
   ("How do I get IPTV Smarters Pro Android?", "Search the Play Store, or install the APK with Downloader. Then log in with Xtream Codes."),
   ("Is smarters IPTV pro the same as IPTV Smarters Pro?", "Yes, the word order varies (smarters pro IPTV, smarters IPTV pro) but it is the same app."))
_q("iptv-smarters-pro-firestick", ("Is IPTV Smarters Pro Firestick free?", "The app is free. You need a subscription for channels: start the <a href=\"/try-iptv-canada/\">free trial</a>."))
_q("iptv-smarters-pro-pc-mac",
   ("What is the best IPTV player PC?", "For Windows and Mac, the Smarters Pro desktop app has a TV guide; VLC is simplest. See the options above."),
   ("Does IPTV Smarters Pro PC exist?", "Yes, there is a desktop version of IPTV Smarters Pro for Windows and Mac."))
_q("iptv-smarters-pro", ("What is IPTV Smarters Lite and IPTV Smarters Player?", "IPTV Smarters Lite and IPTV Smarters Player are names for the lighter TV version of the app, <a href=\"/smarters-player-lite/\">Smarters Player Lite</a>."),
   ("What is IP TV Smart Pro?", "A misspelling or alternate spelling of IPTV Smarters Pro."))
_q("formuler-iptv", ("What is the Formuler Z8 Pro?", "A 4K Android IPTV box from Formuler with more memory than the standard Z8. It runs the MyTVOnline portal app and can install TiviMate."))
_q("mag-box-iptv", ("What is a MAG IPTV box and what are MAG IPTV boxes?", "MAG boxes are Infomir set-top boxes that run IPTV portals. See the model table above."),
   ("What is a TV box MAG?", "Another name for the same Infomir MAG set-top box."))
_q("iptv-reddit", ("What is the best IPTV service reddit users recommend?", "It changes constantly and posts are often promotional. Use Reddit for setup help and test the provider yourself with a free trial."))
_q("iptv-apps", ("What is the best IP TV stream player?", "For Android TV choose TiviMate; for phones, Smarters Pro. See the table above."))
_q("tivimate-firestick", ("Does TiviMate for Firestick work on all sticks?", "Yes, on Fire TV Stick Lite, standard, 4K and Cube. Newer sticks run it faster."),
   ("How do I install TiviMate Firestick?", "Use Downloader, install the app, add your Xtream login, then pick a channel."))
_q("tivimate-premium", ("Do I need a TiviMate premium subscription?", "No, it’s optional. A TiviMate premium subscription adds recording, multi-view and extra playlists."))
_q("vlc-iptv", ("How do I use IP TV VLC?", "Open Media, Open Network Stream, and paste your M3U link."))
_q("watch-iptv-online",
   ("Can I watch IP TV online without an app?", "Only partly: there is no official web version of the common apps. Install a desktop player or use VLC."),
   ("What is the best online IP TV player?", "A trusted desktop app. Avoid pasting your login into unknown websites."))
_q("liste-iptv-m3u",
   ("C’est quoi une IP TV list ou liste M3U IPTV ?", "C’est un fichier ou lien de liste de lecture que votre application lit pour afficher les chaînes."),
   ("What is an IPTV list or M3U IPTV list?", "A playlist file or link your player app reads to find channels. See <a href=\"/m3u-playlist/\">What is M3U?</a>."))
_q("meilleur-iptv", ("Quel est le meilleur IP TV ?", "Celui qui passe un vrai essai gratuit : stabilité, chaînes, prix clairs, service client."))
_q("iptv-apple-tv", ("How do I watch IPTV on Apple TV?", "Install IPTV Smarters Pro or iPlayTV from the App Store and sign in with your subscription login."))
_q("iptv-near-me", ("What is the best IPTV near me?", "Because IPTV works over the internet, the best option near you is the one with a free trial that works on your connection."))
_q("iptv-international", ("What is IPTV worldwide?", "A subscription that includes channels from many countries and languages, available wherever you have broadband."))
