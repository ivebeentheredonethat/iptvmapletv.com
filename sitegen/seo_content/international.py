"""International / community cluster (approved diaspora markets only — see SEO STRUCTURE step 0.0.5). Hub: /iptv-international/

Channel names come from src/data/channels.json. Each page is written for that community living in Canada.
"""


def community(slug, name, country, flag, welcome, cities, groups, sport_line, time_note, faq_extra, related, keywords, h1=None, title=None, blurb=None):
    cards = "".join(f"<tr><td>{g}</td><td>{', '.join(chs)}</td></tr>" for g, chs in groups)
    top = ", ".join(groups[0][1][:4])
    return dict(
        slug=slug, hub="intl",
        title=title or f"{name} IPTV in Canada: {top.split(', ')[0]}, {top.split(', ')[1]} & More | IPTVMaple",
        description=f"{name} IPTV for Canada: {', '.join(groups[0][1][:3])} and more channels from {country} live, plus Canadian TV, in one plan. Try it free for 24h.",
        kicker="International", h1=h1 or f'<span class="grad-text">{name} IPTV</span> in Canada',
        lead=f"{flag} {welcome} Watch channels from {country} live in Canada — together with your Canadian channels, in one subscription.",
        crumb=f"{name} IPTV", blurb=blurb or f"{top.split(', ')[0]}, {top.split(', ')[1]} and more from {country}.",
        answer=f"<p><strong>{name} IPTV in Canada</strong>: IPTVMaple includes live channels from {country} — {top} and many more — alongside Canadian channels like CBC, CTV, TSN and TVA. One subscription, from $9, works on your TV, phone or computer anywhere in Canada.</p>",
        body=f"""
<h2>{name} channels included</h2>
<table>
<thead><tr><th>Category</th><th>Channels</th></tr></thead>
<tbody>{cards}</tbody>
</table>
<p>See every channel on the <a href="/channels-list/">full channels list</a> (search “{country}”).</p>

<h2>Home and Canada in one subscription</h2>
<p>Most {name}-Canadian families want two things: news, shows and football from {country}, and Canadian TV for the rest of the household. With IPTVMaple you don’t need a satellite dish or a second “ethnic package” from your cable company — {country} channels, Canadian networks, sports and 300,000+ movies and series all come in one plan.</p>
<p>{sport_line}</p>

<h2>For {name} communities across Canada</h2>
<p>IPTV works anywhere with internet, so it’s the same service in {cities}. Our team supports you 24/7 on WhatsApp and by email.</p>

<h2>Watching {country} TV from Canada: time zones</h2>
<p>{time_note} Use catch-up on supported channels, or TiviMate recording, to watch evening shows from {country} at a convenient time here.</p>

<h2>How to start</h2>
<ol>
<li>Request the <a href="/try-iptv-canada/">free 24-hour trial</a> and check your favourite {name} channels.</li>
<li>Pick a <a href="/iptv-plans-canada/">plan</a> — 2 to 5 devices if several family members watch at once.</li>
<li>Install an app: <a href="/tivimate/">TiviMate</a> on a <a href="/iptv-firestick/">Firestick</a>, or an app on your <a href="/iptv-samsung-tv/">smart TV</a>.</li>
<li>Open the “{country}” group and add your channels to favourites.</li>
</ol>
""",
        faq=[
            (f"Can I watch {country} channels in Canada?", f"<p>Yes. IPTVMaple includes {top} and many more {country} channels, streamed over the internet anywhere in Canada.</p>"),
            (f"Do I need a satellite dish for {name} TV?", "<p>No. IPTV works over your internet connection — no dish, no installer, no contract.</p>"),
            (f"Are Canadian channels included with {name} IPTV?", "<p>Yes, every plan includes Canadian channels (CBC, CTV, Global, TSN, Sportsnet, TVA, RDS) plus international channels.</p>"),
        ] + faq_extra,
        related=related,
        keywords=keywords,
    )


PAGES = [
    # ------------------------------------------------------------------ HUB
    dict(
        slug="iptv-international", hub="intl", hub_page=True,
        title="International IPTV in Canada: Channels From Home | IPTVMaple",
        description="International IPTV for Canada: Italian, Portuguese, Polish, Greek, Romanian, Ex-YU, British, French and Ukrainian channels plus Canadian TV. Try it free.",
        kicker="International", h1='<span class="grad-text">International IPTV</span> in Canada',
        lead="Channels from home and Canadian TV in one subscription — for Canada’s European and British communities.",
        crumb="International IPTV", blurb="TV from home for Canada’s communities.",
        answer="<p><strong>International IPTV</strong> lets you watch channels from your home country in Canada without a satellite dish. IPTVMaple includes hundreds of channels from <strong>Italy, Portugal, Poland, Greece, Romania, the former Yugoslavia, the UK, France and Ukraine</strong> — plus the full Canadian lineup — in every plan, from $9.</p>",
        body="""
<h2>Why international IPTV beats satellite and ethnic packages</h2>
<ul>
<li><strong>No dish or installer</strong> — works on your internet, even in condos and rentals.</li>
<li><strong>Every country in one plan</strong> — mixed families get all their channels together.</li>
<li><strong>Canadian channels included</strong> — CBC, CTV, Global, TSN, Sportsnet, TVA and RDS.</li>
<li><strong>Home-country sports</strong> — Serie A, Liga Portugal, Ekstraklasa, Super League Greece and more on their home broadcasters.</li>
</ul>

<h2>Countries available</h2>
<p>Choose your community below for the channel list and tips. More countries — Germany, Spain, the Netherlands, Albania and others — are in the <a href="/channels-list/">full channels list</a>.</p>

<h2>Watching in your language</h2>
<p>Each country’s channels are grouped together in your IPTV app, with the original audio. Many movies and series in the on-demand library also offer multiple audio tracks and subtitles.</p>
""",
        faq=[
            ("Which countries are included in IPTVMaple?", "<p>Channels from dozens of countries, including Italy, Portugal, Poland, Greece, Romania, the Ex-YU region, the UK, France, Germany, Spain and Ukraine, plus Canada and the USA.</p>"),
            ("Do I pay extra for international channels?", "<p>No. Every plan includes all countries — there are no add-on packages.</p>"),
            ("Can I watch my home country’s football league?", "<p>Yes, on the home broadcasters included in the lineup, such as Sky Sport and DAZN Italy, Sport TV Portugal, Polsat Sport, Cosmote and Nova Sport, and Arena Sport.</p>"),
            ("Is there an international IPTV free trial?", "<p>Yes, 24 hours of full access to every country, with no credit card.</p>"),
        ],
        related=["best-iptv-canada", "iptv-near-me"],
        keywords=["iptv world", "worldwide iptv", "iptv global", "euro iptv", "euroiptv", "international iptv"],
    ),
    community("italian-iptv", "Italian", "Italy", "🇮🇹", "Benvenuti!",
              "Toronto and Vaughan (Woodbridge), Montréal (Saint-Léonard), Hamilton, Vancouver and Ottawa",
              [("General", ["RAI 1", "RAI 2", "RAI 3", "Canale 5", "Italia 1", "Rete 4", "La7", "TV8", "Nove"]),
               ("Sport", ["Sky Sport Uno", "Sky Sport Football", "Sky Sport 24", "DAZN (Serie A)", "RAI Sport"]),
               ("Cinema &amp; series", ["Sky Cinema Uno", "Sky Cinema Due", "RAI Movie", "Iris", "Cielo", "Paramount Channel"]),
               ("Lifestyle", ["Real Time", "DMAX", "Giallo", "Top Crime", "RAI 5"])],
              "Follow Serie A and the Azzurri on Sky Sport and DAZN, and watch the Giro d’Italia and Formula 1 with Italian commentary on RAI and Sky.",
              "Italy is 6 hours ahead of Toronto and Montréal and 9 hours ahead of Vancouver, so Serie A kick-offs often land on weekend mornings here.",
              [("Can I watch Serie A with Italian commentary?", "<p>Yes, on Sky Sport and DAZN Italy channels included in the lineup.</p>")],
              ["portuguese-iptv", "greek-iptv", "soccer-iptv"], ["italian iptv", "iptv italia", "rai iptv"]),
    community("portuguese-iptv", "Portuguese", "Portugal", "🇵🇹", "Bem-vindos!",
              "Toronto (Little Portugal), Mississauga, Brampton, Montréal, Kitchener–Cambridge and Vancouver",
              [("General", ["RTP 1", "RTP 2", "SIC", "TVI", "RTP Açores", "RTP Madeira", "Porto Canal"]),
               ("News", ["RTP 3", "SIC Notícias", "CMTV", "TVI 24"]),
               ("Sport", ["Sport TV", "Sport TV 4K", "Eleven Sports"]),
               ("Entertainment", ["SIC Mulher", "SIC Radical", "TVI Ficção", "AXN", "TV Cine"])],
              "Follow Benfica, Porto and Sporting in Liga Portugal on Sport TV and Eleven Sports, plus the Seleção in every tournament.",
              "Portugal is 5 hours ahead of Eastern time (4 ahead of the Azores time zone), so evening novelas air in the afternoon in Toronto.",
              [("Are RTP Açores and RTP Madeira included?", "<p>Yes, both regional channels are part of the Portuguese lineup — popular with Canada’s large Azorean community.</p>")],
              ["italian-iptv", "soccer-iptv", "iptv-toronto"], ["portuguese iptv", "iptv portugal", "iptv portugues"]),
    community("polish-iptv", "Polish", "Poland", "🇵🇱", "Witamy!",
              "Toronto (Roncesvalles), Mississauga, Edmonton, Calgary, Montréal and Winnipeg",
              [("General", ["TVP 1", "TVP 2", "Polsat", "TVN", "TV Puls", "TV4", "Polonia 1"]),
               ("Sport", ["Polsat Sport", "Canal+ Sport", "Eleven Sports", "Polsat Sport News"]),
               ("Movies &amp; series", ["Canal+ Film", "Canal+ Seriale", "HBO", "Polsat Film", "FilmBox", "Kino TV"]),
               ("News", ["TVN24 BiS", "TVP Info"])],
              "Watch the Ekstraklasa, the national team and Polish ski jumping and volleyball on Polsat Sport, Canal+ Sport and Eleven Sports.",
              "Poland is 6 hours ahead of Eastern time and 8 ahead of Alberta.",
              [("Can I watch TVN and Polsat in Canada?", "<p>Yes, TVN, Polsat, TVP and many more Polish channels are included.</p>")],
              ["ukrainian-iptv", "romanian-iptv", "iptv-edmonton"], ["polish iptv", "iptv polska", "iptv polonia"]),
    community("greek-iptv", "Greek", "Greece", "🇬🇷", "Καλώς ήρθατε!",
              "Toronto (the Danforth), Montréal (Park Extension, Laval), Vancouver and Calgary",
              [("General", ["ERT 1", "ERT 2", "ERT 3", "ANT1", "Alpha", "Skai", "Mega", "Star", "Open Beyond"]),
               ("Sport", ["Nova Sport", "Cosmote Sport"]),
               ("Cinema", ["Nova Cinema", "Cosmote Cinema", "Village Cinema"]),
               ("Regional", ["Creta TV", "Makedonia TV", "ERT World"])],
              "Follow Olympiacos, Panathinaikos, AEK and PAOK in the Super League on Nova Sport and Cosmote Sport.",
              "Greece is 7 hours ahead of Eastern time and 10 hours ahead of Pacific time.",
              [("Is ERT World included?", "<p>Yes, along with ERT 1, 2 and 3 and the main private channels.</p>")],
              ["italian-iptv", "iptv-montreal", "iptv-toronto"], ["greek iptv", "iptv greece", "ellinika iptv"]),
    community("romanian-iptv", "Romanian", "Romania", "🇷🇴", "Bine ați venit!",
              "Montréal, Toronto, Kitchener–Waterloo, Calgary, Edmonton and Vancouver",
              [("General", ["TVR 1", "TVR 2", "PRO TV", "Antena 1", "Kanal D", "Prima TV", "National TV", "Happy Channel"]),
               ("News", ["Antena 3", "Realitatea TV", "B1 TV", "Digi 24"]),
               ("Movies &amp; series", ["HBO Romania", "AXN", "PRO Cinema", "Antena Stars", "Diva"]),
               ("Documentaries", ["Digi World", "Digi Life", "DocuBox"])],
              "Catch Liga 1 and the national team, plus Romanian tennis and handball, on Digi Sport and Telekom Sport.",
              "Romania is 7 hours ahead of Eastern time.",
              [("Can I watch PRO TV and Antena 1 in Canada?", "<p>Yes, both are included, along with TVR, Kanal D and many more Romanian channels.</p>")],
              ["polish-iptv", "ex-yu-iptv", "iptv-montreal"], ["romanian iptv", "canale romanesti iptv", "iptv romania"],
              title="Romanian IPTV in Canada: Canale Românești Live | IPTVMaple"),
    community("ex-yu-iptv", "Ex-YU", "the Ex-YU region", "🇷🇸🇭🇷🇧🇦", "Dobrodošli! IP televizija sa vašim kanalima, bilo gdje u Kanadi.",
              "Toronto, Mississauga, Hamilton, Kitchener, Calgary, Vancouver and Montréal",
              [("Serbia", ["RTS 1", "RTS Svet", "Pink", "Prva", "Nova S", "N1 Srbija"]),
               ("Croatia", ["HRT 1", "HRT 2", "Nova TV", "RTL", "Doma TV", "N1 HR"]),
               ("Bosnia &amp; Herzegovina", ["BHT", "FTV", "Hayat", "Face TV", "OBN", "N1 Bosna"]),
               ("Sport", ["Arena Sport", "Sport Klub"])],
              "Follow the SuperLiga, HNL and Premijer Liga BiH, plus basketball and the ABA League, on Arena Sport and Sport Klub.",
              "The region is 6 hours ahead of Eastern time and 9 hours ahead of Pacific time.",
              [("Šta je IP televizija?", "<p>IP televizija (IPTV) je televizija preko interneta — bez satelitske antene. Sa IPTVMaple gledate RTS, HRT, BHT, Pink, Arena Sport i kanadske kanale u jednoj pretplati.</p>"),
               ("Can I watch Arena Sport and Sport Klub in Canada?", "<p>Yes, both are included with every plan.</p>")],
              ["romanian-iptv", "ukrainian-iptv", "iptv-toronto"],
              ["ip televizija", "iptv kanali", "exyu iptv", "iliria iptv", "balkan iptv"],
              h1='<span class="grad-text">IP televizija</span>: Ex-YU IPTV in Canada',
              title="IP Televizija u Kanadi: RTS, HRT, BHT, Arena Sport | IPTVMaple",
              blurb="IP televizija: RTS, HRT, BHT, Pink, Arena Sport."),
    community("uk-iptv", "UK", "the United Kingdom", "🇬🇧", "Welcome, fellow Brits!",
              "Toronto, Vancouver, Calgary, Ottawa, Victoria and Halifax",
              [("General", ["BBC One", "BBC Two", "ITV1", "ITV2", "Channel 4", "Channel 5", "E4", "BBC Scotland"]),
               ("Sport", ["Sky Sports Main Event", "Sky Sports Premier League", "Sky Sports F1", "BT Sport / TNT Sports", "Premier Sports", "Eurosport"]),
               ("Entertainment", ["Sky Atlantic", "Sky Max", "Gold", "Dave", "Alibi", "Comedy Central"]),
               ("News &amp; docs", ["Sky News", "BBC regional news", "Quest", "Discovery"])],
              "Watch every Premier League, EFL and Scottish football match on Sky Sports, BT Sport and club channels, plus cricket, darts and F1.",
              "The UK is 5 hours ahead of Eastern time and 8 hours ahead of Pacific time — Saturday 3 p.m. games are 10 a.m. in Toronto.",
              [("Can I watch BBC iPlayer-style BBC channels live?", "<p>Yes, BBC One (including regional versions), BBC Two, BBC Three and BBC Four are included live.</p>")],
              ["soccer-iptv", "f1-iptv", "iptv-vancouver"], ["ukiptv", "uk iptv", "british iptv", "iptv uk", "iptv sky sports"],
              title="UK IPTV in Canada: BBC, ITV & Sky Sports Live | IPTVMaple",
              blurb="BBC, ITV, Channel 4 and Sky Sports live."),
    community("french-iptv", "French", "France", "🇫🇷", "Bienvenue !",
              "Montréal, Québec City, Gatineau, Ottawa, Toronto and Vancouver",
              [("Généralistes", ["TF1", "France 2", "France 3", "France 5", "M6", "Arte", "TV5 Monde", "W9", "C8"]),
               ("Info", ["BFM TV", "LCI", "BFM Business"]),
               ("Sport", ["beIN Sports 1", "beIN Sports 2", "beIN Sports 3", "RMC Sport", "Eurosport"]),
               ("Divertissement", ["TF1 Séries Films", "6ter", "TMC", "Paris Première", "Téva", "RMC Découverte"])],
              "Suivez la Ligue 1, le Top 14 et Roland-Garros sur beIN Sports, RMC Sport et France Télévisions.",
              "La France a 6 heures d’avance sur Montréal et 9 heures sur Vancouver.",
              [("Is this different from Québec channels?", "<p>Yes — this page is about channels from France (TF1, France 2, M6…). For TVA, ICI Radio-Canada and Noovo, see <a href=\"/iptv-quebec/\">IPTV Québec</a>. Both are included in every plan.</p>")],
              ["iptv-quebec", "iptv-montreal", "soccer-iptv"], ["iptvfrance", "iptv france", "iptv orange", "french iptv", "tf1 iptv"],
              title="French IPTV in Canada: TF1, France 2, M6 & beIN | IPTVMaple"),
    community("ukrainian-iptv", "Ukrainian", "Ukraine", "🇺🇦", "Ласкаво просимо!",
              "Winnipeg, Edmonton, Toronto, Saskatoon, Calgary and Vancouver",
              [("General", ["1+1", "1+1 International", "ICTV", "STB", "Novy Channel", "Inter", "TET", "2+2"]),
               ("News", ["5 Kanal", "News 24", "UNIAN TV", "112 Ukraine"]),
               ("Music &amp; kids", ["M1", "M2", "Music Box", "Plus Plus"]),
               ("Regional", ["TRK Ukraina", "Tysa 1", "ATR"])],
              "Follow Ukrainian Premier League football and the national team, plus boxing events, through the sports lineup.",
              "Kyiv is 7 hours ahead of Eastern time and 8 hours ahead of Winnipeg.",
              [("Are Ukrainian news channels included?", "<p>Yes, including 5 Kanal, News 24 and UNIAN TV, alongside 1+1, ICTV and STB.</p>")],
              ["polish-iptv", "iptv-winnipeg", "iptv-edmonton"], ["ukrainian iptv", "iptv ukraine"],
              title="Ukrainian IPTV in Canada: 1+1, ICTV, STB & More | IPTVMaple"),
]
