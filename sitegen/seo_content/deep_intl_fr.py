"""Depth pass, part 4: location hubs, the international hub and the French pages. See deep.py for how entries are applied."""
from ._util import price_table
from .geo import CA_CITY_SLUG, PROV, US_CITY_SLUG

DATA = {}

# ---- generated link lists (built from the geo data, so they cannot point at a missing page) ------------------------
_PROV_LINKS = "".join(f'<li><a href="/canada/{k}/">IPTV in {v[1]}</a></li>' for k, v in PROV.items())
_TOP_CA = ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Halifax", "Victoria", "Saskatoon"]
_CITY_LINKS = "".join(f'<li><a href="/{CA_CITY_SLUG[c]}/">IPTV in {c}</a></li>' for c in _TOP_CA if c in CA_CITY_SLUG)
_TOP_US = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "Dallas", "Seattle", "Boston", "Detroit"]
_US_LINKS = "".join(f'<li><a href="/{US_CITY_SLUG[c]}/">IPTV in {c}</a></li>' for c in _TOP_US if c in US_CITY_SLUG)

DATA["iptv-near-me"] = dict(
    add=f"""
<h2>IPTV by province</h2>
<ul>{_PROV_LINKS}</ul>

<h2>Popular Canadian cities</h2>
<ul>{_CITY_LINKS}</ul>
<p>More cities, including Mississauga, Surrey, Laval and Kelowna, are listed on each province page. Living in the USA? See <a href="/usa/">IPTV across the USA</a>: {_US_LINKS and "popular guides include " + ", ".join(f'<a href="/{US_CITY_SLUG[c]}/">{c}</a>' for c in _TOP_US[:5] if c in US_CITY_SLUG)}.</p>

<h2>What “near me” means for an internet service</h2>
<p>A cable company is local because its wires are. IPTV isn’t, because the video arrives over your home internet. What decides your experience is your connection, not your postal code:</p>
<table>
<thead><tr><th>Your internet</th><th>Works for IPTV?</th><th>Tip</th></tr></thead>
<tbody>
<tr><td>Fibre (Bell, Telus, Bell Aliant, Vidéotron and others)</td><td>Excellent</td><td>4K on several screens</td></tr>
<tr><td>Cable internet (Rogers, Cogeco, Eastlink, Shaw legacy)</td><td>Excellent</td><td>Use Ethernet at peak time</td></tr>
<tr><td>5G or LTE home internet</td><td>Good</td><td>Choose HD if 4K stutters; watch your data allowance</td></tr>
<tr><td>Satellite internet such as Starlink</td><td>Good in rural areas</td><td>Check latency and any data limits</td></tr>
<tr><td>DSL</td><td>Fine for HD</td><td>Keep to one or two screens</td></tr>
</tbody>
</table>
<p>Not sure your connection is fast enough? About 10 Mbps for HD and 25 Mbps per screen for 4K is the target. The <a href="/iptv-buffering-fix/">buffering fixes</a> help with weak links, and the <a href="/try-iptv-canada/">free 24-hour trial</a> lets you test it where you live.</p>
<p>Prefer French? <a href="/iptv-quebec/">IPTV Québec</a> and the <a href="/iptv-pas-cher/">prix en français</a>.</p>
""",
    faq=[
        ("How do I know if IPTV works at my address?",
         "<p>If you have a home internet connection of about 10 Mbps per screen for HD (25 Mbps for 4K), it works. Start the free 24-hour trial to test it on your own TV and internet.</p>"),
    ],
    related=["iptv-buffering-fix", "iptv-price"],
)

DATA["canada"] = dict(
    add="""
<h2>Six time zones, one TV guide</h2>
<p>Canada spans six time zones, which affects when games and shows air. Set your app’s time zone so the TV guide shows local times.</p>
<table>
<thead><tr><th>Zone</th><th>Where</th><th>Compared with Eastern</th></tr></thead>
<tbody>
<tr><td>Newfoundland</td><td>Newfoundland and Labrador (island)</td><td>1.5 hours ahead</td></tr>
<tr><td>Atlantic</td><td>Nova Scotia, New Brunswick, PEI</td><td>1 hour ahead</td></tr>
<tr><td>Eastern</td><td>Ontario, Québec</td><td>—</td></tr>
<tr><td>Central</td><td>Manitoba, Saskatchewan</td><td>1 hour behind</td></tr>
<tr><td>Mountain</td><td>Alberta, parts of BC and the territories</td><td>2 hours behind</td></tr>
<tr><td>Pacific</td><td>British Columbia</td><td>3 hours behind</td></tr>
</tbody>
</table>
<p>Looking for a general answer? See <a href="/iptv-near-me/">IPTV near me</a>, the <a href="/iptv-price/">price guide</a> or <a href="/iptv-quebec/">IPTV Québec</a> in French.</p>
""",
    related=["iptv-near-me", "iptv-price"],
)

DATA["usa"] = dict(
    add="""
<h2>US time zones and your TV guide</h2>
<table>
<thead><tr><th>Zone</th><th>Examples</th><th>Compared with Eastern</th></tr></thead>
<tbody>
<tr><td>Eastern</td><td>New York, Atlanta, Miami</td><td>—</td></tr>
<tr><td>Central</td><td>Chicago, Houston, Dallas</td><td>1 hour behind</td></tr>
<tr><td>Mountain</td><td>Denver, Phoenix, Salt Lake City</td><td>2 hours behind</td></tr>
<tr><td>Pacific</td><td>Los Angeles, Seattle, San Francisco</td><td>3 hours behind</td></tr>
<tr><td>Alaska and Hawaii</td><td>Anchorage, Honolulu</td><td>4 hours behind (Alaska); 5 or 6 hours (Hawaii)</td></tr>
</tbody>
</table>
<p>IPTVMaple works over any home internet connection in all 50 states. See <a href="/iptv-sports/">IPTV for sports</a>, <a href="/espn-iptv/">ESPN and US sports networks</a> and <a href="/iptv-price/">prices</a>.</p>
""",
    related=["espn-iptv", "iptv-sports"],
)

_TZ_ROWS = [("United Kingdom", "UK", "5 hours", "8 hours"), ("Portugal", "PT", "5 hours", "8 hours"), ("France", "FR", "6 hours", "9 hours"),
            ("Italy", "IT", "6 hours", "9 hours"), ("Poland", "PL", "6 hours", "9 hours"), ("Serbia, Croatia, Bosnia", "EX-YU", "6 hours", "9 hours"),
            ("Greece", "GR", "7 hours", "10 hours"), ("Romania", "RO", "7 hours", "10 hours"), ("Ukraine", "UA", "7 hours", "10 hours")]

DATA["iptv-international"] = dict(
    add="".join(["""
<h2>Choose your community</h2>
<ul>
<li><a href="/uk-iptv/">UK IPTV</a>: BBC, ITV, Sky Sports and more</li>
<li><a href="/french-iptv/">French IPTV</a>: TF1, France 2, M6, beIN</li>
<li><a href="/italian-iptv/">Italian IPTV</a>: RAI, Mediaset, Sky Sport</li>
<li><a href="/portuguese-iptv/">Portuguese IPTV</a>: RTP, SIC, TVI</li>
<li><a href="/polish-iptv/">Polish IPTV</a>: TVP, Polsat, TVN</li>
<li><a href="/greek-iptv/">Greek IPTV</a>: ERT, Mega, ANT1</li>
<li><a href="/romanian-iptv/">Romanian IPTV</a>: Canale Românești</li>
<li><a href="/ex-yu-iptv/">IP televizija</a>: Serbia, Croatia, Bosnia</li>
<li><a href="/ukrainian-iptv/">Ukrainian IPTV</a>: 1+1, ICTV, STB</li>
</ul>

<h2>Time difference between Canada and Europe</h2>
<table>
<thead><tr><th>Country</th><th>Hours ahead of Eastern</th><th>Hours ahead of Pacific</th></tr></thead>
<tbody>""",
                     "".join(f"<tr><td>{n}</td><td>{e}</td><td>{p}</td></tr>" for n, c, e, p in _TZ_ROWS),
                     """</tbody>
</table>
<p>For a few weeks each year, when Europe and North America change clocks on different dates, the difference shifts by an hour. Use catch-up on supported channels or recording in your app to watch evening programs from home at a convenient time. See <a href="/tivimate-premium/">TiviMate Premium</a> for what recording needs.</p>

<h2>Everything in one plan</h2>
<p>Your community’s channels, Canadian networks, sports and the on-demand library come in a single plan. Compare <a href="/iptv-price/">prices per screen</a>, or <a href="/try-iptv-canada/">test it free for 24 hours</a>.</p>
"""]),
    faq=[
        ("How do I find my country’s channels in the app?",
         "<p>Channels are grouped by country in your IPTV app. Search the group name, such as Italy or Poland, or use the search box on our channels list to see what is included.</p>"),
    ],
    related=["iptv-price", "iptv-near-me"],
)

# ===================================================================================================== FRENCH PAGES
DATA["meilleur-iptv"] = dict(
    add="""
<h2>Les trois types de fournisseurs de télé par Internet</h2>
<table>
<thead><tr><th></th><th>Télé d’un fournisseur de télécommunications</th><th>Services de diffusion autorisés</th><th>IPTV indépendant</th></tr></thead>
<tbody>
<tr><td>Exemples</td><td>Bell Fibe, Telus Optik</td><td>Crave, ICI TOU.TV, Club illico</td><td>IPTVMaple et services semblables</td></tr>
<tr><td>Contrat</td><td>Souvent</td><td>Non</td><td>Généralement aucun</td></tr>
<tr><td>Prix</td><td>Plus élevé</td><td>Par application</td><td>Un forfait pour tout</td></tr>
<tr><td>Idéal pour</td><td>Une facture unique</td><td>Les émissions d’un diffuseur</td><td>Télé en direct, sport et films au même endroit</td></tr>
</tbody>
</table>
<p>Nous vendons un service IPTV indépendant, donc nous ne sommes pas neutres. Utilisez les mêmes critères pour nous juger que pour tout autre service. Pour la loi, lisez <a href="/iptv-legal-canada/">l’IPTV est-il légal au Canada?</a>.</p>

<h2>Aller plus loin</h2>
<ul>
<li><a href="/iptv-pas-cher/">IPTV pas cher : les prix</a></li>
<li><a href="/lecteur-iptv/">Le meilleur lecteur IPTV</a></li>
<li><a href="/iptv-ne-fonctionne-plus/">IPTV qui ne fonctionne plus : 10 solutions</a></li>
<li>En anglais : <a href="/iptv-providers/">comparer les fournisseurs IPTV</a> et <a href="/iptv-reddit/">lire les conseils de Reddit</a> avec prudence</li>
</ul>
""",
    related=["iptv-legal-canada", "iptv-pas-cher", "lecteur-iptv"],
)

DATA["abonnement-iptv"] = dict(
    add=f"""
<h2>Tous les forfaits IPTV en un coup d’œil</h2>
{price_table(lang="fr")}
<p>Les prix sont en dollars américains et comprennent le rabais de lancement de 50 %. Chaque prix mène à la page de commande.</p>

<h2>Quel forfait choisir?</h2>
<table>
<thead><tr><th>Votre situation</th><th>Notre suggestion</th></tr></thead>
<tbody>
<tr><td>Vous voulez essayer d’abord</td><td>L’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>, puis 1 mois</td></tr>
<tr><td>Une personne, un téléviseur</td><td>1 écran, 12 mois</td></tr>
<tr><td>Un couple avec deux téléviseurs</td><td>2 écrans, 12 mois</td></tr>
<tr><td>Une famille</td><td>3 à 5 écrans, 12 mois</td></tr>
</tbody>
</table>
<p>Comptez les écrans allumés <em>en même temps</em>, pas tous vos appareils. Voyez aussi <a href="/iptv-pas-cher/">IPTV pas cher</a>, <a href="/iptv-legal-canada/">la légalité de l’IPTV</a> et <a href="/lecteur-iptv/">le meilleur lecteur IPTV</a>.</p>
""",
    faq=[
        ("Quel forfait IPTV choisir pour une famille?",
         "<p>Comptez les écrans qui regardent en même temps. Pour trois ou quatre téléviseurs et téléphones, un forfait de 3 à 5 écrans sur 12 mois offre le meilleur prix par mois.</p>"),
    ],
    related=["iptv-pas-cher", "iptv-legal-canada", "lecteur-iptv"],
)

DATA["iptv-sur-smart-tv"] = dict(
    add="""
<h2>Guides détaillés, appareil par appareil</h2>
<ul>
<li><a href="/iptv-sur-samsung/">IPTV sur Samsung et LG</a></li>
<li><a href="/iptv-sur-apple-tv-iphone/">IPTV sur Apple TV, iPhone et iPad</a></li>
<li><a href="/iptv-sur-pc-mac/">IPTV sur PC et Mac</a></li>
<li><a href="/iptv-sur-firestick/">IPTV sur Fire TV Stick</a></li>
<li><a href="/iptv-smarters-pro-francais/">IPTV Smarters Pro en français</a></li>
<li><a href="/lecteur-iptv/">Le meilleur lecteur IPTV</a></li>
<li><a href="/iptv-ne-fonctionne-plus/">IPTV qui ne fonctionne plus : 10 solutions</a></li>
</ul>

<h2>Et la PS5, la Xbox ou la Chromecast?</h2>
<p>Les consoles de jeu ne sont pas des appareils IPTV fiables : les applications IPTV n’y sont pas offertes officiellement. Utilisez plutôt un Fire TV Stick ou un appareil Google TV branché au téléviseur. Une Chromecast avec Google TV exécute TiviMate; une ancienne Chromecast sert seulement à diffuser depuis un téléphone. Pour comprendre les écarts, voyez <a href="/iptv-chromecast/">IPTV on Chromecast</a> (en anglais).</p>
""",
    related=["iptv-sur-samsung", "iptv-sur-apple-tv-iphone", "iptv-sur-pc-mac", "iptv-smarters-pro-francais"],
)

DATA["iptv-sur-firestick"] = dict(
    add="""
<h2>Quel Fire TV Stick choisir?</h2>
<table>
<thead><tr><th>Modèle</th><th>Idéal pour</th><th>Remarque</th></tr></thead>
<tbody>
<tr><td>Fire TV Stick 4K Max</td><td>Sport en 4K, longues listes de chaînes</td><td>Le meilleur choix pour l’IPTV</td></tr>
<tr><td>Fire TV Stick 4K</td><td>4K à petit prix</td><td>Bon choix polyvalent</td></tr>
<tr><td>Fire TV Stick (HD) ou Lite</td><td>HD sur un deuxième téléviseur</td><td>Masquez les groupes de chaînes inutiles</td></tr>
<tr><td>Fire TV Cube</td><td>Le plus rapide</td><td>Port Ethernet intégré</td></tr>
</tbody>
</table>
<p>Certains modèles récents d’Amazon utilisent un autre système (Vega OS) qui n’installe pas d’applications Android comme TiviMate : vérifiez la fiche du produit avant d’acheter.</p>

<h2>Dépannage sur Fire TV Stick</h2>
<table>
<thead><tr><th>Problème</th><th>Solution</th></tr></thead>
<tbody>
<tr><td>« Options pour les développeurs » introuvable</td><td>Paramètres → Mon Fire TV → À propos, puis sélectionnez 7 fois le nom de l’appareil</td></tr>
<tr><td>L’application ne s’installe pas</td><td>Libérez de l’espace de stockage et réessayez</td></tr>
<tr><td>Ça saccade</td><td>Adaptateur Ethernet ou Wi-Fi 5 GHz. Voyez <a href="/iptv-ne-fonctionne-plus/">10 solutions</a></td></tr>
</tbody>
</table>
<p>Guides en anglais, étape par étape : <a href="/tivimate-firestick/">TiviMate sur Firestick</a> et <a href="/iptv-smarters-pro-firestick/">IPTV Smarters sur Firestick</a>.</p>
""",
    related=["iptv-ne-fonctionne-plus", "lecteur-iptv"],
)

DATA["tivimate-en-francais"] = dict(
    add="""
<h2>TiviMate fonctionne sur quels appareils?</h2>
<table>
<thead><tr><th>Appareil</th><th>TiviMate?</th><th>Alternative</th></tr></thead>
<tbody>
<tr><td>Fire TV Stick, Android TV, Google TV, Nvidia Shield</td><td>Oui</td><td>—</td></tr>
<tr><td>Samsung et LG</td><td>Non</td><td><a href="/iptv-sur-samsung/">Applications du téléviseur</a> ou un Fire TV Stick</td></tr>
<tr><td>Apple TV, iPhone, iPad</td><td>Non</td><td><a href="/iptv-sur-apple-tv-iphone/">Smarters Player Lite, iPlayTV</a></td></tr>
<tr><td>PC et Mac</td><td>Non</td><td><a href="/iptv-sur-pc-mac/">IPTV Smarters Pro, VLC</a></td></tr>
</tbody>
</table>
<p>TiviMate Premium est facultatif et vendu par le développeur. IPTVMaple ne vend ni comptes ni licences. Détails en anglais : <a href="/tivimate-premium/">TiviMate Premium</a>, <a href="/tivimate-firestick/">installation sur Firestick</a> et <a href="/tivimate-devices/">appareils compatibles</a>. Voyez aussi <a href="/lecteur-iptv/">le meilleur lecteur IPTV</a>.</p>
""",
    related=["lecteur-iptv", "iptv-sur-samsung"],
)

DATA["iptv-quebec"] = dict(
    add="""
<h2>Guides IPTV en français</h2>
<ul>
<li><a href="/abonnement-iptv/">Abonnement IPTV : forfaits et prix</a> et <a href="/iptv-pas-cher/">IPTV pas cher</a></li>
<li><a href="/meilleur-iptv/">Le meilleur IPTV au Québec</a></li>
<li><a href="/iptv-legal-canada/">L’IPTV est-il légal au Canada?</a></li>
<li><a href="/lecteur-iptv/">Le meilleur lecteur IPTV</a> et <a href="/liste-iptv-m3u/">liste IPTV M3U</a></li>
<li>Installation : <a href="/iptv-sur-firestick/">Fire TV Stick</a>, <a href="/iptv-sur-samsung/">Samsung et LG</a>, <a href="/iptv-sur-apple-tv-iphone/">Apple TV et iPhone</a>, <a href="/iptv-sur-pc-mac/">PC et Mac</a></li>
<li>Dépannage : <a href="/iptv-ne-fonctionne-plus/">IPTV qui ne fonctionne plus</a></li>
</ul>
""",
    related=["iptv-legal-canada", "iptv-pas-cher", "lecteur-iptv", "iptv-ne-fonctionne-plus"],
)


# ---- every community page links to the other communities (natural "also available" navigation) -------------------------
_COMM = [("uk-iptv", "UK"), ("french-iptv", "French"), ("italian-iptv", "Italian"), ("portuguese-iptv", "Portuguese"), ("polish-iptv", "Polish"),
         ("greek-iptv", "Greek"), ("romanian-iptv", "Romanian"), ("ex-yu-iptv", "Ex-YU (IP televizija)"), ("ukrainian-iptv", "Ukrainian")]
for _slug, _name in _COMM:
    _others = ", ".join(f'<a href="/{s}/">{n}</a>' for s, n in _COMM if s != _slug)
    DATA[_slug] = dict(add=f"""
<h2>Other communities</h2>
<p>IPTVMaple carries channels for many communities in one plan. Also see: {_others}. Browse them all on the <a href="/iptv-international/">international IPTV</a> page, and compare <a href="/iptv-price/">prices per screen</a>.</p>
""")

DATA["jellyfin-iptv"] = dict(related=["stremio-iptv", "plex-iptv"])
