"""Helpers shared by the SEO content modules. Prices always come from src/data/plans.json, never typed by hand."""
from ..components import PLANS


def _by_months(conn):
    return {p["months"]: p for p in conn["plans"]}


def price_table(link=True, lang="en"):
    """All plans: screens x (1, 6, 12 months), each price linking to its order page, plus the 12-month cost per month."""
    fr = lang == "fr"
    money = (lambda v: f"{v:.2f} $".replace(".", ",")) if fr else (lambda v: f"${v:.2f}")
    whole = (lambda v: f"{v} $") if fr else (lambda v: f"${v}")
    rows = []
    for c in PLANS["connections"]:
        by = _by_months(c)
        cell = lambda m: (f'<a href="/{by[m]["slug"]}/">{whole(by[m]["price"])}</a>' if link else whole(by[m]["price"]))
        label = f'{c["devices"]} écran{"s" if c["devices"] > 1 else ""}' if fr else f'{c["devices"]} device{"s" if c["devices"] > 1 else ""}'
        rows.append(f'<tr><td>{label}</td><td>{cell(1)}</td><td>{cell(6)}</td><td>{cell(12)}</td><td>{money(by[12]["price"] / 12)}</td></tr>')
    head = (("Écrans", "1 mois", "6 mois", "12 mois", "Par mois (12 m.)") if fr else
            ("Screens", "1 month", "6 months", "12 months", "Per month (12 mo)"))
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def per_screen_table():
    """12-month price per screen per month — shows that extra screens cost less than a second subscription."""
    rows = []
    for c in PLANS["connections"]:
        by = _by_months(c)
        total = by[12]["price"]
        rows.append(f'<tr><td>{c["devices"]}</td><td>${total}</td><td>${total / 12:.2f}</td><td>${total / 12 / c["devices"]:.2f}</td></tr>')
    return ('<table><thead><tr><th>Screens</th><th>12-month price</th><th>Per month</th><th>Per screen, per month</th></tr></thead>'
            "<tbody>" + "".join(rows) + "</tbody></table>")


def one_device(months):
    """The 1-device plan for the given length, e.g. one_device(12)['price'] -> 49."""
    return _by_months(PLANS["connections"][0])[months]


def price_range():
    """(lowest price, 12-month 1-device price per month) for copy such as 'from $9' or '$4.08 a month'."""
    one = PLANS["connections"][0]
    by = _by_months(one)
    return by[1]["price"], by[12]["price"] / 12


def plan(devices, months):
    """A single plan dict, e.g. plan(3, 12)['price']."""
    conn = next(c for c in PLANS["connections"] if c["devices"] == devices)
    return _by_months(conn)[months]
