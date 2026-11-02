# De week van Eli — werkwijze in code

Dit document beschrijft stap voor stap wat de avondronde elke dag doet. Het is bedoeld zodat een ander systeem (bv. Grok) hetzelfde kan nadoen. **REGELS.md blijft de enige bron van de inhoudelijke regels.** Dit bestand beschrijft alleen het *hoe*.

Onderdelen in de repository:

| Bestand | Rol |
|---|---|
| `REGELS.md` | Wat er wel en niet op de pagina komt, en in welke vorm. Elke ronde opnieuw lezen. |
| `index.html` | De gepubliceerde pagina (GitHub Pages: https://scottvtksv-cpu.github.io/Eli-Week/). |
| `tools/bouw.py` | Zet een JSON met drie weken om naar de HTML van de weekkaarten en zet de stempel. |
| `tools/render.js` | Rendert op 390 px en 820 px, controleert op horizontale overloop en maakt screenshots. |
| `tools/voorbeeld-weken.json` | De JSON die de pagina van 2 november 2026 exact oplevert. Handig als voorbeeld. |

---

## 0. Wanneer

Elke avond rond 20u (Brusselse tijd) start er een geplande taak met de opdracht "Avondronde De week van Eli".

## 1. Repository bijwerken

```bash
git fetch -q origin main
git checkout -q -B werkbranch origin/main   # altijd vertrekken van de laatste main
```

Lees daarna `REGELS.md` en `index.html` volledig. De regels kunnen sinds gisteren veranderd zijn.

## 2. Welke drie weken

```python
import datetime
from zoneinfo import ZoneInfo

vandaag = datetime.datetime.now(ZoneInfo('Europe/Brussels')).date()
if vandaag.weekday() == 6:                       # zondag: "deze week" is de week die morgen begint
    maandag = vandaag + datetime.timedelta(days=1)
else:
    maandag = vandaag - datetime.timedelta(days=vandaag.weekday())
weken = [(maandag + datetime.timedelta(weeks=i), maandag + datetime.timedelta(weeks=i, days=6)) for i in range(3)]
start, einde = weken[0][0], weken[2][1] + datetime.timedelta(days=1)   # einde exclusief
```

De titels zijn altijd "Deze week", "Volgende week" en "De week daarna". Het bereik schrijf je als "2 tot 8 november", of "26 oktober tot 1 november" als de week over een maandgrens loopt.

## 3. Beide agenda's lezen

Bronnen: `kimberly.dke@gmail.com` en `scottvtk.sv@gmail.com`. Beide tellen evenveel. Wij lezen ze via een Google Calendar-koppeling. Met de gewone Google Calendar API in Python ziet dat er ongeveer zo uit. Dit voorbeeld zelf is niet getest: hier gebeurt het via een connector.

```python
from googleapiclient.discovery import build   # pip install google-api-python-client
# creds = ... OAuth-credentials met leesrecht op beide agenda's
svc = build('calendar', 'v3', credentials=creds)

def items(kalender):
    r = svc.events().list(
        calendarId=kalender,
        timeMin=f'{start}T00:00:00+01:00', timeMax=f'{einde}T00:00:00+01:00',
        timeZone='Europe/Brussels', singleEvents=True, orderBy='startTime', maxResults=250,
    ).execute()
    return r.get('items', [])

alle = items('kimberly.dke@gmail.com') + items('scottvtk.sv@gmail.com')
```

Let op: een item dat de hele dag duurt heeft `start.date` en geen `start.dateTime`, en `end.date` is exclusief.

Tip: sorteer ook eens op laatst gewijzigd (`orderBy='updated'`). Zo zie je snel wat er sinds de vorige ronde nieuw of aangepast is.

## 4. Elk item beoordelen (het eigenlijke denkwerk)

Dit deel kan geen script alleen. Voor elk item beslis je met REGELS.md in de hand. Hieronder staat de samenvatting zoals ze in de praktijk wordt toegepast, met voorbeelden uit oktober en november 2026.

| Soort item | Op de pagina? | Vorm |
|---|---|---|
| Schoolvakantie, pedagogische studiedag, feestdag (Herfstvakantie, Wapenstilstand) | Ja, elke dag | `{"vet": "Herfstvakantie"}` / `{"vet": "Geen school", "rest": "— Wapenstilstand"}` |
| Schoolactiviteit voor Eli (sportdag, zwemmen, Halloween, schoolfotograaf) | Ja | `{"vet": "Zwemmen", "rest": "— zwemzak mee"}`. Met uur: `{"uur": "8u", "tekst": "<strong>Schoolfotograaf</strong>"}` |
| Eli's eigen activiteit (turnen, ponyles, feestje) | Ja, met uur | `{"uur": "15u40", "tekst": "Turnen bij Studio Minne, Sporthal Rodelos"}` |
| Grootouder of Opa haalt af of brengt | Ja | `{"wie": "MePe", "tekst": "haalt Eli af"}` |
| Vast patroon: maandag haalt MePe af, woensdag MaPie | Ja, behalve op dagen zonder school | idem |
| Eli slaapt elders ("X haalt Eli op en blijft slapen" betekent altijd dat Eli bij X slaapt) | Ja | `{"tekst": "Eli slaapt bij", "wie_na": "Opa"}` |
| Eli is een dag bij iemand of gaat alleen met iemand mee | Ja | `{"tekst": "Eli is de hele dag bij", "wie_na": "MaPie"}` |
| Kim moet 's ochtends vroeg weg of is 's ochtends in het buitenland, en niemand brengt | Ja, als alarm | `{"alarm": "Voeren"}` |
| Niemand om af te halen | Ja, als alarm | `{"alarm": "Ophalen"}` |
| Niemand voor de nacht | Ja, als alarm | `{"alarm": "Overnachting"}` |
| Iets van Kim of Scott zelf (werk, gym, dokter, etentje, oudercomité, workshops, reispas, verjaardagen, betalingen) | Nee | — |
| Gezinsmoment waarbij de ouders er zelf bij zijn | Nee | — |
| Iets wat brengen of halen door Kim betekent | Nee, Kim is de standaard | — |
| Twijfel ("wellicht", onduidelijke titel) | Nee | Niet op de pagina zetten, maar als vraag aan Scott stellen |

Extra afspraken:

- **Nooit afleiden uit een afwezigheid.** "Kim Bxl" alleen is geen probleem. Pas als er staat dat ze vroeg weg moet, komt er `!Voeren`.
- "Pépé" in de agenda is MePe.
- Woensdag krijgt `"u": "school tot 12u15"`, behalve op dagen zonder school.
- Uurnotatie: `7u30`, `12u`, `15u40`, nooit `12u00`.
- Geen achternamen, adressen of telefoonnummers. De pagina is publiek.
- Eenmalige uitzonderingen staan onderaan in REGELS.md (als die sectie er is). Na de datum mogen ze weg, maar alleen als Scott dat goedkeurt.

Het resultaat van deze stap is een JSON met drie weken in de vorm van `tools/voorbeeld-weken.json`.

## 5. Vergelijken: is er iets veranderd?

```bash
cp index.html /tmp/oud.html
python3 tools/bouw.py weken.json --stempel "$(grep -o 'Laatste update: [^<]*' index.html | sed 's/Laatste update: //')"
if diff -q /tmp/oud.html index.html >/dev/null && [ "$(TZ=Europe/Brussels date +%u)" != 7 ]; then
  git checkout index.html          # niets gewijzigd en geen zondag: niets doen
  echo "geen wijzigingen"; exit 0
fi
```

Bij **geen wijzigingen** (en geen zondag): niet renderen, niet pushen, de stempel niet aanraken. Meld kort "geen wijzigingen".

## 6. Opbouwen met de echte stempel

```bash
python3 tools/bouw.py weken.json      # stempel = nu, in Brusselse tijd, bv. "maandag 2 november 2026 om 8u52"
```

## 7. Renderen en zelf nakijken

```bash
NODE_PATH=$(npm root -g) node tools/render.js /tmp/shots   # exit 1 bij horizontale overloop
```

Gebruik de vooraf geïnstalleerde Chromium (`CHROME=/pad/naar/chrome` als die elders staat). Draai nooit `playwright install`. **Bekijk daarna elke screenshot**: niets mag afbreken, overlappen of afgesneden zijn. De gsm-breedte van 390 px is de belangrijkste, want daar lezen de grootouders het.

## 8. Publiceren

```bash
git add index.html
git -c user.email=kimberly.dke@gmail.com -c user.name="Schoolassistent" \
    commit -m "De week van Eli — 2 november 2026: <wat er veranderde>"
git push origin HEAD:main            # GitHub Pages zet het binnen een minuut online
```

## 9. Bericht aan Scott

Eén kort, genummerd bericht in het Nederlands, warm van toon:

1. Per week: wat er op de pagina staat (afwijkingen, activiteiten, alarmen).
2. Wat je hebt weggelaten en waarom.
3. **Uitdrukkelijk of je gepusht hebt of niet.**
4. Vragen over alles wat onduidelijk was. Die dingen staan dan ook niet op de pagina.

## 10. Als Scott een probleem in de agenda wil

Vraagt Scott om een probleem in de agenda te zetten, dan maak je in Kims agenda een item voor de hele dag aan. Als titel neem je het alarm met een korte uitleg, bv. "!Voeren — nog niemand om Eli naar school te brengen". In de beschrijving zet je waarom. Raak de agenda verder nooit aan zonder uitdrukkelijke vraag.
