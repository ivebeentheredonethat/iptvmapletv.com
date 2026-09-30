"""Site-wide settings. Change contact details, analytics IDs and navigation here."""
from urllib.parse import quote

SITE_URL = "https://iptvmapletv.com"
NAME = "IPTVMaple"
LEGAL_NAME = "IPTVMaple 4K"
TAGLINE = "Premium 4K IPTV for Canada"
DEFAULT_OG = "/brand/og-default.jpg"
YEAR = 2026

EMAIL = "Help@iptvmapletv.com"
EMAIL_SUBJECT = "Interest in IPTVmaple Service"
EMAIL_BODY = "Hello IPTVmaple Team,\n\nI am interested in your IPTV service and would like to get more information.\n\nThank you."
MAILTO = f"mailto:{EMAIL}?subject={quote(EMAIL_SUBJECT)}&body={quote(EMAIL_BODY)}"

WHATSAPP = "17828026280"  # main support line (floating button, contact page)
WHATSAPP_TEXT = "Hi, I'm interested in your Maple service"
WHATSAPP_URL = f"https://api.whatsapp.com/send?phone={WHATSAPP}&text={quote(WHATSAPP_TEXT)}"
WHATSAPP_ORDERS = "16727022155"  # shown on the thank-you page / referral program
WHATSAPP_ORDERS_DISPLAY = "+1 (672) 702-2155"
TELEGRAM_URL = "https://t.me/LiveSupportIPTV"

GOOGLE_TAGS = ["GT-WF62KHHF", "G-JJR5ECP8RV"]
REDDIT_PIXEL = "a2_g8z3rkvzo68a"
GOOGLE_SITE_VERIFICATION = "9QinAgZmvCoRQKS99jjmNbTDzV5TcQVUZ8VnO2poI0M"

PROMO = ("🎁 Refer 1 friend · get 1 year FREE", "/refer-a-friend/")

NAV = [
    ("Home", "/"),
    ("Pricing", "/iptv-plans-canada/"),
    ("Channels", "/channels-list/"),
    ("How it works", "/how-it-works/"),
    ("Referral", "/refer-a-friend/"),
    ("Free trial", "/try-iptv-canada/"),
    ("Contact", "/contact/"),
]

FOOTER = [
    ("Service", [("Pricing", "/iptv-plans-canada/"), ("Free 24h trial", "/try-iptv-canada/"), ("Channels list", "/channels-list/"), ("How it works", "/how-it-works/")]),
    ("Company", [("About us", "/about-iptvmaple/"), ("Referral program", "/refer-a-friend/"), ("Contact us", "/contact/"), ("Cord-cutting guide", "/cord-cutting-guide/")]),
    ("Legal", [("Terms & conditions", "/terms/"), ("Privacy policy", "/privacy/"), ("Refund policy", "/refund/")]),
]
