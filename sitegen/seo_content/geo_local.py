"""Short, factual local context for city pages whose lineup is shared with a neighbouring city (suburbs of the same metro).
Each line is plain geography: where the city sits, what it is next to. Keyed by city name; FR is used on /fr/ pages."""

EN = {
    "Terrebonne": "Terrebonne sits on the Mille Îles River north of Montreal, in the Lanaudière region, and is one of the largest cities on the North Shore. Many households commute into Montreal, so Canadiens games and Montreal news are the TV staples here.",
    "Brossard": "Brossard is a South Shore city in the Montérégie region, across the St. Lawrence from Montreal and home to the Quartier DIX30 shopping district. Households here often mix French and English channels in the same evening.",
    "Laval": "Laval fills Île Jésus, between the Rivière des Prairies and the Mille Îles River, and is Quebec’s third-largest city after Montreal and Quebec City.",
    "Longueuil": "Longueuil is the largest city on Montreal’s South Shore and the home of Montréal–Saint-Hubert airport.",
    "Gatineau": "Gatineau lies across the Ottawa River from Ottawa, in the Outaouais region, so households often follow both Quebec and Ottawa broadcasts.",
    "Saguenay": "Saguenay is in the Saguenay–Lac-Saint-Jean region along the Saguenay River, a long way from the Montreal market, which makes an internet-delivered lineup especially useful.",
    "Lévis": "Lévis faces Quebec City across the St. Lawrence River, linked by the Pierre-Laporte and Quebec bridges and a passenger ferry.",
    "Trois-Rivières": "Trois-Rivières sits on the north shore of the St. Lawrence, about halfway between Montreal and Quebec City, at the mouth of the Saint-Maurice River.",
    "Sherbrooke": "Sherbrooke is the largest city of the Eastern Townships (Estrie) and home to the Université de Sherbrooke.",
    "Ajax": "Ajax is a Durham Region town on Lake Ontario, east of Toronto, which makes Toronto teams and broadcasts the default viewing.",
    "Scarborough": "Scarborough is Toronto’s eastern district, running along Lake Ontario and the Scarborough Bluffs, so it follows the full Toronto lineup.",
    "Etobicoke": "Etobicoke is Toronto’s western district, along Lake Ontario and the Humber River, and shares the full Toronto lineup.",
    "Milton": "Milton is in Halton Region, west of Toronto, and one of the fastest-growing towns in the Greater Toronto Area.",
    "Windsor": "Windsor faces Detroit across the Detroit River, so many households follow Canadian teams and Detroit’s Red Wings, Lions, Pistons and Tigers.",
    "Guelph": "Guelph is home to the University of Guelph, about an hour west of Toronto in Wellington County.",
    "Kitchener": "Kitchener is part of Waterloo Region with Waterloo and Cambridge, known for its tech sector and its Oktoberfest.",
    "Brampton": "Brampton is in Peel Region, northwest of Toronto, and one of Canada’s fastest-growing large cities.",
    "Coquitlam": "Coquitlam is one of the Tri-Cities of Metro Vancouver, east of Burnaby, and follows the Vancouver lineup.",
    "Delta": "Delta lies south of the Fraser River in Metro Vancouver and includes Ladner, Tsawwassen and North Delta, with the BC Ferries terminal at Tsawwassen.",
    "Victoria": "Victoria is British Columbia’s capital, at the southern tip of Vancouver Island, where the Pacific time zone makes East Coast games start in the morning.",
    "Kelowna": "Kelowna sits on Okanagan Lake in the Okanagan Valley, in the interior of British Columbia, away from the Vancouver market.",
    "Nanaimo": "Nanaimo is on central Vancouver Island, linked to the mainland by BC Ferries.",
    "Lethbridge": "Lethbridge is in southern Alberta, home to the University of Lethbridge and the WHL’s Lethbridge Hurricanes.",
    "Airdrie": "Airdrie is just north of Calgary along Highway 2, and follows the Calgary lineup.",
    "Chandler": "Chandler is part of the East Valley, southeast of Phoenix in Maricopa County.",
    "Scottsdale": "Scottsdale is known for Old Town and for MLB spring training, when the Giants play at Scottsdale Stadium.",
    "Mesa": "Mesa is one of Arizona’s largest cities, in the East Valley, and the Cubs’ spring training home at Sloan Park.",
    "Gilbert": "Gilbert is a fast-growing East Valley town southeast of Phoenix, known for its Heritage District.",
}
FR = {
    "Terrebonne": "Terrebonne s’étend le long de la rivière des Mille Îles, au nord de Montréal, dans Lanaudière. C’est l’une des plus grandes villes de la Rive-Nord, et beaucoup de familles travaillent à Montréal : les matchs du Canadien et les nouvelles de Montréal y dominent l’écran.",
    "Brossard": "Brossard est une ville de la Rive-Sud, en Montérégie, de l’autre côté du Saint-Laurent par rapport à Montréal, et abrite le quartier commercial DIX30. On y passe souvent des chaînes françaises aux chaînes anglaises dans la même soirée.",
    "Laval": "Laval occupe toute l’île Jésus, entre la rivière des Prairies et la rivière des Mille Îles, et est la troisième plus grande ville du Québec après Montréal et Québec.",
    "Longueuil": "Longueuil est la plus grande ville de la Rive-Sud de Montréal et accueille l’aéroport de Montréal–Saint-Hubert.",
    "Gatineau": "Gatineau fait face à Ottawa, de l’autre côté de la rivière des Outaouais, en Outaouais : beaucoup de foyers suivent à la fois les diffusions québécoises et celles d’Ottawa.",
    "Saguenay": "Saguenay se trouve au Saguenay–Lac-Saint-Jean, le long de la rivière Saguenay, loin du marché montréalais : un abonnement livré par Internet y est particulièrement pratique.",
    "Lévis": "Lévis fait face à Québec, de l’autre côté du Saint-Laurent, reliée par les ponts Pierre-Laporte et de Québec et par un traversier pour piétons.",
    "Trois-Rivières": "Trois-Rivières est située sur la rive nord du Saint-Laurent, à mi-chemin entre Montréal et Québec, à l’embouchure de la rivière Saint-Maurice.",
    "Sherbrooke": "Sherbrooke est la plus grande ville de l’Estrie (Cantons-de-l’Est) et le siège de l’Université de Sherbrooke.",
}


def local_note(city, fr=False):
    txt = (FR if fr else EN).get(city, "")
    return f"<p>{txt}</p>" if txt else ""
