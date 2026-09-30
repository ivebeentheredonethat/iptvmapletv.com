"""Canadian cities cluster ("iptv near me"). Hub: /iptv-near-me/

Each city page has its own local context (ISPs, teams, neighbouring cities, local channels from our lineup)
so none of them are duplicates of each other.
"""


def city(slug, name, province, tz, isps, teams, nearby, local_channels, intro, extra, faq_extra, related, keywords, fr_note=""):
    teams_li = "".join(f"<li>{t}</li>" for t in teams)
    nearby_links = ", ".join(nearby)
    return dict(
        slug=slug, hub="cities",
        title=f"IPTV {name}: 4K Live TV & Sports Without Cable | IPTVMaple",
        description=f"IPTV in {name}, {province}: 50,000+ channels including {local_channels.split(',')[0].split(' and ')[0]}, local sports and 4K movies — no cable contract. Try IPTVMaple free for 24h.",
        kicker="Cities", h1=f'IPTV in <span class="grad-text">{name}</span>',
        lead=f"Live TV, local news and every {teams[0].split(' (')[0]} game in 4K — delivered over the internet you already have in {name}.",
        crumb=name, blurb=f"Local channels, {teams[0].split(' (')[0]} and 4K in {name}.",
        answer=f"<p><strong>IPTV in {name}</strong> works over any home internet connection — {isps} or a smaller provider. IPTVMaple gives {name} households 50,000+ live channels, including local stations like {local_channels}, all the sports networks and 300,000+ movies and series, from $9/month with a free 24-hour trial.</p>",
        body=f"""
<h2>Why {name} is switching to IPTV</h2>
{intro}

<h2>Local channels and sports in {name}</h2>
<p>Your IPTVMaple lineup includes local {name} stations — {local_channels} — plus national networks, TSN and Sportsnet. Follow your teams:</p>
<ul>{teams_li}</ul>
<p>More on hockey in our <a href="/nhl-iptv/">NHL IPTV guide</a> and on every league in <a href="/iptv-sports/">sports IPTV</a>.</p>

<h2>Does IPTV work with my {name} internet provider?</h2>
<p>Yes. IPTV streams over the internet, so it works with {isps} and any other ISP in {province}. You don’t need to change provider or rent a TV box. For 4K, 25 Mbps per screen is plenty — most {name} internet plans offer far more.</p>
{extra}

<h2>Get IPTV in {name} in 4 steps</h2>
<ol>
<li><strong>Choose a plan</strong> on the <a href="/iptv-plans-canada/">IPTV subscription page</a> — or start with the <a href="/try-iptv-canada/">free 24-hour trial</a>.</li>
<li><strong>Get your login</strong> on WhatsApp and by email, usually within minutes, any time of day ({tz}).</li>
<li><strong>Install an app</strong> — <a href="/tivimate/">TiviMate</a> on a <a href="/iptv-firestick/">Firestick</a>, or an app on your <a href="/iptv-samsung-tv/">smart TV</a>.</li>
<li><strong>Watch</strong> live TV, sports, movies and series on every screen in your home.</li>
</ol>
<p>We also serve {nearby_links} and <a href="/iptv-near-me/">every other city in Canada</a>.</p>
{fr_note}
""",
        faq=[
            (f"Is IPTV available in {name}?", f"<p>Yes. IPTVMaple works anywhere in {name} and across {province} — all you need is an internet connection.</p>"),
            (f"Do I need to change my internet provider in {name}?", f"<p>No. IPTV works with {isps} and every other ISP. Keep your internet plan and cancel only the cable TV part if you want.</p>"),
            (f"Can I watch local {name} channels?", f"<p>Yes, including {local_channels}, plus national Canadian networks.</p>"),
        ] + faq_extra,
        related=related,
        keywords=keywords,
    )


PAGES = [
    # ------------------------------------------------------------------ HUB
    dict(
        slug="iptv-near-me", hub="cities", hub_page=True,
        title="IPTV Near Me: IPTV Service in Every Canadian City | IPTVMaple",
        description="Looking for IPTV near you? IPTVMaple serves every city in Canada — Toronto, Montreal, Vancouver, Calgary, Edmonton, Ottawa and more. Try it free for 24 hours.",
        kicker="Cities", h1='IPTV <span class="grad-text">near me</span>: every city in Canada',
        lead="IPTV doesn’t need a local store or technician. If you have internet, you can be watching in minutes — wherever you are in Canada.",
        crumb="IPTV near me", blurb="IPTV service in every Canadian city.",
        answer="<p>You don’t need a local IPTV store: <strong>IPTV works anywhere in Canada with an internet connection</strong>. IPTVMaple sends your login online within minutes and supports you 24/7 on WhatsApp, whether you’re in Toronto, Montréal, Vancouver, Calgary, Edmonton, Ottawa, Winnipeg, Halifax or a small town. Local channels for major Canadian cities are included.</p>",
        body="""
<h2>How “IPTV near me” works</h2>
<p>Traditional cable depends on the wires in your street. IPTV (Internet Protocol Television) streams over your existing internet, so availability doesn’t depend on your address — only on your connection. There’s nothing to install besides an app, and no technician visit.</p>

<h2>What you get wherever you live</h2>
<ul>
<li>Local news from CBC, CTV, Global and Citytv stations across Canada</li>
<li>French-language channels: TVA, ICI Radio-Canada, Noovo, Télé-Québec</li>
<li>TSN, Sportsnet, RDS and TVA Sports for every Canadian team</li>
<li>300,000+ movies and series on demand</li>
<li>Same-day activation and 24/7 support on WhatsApp</li>
</ul>

<h2>City guides</h2>
<p>Pick your city below for local channels, teams and internet provider tips. Don’t see yours? IPTVMaple still works there — the service is the same everywhere in Canada.</p>
<p>En français : <a href="/iptv-quebec/">IPTV au Québec</a>.</p>
""",
        faq=[
            ("Is there an IPTV provider near me?", "<p>IPTV doesn’t require a local provider. IPTVMaple works anywhere in Canada over the internet, with activation in minutes.</p>"),
            ("Do I need a technician to install IPTV?", "<p>No. You install an app on your TV, stick or phone and enter your login. We guide you on WhatsApp if needed.</p>"),
            ("Can I get local channels with IPTV?", "<p>Yes, local CBC, CTV, Global, Citytv and French-language stations for major Canadian cities are included.</p>"),
            ("Does IPTV work in rural Canada?", "<p>Yes, as long as your connection offers about 10 Mbps for HD or 25 Mbps for 4K. Satellite internet like Starlink works too.</p>"),
        ],
        related=["best-iptv-canada", "iptv-quebec"],
        keywords=["iptv near me", "best iptv near me", "iptv 4k near me", "iptv service near me", "iptv box near me", "local iptv", "iptv areas", "iptv canada", "canada iptv", "iptv in canada", "iptv for canada", "iptv from canada", "iptv canadian", "canadian iptv", "starlink iptv"],
    ),
    city("iptv-toronto", "Toronto", "Ontario", "Eastern time",
         "Rogers, Bell, TekSavvy, Start.ca",
         ["Toronto Maple Leafs (NHL)", "Toronto Raptors (NBA)", "Toronto Blue Jays (MLB)", "Toronto FC (MLS)", "Toronto Argonauts (CFL)"],
         ['<a href="/iptv-hamilton/">Hamilton</a>', "Mississauga", "Brampton", "Markham", "Vaughan", "Oshawa"],
         "CTV Toronto, CBC Toronto, Global Toronto, Citytv Toronto, CP24 and OMNI",
         """<p>Toronto households pay some of the highest TV bills in Canada, often $80–$120 a month for cable before sports add-ons. IPTV replaces the cable box with an app, keeps the channels Torontonians actually watch — CP24, the Leafs, the Raptors, the Jays — and adds a huge on-demand library for a fraction of the price.</p>
<p>Condo living is another reason: no coax outlet in the right room is no problem when your TV only needs Wi-Fi.</p>""",
         """<h3>Watching in a Toronto condo</h3>
<p>Busy building Wi-Fi can cause buffering at peak times. Use 5 GHz Wi-Fi or an Ethernet adapter for your Firestick, and place the router in the same room as the TV if you can.</p>""",
         [("Can I watch Leafs, Raptors and Jays games?", "<p>Yes. TSN, Sportsnet (including Sportsnet Ontario) and CBC are included, along with NHL Center Ice and NBA League Pass.</p>")],
         ["iptv-hamilton", "iptv-ottawa", "nhl-iptv", "nba-iptv"],
         ["iptv toronto", "toronto iptv"]),
    city("iptv-montreal", "Montreal", "Québec", "Eastern time",
         "Vidéotron, Bell, Fizz, Oxio",
         ["Montréal Canadiens (NHL)", "CF Montréal (MLS)", "Montréal Alouettes (CFL)", "Laval Rocket (AHL)"],
         ["Laval", "Longueuil", "Brossard", "Terrebonne", '<a href="/iptv-quebec/">Québec City</a>', "Gatineau"],
         "CTV Montréal, CBC Montréal, Citytv Montréal, TVA Montréal and ICI Radio-Canada Télé Montréal",
         """<p>Montréal is Canada’s most bilingual TV market, and IPTV suits it perfectly: English and French channels in one lineup — TVA, ICI Radio-Canada, Noovo, RDS and TVA Sports alongside CTV, CBC, TSN and Sportsnet. No need to choose between two cable packages.</p>
<p>Habs fans can watch every game in French on TVA Sports or RDS, or in English on Sportsnet — switching with one button.</p>""",
         """<h3>Grand Prix and festival season</h3>
<p>Formula 1 fans can watch the Grand Prix du Canada on TSN, RDS or Sky Sports F1 — see our <a href="/f1-iptv/">F1 IPTV guide</a>.</p>""",
         [("Are French channels included for Montreal?", "<p>Yes: TVA, ICI Radio-Canada Télé, Noovo, Télé-Québec, RDS, TVA Sports, Super Écran and many more.</p>"),
          ("Can I watch the Canadiens in French?", "<p>Yes, on TVA Sports or RDS depending on the game, both included.</p>")],
         ["iptv-quebec", "nhl-iptv", "f1-iptv", "iptv-ottawa"],
         ["iptv montreal", "iptv montréal", "iptv montréal québec", "iptv rive nord"],
         fr_note='<p><strong>En français :</strong> consultez notre page <a href="/iptv-quebec/">IPTV Québec</a>.</p>'),
    city("iptv-vancouver", "Vancouver", "British Columbia", "Pacific time",
         "Telus, Rogers (formerly Shaw), Novus",
         ["Vancouver Canucks (NHL)", "Vancouver Whitecaps (MLS)", "BC Lions (CFL)"],
         ["Surrey", "Burnaby", "Richmond", "Coquitlam", "North Vancouver", '<a href="/iptv-calgary/">Calgary</a>'],
         "CTV Vancouver, CBC Vancouver, Global Vancouver, Citytv Vancouver and CTV 2 Vancouver",
         """<p>In Vancouver, many live events start early: Eastern hockey games at 4 p.m. and Premier League matches at dawn. IPTV with catch-up (on supported channels) and TiviMate recording lets you watch on your schedule — something cable boxes make expensive.</p>
<p>Vancouver is also one of Canada’s most international cities; with channels from the UK and across Europe, the whole household finds something to watch.</p>""",
         """<h3>Pacific time TV guide</h3>
<p>If the guide looks three hours off, set your app’s EPG time offset or your device’s time zone to Pacific time.</p>""",
         [("Can I watch Canucks games?", "<p>Yes, on Sportsnet Pacific and national broadcasts, plus NHL Center Ice.</p>")],
         ["iptv-calgary", "iptv-edmonton", "nhl-iptv", "soccer-iptv"],
         ["iptv vancouver", "vancouver iptv"]),
    city("iptv-calgary", "Calgary", "Alberta", "Mountain time",
         "Telus, Rogers (formerly Shaw), local fibre providers",
         ["Calgary Flames (NHL)", "Calgary Stampeders (CFL)", "Calgary Wranglers (AHL)"],
         ["Airdrie", "Cochrane", "Okotoks", "Chestermere", '<a href="/iptv-edmonton/">Edmonton</a>'],
         "CTV Calgary, CBC Calgary and Global Calgary",
         """<p>Calgary households switched from cable in big numbers as prices rose after telecom mergers. IPTV keeps the Flames, the Stampeders and Alberta news, and adds 50,000+ channels and a massive movie library — for less than a basic cable package.</p>
<p>It’s also perfect for Calgary’s growing suburbs, where new builds may have fibre internet but no cable TV wiring.</p>""",
         """<h3>The Battle of Alberta</h3>
<p>Flames vs Oilers night? Sportsnet West and national feeds are included, and a 2-device plan lets the house divided watch on two TVs.</p>""",
         [("Can I watch the Flames on IPTV?", "<p>Yes, on Sportsnet West and national broadcasts, plus NHL Center Ice.</p>")],
         ["iptv-edmonton", "iptv-vancouver", "nhl-iptv"],
         ["iptv calgary", "calgary iptv"]),
    city("iptv-edmonton", "Edmonton", "Alberta", "Mountain time",
         "Telus, Rogers (formerly Shaw), local fibre providers",
         ["Edmonton Oilers (NHL)", "Edmonton Elks (CFL)", "Edmonton Oil Kings (WHL)"],
         ["St. Albert", "Sherwood Park", "Spruce Grove", "Leduc", '<a href="/iptv-calgary/">Calgary</a>'],
         "Alberta stations like CTV Calgary, Global Calgary, CBC Calgary and ICI Télé Alberta",
         """<p>Edmonton is one of the most searched cities for IPTV in Canada — and hockey is a big reason. Oilers fans want every game, including out-of-town broadcasts, without paying for multiple sports add-ons. IPTV bundles Sportsnet, TSN, CBC and NHL Center Ice into one plan.</p>
<p>Long winters mean a lot of time indoors — 300,000+ movies and series on demand help too.</p>""",
         """<h3>Watching the Oilers in 4K</h3>
<p>For the sharpest picture, use a 4K device (Firestick 4K Max, Nvidia Shield or Formuler) on a wired connection and pick the 4K sports feeds.</p>""",
         [("Can I watch every Oilers game?", "<p>Yes, via Sportsnet regional and national broadcasts, CBC and NHL Center Ice.</p>")],
         ["iptv-calgary", "nhl-iptv", "4k-iptv"],
         ["iptv in edmonton", "iptv edmonton", "edmonton iptv"]),
    city("iptv-ottawa", "Ottawa", "Ontario", "Eastern time",
         "Bell, Rogers, TekSavvy, Vidéotron (Gatineau side)",
         ["Ottawa Senators (NHL)", "Ottawa Redblacks (CFL)", "Atlético Ottawa (CPL)"],
         ["Gatineau", "Kanata", "Orléans", "Nepean", '<a href="/iptv-montreal/">Montreal</a>', '<a href="/iptv-toronto/">Toronto</a>'],
         "CTV Ottawa, CTV2 Ottawa, CBC Ottawa and TVA Gatineau",
         """<p>Ottawa–Gatineau is a bilingual region, and IPTV gives you English and French channels together: CTV Ottawa and CBC alongside TVA Gatineau, ICI Radio-Canada, RDS and TVA Sports.</p>
<p>For public servants and families alike, it’s an easy way to cut a cable bill without losing local news or the Senators.</p>""",
         """<h3>Both sides of the river</h3>
<p>IPTV works the same in Ottawa and Gatineau. Want the French experience? See our <a href="/iptv-quebec/">page en français</a>.</p>""",
         [("Can I watch the Senators on IPTV?", "<p>Yes, on TSN regional broadcasts, Sportsnet and national games, plus NHL Center Ice.</p>")],
         ["iptv-montreal", "iptv-toronto", "iptv-quebec", "iptv-halifax", "nhl-iptv"],
         ["iptv ottawa", "ottawa iptv", "iptv gatineau"]),
    city("iptv-winnipeg", "Winnipeg", "Manitoba", "Central time",
         "Bell MTS, Rogers (formerly Shaw), local fibre providers",
         ["Winnipeg Jets (NHL)", "Winnipeg Blue Bombers (CFL)", "Valour FC (CPL)", "Manitoba Moose (AHL)"],
         ["Steinbach", "Selkirk", "Brandon", "Portage la Prairie"],
         "CBC Winnipeg and ICI Télé Manitoba",
         """<p>Winnipeg sports fans are among the most loyal in the country, and IPTV lets them follow the Jets and Blue Bombers without a long cable contract. Central time means evening games from both coasts — ideal for a subscription that includes every sports network.</p>""",
         """<h3>Cold-weather tip</h3>
<p>Winter storms rarely affect IPTV the way they can affect satellite dishes — as long as your internet is up, so is your TV.</p>""",
         [("Can I watch the Jets on IPTV?", "<p>Yes, on TSN regional broadcasts and Sportsnet national games, plus NHL Center Ice.</p>")],
         ["iptv-calgary", "iptv-edmonton", "nhl-iptv"],
         ["iptv winnipeg", "winnipeg iptv"]),
    city("iptv-hamilton", "Hamilton", "Ontario", "Eastern time",
         "Bell, Rogers, Cogeco and independent ISPs",
         ["Hamilton Tiger-Cats (CFL)", "Forge FC (CPL)", "Toronto Maple Leafs (NHL, nearby)"],
         ["Burlington", "Stoney Creek", "Ancaster", "Grimsby", '<a href="/iptv-toronto/">Toronto</a>'],
         "CHCH, CTV Toronto, Global Toronto and CBC Toronto",
         """<p>Hamilton sits between Toronto and Niagara, and many households watch Toronto stations and teams. IPTV brings in the full Golden Horseshoe lineup plus national networks, without a regional cable package.</p>
<p>Ti-Cats fans get the CFL on TSN, and soccer fans can follow Forge FC and the Premier League.</p>""",
         """<h3>Works with Cogeco, Bell and Rogers internet</h3>
<p>Whichever provider serves your street, IPTV runs on top of your internet — no switch required.</p>""",
         [("Can I watch Tiger-Cats games?", "<p>Yes, CFL games on TSN are included.</p>")],
         ["iptv-toronto", "soccer-iptv", "iptv-ottawa"],
         ["iptv hamilton", "hamilton iptv"]),
    city("iptv-halifax", "Halifax", "Nova Scotia", "Atlantic time",
         "Bell (Aliant), Eastlink and independent ISPs",
         ["Halifax Mooseheads (QMJHL)", "HFX Wanderers (CPL)", "Halifax Thunderbirds (NLL)"],
         ["Dartmouth", "Bedford", "Sackville", "Truro", "Moncton"],
         "CTV Halifax and Global Halifax",
         """<p>Halifax is an hour ahead of Eastern time, which makes late West Coast games very late. IPTV with catch-up (on supported channels) and recording helps Maritimers watch on their own schedule.</p>
<p>East Coast viewers also get local news from CTV Halifax and Global Halifax, and the full national lineup.</p>""",
         """<h3>Atlantic time guide</h3>
<p>Set your IPTV app’s guide offset to Atlantic time so program times match your clock.</p>""",
         [("Is IPTV available in the Maritimes?", "<p>Yes, across Nova Scotia, New Brunswick, PEI and Newfoundland and Labrador — anywhere with internet.</p>")],
         ["iptv-montreal", "iptv-near-me", "nhl-iptv"],
         ["iptv halifax", "halifax iptv"]),
]
