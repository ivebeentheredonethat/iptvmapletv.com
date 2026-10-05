"""French (fr-CA) cluster, part 2: legality, price, troubleshooting, players, M3U lists, Smarters, and device guides.

Written in Québec French, formal « vous », matching sitegen/seo_content/fr.py. Each page is paired by hreflang with its English twin
where one exists (see PAIRS in __init__.py).
"""
from ._util import plan, price_range, price_table

LOW, PER_MONTH = price_range()
PM = f"{PER_MONTH:.2f}".replace(".", ",")
D = dict(lang="fr", published="2026-10-01", updated="2026-10-01")

LOGIN_FR = """<p>Après votre commande, ou votre <a href="/try-iptv-canada/">essai gratuit de 24 heures</a>, IPTVMaple vous envoie vos identifiants par courriel et par WhatsApp : une <strong>URL de serveur, un nom d’utilisateur et un mot de passe</strong> (identifiants Xtream Codes), ainsi qu’un <strong>lien M3U</strong> si votre application le préfère.</p>"""

PAGES = [
    # ------------------------------------------------------------------ LÉGAL
    dict(
        slug="iptv-legal-canada", hub="fr", **D,
        title="IPTV légal au Canada : ce que dit la loi (2026) | IPTVMaple",
        description="L’IPTV est-il légal au Canada? La technologie l’est; ce qui compte, ce sont les droits sur les chaînes. Voici la loi et comment vérifier un service.",
        kicker="Explication juridique", h1='IPTV légal au Canada : <span class="grad-text">la réponse honnête</span>',
        lead="L’IPTV est une technologie de diffusion, pas un type de contenu. Ce qui compte pour la loi, c’est de savoir si le service a le droit de diffuser ce qu’il montre.",
        crumb="IPTV légal au Canada", blurb="Ce que dit la loi canadienne sur l’IPTV et comment vérifier un service.",
        answer="<p><strong>L’IPTV est légal au Canada en tant que technologie.</strong> Il s’agit simplement de télévision diffusée par Internet, et de grandes entreprises de télécommunications l’utilisent pour leurs propres services de télé. Ce qui compte, c’est que le service ait l’autorisation des titulaires de droits pour les chaînes et les contenus qu’il diffuse. Un service qui retransmet du contenu protégé sans autorisation peut enfreindre le droit d’auteur et les règles de radiodiffusion. Cette page est de l’information générale, pas un avis juridique.</p>",
        body="""
<h2>Ce qu’est l’IPTV</h2>
<p>IPTV signifie « télévision par protocole Internet ». Au lieu d’un signal de câble ou de satellite, la vidéo arrive par votre connexion Internet. Des entreprises comme Bell et Telus diffusent leur télé de cette façon, tout comme des services de diffusion en continu comme Crave, ICI TOU.TV et CBC Gem. La technologie n’a rien d’illégal. La question juridique porte toujours sur le <em>contenu et l’autorisation</em>.</p>

<h2>Qu’est-ce qui rend un service IPTV légitime?</h2>
<p>Un service est en règle lorsque les propriétaires ou les détenteurs de licences du contenu l’ont autorisé à le distribuer. Au Canada, plusieurs lois sont pertinentes :</p>
<ul>
<li><strong>Le droit d’auteur.</strong> La <a href="https://laws-lois.justice.gc.ca/fra/lois/C-42/" rel="noopener">Loi sur le droit d’auteur</a> donne aux créateurs et aux titulaires de droits le droit exclusif de communiquer leur œuvre au public par télécommunication.</li>
<li><strong>La radiodiffusion.</strong> Le <a href="https://crtc.gc.ca/fra/home-accueil.htm" rel="noopener">CRTC</a> réglemente la radiodiffusion au Canada, y compris les entreprises de distribution qui ont besoin d’une licence.</li>
<li><strong>La protection des signaux.</strong> La <a href="https://laws-lois.justice.gc.ca/fra/lois/R-2/" rel="noopener">Loi sur la radiocommunication</a> restreint le décodage d’un signal d’abonnement crypté sans l’autorisation du distributeur légitime.</li>
</ul>
<p>En pratique, un forfait de télé d’un fournisseur de télécommunications ou un service de diffusion en continu autorisé est légal parce que l’entreprise a des ententes avec les radiodiffuseurs. Un service IPTV qui retransmet simplement les chaînes d’autres entreprises n’est légitime que s’il a le même genre d’autorisation.</p>

<h2>Ce qui s’est passé devant les tribunaux canadiens</h2>
<p>Les titulaires de droits au Canada ont utilisé les tribunaux contre l’IPTV non autorisé. En 2019, la Cour fédérale a ordonné à des fournisseurs d’accès Internet de bloquer l’accès à un service IPTV non autorisé, et la Cour d’appel fédérale a ensuite confirmé cette approche. De telles ordonnances montrent qu’un service non autorisé peut être bloqué ou coupé du jour au lendemain, sans remboursement pour les abonnés.</p>

<h2>Les risques d’un service non autorisé</h2>
<ul>
<li><strong>Arrêt soudain ou blocage par le fournisseur Internet.</strong></li>
<li><strong>Aucun soutien ni remboursement</strong>, car le vendeur peut disparaître.</li>
<li><strong>Risques de sécurité</strong> liés aux applications modifiées et aux listes gratuites, qui peuvent contenir des logiciels malveillants.</li>
<li><strong>Fraude au paiement</strong> : un vendeur encaisse et disparaît.</li>
</ul>
<p>Au Canada, les mesures se sont surtout concentrées sur les exploitants, les vendeurs et le blocage des services plutôt que sur les spectateurs, mais nous ne sommes pas avocats. Si vous avez besoin d’une certitude pour votre situation, consultez-en un.</p>

<h2>Comment vérifier un service IPTV avant de vous abonner</h2>
<ol>
<li><strong>Lisez les conditions d’utilisation.</strong> Une vraie entreprise publie ses conditions, sa politique de confidentialité et ses coordonnées.</li>
<li><strong>Demandez d’où vient le contenu.</strong> Un fournisseur qui peut expliquer ses sources vaut mieux qu’un fournisseur qui évite la question.</li>
<li><strong>Trouvez qui est derrière l’entreprise.</strong> Un site qui fonctionne, des coordonnées et un vrai soutien sont de bons signes. Un simple compte de médias sociaux n’en est pas un.</li>
<li><strong>Utilisez l’essai gratuit et la garantie de remboursement</strong> pour limiter vos risques.</li>
<li><strong>Évitez les applications piratées et les listes M3U « gratuites »</strong> trouvées sur des forums. Voyez notre page <a href="/liste-iptv-m3u/">liste IPTV M3U</a>.</li>
</ol>

<h2>Façons autorisées de regarder la télé au Canada</h2>
<p>Pour être certain que chaque chaîne est autorisée, les options sûres sont les forfaits de télé d’un fournisseur de télécommunications (Bell Fibe, Telus Optik et d’autres) ou des services de diffusion en continu autorisés comme Crave, ICI TOU.TV, CBC Gem et Club illico. Ils coûtent généralement plus cher et répartissent le contenu entre plusieurs abonnements. Comparez les coûts sur notre page <a href="/iptv-pas-cher/">IPTV pas cher</a>.</p>

<h2>Et IPTVMaple?</h2>
<p>IPTVMaple est un service d’abonnement IPTV indépendant. Nous publions nos <a href="/terms/">conditions d’utilisation</a>, notre <a href="/privacy/">politique de confidentialité</a> et notre <a href="/refund/">politique de remboursement</a>, et nous offrons un <a href="/try-iptv-canada/">essai gratuit de 24 heures</a> pour que vous puissiez voir le service avant de payer. Si vous avez des questions sur les droits, les licences ou nos conditions, écrivez à help@iptvmapletv.com avant d’acheter.</p>
<p>Pour comparer les services avec les mêmes critères, consultez aussi <a href="/meilleur-iptv/">le meilleur IPTV au Québec</a>. Version anglaise : <a href="/is-iptv-legal-in-canada/">Is IPTV legal in Canada?</a></p>
""",
        faq=[
            ("L’IPTV est-il légal au Canada?",
             "<p>L’IPTV en tant que technologie est légal au Canada. Les entreprises de télécommunications et les services de diffusion en continu l’utilisent tous les jours. Qu’un service précis soit légitime dépend de l’autorisation des titulaires de droits pour le contenu qu’il diffuse.</p>"),
            ("Est-il illégal de regarder l’IPTV au Canada?",
             "<p>Regarder un service autorisé est légal. La responsabilité d’un spectateur qui utilise un service non autorisé dépend des circonstances, et les mesures au Canada ont surtout visé les exploitants, les vendeurs et le blocage des services. Nous ne sommes pas avocats; consultez-en un si vous avez besoin d’une certitude.</p>"),
            ("Bell Fibe TV et Telus Optik sont-ils de l’IPTV?",
             "<p>Oui. Les deux diffusent la télévision par un réseau IP, ce qui correspond à la définition de l’IPTV. Ils sont autorisés parce que les entreprises ont des ententes avec les radiodiffuseurs.</p>"),
            ("Quels sont les risques d’un service IPTV non autorisé?",
             "<p>Les principaux risques sont un arrêt soudain ou un blocage par le fournisseur Internet, l’absence de soutien et de remboursement, les logiciels malveillants dans les applications et listes modifiées, et la fraude au paiement.</p>"),
            ("Comment vérifier qu’un fournisseur IPTV est sérieux?",
             "<p>Lisez ses conditions, sa politique de confidentialité et de remboursement, vérifiez qu’il a un vrai site avec des coordonnées, demandez d’où vient son contenu, et profitez de l’essai gratuit et de la garantie de remboursement.</p>"),
            ("Les listes IPTV M3U gratuites sont-elles légales?",
             "<p>Certaines listes pointent vers des flux publics gratuits et légitimes. La plupart des listes partagées sur les forums mènent à des chaînes non autorisées, cessent de fonctionner en quelques heures et peuvent vous exposer à des logiciels malveillants.</p>"),
        ],
        related=["abonnement-iptv", "meilleur-iptv", "liste-iptv-m3u"],
        cta_title="Testez avant de décider",
        keywords=["iptv légal", "iptv legale", "iptv légale", "iptv legal"],
    ),

    # ------------------------------------------------------------------ PAS CHER
    dict(
        slug="iptv-pas-cher", hub="fr", **D,
        title="IPTV pas cher au Québec : prix dès 9 $ (2026) | IPTVMaple",
        description="Combien coûte l’IPTV au Canada? Prix de 2026 dès 9 $, coût par écran, pièges de l’IPTV pas cher et comment payer moins. Essai gratuit de 24 h.",
        kicker="Guide des prix", h1='IPTV pas cher au Québec : <span class="grad-text">combien ça coûte vraiment</span>',
        lead="L’IPTV coûte une fraction du câble, mais les prix varient beaucoup d’un fournisseur à l’autre. Voici à quoi vous attendre et comment ne pas payer deux fois.",
        crumb="IPTV pas cher", blurb="Les prix de l’IPTV, par mois et par écran.",
        answer=f"<p><strong>L’IPTV coûte dès {LOW} $ pour un mois</strong> chez IPTVMaple, soit environ <strong>{PM} $ par mois</strong> avec le forfait de 12 mois pour un écran. Les écrans supplémentaires coûtent moins cher qu’un deuxième abonnement. Le câble et le satellite avec le sport coûtent couramment de 80 $ à 150 $ et plus par mois. Les prix sont en dollars américains.</p>",
        body=f"""
<h2>Les prix de l’IPTV en un coup d’œil</h2>
<p>Voici les prix actuels de tous les forfaits IPTVMaple. Chaque prix mène à la page de commande. Tous les forfaits incluent les chaînes, les films et séries, la 4K et les événements PPV; seuls le nombre d’écrans et la durée changent.</p>
{price_table(lang="fr")}
<p>Les prix sont en dollars américains et comprennent déjà le rabais de lancement de 50 %. Si vous payez avec une carte canadienne, votre banque convertit le montant. Comparez tous les forfaits sur la page <a href="/abonnement-iptv/">abonnement IPTV</a>.</p>

<h2>IPTV, câble ou applications : le coût mensuel</h2>
<table>
<thead><tr><th></th><th>Câble / satellite</th><th>Applications de diffusion</th><th>IPTV (IPTVMaple)</th></tr></thead>
<tbody>
<tr><td>Coût mensuel typique</td><td>80 $ à 150 $ et plus avec le sport</td><td>15 $ à 25 $ par application</td><td>dès {LOW} $; environ {PM} $/mois sur 12 mois</td></tr>
<tr><td>Contrat</td><td>Souvent</td><td>Non</td><td>Non</td></tr>
<tr><td>Chaînes québécoises en direct</td><td>Oui</td><td>Limité</td><td>Oui, en français et en anglais</td></tr>
<tr><td>Sport et PPV</td><td>Forfaits en supplément</td><td>Répartis entre les applications</td><td>Inclus</td></tr>
</tbody>
</table>
<p>Un ménage qui paie 110 $ par mois pour le câble dépense 1 320 $ par année. Un forfait IPTV de 12 mois pour trois écrans coûte {plan(3, 12)['price']} $ US pour toute l’année. Même après la conversion de devises, l’écart est important. Voyez aussi notre page sur <a href="/iptv-quebec/">l’IPTV au Québec</a>.</p>

<h2>Ce qui fait varier le prix</h2>
<ul>
<li><strong>Le nombre d’écrans en même temps</strong> : de 1 à 5 selon le forfait.</li>
<li><strong>La durée</strong> : le forfait de 12 mois a le plus bas prix par mois; un mois est la façon la moins chère d’essayer.</li>
<li><strong>Ce qui est inclus</strong> : chaînes québécoises et canadiennes, 4K, PPV, reprises et bibliothèque de films et séries.</li>
<li><strong>Le soutien</strong> : un vrai soutien 24/7 a un coût que n’a pas un revendeur à rabais.</li>
</ul>

<h2>IPTV pas cher : quand un prix trop bas est un signal d’alarme</h2>
<ul>
<li><strong>L’IPTV « à vie »</strong> pour un petit paiement unique : les serveurs coûtent de l’argent chaque mois, et ces offres disparaissent souvent.</li>
<li><strong>Aucun essai gratuit et aucune politique de remboursement écrite.</strong></li>
<li><strong>Paiement seulement par carte-cadeau</strong> ou par un compte de clavardage anonyme.</li>
<li><strong>Aucun site avec coordonnées</strong>, seulement un profil de médias sociaux.</li>
</ul>

<h2>Les autres coûts à prévoir</h2>
<ul>
<li><strong>Un appareil de diffusion</strong> si votre téléviseur n’est pas intelligent : voyez <a href="/iptv-sur-firestick/">l’IPTV sur Fire TV Stick</a>.</li>
<li><strong>Une mise à niveau facultative de l’application</strong> : <a href="/tivimate-en-francais/">TiviMate Premium</a> est vendu par le développeur de l’application; des applications gratuites fonctionnent avec tous les forfaits.</li>
<li><strong>Votre Internet</strong> : prévoyez environ 10 Mb/s en HD et 25 Mb/s par écran en 4K. Vous gardez votre fournisseur actuel.</li>
</ul>

<h2>Comment payer moins</h2>
<ol>
<li><strong>Commencez par l’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>.</strong> Il est gratuit et sans carte de crédit.</li>
<li><strong>Choisissez 12 mois si vous aimez le service.</strong> C’est le plus bas prix par mois, et la <a href="/refund/">garantie de remboursement de 7 jours</a> s’applique.</li>
<li><strong>Ajustez le nombre d’écrans à votre usage réel.</strong></li>
<li><strong>Profitez du programme de parrainage</strong> : quand un ami s’abonne pour 12 mois, vous recevez une année gratuite. Voir <a href="/refer-a-friend/">parrainez un ami</a> (en anglais).</li>
</ol>
<p>Prêt? <a href="/abonnement-iptv/">Voyez les forfaits</a> ou <a href="/try-iptv-canada/">essayez gratuitement</a>. Version anglaise : <a href="/iptv-price/">IPTV price in Canada</a>.</p>
""",
        faq=[
            ("Combien coûte l’IPTV par mois au Québec?",
             f"<p>Chez IPTVMaple, l’IPTV coûte {LOW} $ pour un mois sur un écran, ou environ {PM} $ par mois avec le forfait de 12 mois. Le prix augmente avec le nombre d’écrans qui regardent en même temps, jusqu’à cinq. Tous les prix sont en dollars américains.</p>"),
            ("Quel est le forfait IPTV le moins cher?",
             f"<p>Le plus bas coût mensuel est le forfait de 12 mois, environ {PM} $ par mois pour un écran. Le plus bas coût initial est le forfait d’un mois à {LOW} $. Les deux incluent les mêmes chaînes, films et séries.</p>"),
            ("Y a-t-il un essai gratuit?",
             "<p>Oui. IPTVMaple offre un essai gratuit de 24 heures avec accès complet et sans carte de crédit, pour tester votre téléviseur, votre connexion et vos chaînes avant de choisir un forfait.</p>"),
            ("Paie-t-on un supplément pour la 4K ou le sport?",
             "<p>Non. Tous les forfaits incluent la 4K, les forfaits sportifs et les événements PPV comme l’UFC, la boxe et la F1. Le prix dépend seulement du nombre d’écrans et de la durée.</p>"),
            ("Peut-on obtenir un remboursement?",
             "<p>Oui. Chaque achat est couvert par une garantie de remboursement de 7 jours. Les détails sont sur la page de la <a href=\"/refund/\">politique de remboursement</a>.</p>"),
        ],
        related=["abonnement-iptv", "meilleur-iptv", "iptv-quebec"],
        cta_title="Voyez le prix, puis testez",
        keywords=["iptv pas cher", "iptv prix", "prix iptv", "iptv prix canada", "tivimate premium prix", "tivimate premium prix", "iptv promo"],
    ),

    # ------------------------------------------------------------------ NE FONCTIONNE PLUS
    dict(
        slug="iptv-ne-fonctionne-plus", hub="fr", **D,
        title="IPTV qui ne fonctionne plus : 10 solutions | IPTVMaple",
        description="Votre IPTV ne fonctionne plus, se bloque ou saccade? 10 solutions testées : Wi-Fi, vitesse, réglages de l’application, DNS et quoi dire au soutien.",
        kicker="Dépannage", h1='IPTV qui ne fonctionne plus : <span class="grad-text">10 solutions</span>',
        lead="La plupart des problèmes d’IPTV ont une cause simple. Suivez ces étapes dans l’ordre et vous réglerez presque tout en moins d’une demi-heure.",
        crumb="IPTV ne fonctionne plus", blurb="Dix solutions quand l’IPTV se bloque, saccade ou ne démarre plus.",
        answer="<p><strong>Quand l’IPTV ne fonctionne plus, la cause est le plus souvent votre Wi-Fi ou votre appareil, pas le service.</strong> Redémarrez le routeur et l’appareil, branchez-le par câble Ethernet ou utilisez le Wi-Fi 5 GHz, vérifiez que vous avez environ 10 Mb/s en HD ou 25 Mb/s en 4K par écran, puis vérifiez vos identifiants dans l’application. Si une seule chaîne est touchée, avisez le soutien avec le nom de la chaîne et l’heure.</p>",
        body="""
<h2>Quel est votre problème?</h2>
<table>
<thead><tr><th>Ce que vous voyez</th><th>Cause probable</th><th>Première solution</th></tr></thead>
<tbody>
<tr><td>Rien ne démarre, message d’erreur</td><td>Identifiants ou URL incorrects, abonnement expiré</td><td>Recopiez les identifiants; vérifiez la date d’échéance</td></tr>
<tr><td>Toutes les chaînes saccadent</td><td>Wi-Fi ou vitesse Internet</td><td>Ethernet ou Wi-Fi 5 GHz; test de vitesse</td></tr>
<tr><td>Seules les chaînes 4K saccadent</td><td>Pas assez de vitesse pour la 4K</td><td>Choisissez la version HD de la chaîne</td></tr>
<tr><td>Ça saccade le soir seulement</td><td>Congestion chez le fournisseur Internet</td><td>Changez de DNS; réessayez plus tard</td></tr>
<tr><td>Une seule chaîne est figée</td><td>Source de cette chaîne</td><td>Avisez le soutien (nom de la chaîne, heure)</td></tr>
<tr><td>« IPTV bloqué » ou chaînes qui ne chargent pas</td><td>Blocage par le fournisseur Internet, DNS</td><td>Changez de DNS; testez avec et sans VPN</td></tr>
<tr><td>L’application plante</td><td>Mémoire ou antémémoire pleine</td><td>Videz l’antémémoire; réinstallez</td></tr>
</tbody>
</table>

<h2>Les 10 solutions</h2>
<h3>1. Vérifiez vos identifiants</h3>
<p>Recopiez l’URL du serveur, le nom d’utilisateur et le mot de passe à partir du message que nous vous avons envoyé. Une espace en trop ou une majuscule mal placée suffit à causer une erreur. Vérifiez aussi que votre abonnement n’est pas échu.</p>
<h3>2. Redémarrez tout</h3>
<p>Débranchez le modem, le routeur et l’appareil de diffusion pendant 30 secondes, puis rebranchez le modem en premier.</p>
<h3>3. Testez votre vitesse Internet</h3>
<p>Prévoyez environ 10 Mb/s pour un flux HD et 25 Mb/s pour un flux 4K, <em>par écran</em>. Faites le test sur l’appareil qui pose problème.</p>
<h3>4. Utilisez un câble Ethernet ou le Wi-Fi 5 GHz</h3>
<p>Une connexion filaire est la plus grande amélioration possible. Pour un Fire TV Stick, un adaptateur Ethernet coûte peu. Sinon, choisissez le réseau 5 GHz et rapprochez le routeur.</p>
<h3>5. Mettez le reste en pause</h3>
<p>Téléchargements, sauvegardes en ligne, mises à jour de jeux et appels vidéo concurrencent votre flux.</p>
<h3>6. Augmentez la mémoire tampon de l’application</h3>
<p>Dans TiviMate : Paramètres → Lecture → taille de la mémoire tampon, « Moyenne » ou « Grande ». Dans IPTV Smarters Pro : essayez un autre lecteur dans les paramètres.</p>
<h3>7. Choisissez la chaîne en HD plutôt qu’en 4K</h3>
<p>Si la 4K saccade mais pas la HD, votre connexion ne soutient pas la 4K à ce moment-là.</p>
<h3>8. Videz l’antémémoire ou réinstallez l’application</h3>
<p>Sur Fire TV : Paramètres → Applications → Gérer les applications installées → choisissez l’application → Vider l’antémémoire.</p>
<h3>9. Changez de DNS et testez avec ou sans VPN</h3>
<p>Un DNS public comme 1.1.1.1 (Cloudflare) ou 8.8.8.8 (Google) règle parfois le chargement lent des chaînes. Un VPN aide parfois si votre fournisseur Internet ralentit le vidéo, mais il peut aussi ralentir. Testez les deux.</p>
<h3>10. Écrivez au soutien avec les bons détails</h3>
<p>Donnez le nom de la chaîne, l’heure du problème, votre appareil et votre application, ainsi que le résultat de votre test de vitesse. Notre équipe répond jour et nuit sur WhatsApp et par courriel.</p>

<h2>Comment IPTVMaple limite les blocages</h2>
<p>Tous les forfaits utilisent une technologie anti-blocage pour garder le sport en direct fluide aux heures de pointe. Testez-la vous-même avec l’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>. Si un problème technique rend le service inutilisable et que nous ne le réglons pas en 48 heures, la <a href="/refund/">politique de remboursement</a> s’applique.</p>
<p>Plus de détails en anglais : <a href="/iptv-buffering-fix/">IPTV buffering fixes</a>. Installation : <a href="/iptv-sur-smart-tv/">IPTV sur votre appareil</a>.</p>
""",
        faq=[
            ("Pourquoi mon IPTV ne fonctionne-t-il plus?",
             "<p>Les causes les plus fréquentes sont des identifiants mal saisis, un abonnement échu, un Wi-Fi faible ou une vitesse Internet insuffisante. Vérifiez vos identifiants, redémarrez le routeur et l’appareil, puis testez avec un câble Ethernet.</p>"),
            ("Pourquoi l’IPTV saccade-t-il le soir?",
             "<p>Le soir, beaucoup de foyers diffusent en même temps, et le réseau de votre fournisseur Internet peut être congestionné. Utilisez une connexion filaire, choisissez des chaînes HD plutôt que 4K et essayez un DNS public.</p>"),
            ("De quelle vitesse Internet ai-je besoin?",
             "<p>Environ 10 Mb/s pour un flux HD et 25 Mb/s pour un flux 4K, par écran qui regarde en même temps. Additionnez les flux si plusieurs écrans sont allumés.</p>"),
            ("Mon fournisseur Internet bloque l’IPTV, que faire?",
             "<p>Essayez un DNS public (1.1.1.1 ou 8.8.8.8), puis testez avec et sans VPN. Si les chaînes ne se chargent toujours pas, écrivez au soutien avec le message d’erreur.</p>"),
            ("Le problème vient-il du fournisseur ou de chez moi?",
             "<p>Si toutes vos applications sont lentes, le problème vient de votre connexion. Si les autres applications sont fluides et qu’une chaîne ou tout l’IPTV se fige, écrivez au soutien avec la chaîne, l’heure et l’appareil.</p>"),
        ],
        related=["iptv-sur-smart-tv", "abonnement-iptv", "tivimate-en-francais"],
        cta_title="Un service testé avant de payer",
        keywords=["iptv ne fonctionne plus", "iptv bloqué", "iptv ne marche plus", "iptv bloque"],
    ),

    # ------------------------------------------------------------------ LECTEUR IPTV
    dict(
        slug="lecteur-iptv", hub="fr", **D,
        title="Meilleur lecteur IPTV : Android, Fire TV, iPhone | IPTVMaple",
        description="Le meilleur lecteur IPTV pour chaque appareil : Android, Fire TV, Samsung, LG, iPhone, Apple TV, PC et Mac. Comparatif et comment ajouter vos identifiants.",
        kicker="Comparatif", h1='Meilleur <span class="grad-text">lecteur IPTV</span> pour chaque appareil',
        lead="Un lecteur IPTV est l’application qui affiche vos chaînes. Voici le meilleur choix selon votre appareil et comment l’utiliser avec votre abonnement.",
        crumb="Lecteur IPTV", blurb="Le meilleur lecteur IPTV pour chaque appareil.",
        answer="<p><strong>Le meilleur lecteur IPTV dépend de votre appareil.</strong> Sur Fire TV Stick et Android TV, TiviMate est le plus agréable pour la télé en direct. Sur téléphone, tablette et ordinateur, IPTV Smarters Pro est simple et gratuit. Sur iPhone et Apple TV, utilisez Smarters Player Lite ou iPlayTV. Sur Samsung et LG, choisissez une application de la boutique du téléviseur, comme Smart IPTV ou Flix IPTV. Sur ordinateur, VLC suffit pour un lien M3U.</p>",
        body="""
<h2>Quel lecteur pour quel appareil?</h2>
<table>
<thead><tr><th>Appareil</th><th>Lecteur recommandé</th><th>Guide</th></tr></thead>
<tbody>
<tr><td>Fire TV Stick</td><td>TiviMate, IPTV Smarters Pro</td><td><a href="/iptv-sur-firestick/">IPTV sur Fire TV Stick</a></td></tr>
<tr><td>Android TV, Google TV, Nvidia Shield</td><td>TiviMate</td><td><a href="/tivimate-en-francais/">TiviMate en français</a></td></tr>
<tr><td>Téléphone et tablette Android</td><td>IPTV Smarters Pro, XCIPTV</td><td><a href="/iptv-smarters-pro-francais/">Smarters Pro en français</a></td></tr>
<tr><td>Samsung et LG</td><td>Smart IPTV, Flix IPTV, SmartOne, Smarters Player Lite</td><td><a href="/iptv-sur-samsung/">IPTV sur Samsung et LG</a></td></tr>
<tr><td>iPhone, iPad, Apple TV</td><td>Smarters Player Lite, iPlayTV</td><td><a href="/iptv-sur-apple-tv-iphone/">IPTV sur Apple TV et iPhone</a></td></tr>
<tr><td>Windows et Mac</td><td>IPTV Smarters Pro, VLC, Kodi</td><td><a href="/iptv-sur-pc-mac/">IPTV sur PC et Mac</a></td></tr>
<tr><td>Boîtier MAG ou Formuler</td><td>Portail intégré, MyTVOnline</td><td><a href="/mag-box-iptv/">Boîtiers MAG</a> (en anglais)</td></tr>
</tbody>
</table>

<h2>Ce qu’il faut chercher dans un lecteur IPTV</h2>
<ul>
<li><strong>Le guide télé (EPG)</strong> : une grille claire, avec les heures dans votre fuseau horaire.</li>
<li><strong>Les types d’identifiants</strong> : Xtream Codes, lien M3U, ou portail pour les boîtiers.</li>
<li><strong>Les groupes de chaînes</strong> : pouvoir masquer ce que vous ne regardez pas.</li>
<li><strong>Les favoris</strong> et les reprises (catch-up) quand la chaîne les offre.</li>
<li><strong>La stabilité</strong> sur votre appareil. Un lecteur léger est plus fluide sur un vieux Fire TV Stick.</li>
</ul>

<h2>Xtream Codes ou lien M3U?</h2>
<p>Avec <strong>Xtream Codes</strong>, vous entrez trois éléments (URL du serveur, nom d’utilisateur, mot de passe) et le guide, les films et les séries se chargent automatiquement. Avec un <strong>lien M3U</strong>, l’application lit une liste de chaînes; le guide peut demander un lien supplémentaire (EPG). Quand c’est possible, choisissez Xtream Codes. Plus de détails sur la page <a href="/liste-iptv-m3u/">liste IPTV M3U</a>.</p>

<h2>Comment ajouter vos identifiants IPTVMaple</h2>
""" + LOGIN_FR + """
<ol>
<li>Installez le lecteur choisi depuis une source officielle.</li>
<li>Choisissez « Xtream Codes » (ou « M3U »).</li>
<li>Entrez l’URL du serveur, le nom d’utilisateur et le mot de passe tels que reçus.</li>
<li>Attendez le chargement des chaînes et du guide.</li>
</ol>

<h2>Les pièges à éviter</h2>
<ul>
<li>Les versions « modifiées » ou « premium débloqué » : elles peuvent contenir des logiciels malveillants.</li>
<li>Les sites qui lisent votre lien M3U « en ligne » : votre lien contient votre mot de passe.</li>
</ul>
<p>Guide complet en anglais : <a href="/iptv-apps/">best IPTV apps and players</a>. Besoin d’identifiants pour tester? Essayez l’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>.</p>
""",
        faq=[
            ("Quel est le meilleur lecteur IPTV?",
             "<p>TiviMate sur Fire TV Stick et Android TV pour la télé en direct, IPTV Smarters Pro sur téléphone, tablette et ordinateur, Smarters Player Lite ou iPlayTV sur Apple, et une application de la boutique du téléviseur sur Samsung et LG.</p>"),
            ("Quel est le meilleur lecteur IPTV pour Android?",
             "<p>Pour un téléviseur Android ou un Fire TV Stick, TiviMate. Pour un téléphone ou une tablette Android, IPTV Smarters Pro ou XCIPTV, qui sont gratuits.</p>"),
            ("Un lecteur IPTV inclut-il des chaînes?",
             "<p>Non. Le lecteur est seulement l’application. Les chaînes viennent de votre abonnement IPTV, que vous ajoutez avec vos identifiants.</p>"),
            ("Peut-on lire une liste M3U en ligne?",
             "<p>C’est possible sur certains sites, mais déconseillé : votre lien M3U contient votre nom d’utilisateur et votre mot de passe. Utilisez plutôt une application installée depuis une source officielle, ou VLC.</p>"),
            ("Quel lecteur choisir pour un vieux Fire TV Stick?",
             "<p>Un lecteur léger comme IPTV Smarters Pro, et masquez les groupes de chaînes que vous ne regardez pas pour accélérer l’application.</p>"),
        ],
        related=["iptv-sur-smart-tv", "tivimate-en-francais", "iptv-smarters-pro-francais"],
        cta_title="Essayez avec un vrai service",
        keywords=["lecteur iptv", "meilleur lecteur iptv", "meilleur lecteur iptv android", "lecteur m3u en ligne", "ip player", "iptv player", "player m3u", "iptv player m3u"],
    ),

    # ------------------------------------------------------------------ LISTE M3U
    dict(
        slug="liste-iptv-m3u", hub="fr", **D,
        title="Liste IPTV M3U : fonctionnement et pièges | IPTVMaple",
        description="Qu’est-ce qu’une liste IPTV M3U? Comment l’utiliser avec VLC, Kodi et TiviMate, pourquoi les listes gratuites posent problème et quoi utiliser plutôt.",
        kicker="Guide pratique", h1='Liste IPTV M3U : <span class="grad-text">comment ça marche</span> (et quoi éviter)',
        lead="Une liste M3U est un simple fichier texte qui indique à une application où trouver vos chaînes. Voici comment l’utiliser, et pourquoi les listes gratuites trouvées en ligne sont risquées.",
        crumb="Liste IPTV M3U", blurb="Ce qu’est une liste M3U, comment l’utiliser et quoi éviter.",
        answer="<p><strong>Une liste IPTV M3U est un fichier ou un lien qui contient les adresses des chaînes</strong> et leur nom. Vous l’ouvrez dans un lecteur comme VLC, Kodi ou TiviMate. Un lien M3U fourni par votre abonnement contient votre nom d’utilisateur et votre mot de passe : ne le partagez pas. Les listes gratuites trouvées sur les forums cessent souvent de fonctionner en quelques heures et peuvent mener à des contenus non autorisés ou à des sites dangereux.</p>",
        body="""
<h2>Qu’est-ce qu’une liste M3U?</h2>
<p>M3U (et sa variante M3U8) est un format de liste de lecture. Chaque ligne indique un nom de chaîne, parfois un logo et un groupe, puis l’adresse du flux. Les lecteurs IPTV lisent cette liste et affichent vos chaînes. Une liste M3U ne contient pas de vidéo : elle ne fait que pointer vers elle.</p>

<h2>M3U, M3U8 et Xtream Codes</h2>
<table>
<thead><tr><th></th><th>Lien M3U / M3U8</th><th>Xtream Codes</th></tr></thead>
<tbody>
<tr><td>Ce que vous entrez</td><td>Un lien ou un fichier</td><td>URL du serveur, nom d’utilisateur, mot de passe</td></tr>
<tr><td>Guide télé (EPG)</td><td>Souvent un lien séparé</td><td>Automatique</td></tr>
<tr><td>Films et séries</td><td>Dans la liste, sans classement</td><td>Classés par catégories</td></tr>
<tr><td>Meilleur pour</td><td>VLC, Kodi, essais rapides</td><td>TiviMate, IPTV Smarters Pro</td></tr>
</tbody>
</table>

<h2>Comment utiliser une liste M3U</h2>
<h3>Avec VLC</h3>
<ol>
<li>Ouvrez VLC et choisissez <strong>Média → Ouvrir un flux réseau</strong> (sur Mac : <strong>Fichier → Ouvrir un réseau</strong>).</li>
<li>Collez le lien M3U et cliquez sur <strong>Lire</strong>.</li>
<li>Ouvrez la liste de lecture (Ctrl + L) pour choisir une chaîne.</li>
</ol>
<h3>Avec Kodi</h3>
<p>Installez le module <em>PVR IPTV Simple Client</em>, puis entrez le lien M3U (et le lien EPG) dans ses paramètres.</p>
<h3>Avec TiviMate ou IPTV Smarters Pro</h3>
<p>Choisissez « Ajouter une liste » puis « M3U », ou préférez « Xtream Codes » si vous avez les trois identifiants. Voyez <a href="/lecteur-iptv/">le meilleur lecteur IPTV</a>.</p>

<h2>Pourquoi éviter les listes M3U gratuites</h2>
<ul>
<li><strong>Elles cessent de fonctionner</strong> rapidement : les liens expirent ou sont fermés.</li>
<li><strong>Beaucoup de chaînes sont mortes</strong> ou de mauvaise qualité.</li>
<li><strong>Elles peuvent mener à des contenus non autorisés.</strong> Voyez <a href="/iptv-legal-canada/">l’IPTV est-il légal au Canada?</a></li>
<li><strong>Elles peuvent exposer votre appareil</strong> à des sites et des fichiers dangereux.</li>
</ul>

<h2>Protégez votre lien M3U</h2>
<p>Votre lien M3U contient votre nom d’utilisateur et votre mot de passe. N’y touchez pas sur des sites qui offrent de « lire votre M3U en ligne » ou de « vérifier votre IPTV » : ils peuvent conserver votre lien. Si vous l’avez fait, demandez à votre fournisseur de changer votre mot de passe.</p>

<h2>Obtenir un lien M3U fiable</h2>
<p>Avec IPTVMaple, votre lien M3U et vos identifiants Xtream Codes arrivent par courriel et par WhatsApp après votre commande ou votre <a href="/try-iptv-canada/">essai gratuit de 24 heures</a>. Voyez aussi notre explication en anglais : <a href="/m3u-playlist/">what is an M3U playlist?</a></p>
""",
        faq=[
            ("Qu’est-ce qu’une liste M3U?",
             "<p>Une liste M3U est un fichier texte qui contient les adresses et les noms des chaînes. Un lecteur comme VLC, Kodi ou TiviMate la lit pour afficher vos chaînes. Elle ne contient pas de vidéo.</p>"),
            ("Quelle est la différence entre M3U et Xtream Codes?",
             "<p>Une liste M3U est un lien ou un fichier. Xtream Codes est un type d’identifiants (URL, nom d’utilisateur, mot de passe) qui charge automatiquement le guide télé et classe les films et séries.</p>"),
            ("Où trouver une liste IPTV M3U gratuite et fiable?",
             "<p>Les listes gratuites partagées en ligne sont généralement peu fiables et cessent vite de fonctionner. Pour un service stable, utilisez le lien fourni par votre abonnement. Un essai gratuit permet de tester sans payer.</p>"),
            ("Mon lien M3U ne fonctionne pas dans le navigateur. Pourquoi?",
             "<p>Les navigateurs ne lisent pas directement les listes M3U ni les flux MPEG-TS. Ouvrez le lien dans VLC ou dans une application IPTV.</p>"),
            ("Est-ce sûr de coller mon lien M3U sur un site?",
             "<p>Non. Le lien contient votre nom d’utilisateur et votre mot de passe. Utilisez une application installée depuis une source officielle.</p>"),
        ],
        related=["lecteur-iptv", "iptv-sur-smart-tv", "iptv-legal-canada"],
        cta_title="Un lien M3U qui fonctionne",
        keywords=["liste m3u", "liste m3u iptv", "liste iptv m3u fr", "iptv liste", "liste iptv", "m3u lista", "iptv listas m3u", "iptv liste", "m3u8 list", "m3u list", "iptv list",
                  "m3u iptv", "m3u ip tv", "ip tv m3u", "iptv m3u", "iptv m3u list", "iptv play list", "play list iptv", "tv m3u", "m3u", "m3u8 iptv", "m3u8 tv", "iptv m3u8",
                  "list iptv", "ip tv list", "vod m3u", "m3u vod", "m3u premium", "kodi m3u", "m3u kodi", "iptv mu3", "mu3 iptv", "playlist iptv"],
    ),

    # ------------------------------------------------------------------ SMARTERS EN FRANÇAIS
    dict(
        slug="iptv-smarters-pro-francais", hub="fr", **D,
        title="IPTV Smarters Pro en français : installation | IPTVMaple",
        description="Installer IPTV Smarters Pro (parfois écrit « Smasters ») sur Android, Fire TV, iPhone, Samsung, LG, PC et Mac. Identifiants Xtream Codes et dépannage.",
        kicker="Guide d’installation", h1='IPTV Smarters Pro <span class="grad-text">en français</span> : installation et aide',
        lead="IPTV Smarters Pro est l’un des lecteurs IPTV les plus populaires. Voici où le trouver, comment vous connecter et quoi faire quand ça ne marche pas.",
        crumb="Smarters Pro en français", blurb="Installer IPTV Smarters Pro et régler les problèmes courants.",
        answer="<p><strong>IPTV Smarters Pro est une application gratuite pour lire votre abonnement IPTV</strong> (on l’écrit parfois « Smasters » par erreur). Installez-la depuis une source officielle, choisissez « Connexion avec l’API Xtream Codes », puis entrez un nom, votre nom d’utilisateur, votre mot de passe et l’URL du serveur. Elle existe pour Android, Fire TV, Windows et Mac; sur iPhone et Apple TV, elle s’appelle Smarters Player Lite.</p>",
        body="""
<h2>Où installer IPTV Smarters Pro?</h2>
<table>
<thead><tr><th>Appareil</th><th>Où l’obtenir</th></tr></thead>
<tbody>
<tr><td>Téléphone et tablette Android</td><td>Google Play si l’application y est offerte dans votre pays; sinon le fichier APK du site officiel</td></tr>
<tr><td>Android TV, Google TV</td><td>Google Play sur le téléviseur ou l’APK officiel</td></tr>
<tr><td>Fire TV Stick</td><td>Application Downloader avec l’adresse officielle du site d’IPTV Smarters</td></tr>
<tr><td>iPhone, iPad, Apple TV</td><td>App Store, sous le nom Smarters Player Lite</td></tr>
<tr><td>Samsung et LG</td><td>Boutique du téléviseur : cherchez « Smarters »</td></tr>
<tr><td>Windows et Mac</td><td>Le site officiel d’IPTV Smarters ou la boutique de votre système</td></tr>
</tbody>
</table>
<p>Téléchargez toujours l’application à partir du site du développeur ou d’une boutique officielle. Évitez les versions « modifiées » ou « premium débloqué ».</p>

<h2>Se connecter avec vos identifiants</h2>
""" + LOGIN_FR + """
<ol>
<li>Ouvrez l’application et choisissez <strong>Connexion avec l’API Xtream Codes</strong> (ou « Login with Xtream Codes API »).</li>
<li>Entrez un nom quelconque, par exemple « IPTVMaple ».</li>
<li>Entrez le nom d’utilisateur, le mot de passe et l’URL du serveur tels que reçus (copiez-collez si possible).</li>
<li>Appuyez sur <strong>Ajouter l’utilisateur</strong>. Les chaînes, les films, les séries et le guide se chargent.</li>
</ol>

<h2>Problèmes fréquents</h2>
<h3>IPTV Smarters Pro est introuvable sur Google Play</h3>
<p>La disponibilité varie selon les pays et le temps. Installez le fichier APK à partir du site officiel d’IPTV Smarters, ou utilisez un autre lecteur offert sur Google Play, comme <a href="/tivimate-en-francais/">TiviMate</a> sur Android TV.</p>
<h3>Ça ne fonctionne pas sur ma télé Samsung</h3>
<p>Vérifiez d’abord que le téléviseur est à jour et que l’application est offerte dans la boutique de votre pays. Sur Samsung, l’application s’appelle généralement « Smarters Player Lite ». Si elle est absente, utilisez Smart IPTV, Flix IPTV ou SmartOne, ou branchez un Fire TV Stick. Voyez <a href="/iptv-sur-samsung/">l’IPTV sur Samsung et LG</a>.</p>
<h3>Je veux l’utiliser sur mon ordinateur</h3>
<p>Installez la version Windows ou Mac depuis le site officiel, ou ouvrez votre lien M3U dans VLC. Voyez <a href="/iptv-sur-pc-mac/">l’IPTV sur PC et Mac</a>.</p>
<h3>« Nom d’utilisateur ou mot de passe invalide »</h3>
<p>Recopiez les identifiants sans espace ni faute de majuscule. Si l’erreur continue, écrivez-nous sur WhatsApp avec une capture d’écran.</p>
<h3>Ça saccade</h3>
<p>Utilisez un câble Ethernet ou le Wi-Fi 5 GHz. Voyez <a href="/iptv-ne-fonctionne-plus/">10 solutions quand l’IPTV ne fonctionne plus</a>.</p>

<h2>Smarters Pro ou TiviMate?</h2>
<p>Smarters Pro est gratuit, simple et fonctionne partout. TiviMate offre le plus beau guide télé, mais seulement sur Android TV et Fire TV. Beaucoup de gens utilisent les deux avec les mêmes identifiants. Comparaison en anglais : <a href="/iptv-smarters-pro/">IPTV Smarters Pro setup guide</a>.</p>
""",
        faq=[
            ("IPTV Smarters Pro est-il gratuit?",
             "<p>L’application est gratuite. Elle ne contient pas de chaînes : il vous faut un abonnement IPTV, comme IPTVMaple, pour avoir la télé en direct, les films et les séries.</p>"),
            ("Pourquoi IPTV Smarters Pro est-il introuvable sur Google Play?",
             "<p>La disponibilité varie selon le pays et change avec le temps. Installez le fichier APK officiel à partir du site d’IPTV Smarters, ou utilisez un autre lecteur offert sur Google Play.</p>"),
            ("IPTV Smarters Pro fonctionne-t-il sur Samsung?",
             "<p>Souvent oui, sous le nom Smarters Player Lite, selon le modèle et le pays. S’il est absent, essayez Smart IPTV, Flix IPTV ou SmartOne, ou branchez un Fire TV Stick au téléviseur.</p>"),
            ("Quelle est la différence entre « Smasters » et « Smarters »?",
             "<p>Il s’agit de la même application. « Smasters » est une faute de frappe courante dans les recherches. Le nom correct est IPTV Smarters Pro.</p>"),
            ("Comment installer IPTV Smarters Pro sur PC?",
             "<p>Téléchargez la version Windows ou Mac depuis le site officiel d’IPTV Smarters, installez-la et connectez-vous avec Xtream Codes. VLC est une autre option simple.</p>"),
        ],
        related=["tivimate-en-francais", "iptv-sur-smart-tv", "lecteur-iptv"],
        cta_title="Prêt à vous connecter?",
        keywords=["iptv smasters pro pour pc", "iptv smasters pro sur pc", "smasters player lite télécharger", "iptv smasters pro introuvable google play",
                  "iptv smasters pro ne fonctionne pas sur tv samsung", "smarters player lite sur tv samsung", "iptv smasters pro pc fr"],
    ),

    # ------------------------------------------------------------------ SUR SAMSUNG / LG
    dict(
        slug="iptv-sur-samsung", hub="fr", **D,
        title="IPTV sur Samsung et LG : installation pas à pas | IPTVMaple",
        description="Installer l’IPTV sur un téléviseur Samsung ou LG : quelle application choisir, comment entrer vos identifiants et quoi faire si l’application est introuvable.",
        kicker="Installation", h1='IPTV sur <span class="grad-text">Samsung et LG</span> : installation pas à pas',
        lead="Les téléviseurs Samsung (Tizen) et LG (webOS) ont leurs propres boutiques d’applications. Voici comment choisir l’application et vous connecter.",
        crumb="IPTV sur Samsung et LG", blurb="Choisir l’application et installer l’IPTV sur Samsung et LG.",
        answer="<p><strong>Sur Samsung et LG, installez une application IPTV depuis la boutique du téléviseur</strong> : Smart IPTV, Flix IPTV, SmartOne IPTV ou Smarters Player Lite. Selon l’application, vous entrez vos identifiants Xtream Codes directement ou vous associez l’adresse MAC du téléviseur à votre lien M3U sur le site de l’application. Si aucune application ne fonctionne sur votre modèle, branchez un Fire TV Stick à l’entrée HDMI.</p>",
        body="""
<h2>Quelle application choisir?</h2>
<table>
<thead><tr><th>Application</th><th>Comment ça fonctionne</th><th>À savoir</th></tr></thead>
<tbody>
<tr><td>Smarters Player Lite</td><td>Connexion directe avec Xtream Codes</td><td>Disponibilité selon le modèle et le pays</td></tr>
<tr><td>Smart IPTV (SIPTV)</td><td>Adresse MAC + lien M3U sur le site de l’application</td><td>Activation payante unique, selon l’éditeur</td></tr>
<tr><td>Flix IPTV</td><td>Adresse MAC + lien M3U sur le site de l’application</td><td>Essai puis activation, selon l’éditeur</td></tr>
<tr><td>SmartOne IPTV</td><td>Adresse MAC + lien M3U</td><td>Disponible sur Samsung, LG et Android</td></tr>
</tbody>
</table>
<p>Les conditions d’activation (essai, prix) sont fixées par chaque éditeur et peuvent changer : vérifiez-les sur son site. IPTVMaple ne vend pas ces activations.</p>

<h2>Installer sur un téléviseur Samsung</h2>
<ol>
<li>Appuyez sur <strong>Accueil</strong> et ouvrez <strong>Apps</strong>.</li>
<li>Cherchez l’application choisie (par exemple « Smarters » ou « Smart IPTV ») et installez-la.</li>
<li>Ouvrez-la. Selon l’application, connectez-vous avec Xtream Codes, ou notez l’<strong>adresse MAC</strong> affichée.</li>
</ol>

<h2>Installer sur un téléviseur LG</h2>
<ol>
<li>Appuyez sur <strong>Accueil</strong> et ouvrez le <strong>LG Content Store</strong>.</li>
<li>Cherchez l’application, installez-la, puis lancez-la.</li>
<li>Connectez-vous avec Xtream Codes, ou notez l’adresse MAC affichée.</li>
</ol>

<h2>Entrer vos identifiants IPTVMaple</h2>
""" + LOGIN_FR + """
<p>Pour les applications avec <strong>adresse MAC</strong> : sur le site de l’application, entrez l’adresse MAC et collez votre lien M3U, puis redémarrez l’application sur le téléviseur. Pour celles avec <strong>Xtream Codes</strong> : choisissez cette option et entrez l’URL du serveur, le nom d’utilisateur et le mot de passe.</p>

<h2>Si l’application est introuvable ou ne fonctionne pas</h2>
<ul>
<li><strong>Mettez le téléviseur à jour</strong> (Paramètres → Assistance → Mise à jour du logiciel).</li>
<li><strong>Vérifiez l’âge du modèle.</strong> Les téléviseurs trop anciens n’offrent pas les applications récentes.</li>
<li><strong>Essayez une autre application</strong> de la même boutique.</li>
<li><strong>Branchez un Fire TV Stick</strong> : c’est souvent plus rapide. Voyez <a href="/iptv-sur-firestick/">IPTV sur Fire TV Stick</a>.</li>
<li><strong>Ça saccade?</strong> Un câble Ethernet au téléviseur aide beaucoup. Voyez <a href="/iptv-ne-fonctionne-plus/">les solutions</a>.</li>
</ul>
<p>Plus de détails (en anglais) : <a href="/iptv-samsung-tv/">IPTV on Samsung TV</a> et <a href="/iptv-lg-tv/">IPTV on LG TV</a>. Essayez d’abord avec l’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>.</p>
""",
        faq=[
            ("Comment installer l’IPTV sur une télé Samsung?",
             "<p>Installez une application IPTV depuis la boutique d’applications Samsung, ouvrez-la, puis entrez vos identifiants Xtream Codes ou associez l’adresse MAC du téléviseur à votre lien M3U sur le site de l’application.</p>"),
            ("Quelle est la meilleure application IPTV pour LG?",
             "<p>Smarters Player Lite, Smart IPTV, Flix IPTV et SmartOne IPTV sont des choix courants dans le LG Content Store. Le meilleur dépend de votre modèle; essayez-en une, puis une autre si elle est absente.</p>"),
            ("Où trouver l’adresse MAC de mon téléviseur?",
             "<p>La plupart des applications IPTV affichent l’adresse MAC à l’ouverture. Vous pouvez aussi la trouver dans les paramètres réseau du téléviseur.</p>"),
            ("Mon application IPTV est introuvable sur Samsung, que faire?",
             "<p>Mettez le téléviseur à jour, essayez une autre application de la boutique ou branchez un Fire TV Stick à l’entrée HDMI.</p>"),
            ("Peut-on installer TiviMate sur une télé Samsung ou LG?",
             "<p>Non. TiviMate fonctionne seulement sur Android TV et Fire TV. Branchez un Fire TV Stick au téléviseur si vous voulez l’utiliser.</p>"),
        ],
        related=["iptv-sur-smart-tv", "iptv-sur-firestick", "iptv-smarters-pro-francais"],
        cta_title="Testez sur votre téléviseur",
        keywords=["iptv sur samsung", "iptv sur tv samsung", "iptv samsung smart tv", "iptv samsung", "iptv lg", "iptv lg smart", "iptv lg tv", "iptv lg webos", "iptv sony",
                  "smart iptv sony", "iptv hisense", "vidaa iptv", "iptv smart tv", "ip tv smart tv"],
    ),

    # ------------------------------------------------------------------ SUR APPLE TV / IPHONE
    dict(
        slug="iptv-sur-apple-tv-iphone", hub="fr", **D,
        title="IPTV sur Apple TV et iPhone : installation | IPTVMaple",
        description="IPTV sur Apple TV, iPhone et iPad : quelles applications utiliser (Smarters Player Lite, iPlayTV), comment vous connecter et que faire en cas de problème.",
        kicker="Installation", h1='IPTV sur <span class="grad-text">Apple TV, iPhone et iPad</span>',
        lead="Les appareils Apple n’utilisent pas les mêmes applications qu’Android. Voici lesquelles choisir et comment vous connecter.",
        crumb="IPTV sur Apple TV et iPhone", blurb="Les applications IPTV pour Apple TV, iPhone et iPad.",
        answer="<p><strong>Sur Apple TV, iPhone et iPad, utilisez Smarters Player Lite ou iPlayTV</strong>, offertes dans l’App Store. Installez l’application, choisissez la connexion Xtream Codes (ou un lien M3U) et entrez vos identifiants IPTVMaple. TiviMate n’existe pas sur les appareils Apple.</p>",
        body="""
<h2>Les applications IPTV pour appareils Apple</h2>
<table>
<thead><tr><th>Application</th><th>Appareils</th><th>Identifiants</th></tr></thead>
<tbody>
<tr><td>Smarters Player Lite</td><td>iPhone, iPad, Apple TV</td><td>Xtream Codes, M3U</td></tr>
<tr><td>iPlayTV</td><td>iPhone, iPad, Apple TV</td><td>M3U, Xtream Codes selon la version</td></tr>
<tr><td>Autres applications</td><td>Par exemple GSE Smart IPTV</td><td>Selon l’application</td></tr>
</tbody>
</table>
<p>Les fonctions et les prix changent selon les versions : lisez la fiche de l’App Store avant d’installer. Pour les détails, voyez <a href="/smarters-player-lite/">Smarters Player Lite</a> et <a href="/iplaytv/">iPlayTV</a> (en anglais).</p>

<h2>Installer sur iPhone et iPad</h2>
<ol>
<li>Ouvrez l’<strong>App Store</strong> et cherchez « Smarters Player Lite » ou « iPlayTV ».</li>
<li>Appuyez sur <strong>Obtenir</strong>, puis sur <strong>Ouvrir</strong>.</li>
<li>Acceptez les conditions de l’application.</li>
</ol>

<h2>Installer sur Apple TV</h2>
<ol>
<li>Sur l’Apple TV, ouvrez l’<strong>App Store</strong> et cherchez l’application.</li>
<li>Installez-la et ouvrez-la.</li>
<li>Pour saisir les identifiants plus vite, utilisez l’application Télécommande de l’iPhone comme clavier.</li>
</ol>

<h2>Vous connecter avec vos identifiants</h2>
""" + LOGIN_FR + """
<ol>
<li>Choisissez la connexion <strong>Xtream Codes</strong> (ou « Ajouter une liste M3U »).</li>
<li>Entrez un nom, le nom d’utilisateur, le mot de passe et l’URL du serveur.</li>
<li>Validez. Les chaînes et le guide se chargent.</li>
</ol>

<h2>Diffuser de l’iPhone vers le téléviseur</h2>
<p>Si vous n’avez pas d’Apple TV, vous pouvez utiliser AirPlay depuis l’iPhone vers un téléviseur compatible. La qualité dépend de votre Wi-Fi. Pour un usage quotidien, un Apple TV ou un Fire TV Stick est plus confortable.</p>

<h2>Problèmes fréquents</h2>
<ul>
<li><strong>Identifiants refusés</strong> : recopiez sans espace.</li>
<li><strong>Pas de guide</strong> : ajoutez le lien EPG ou utilisez Xtream Codes.</li>
<li><strong>Saccades</strong> : Wi-Fi 5 GHz ou Ethernet pour l’Apple TV. Voyez <a href="/iptv-ne-fonctionne-plus/">les solutions</a>.</li>
</ul>
<p>Guide complet en anglais : <a href="/iptv-apple-tv/">IPTV on Apple TV</a> et <a href="/iptv-iphone/">IPTV on iPhone</a>. Essayez d’abord l’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>.</p>
""",
        faq=[
            ("Quelle application IPTV utiliser sur iPhone?",
             "<p>Smarters Player Lite ou iPlayTV, toutes deux offertes dans l’App Store. Elles acceptent les identifiants Xtream Codes ou un lien M3U.</p>"),
            ("TiviMate existe-t-il sur Apple TV?",
             "<p>Non. TiviMate fonctionne seulement sur Android TV et Fire TV. Sur Apple TV, utilisez Smarters Player Lite ou iPlayTV.</p>"),
            ("Comment regarder l’IPTV sur Apple TV?",
             "<p>Installez une application IPTV depuis l’App Store de l’Apple TV, ouvrez-la et entrez vos identifiants Xtream Codes ou votre lien M3U.</p>"),
            ("L’IPTV fonctionne-t-il sur iPad?",
             "<p>Oui, avec les mêmes applications que sur l’iPhone, comme Smarters Player Lite.</p>"),
        ],
        related=["iptv-sur-smart-tv", "lecteur-iptv", "iptv-smarters-pro-francais"],
        cta_title="Testez sur votre iPhone",
        keywords=["iptv sur apple tv", "iptv sur iphone", "iptv apple tv", "iptv apple", "iptv ipad", "iplaytv apple tv", "iptv sur chromecast", "iptv chromecast", "iptv sur ps5"],
    ),

    # ------------------------------------------------------------------ SUR PC / MAC
    dict(
        slug="iptv-sur-pc-mac", hub="fr", **D,
        title="IPTV sur PC et Mac : IPTV Smarters, VLC et Kodi | IPTVMaple",
        description="Regarder l’IPTV sur un ordinateur Windows ou Mac : IPTV Smarters Pro, VLC ou Kodi. Installation, identifiants Xtream Codes et lien M3U expliqués simplement.",
        kicker="Installation", h1='IPTV sur <span class="grad-text">PC et Mac</span> : trois façons simples',
        lead="Un ordinateur est un excellent écran pour l’IPTV. Voici comment choisir entre IPTV Smarters Pro, VLC et Kodi, et comment les configurer.",
        crumb="IPTV sur PC et Mac", blurb="IPTV Smarters Pro, VLC ou Kodi sur Windows et Mac.",
        answer="<p><strong>Sur PC et Mac, utilisez IPTV Smarters Pro, VLC ou Kodi.</strong> IPTV Smarters Pro donne une liste de chaînes avec guide et bibliothèque de films; VLC lit simplement votre lien M3U; Kodi est un centre multimédia complet. Évitez de coller votre lien dans des sites de lecture « en ligne » : il contient votre mot de passe.</p>",
        body="""
<h2>Quel logiciel choisir?</h2>
<table>
<thead><tr><th>Logiciel</th><th>Idéal pour</th><th>Difficulté</th></tr></thead>
<tbody>
<tr><td>IPTV Smarters Pro</td><td>Chaînes, guide télé, films et séries</td><td>Facile</td></tr>
<tr><td>VLC</td><td>Lire un lien M3U rapidement</td><td>Très facile</td></tr>
<tr><td>Kodi</td><td>Centre multimédia avec guide télé</td><td>Moyenne</td></tr>
</tbody>
</table>

<h2>IPTV Smarters Pro sur Windows et Mac</h2>
<ol>
<li>Téléchargez la version Windows ou Mac depuis le site officiel d’IPTV Smarters (ou la boutique de votre système).</li>
<li>Installez-la et ouvrez-la.</li>
<li>Choisissez <strong>Connexion avec l’API Xtream Codes</strong> et entrez votre nom d’utilisateur, votre mot de passe et l’URL du serveur.</li>
</ol>
""" + LOGIN_FR + """
<h2>VLC</h2>
<ol>
<li>Installez VLC depuis <a href="https://www.videolan.org/" rel="noopener">videolan.org</a>.</li>
<li>Windows : <strong>Média → Ouvrir un flux réseau</strong>. Mac : <strong>Fichier → Ouvrir un réseau</strong>.</li>
<li>Collez le lien M3U et cliquez sur <strong>Lire</strong>. Ouvrez la liste de lecture pour choisir une chaîne.</li>
</ol>

<h2>Kodi</h2>
<p>Installez Kodi depuis <a href="https://kodi.tv/" rel="noopener">kodi.tv</a>, puis le module <em>PVR IPTV Simple Client</em> et entrez votre lien M3U (et le lien du guide). Détails en anglais : <a href="/kodi-iptv/">Kodi IPTV guide</a>.</p>

<h2>Sur un ordinateur ou sur la télé?</h2>
<p>Un ordinateur branché au téléviseur par câble HDMI fonctionne très bien. Pour un usage quotidien dans le salon, un <a href="/iptv-sur-firestick/">Fire TV Stick</a> avec TiviMate est plus confortable.</p>

<h2>Problèmes fréquents</h2>
<ul>
<li><strong>Écran noir</strong> : mettez à jour le pilote graphique ou changez de lecteur dans les paramètres.</li>
<li><strong>Le lien M3U ne s’ouvre pas dans le navigateur</strong> : un navigateur ne lit pas les listes M3U. Utilisez VLC ou une application.</li>
<li><strong>Saccades</strong> : câble Ethernet et fermeture des autres applications. Voyez <a href="/iptv-ne-fonctionne-plus/">les solutions</a>.</li>
</ul>
<p>Guide complet en anglais : <a href="/iptv-pc-mac/">IPTV on PC and Mac</a>. Essayez avec l’<a href="/try-iptv-canada/">essai gratuit de 24 heures</a>.</p>
""",
        faq=[
            ("Comment regarder l’IPTV sur PC?",
             "<p>Installez IPTV Smarters Pro pour Windows et connectez-vous avec Xtream Codes, ou ouvrez votre lien M3U dans VLC (Média, Ouvrir un flux réseau).</p>"),
            ("Comment regarder l’IPTV sur un Mac ou un MacBook?",
             "<p>Utilisez IPTV Smarters Pro pour macOS, ou VLC avec le menu Fichier, Ouvrir un réseau, puis collez votre lien M3U.</p>"),
            ("VLC est-il meilleur qu’IPTV Smarters Pro?",
             "<p>VLC est plus simple pour lire un lien. IPTV Smarters Pro offre une liste de chaînes, un guide télé et une bibliothèque de films et séries. Choisissez selon l’interface voulue.</p>"),
            ("Peut-on regarder l’IPTV dans Chrome?",
             "<p>Pas directement avec un lien M3U. Les navigateurs ne lisent pas ces listes. Utilisez une application ou VLC.</p>"),
        ],
        related=["iptv-sur-smart-tv", "lecteur-iptv", "liste-iptv-m3u"],
        cta_title="Testez sur votre ordinateur",
        keywords=["iptv sur pc", "iptv pour pc", "iptv sur mac", "iptv sur vlc", "iptv sur kodi", "iptv pc", "lecteur iptv pc", "iptv macbook fr"],
    ),
]
