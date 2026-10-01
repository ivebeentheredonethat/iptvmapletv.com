"""Depth pass, part 3: sports pages. Every channel named here is in src/data/channels.json. See deep.py for how entries are applied."""

DATA = {}

NOTE = """<p>Schedules and broadcast rights change from season to season, so we don’t promise individual games. To check a specific game, ask our team on WhatsApp before you buy or watch it during the <a href="/try-iptv-canada/">free 24-hour trial</a>.</p>"""

DATA["iptv-sports"] = dict(
    add="""
<h2>Sports guides</h2>
<ul>
<li><a href="/nhl-iptv/">NHL</a>: Sportsnet, TSN, NHL Center Ice and French coverage.</li>
<li><a href="/nba-iptv/">NBA</a>: NBA TV, League Pass and Raptors games.</li>
<li><a href="/ufc-iptv/">UFC, boxing and wrestling</a>: PPV event channels.</li>
<li><a href="/f1-iptv/">Formula 1</a>: F1 TV and Sky Sports F1.</li>
<li><a href="/soccer-iptv/">Soccer</a>, <a href="/premier-league-iptv/">Premier League</a>, <a href="/champions-league-iptv/">Champions League</a> and <a href="/bein-sports-iptv/">beIN Sports</a>.</li>
<li><a href="/espn-iptv/">ESPN and the US sports networks</a>.</li>
</ul>

<h2>More leagues in the lineup</h2>
<table>
<thead><tr><th>League</th><th>Channels in the lineup</th></tr></thead>
<tbody>
<tr><td>NFL</td><td>NFL Network, NFL RedZone, NFL Sunday Ticket feed</td></tr>
<tr><td>MLB</td><td>MLB Network, MLB Extra Innings, MLB Strike Zone</td></tr>
<tr><td>MLS</td><td>MLS Soccer channels 01 to 11</td></tr>
<tr><td>Boxing and wrestling</td><td>PPV Boxing and PPV Wrestling event channels, WWE Network, DAZN</td></tr>
<tr><td>Combat sports</td><td>UFC PPV and Fight Pass channels, Fight Network</td></tr>
</tbody>
</table>

<h2>Follow several games at once</h2>
<p>Pick a plan with enough screens (1 to 5) so every viewer can watch their own game. Some apps also offer a multi-view mode on supported devices: see <a href="/tivimate-premium/">TiviMate Premium</a>. Compare the <a href="/iptv-price/">price per screen</a> before you choose.</p>

<h2>Big-event checklist</h2>
<ol>
<li>Test the setup a few days earlier with the <a href="/try-iptv-canada/">free trial</a>.</li>
<li>Use Ethernet or 5 GHz Wi-Fi; see the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
<li>Favourite the channels and any backup channels.</li>
<li>Start the stream 20 to 30 minutes early.</li>
</ol>
""" + NOTE,
    faq=[
        ("Is the NFL included?",
         "<p>The lineup includes NFL Network, NFL RedZone and an NFL Sunday Ticket feed, along with the US networks that carry games. Check the channels list to confirm what you need.</p>"),
        ("Can I watch MLB and MLS?",
         "<p>Yes. The lineup includes MLB Network and MLB Extra Innings, plus MLS Soccer channels 01 to 11.</p>"),
    ],
    related=["premier-league-iptv", "champions-league-iptv", "bein-sports-iptv", "espn-iptv"],
)

DATA["nhl-iptv"] = dict(
    add="""
<h2>NHL channels in the lineup</h2>
<table>
<thead><tr><th>Channel group</th><th>In the lineup</th></tr></thead>
<tbody>
<tr><td>Sportsnet</td><td>Sportsnet East, Ontario, West, Pacific, One and 360</td></tr>
<tr><td>TSN</td><td>TSN 1 to 5</td></tr>
<tr><td>French</td><td>RDS, RDS 2, RDS Info, TVA Sports, TVA Sports 2</td></tr>
<tr><td>League channels</td><td>NHL Network, NHL Center Ice</td></tr>
<tr><td>Game feeds</td><td>Numbered NHL Game channels</td></tr>
<tr><td>Free-to-air</td><td>CBC stations</td></tr>
</tbody>
</table>

<h2>Game times in your time zone</h2>
<p>A 7:00 p.m. Eastern puck drop is:</p>
<table>
<thead><tr><th>Newfoundland</th><th>Atlantic</th><th>Eastern</th><th>Central</th><th>Mountain</th><th>Pacific</th></tr></thead>
<tbody>
<tr><td>8:30 p.m.</td><td>8:00 p.m.</td><td>7:00 p.m.</td><td>6:00 p.m.</td><td>5:00 p.m.</td><td>4:00 p.m.</td></tr>
</tbody>
</table>
<p>Set your app’s time zone so the TV guide shows local times. In <a href="/tivimate/">TiviMate</a>, use the EPG time shift if programs look an hour off.</p>

<h2>Why the same game can be on different channels</h2>
<p>In Canada, rights to NHL games are split between several networks and by region, so the same game can appear on a national channel, a regional Sportsnet feed or TSN. Out-of-market games are on NHL Center Ice. Look at the guide for your team, and add every likely channel to your favourites.</p>

<h2>Playoff night checklist</h2>
<ul>
<li>Use Ethernet and a 4K-capable stick; see the <a href="/iptv-firestick/">Firestick guide</a>.</li>
<li>Start the stream 20 minutes early and keep a backup channel favourited.</li>
<li>Family with two games on at once? A 2 to 5 screen plan helps: see <a href="/iptv-price/">prices per screen</a>.</li>
</ul>
""" + NOTE,
    faq=[
        ("What time are NHL games in Canada?",
         "<p>A 7:00 p.m. Eastern game starts at 4:00 p.m. Pacific, 5:00 p.m. Mountain, 6:00 p.m. Central and 8:00 p.m. Atlantic. Your app’s TV guide shows the time in your own zone once you set it.</p>"),
        ("Which channels show NHL games?",
         "<p>Sportsnet and TSN feeds, CBC, RDS and TVA Sports in French, and NHL Network and NHL Center Ice. Which channel has a given game depends on the broadcast rights that season.</p>"),
    ],
    related=["espn-iptv", "iptv-sports", "iptv-firestick"],
)

DATA["nba-iptv"] = dict(
    add="""
<h2>NBA channels in the lineup</h2>
<table>
<thead><tr><th>Group</th><th>In the lineup</th></tr></thead>
<tbody>
<tr><td>NBA channels</td><td>NBA TV (Canada and US feeds), NBA League Pass</td></tr>
<tr><td>Team channels</td><td>NBA Teams channels for individual franchises, including the Toronto Raptors</td></tr>
<tr><td>Canadian networks</td><td>TSN 1 to 5 and Sportsnet channels</td></tr>
<tr><td>US networks</td><td>ESPN, ABC, TNT: see <a href="/espn-iptv/">ESPN on IPTV</a></td></tr>
</tbody>
</table>

<h2>NBA game times in your time zone</h2>
<table>
<thead><tr><th>Tip-off (Eastern)</th><th>Central</th><th>Mountain</th><th>Pacific</th></tr></thead>
<tbody>
<tr><td>7:30 p.m.</td><td>6:30 p.m.</td><td>5:30 p.m.</td><td>4:30 p.m.</td></tr>
<tr><td>10:00 p.m.</td><td>9:00 p.m.</td><td>8:00 p.m.</td><td>7:00 p.m.</td></tr>
</tbody>
</table>
<p>Late West Coast games can run past midnight in Eastern Canada. Catch-up and recording on supported apps let you watch them the next morning; see <a href="/tivimate-premium/">TiviMate Premium</a>.</p>

<h2>League Pass vs your usual channels</h2>
<p>League Pass channels give you the out-of-market games. Your local Raptors games are normally on the Canadian networks listed above. Use the favourites list in your app to put your team’s channels on one page.</p>
""" + NOTE,
    faq=[
        ("What time are NBA games in Canada?",
         "<p>A 7:30 p.m. Eastern tip-off is 4:30 p.m. Pacific. A 10:00 p.m. Eastern game is 7:00 p.m. Pacific. Set your app’s time zone so the guide shows local times.</p>"),
    ],
    related=["espn-iptv", "iptv-sports"],
)

DATA["ufc-iptv"] = dict(
    add="""
<h2>Combat sports channels in the lineup</h2>
<table>
<thead><tr><th>Channel</th><th>What it carries</th></tr></thead>
<tbody>
<tr><td>PPV UFC and numbered UFC event channels</td><td>UFC events, prelims and main cards</td></tr>
<tr><td>UFC Fight Pass and UFC 24/7</td><td>Fight Nights, the fight library and classics</td></tr>
<tr><td>PPV Boxing event channels</td><td>Major boxing cards (also on DAZN)</td></tr>
<tr><td>PPV Wrestling and WWE Network</td><td>Wrestling events</td></tr>
<tr><td>Fight Network</td><td>Combat sports programming</td></tr>
</tbody>
</table>

<h2>Fight night timeline</h2>
<p>Times vary by event, but a Saturday UFC card usually runs like this in Eastern time:</p>
<table>
<thead><tr><th>Part of the card</th><th>Typical start (ET)</th><th>Pacific</th></tr></thead>
<tbody>
<tr><td>Early prelims</td><td>6:00 to 8:00 p.m.</td><td>3:00 to 5:00 p.m.</td></tr>
<tr><td>Main card</td><td>10:00 p.m.</td><td>7:00 p.m.</td></tr>
</tbody>
</table>
<p>International events can start in the morning. Check the guide and the event’s official schedule.</p>

<h2>Fight night checklist</h2>
<ol>
<li>Install the app and test the setup in advance with the <a href="/try-iptv-canada/">free trial</a>.</li>
<li>Find the event channel when the card goes live and favourite it.</li>
<li>Use Ethernet; PPV nights are busy. See the <a href="/iptv-buffering-fix/">buffering fixes</a>.</li>
</ol>
""" + NOTE,
    faq=[
        ("What time does the UFC main card start in Canada?",
         "<p>A typical Saturday main card starts around 10:00 p.m. Eastern (7:00 p.m. Pacific), with prelims earlier. International events can start at different times.</p>"),
    ],
    related=["espn-iptv", "iptv-sports"],
)

DATA["f1-iptv"] = dict(
    add="""
<h2>F1 channels in the lineup</h2>
<table>
<thead><tr><th>Channel</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>F1 TV (4K)</td><td>The official F1 feed</td></tr>
<tr><td>Sky Sports F1 (UHD / FHD)</td><td>The UK’s dedicated F1 channel, with build-up and analysis</td></tr>
<tr><td>TSN and RDS</td><td>English and French Canadian sports networks</td></tr>
<tr><td>Other country feeds</td><td>F1 channels from Italy, Spain and elsewhere</td></tr>
</tbody>
</table>

<h2>Race weekend times in Canada</h2>
<table>
<thead><tr><th>Where the race is</th><th>Typical Sunday start (Eastern)</th></tr></thead>
<tbody>
<tr><td>Europe</td><td>Around 9:00 a.m. (6:00 a.m. Pacific)</td></tr>
<tr><td>North America (Montréal, Miami, Austin)</td><td>Afternoon</td></tr>
<tr><td>Asia and Australia</td><td>Overnight or very early morning</td></tr>
</tbody>
</table>
<p>Start times differ by race, so check the F1 calendar. Use catch-up on supported channels, or recording in <a href="/tivimate-premium/">TiviMate Premium</a>, to watch at a normal hour.</p>
<p>See also <a href="/iptv-sports/">all sports</a> and <a href="/iptv-quebec/">IPTV Québec</a> for French commentary.</p>
""" + NOTE,
    faq=[
        ("What time are F1 races in Canada?",
         "<p>European races usually start around 9:00 a.m. Eastern on Sunday, and North American races in the afternoon. Always check the official F1 calendar for each race.</p>"),
    ],
    related=["iptv-sports", "bein-sports-iptv"],
)

DATA["soccer-iptv"] = dict(
    add="""
<h2>Soccer guides</h2>
<ul>
<li><a href="/premier-league-iptv/">Premier League IPTV</a>: Premier League 4K, Sky Sports and club channels, plus kickoff times in Canada.</li>
<li><a href="/champions-league-iptv/">Champions League and European football</a>: UEFA, La Liga, Bundesliga and Serie A channels.</li>
<li><a href="/bein-sports-iptv/">beIN Sports</a>: beIN Sports 4K and the French beIN channels.</li>
</ul>

<h2>MLS in the lineup</h2>
<p>The lineup includes MLS Soccer channels 01 to 11, which cover Toronto FC, CF Montréal and the Vancouver Whitecaps along with the other MLS clubs. Local broadcast rights change by season, so confirm the fixture in the guide or ask us on WhatsApp.</p>

<h2>A note on channel names</h2>
<p>UK TNT Sports channels appear in the lineup under their former BT Sport names (BT Sports 1 to 10). If you can’t find “TNT Sports” in your app, search for BT Sport.</p>
""",
    related=["premier-league-iptv", "champions-league-iptv", "bein-sports-iptv"],
)
