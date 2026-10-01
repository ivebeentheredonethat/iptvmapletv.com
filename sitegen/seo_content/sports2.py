"""Sports long-tail: Premier League, European football, beIN Sports, ESPN.

Every channel named here is checked against src/data/channels.json. We never promise a particular match: schedules and
broadcast rights change, so each page says what the lineup carries and how to confirm a game before you subscribe.
"""
D = dict(published="2026-10-01", updated="2026-10-01")
VERIFY = """<p>Broadcast schedules and rights change from season to season, so we don’t promise individual matches. To check a specific game or competition, message our team on WhatsApp before you buy, or watch it during the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>"""

PAGES = [
    dict(
        slug="premier-league-iptv", hub="sports", **D,
        title="Premier League IPTV in Canada: Channels & Setup | IPTVMaple",
        description="Watch the Premier League on IPTV in Canada: the Sky Sports, Premier League 4K and club channels in the lineup, kickoff times in Eastern and Pacific, and setup.",
        kicker="Football", h1='Premier League IPTV <span class="grad-text">in Canada</span>',
        lead="Early-morning kickoffs, 4K feeds and all twenty clubs. Here is what the IPTVMaple lineup carries for English football and how to watch it.",
        crumb="Premier League IPTV", blurb="Premier League channels, kickoff times and setup in Canada.",
        answer="<p><strong>The IPTVMaple lineup includes a Premier League 4K channel, the Sky Sports football and Premier League channels from the UK, and a group of channels for individual Premier League clubs.</strong> Weekend matches kick off from 7:30 a.m. Eastern (4:30 a.m. Pacific) for early games. You need an IPTV app and a plan from $9; try it free for 24 hours first.</p>",
        body="""
<h2>What the lineup carries for English football</h2>
<table>
<thead><tr><th>Group</th><th>Examples in the lineup</th></tr></thead>
<tbody>
<tr><td>Premier League 4K</td><td>Premier League | 4K</td></tr>
<tr><td>Sky Sports (UK)</td><td>Sky Sports Premier League, Sky Sports Football UHD, Sky Sports Main Events UHD</td></tr>
<tr><td>Club channels (EPL group)</td><td>Arsenal, Chelsea, Liverpool, Manchester City, Manchester United, Tottenham and the other clubs in the EPL group</td></tr>
<tr><td>Other UK sports</td><td>BT Sports 1 to 10 channels (the UK’s TNT Sports, listed under the former BT Sport name), DAZN events</td></tr>
<tr><td>Second tier</td><td>EFL Championship channel and club channels</td></tr>
</tbody>
</table>
<p>Browse the exact names in the <a href="/channels-list/">channels list</a> (search “Premier League” or “Sky Sports”).</p>

<h2>Kickoff times in Canada</h2>
<p>Most English matches are played in the UK afternoon, which falls in the morning in Canada. The usual times are:</p>
<table>
<thead><tr><th>UK kickoff</th><th>Eastern</th><th>Central</th><th>Mountain</th><th>Pacific</th></tr></thead>
<tbody>
<tr><td>12:30</td><td>7:30 a.m.</td><td>6:30 a.m.</td><td>5:30 a.m.</td><td>4:30 a.m.</td></tr>
<tr><td>15:00</td><td>10:00 a.m.</td><td>9:00 a.m.</td><td>8:00 a.m.</td><td>7:00 a.m.</td></tr>
<tr><td>17:30</td><td>12:30 p.m.</td><td>11:30 a.m.</td><td>10:30 a.m.</td><td>9:30 a.m.</td></tr>
<tr><td>20:00 (weekday)</td><td>3:00 p.m.</td><td>2:00 p.m.</td><td>1:00 p.m.</td><td>12:00 p.m.</td></tr>
</tbody>
</table>
<p>For two weeks a year the UK and Canada change clocks on different dates, so the gap can be one hour shorter or longer. Set your app’s time zone and the TV guide shows local times. In TiviMate you can fine-tune this with the EPG time shift.</p>

<h2>How to watch Premier League matches</h2>
<ol>
<li>Start the <a href="/try-iptv-canada/">free trial</a> or <a href="/iptv-plans-canada/">choose a plan</a>.</li>
<li>Install an app: <a href="/tivimate-firestick/">TiviMate on Firestick</a> is the best for sports; phones and computers can use <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</li>
<li>Open the sports category, then the UK or “Premier League” group.</li>
<li>Use the guide to find the match, and add the channel to favourites.</li>
</ol>

<h2>Tips for match days</h2>
<ul>
<li>Use Ethernet or 5 GHz Wi-Fi. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li>Choose the 4K channel only if you have about 25 Mbps free for that screen; otherwise pick the HD channel.</li>
<li>Record or use catch-up on supported channels if the match is too early for you (TiviMate Premium: <a href="/tivimate-premium/">cost and features</a>).</li>
</ul>
""" + VERIFY + """
<p>More football: <a href="/champions-league-iptv/">Champions League and European football</a>, <a href="/bein-sports-iptv/">beIN Sports</a> and the general <a href="/soccer-iptv/">soccer IPTV guide</a>. For every sport, see <a href="/iptv-sports/">IPTV for sports in Canada</a>.</p>
""",
        faq=[
            ("Can I watch the Premier League on IPTV in Canada?",
             "<p>Yes. The IPTVMaple lineup includes a Premier League 4K channel, Sky Sports football channels from the UK and channels for individual clubs. Check the channels list or use the free trial to confirm the match you want.</p>"),
            ("What time are Premier League games in Canada?",
             "<p>A 12:30 p.m. UK kickoff is 7:30 a.m. Eastern and 4:30 a.m. Pacific. A 3 p.m. UK kickoff is 10 a.m. Eastern and 7 a.m. Pacific. Evening UK games are in the afternoon in Canada.</p>"),
            ("Is Premier League in 4K on IPTV?",
             "<p>The lineup includes a Premier League 4K channel and UHD Sky Sports feeds. You need about 25 Mbps per screen and a 4K device for the best quality.</p>"),
            ("Can I catch up on a match I missed?",
             "<p>On channels that support catch-up, you can replay a recent match from the TV guide in apps such as TiviMate Premium and IPTV Smarters Pro. Support varies by channel.</p>"),
            ("Which app is best for watching football?",
             "<p>TiviMate on a Firestick or Android TV has the best live guide, with favourites and quick channel switching. IPTV Smarters Pro works well on phones and computers.</p>"),
        ],
        related=["soccer-iptv", "champions-league-iptv", "bein-sports-iptv", "iptv-sports"],
        keywords=["iptv premier league", "premier league iptv", "iptv sky sports", "sky iptv", "iptv soccer", "iptv bein"],
    ),

    dict(
        slug="champions-league-iptv", hub="sports", **D,
        title="Champions League IPTV in Canada: UCL & Europe | IPTVMaple",
        description="Watch the UEFA Champions League, Europa League, La Liga, Bundesliga and Serie A on IPTV in Canada. Channels in the lineup, match times in Eastern and Pacific.",
        kicker="Football", h1='Champions League IPTV <span class="grad-text">and European football</span>',
        lead="Champions League nights, the Europa League and Europe’s top domestic leagues, on one subscription and every screen in the house.",
        crumb="Champions League IPTV", blurb="UEFA Champions League and European football channels in Canada.",
        answer="<p><strong>The IPTVMaple lineup includes a UEFA Champions League 4K channel, a UEFA Europa League 4K channel and 4K channels for La Liga, Bundesliga and Serie A</strong>, along with beIN Sports and DAZN. Champions League matches usually kick off at 12:45 p.m. or 3:00 p.m. Eastern (9:45 a.m. or 12:00 p.m. Pacific).</p>",
        body="""
<h2>European football in the lineup</h2>
<table>
<thead><tr><th>Competition</th><th>Channel in the lineup</th></tr></thead>
<tbody>
<tr><td>UEFA Champions League</td><td>UEFA Champions League | 4K</td></tr>
<tr><td>UEFA Europa League</td><td>UEFA Europa League | 4K</td></tr>
<tr><td>Spanish league</td><td>La Liga | 4K</td></tr>
<tr><td>German league</td><td>Bundesliga | 4K</td></tr>
<tr><td>Italian league</td><td>Serie A | 4K</td></tr>
<tr><td>International sport networks</td><td><a href="/bein-sports-iptv/">beIN Sports</a>, DAZN, Eurosport and Sky Sports feeds</td></tr>
</tbody>
</table>

<h2>Match times in Canada</h2>
<table>
<thead><tr><th>Kickoff (Central European Time)</th><th>Eastern</th><th>Pacific</th></tr></thead>
<tbody>
<tr><td>18:45</td><td>12:45 p.m.</td><td>9:45 a.m.</td></tr>
<tr><td>21:00</td><td>3:00 p.m.</td><td>12:00 p.m.</td></tr>
</tbody>
</table>
<p>Daylight-saving dates differ between Europe and Canada for a couple of weeks each year, so the gap can change by an hour. Use your app’s time zone setting and the TV guide shows local times.</p>

<h2>How to watch</h2>
<ol>
<li>Start the <a href="/try-iptv-canada/">free 24-hour trial</a> or pick a <a href="/iptv-plans-canada/">plan</a>.</li>
<li>Install <a href="/tivimate-firestick/">TiviMate</a> or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</li>
<li>Open the sports category and look for the UEFA, league or beIN Sports groups.</li>
<li>Add the channels you follow to favourites, so they are one press away on match night.</li>
</ol>

<h2>Match-night tips</h2>
<ul>
<li>Several games can run at once. Many apps let you add channels to a favourites row and switch quickly.</li>
<li>Test your setup before the first match. A free trial run on a weekend is enough.</li>
<li>If a stream stutters, use the HD version and a wired connection. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
</ul>
""" + VERIFY + """
<p>See also <a href="/premier-league-iptv/">Premier League IPTV</a>, the <a href="/soccer-iptv/">soccer IPTV guide</a> and <a href="/iptv-sports/">all sports on IPTV</a>.</p>
""",
        faq=[
            ("Can I watch the Champions League on IPTV in Canada?",
             "<p>The IPTVMaple lineup includes a UEFA Champions League 4K channel, along with beIN Sports and DAZN. Check the channel list or use the free trial to confirm the match you want.</p>"),
            ("What time is the Champions League in Canada?",
             "<p>A 21:00 CET kickoff is 3:00 p.m. Eastern (12:00 p.m. Pacific). An 18:45 CET game is 12:45 p.m. Eastern (9:45 a.m. Pacific).</p>"),
            ("Is the Europa League included?",
             "<p>The lineup includes a UEFA Europa League 4K channel as well as the Champions League channel.</p>"),
            ("Can I watch La Liga, Bundesliga and Serie A?",
             "<p>Yes. The lineup includes 4K channels for La Liga, Bundesliga and Serie A, plus other international sports networks.</p>"),
            ("What internet speed do I need for 4K football?",
             "<p>About 25 Mbps per screen. For lower speeds, choose the HD version of the channel.</p>"),
        ],
        related=["soccer-iptv", "premier-league-iptv", "bein-sports-iptv", "iptv-sports"],
        keywords=["iptv champions league", "champions league iptv", "iptv world cup", "world cup iptv", "iptv eurosport"],
    ),

    dict(
        slug="bein-sports-iptv", hub="sports", **D,
        title="beIN Sports IPTV in Canada: Channels & Setup | IPTVMaple",
        description="Watch beIN Sports on IPTV in Canada: the beIN Sports 4K channel and French beIN Sports 1 to 7 in the lineup, what each shows, DAZN and how to set up.",
        kicker="Sports channels", h1='beIN Sports IPTV <span class="grad-text">in Canada</span>',
        lead="beIN Sports is a global home for football and more. Here is which beIN channels are in the lineup, what they show and how to watch.",
        crumb="beIN Sports IPTV", blurb="beIN Sports 4K and the French beIN channels in the IPTVMaple lineup.",
        answer="<p><strong>The IPTVMaple lineup includes beIN Sports 4K and the French beIN Sports channels (beIN Sports 1, 2, 3 and the Max channels 4 to 7)</strong>, plus DAZN and Eurosport. Football, tennis, motorsport and other competitions appear depending on the season and the channel. Check the schedule before you subscribe, and try the 24-hour free trial.</p>",
        body="""
<h2>beIN Sports channels in the lineup</h2>
<table>
<thead><tr><th>Channel</th><th>Typical content</th></tr></thead>
<tbody>
<tr><td>beIN Sports 4K</td><td>Top matches and events in 4K</td></tr>
<tr><td>beIN Sports 1, 2, 3 (French)</td><td>Football, tennis, rugby, motorsport in French</td></tr>
<tr><td>beIN Sports Max 4 to 7 (French)</td><td>Extra match feeds when several games run at once</td></tr>
<tr><td>DAZN</td><td>Events and competitions from DAZN</td></tr>
<tr><td>Eurosport</td><td>Tennis, cycling, winter sports and more</td></tr>
</tbody>
</table>
<p>Which competition is on which channel changes by season. Look at the TV guide in your app, or search the <a href="/channels-list/">channels list</a>.</p>

<h2>How to watch beIN Sports on IPTV</h2>
<ol>
<li>Start the <a href="/try-iptv-canada/">free 24-hour trial</a> or choose a <a href="/iptv-plans-canada/">plan</a>.</li>
<li>Install an app such as <a href="/tivimate-firestick/">TiviMate</a> (Firestick, Android TV) or <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</li>
<li>Search for “beIN” in the app, or open the sports and France groups.</li>
<li>Add the channels to favourites.</li>
</ol>

<h2>French-language beIN for Québec viewers</h2>
<p>The French beIN Sports channels carry commentary in French, which many Québec viewers prefer for football. For Canadian French sports channels, see <a href="/iptv-quebec/">IPTV Québec</a> (RDS, TVA Sports) and the <a href="/french-iptv/">French IPTV page</a> for channels from France.</p>

<h2>Tips</h2>
<ul>
<li>Several matches at once means more than one beIN channel is active. Use the guide to find the right feed.</li>
<li>For 4K, plan on about 25 Mbps per screen.</li>
<li>Time zones: set the app to your province for correct guide times.</li>
</ul>
""" + VERIFY + """
<p>More: <a href="/premier-league-iptv/">Premier League</a>, <a href="/champions-league-iptv/">Champions League</a> and <a href="/iptv-sports/">all sports on IPTV</a>.</p>
""",
        faq=[
            ("Is beIN Sports included in IPTV in Canada?",
             "<p>The IPTVMaple lineup includes beIN Sports 4K and the French beIN Sports channels. Use the channels list or the free trial to confirm the channels you need.</p>"),
            ("Which beIN Sports channels are in the lineup?",
             "<p>beIN Sports 4K and the French beIN Sports 1, 2, 3 and Max 4 to 7 channels. DAZN and Eurosport are also in the lineup.</p>"),
            ("Can I watch beIN Sports in French?",
             "<p>Yes, the French beIN Sports channels carry French commentary.</p>"),
            ("How do I find a match on beIN Sports?",
             "<p>Open the TV guide in your IPTV app and search the beIN channels. The guide lists the programme on each channel.</p>"),
        ],
        related=["soccer-iptv", "premier-league-iptv", "champions-league-iptv", "iptv-sports"],
        keywords=["iptv bein", "iptv bein sport", "bein sports iptv", "iptv dazn"],
    ),

    dict(
        slug="espn-iptv", hub="sports", **D,
        title="ESPN on IPTV in Canada: ESPN 4K, ESPN2 & ESPN+ | IPTVMaple",
        description="ESPN on IPTV in Canada: ESPN 4K, ESPN2, ESPN+ and ESPN Deportes in the lineup, plus the other US sports networks (FS1, NFL Network, MLB Network) and how to watch.",
        kicker="Sports channels", h1='ESPN on IPTV <span class="grad-text">in Canada</span>',
        lead="ESPN, ESPN2 and the US sports networks are part of the IPTVMaple lineup. Here is what is included and how to start watching.",
        crumb="ESPN IPTV", blurb="ESPN and the US sports networks in the IPTVMaple lineup.",
        answer="<p><strong>The IPTVMaple lineup includes ESPN 4K, ESPN2 4K, ESPN+ 4K and ESPN Deportes 4K</strong>, along with the other US sports networks: Fox Sports 1 and 2, NFL Network, MLB Network, NBA TV, NHL Network and CBS Sports Network. Canadian sports channels (TSN, Sportsnet, RDS, TVA Sports) are included too.</p>",
        body="""
<h2>US sports networks in the lineup</h2>
<table>
<thead><tr><th>Network</th><th>In the lineup</th></tr></thead>
<tbody>
<tr><td>ESPN family</td><td>ESPN 4K, ESPN2 4K, ESPN+ 4K, ESPN Deportes 4K</td></tr>
<tr><td>Fox Sports</td><td>Fox Sports 1 (FS1), Fox Sports 2 (FS2), regional Fox Sports channels</td></tr>
<tr><td>League networks</td><td>NFL Network, NFL Sunday Ticket feed, MLB Network, NBA TV, NBA League Pass, NHL Network, NHL Center Ice</td></tr>
<tr><td>Others</td><td>CBS Sports Network, DAZN, WWE Network</td></tr>
</tbody>
</table>
<p>The lineup also carries <a href="/nhl-iptv/">NHL</a>, <a href="/nba-iptv/">NBA</a>, <a href="/ufc-iptv/">UFC</a> and <a href="/f1-iptv/">F1</a> coverage. Search the <a href="/channels-list/">channels list</a> for the exact channel names.</p>

<h2>How to watch ESPN on IPTV</h2>
<ol>
<li>Start the <a href="/try-iptv-canada/">free 24-hour trial</a> or choose a <a href="/iptv-plans-canada/">plan</a>.</li>
<li>Install an IPTV app: <a href="/tivimate-firestick/">TiviMate</a> on Firestick and Android TV, <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> on phones and computers.</li>
<li>Open the USA group and look for ESPN, or search “ESPN”.</li>
<li>Add ESPN, ESPN2 and the networks you follow to favourites.</li>
</ol>

<h2>Is ESPN available in Canada without IPTV?</h2>
<p>ESPN content in Canada is provided through licensed partners that change over time, and what you can watch depends on the service. IPTV gives you a US-style channel list in one place. Our lineup covers the channels above; the TV guide in your app shows what is on now.</p>

<h2>Tips</h2>
<ul>
<li>US prime-time games start later in the Pacific and Mountain time zones; set the app’s time zone for your province.</li>
<li>Pick HD if 4K stutters. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
</ul>
""" + VERIFY + """
<p>All sports: <a href="/iptv-sports/">IPTV for sports in Canada</a>.</p>
""",
        faq=[
            ("Does IPTV include ESPN in Canada?",
             "<p>The IPTVMaple lineup includes ESPN 4K, ESPN2 4K, ESPN+ 4K and ESPN Deportes 4K. Use the channels list or the free trial to confirm.</p>"),
            ("Which other US sports channels are included?",
             "<p>Fox Sports 1 and 2, NFL Network, MLB Network, NBA TV, NHL Network, CBS Sports Network and others. See the full list on the channels page.</p>"),
            ("Are Canadian sports channels included too?",
             "<p>Yes. TSN, Sportsnet, RDS and TVA Sports are part of the lineup, in English and French.</p>"),
            ("Can I watch ESPN on my phone?",
             "<p>Yes. Install IPTV Smarters Pro or another IPTV app on your phone or tablet and use your IPTVMaple login.</p>"),
        ],
        related=["iptv-sports", "nhl-iptv", "nba-iptv", "ufc-iptv"],
        keywords=["iptv espn", "espn iptv"],
    ),
]
