# De week van Eli — vaste regels

Weekoverzicht voor de grootouders (MePe, MaPie). Gepubliceerd op GitHub Pages, vaste link: https://scottvtksv-cpu.github.io/Eli-Week/ (bestand index.html in de repository scottvtksv-cpu/Eli-Week). Wordt elke avond om 20u nagekeken door een routine; als de inhoud van de drie weken veranderd is (of op zondag, als de week verschuift), overschrijft ze index.html en pusht ze. Geen wijziging = geen publicatie. De vroegere Artifact-pagina (claude.ai/code/artifact/d4f2f3d1-…) is enkel nog reserve; publiek gedeelde artifacts staan vast op één versie.

## Inhoud

- Altijd drie weken, elk van maandag t/m zondag: "Deze week", "Volgende week", "De week daarna".
- Alle zeven dagen staan er, ook als er niets is (dan een streepje "–"; in het weekend "Niets gepland").
- Enkel wat over Eli gaat: schoolafwijkingen (vakantie, pedagogische studiedag, facultatieve verlofdag, schoolactiviteiten zoals Strapdag), wie afhaalt, en Eli's eigen activiteiten (ponyles, turnen, kampen, feestjes).
- Niets van de ouders zelf (werk, tandarts, oudercomité, Fluvius, etentjes …).
- Familiemomenten waar de ouders zelf bij zijn ("eten bij opa", "samenkomen met buren", verjaardagen) staan er NIET op — de grootouders weten dat al en er is geen brengen of afhalen door anderen. Enkel als zo'n moment een afhaling of overnachting door iemand anders inhoudt, komt die handeling erop.
- "Deze week" is de week van maandag tot en met zondag waarin vandaag valt. Op zondag is "deze week" de week die morgen begint.
- Vast ritme staat één keer bovenaan: opstaan 7u30, aan de poort 8u30, school tot 15u30 (woensdag tot 12u), boekentas fruit + koekje + water (woensdag fruit via school, 20 weken vanaf 16/09/2026 — daarna die vermelding weer weghalen), huiswerk ma/di/do. Dit wordt NIET per dag herhaald.
- Afhalen: maandag MePe, woensdag MaPie. Staat per dag als "MePe haalt Eli af" / "MaPie haalt Eli af", zonder uur, identiek van vorm.
- Dat patroon is een standaard, geen zekerheid: bij elke update de agenda nakijken op afwezigheden en logeerpartijen (MaPie/Opa op reis, "Eli naar MePe", ouders weg) en er logica op toepassen.
- Standaard brengt en haalt Kim Eli. Dat is het normale en staat er NIET op.
- Op het dashboard staat elke brengen- of afhaalhandeling die afwijkt van "Kim doet het": door MePe, MaPie, Opa … én door Scott. Staat in de agenda dat Scott brengt of haalt (bv. telewerk), dan komt dat erop als "Scott brengt Eli naar school" / "Scott haalt Eli af". Brengt Scott Eli 's avonds naar een grootouder om daar te slapen, dan staat er "Scott brengt Eli 's avonds naar MaPie" (of wie het is). Als Eli bij iemand slaapt (X), dan brengt X haar de volgende ochtend naar school — dat is automatisch, daar wordt niet naar gevraagd. De enige open vraag is of X haar die dag ook aan school afhaalt of dat Kim of Scott haar 's avonds brengt; zegt de agenda dat niet, dan één keer kort vragen. Zo staat het er, per dag: "X haalt Eli af" / "X brengt Eli naar school". Nooit "logeert bij", nooit "terug naar huis".
- Wat Kim doet (brengen, halen, 's avonds ophalen) staat er nooit op; dat is de standaard. Zegt de agenda niets over een dag, dan doet Kim het en blijft de dag leeg.
- Een verplaatsing of werkafspraak van Kim of Scott ("Kim naar Bxl", "Kim opleiding in Nederland", "Scott telewerk") is op zich géén signaal dat brengen of halen niet lukt: Kim kan ’s ochtends nog voeren en ’s avonds nog halen. Enkel als de agenda het uitdrukkelijk zegt — bv. "Kim naar Vilvoorde: Eli naar school brengen en afhalen lukt niet" — verandert die dag. Staat het er niet bij, dan doet Kim het en blijft de dag leeg. Nooit zelf afleiden uit een afwezigheid.
- Woensdag krijgt in de datumkolom een derde regeltje "school tot 12u".
- Weekendactiviteiten en andere activiteiten met een uur: uur in het roze vooraan, bv. "11u Ponyles op Hof Ter Zevekote".
- Uurnotatie: 7u30, 8u30, 11u, 12u, 13u, 15u15 — nooit "12u00".
- Datum: weekdag vet, daaronder "7 september" klein grijs. Nooit "maandag 7".
- Grote schoolactiviteit (zoals Strapdag): korte titel op de dagregel, daaronder een roze kader over de volle rijbreedte met een opsomming van wat mee moet / wat je moet weten.
- Geen "vandaag"-markering, geen interne notities ("na te kijken") op de pagina.
- Bovenaan staat enkel de laatste update, mét uur: "Laatste update: maandag 21 september 2026 om 12u45". Geen belofte over wanneer de pagina bijgewerkt wordt — niet bovenaan en niet in de voettekst. Die stempel verandert alleen mee als er effectief gepubliceerd wordt.
- Uitroepteken bij een probleem met halen of brengen, in hetzelfde roze accent als de rest van de pagina, zonder uitleg erbij — enkel het teken en één woord. Elke dag krijgt zijn eigen teken, volgens wat er die dag mist: `!Ophalen` als er nog niemand is om Eli aan school af te halen, `!Voeren` als er nog niemand is om haar te brengen, `!!Overnachting` enkel op de dag dat Eli ergens moet blijven slapen. Een dag krijgt `!!Overnachting` alleen als Eli díé avond ergens moet blijven slapen. Zijn er twee nachten na elkaar niet geregeld, dan krijgen beide dagen `!!Overnachting`, elk voor zijn eigen nacht. Ontbreekt op een dag enkel het afhalen en is de nacht wel geregeld, dan staat er `!Ophalen` en niet het dubbele teken. Vorm: `<div class="line alarm"><span class="bang">!</span>Ophalen</div>`. Het teken staat er enkel zolang er niemand geregeld is: zodra de agenda iemand noemt, grootouder of ouder, verdwijnt het en komt de gewone regel of een streepje in de plaats.
- De pagina is publiek leesbaar: nooit achternaam, adres, telefoonnummers, foto's of andere identificerende gegevens op de pagina. Enkel voornamen/roepnamen (Eli, MePe, MaPie, Opa, Scott).

## Vormgeving

- Altijd licht thema, roze accent (#c2185b). Geen donkere modus.
- Eén kaart per week, dagen als rijen; weekendrijen zachtroze getint.
- "Deze week" met schaduw, de twee volgende weken zonder (lichter).
- Lettertypen: Gabarito (koppen), Source Sans 3 (tekst), via Google Fonts.
- Gsm-breedte (390 px) moet perfect zijn; dat is waar de grootouders het lezen.

## Werkwijze

- Altijd zelf renderen (Playwright, 390 px én 820 px) en de screenshots bekijken vóór publicatie. Geen halfaf versies tonen.
- Publiceren = index.html in de repository scottvtksv-cpu/Eli-Week overschrijven, committen en pushen naar main (vanuit een Claude Code-sessie waaraan die repository gekoppeld is). Niet meer via de Artifact-tool.
- Bronagenda's: kimberly.dke@gmail.com én scottvtk.sv@gmail.com. Beide worden elke keer gelezen; samen vormen ze het beeld. Wat op één van de twee staat telt evenveel.
- Bij onduidelijkheid in de agenda: niet op de pagina zetten, wel melden.
- Dit bestand (REGELS.md) is de enige bron van de regels voor de wekelijkse update; de Claude-projectdocumenten zijn vanuit een Code-sessie niet bereikbaar. Wijzigingen aan de regels gebeuren hier.
