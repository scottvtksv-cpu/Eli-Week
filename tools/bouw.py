#!/usr/bin/env python3
"""Bouwt de drie weekkaarten van index.html opnieuw op uit een JSON-bestand.

Gebruik:  python3 tools/bouw.py weken.json [--stempel "maandag 2 november 2026 om 8u52"]

Zonder --stempel wordt het huidige moment in Brusselse tijd gebruikt.
Alles buiten de drie weken (kop, vast ritme, voettekst, CSS) blijft onaangeroerd.

Vorm van weken.json (precies drie weken, elk zeven dagen ma..zo):
{
  "weken": [
    {"titel": "Deze week", "bereik": "2 tot 8 november", "dagen": [
      {"dag": "maandag", "datum": "2 november", "regels": [{"vet": "Herfstvakantie"}]},
      {"dag": "woensdag", "datum": "18 november", "u": "school tot 12u15",
       "regels": [{"wie": "MaPie", "tekst": "haalt Eli af"}]},
      {"dag": "vrijdag", "datum": "6 november", "regels": [
          {"vet": "Herfstvakantie"},
          {"uur": "12u", "tekst": "Lunch en boswandeling met", "wie_na": "Opa"}]},
      {"dag": "dinsdag", "datum": "17 november", "regels": [{"alarm": "Voeren"}]},
      {"dag": "zondag", "datum": "22 november", "regels": []}
    ]},
    ...
  ]
}

Soorten regels:
  {"vet": "Sportdag", "rest": "— sportkledij aan"}   -> vetgedrukte titel + optionele uitleg
  {"uur": "15u40", "tekst": "Turnen bij ..."}        -> roze uur vooraan
  {"wie": "MePe", "tekst": "haalt Eli af"}           -> roze naam vooraan
  {"tekst": "Eli slaapt bij", "wie_na": "Opa"}       -> roze naam achteraan
  {"alarm": "Voeren"} / "Ophalen" / "Overnachting"   -> roze uitroepteken (Overnachting krijgt !!)
  {"html": "..."}                                    -> letterlijke HTML (noodgreep)
Lege regels-lijst: "–" op weekdagen, "Niets gepland" op zaterdag/zondag.
"""
import json, re, sys, datetime
from zoneinfo import ZoneInfo

INDEX = 'index.html'
WEEKEND = {'zaterdag', 'zondag'}
DAGEN = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
MAANDEN = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli',
           'augustus', 'september', 'oktober', 'november', 'december']


def regel(r):
    if 'html' in r:
        return r['html']
    if 'alarm' in r:
        bang = '!!' if r['alarm'] == 'Overnachting' else '!'
        return f'<div class="line alarm"><span class="bang">{bang}</span>{r["alarm"]}</div>'
    if 'vet' in r:
        rest = f' {r["rest"]}' if r.get('rest') else ''
        return f'<div class="line"><strong>{r["vet"]}</strong>{rest}</div>'
    binnen = ''
    if r.get('uur'):
        binnen += f'<span class="t">{r["uur"]}</span>'
    if r.get('wie'):
        binnen += f'<span class="who">{r["wie"]}</span> '
    binnen += r.get('tekst', '')
    if r.get('wie_na'):
        binnen += f' <span class="who">{r["wie_na"]}</span>'
    return f'<div class="line">{binnen}</div>'


def dag(d):
    we = d['dag'] in WEEKEND
    u = f'<span class="u">{d["u"]}</span>' if d.get('u') else ''
    if d['regels']:
        inhoud = ''.join(regel(r) for r in d['regels'])
    else:
        inhoud = '<span class="vrij">Niets gepland</span>' if we else '<span class="leeg">–</span>'
    return (f'      <div class="row{" we" if we else ""}"><div class="day"><span class="d">{d["dag"]}</span>'
            f'<span class="n">{d["datum"]}</span>{u}</div><div class="what">{inhoud}</div></div>\n')


def week(w, i):
    klasse = 'week' if i == 0 else 'week later'            # enkel "Deze week" krijgt schaduw
    commentaar = ['DEZE WEEK', 'VOLGENDE WEEK', 'DE WEEK DAARNA'][i]
    assert [d['dag'] for d in w['dagen']] == DAGEN, f'week {i}: dagen moeten ma..zo zijn'
    rijen = ''.join(dag(d) for d in w['dagen'])
    return (f'  <!-- ===== {commentaar} ===== -->\n  <section class="{klasse}">\n'
            f'    <div class="weekhead"><h2>{w["titel"]}</h2><span class="range">{w["bereik"]}</span></div>\n'
            f'    <div class="weekcard">\n{rijen}    </div>\n  </section>\n\n')


def stempel_nu():
    n = datetime.datetime.now(ZoneInfo('Europe/Brussels'))
    uur = f'{n.hour}u' if n.minute == 0 else f'{n.hour}u{n.minute:02d}'   # 12u, 8u52 — nooit 12u00
    return f'{DAGEN[n.weekday()]} {n.day} {MAANDEN[n.month - 1]} {n.year} om {uur}'


def main():
    data = json.load(open(sys.argv[1]))
    stempel = sys.argv[sys.argv.index('--stempel') + 1] if '--stempel' in sys.argv else stempel_nu()
    assert len(data['weken']) == 3, 'precies drie weken'
    s = open(INDEX).read()
    a = s.index('  <!-- ===== DEZE WEEK ===== -->')
    b = s.index('  <footer>')
    s = s[:a] + ''.join(week(w, i) for i, w in enumerate(data['weken'])) + s[b:]
    s = re.sub(r'Laatste update: [^<]*', f'Laatste update: {stempel}', s)
    open(INDEX, 'w').write(s)
    print('index.html opgebouwd, stempel:', stempel)


if __name__ == '__main__':
    main()
