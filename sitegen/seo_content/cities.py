"""IPTV near me hub. City, state and province pages live in geo.py (/usa/…, /canada/…)."""

PAGES = [
    dict(
        slug="iptv-near-me", hub="cities", hub_page=True,
        children=["usa", "canada", "canada/ontario/toronto", "canada/quebec/montreal", "canada/british-columbia/vancouver", "canada/alberta/calgary", "usa/new-york/new-york-city", "usa/california/los-angeles", "usa/illinois/chicago", "usa/texas/houston", "usa/florida/miami"],
        title="IPTV Near Me: Service in Every Canadian City | IPTVMaple",
        description="Looking for IPTV near you? IPTVMaple serves every city in Canada — Toronto, Montreal, Vancouver, Calgary, Edmonton, Ottawa and more. Try it free for 24 hours.",
        kicker="Cities", h1='IPTV <span class="grad-text">near me</span>: every city in Canada',
        lead="IPTV near me? It doesn’t need a local store or technician. If you have internet, you can be watching in minutes — wherever you are in Canada.",
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
<p>Pick your country, province, state or city below for local stations, teams and internet provider tips: <a href="/canada/">IPTV across Canada</a> (every province and 80 cities) and <a href="/usa/">IPTV in the USA</a> (all 50 states and 100+ cities). Don’t see your town? IPTVMaple still works there — the service is the same everywhere.</p>
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
]
