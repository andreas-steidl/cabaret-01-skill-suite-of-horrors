# CLAUDE.md – 01-grauen

Erste Spielzeit des Kabaretts von Falzbein und Andy: **„Die Skill-Suite des Grauens“** /
**„The Skill Suite of Horrors“**. Sechs Spickzettel gegen Windows-Fallen (slash-n-back,
return-to-sender, fluchthelfer, tischlein-deck-dich, lattenzaun, suite-des-grauens).
Host: **https://horrors.special.at/** (Inhalt von `web/`, flach hochgeladen).

## Ordner
- `skills/de/<name>/SKILL.md`, `skills/en/<name>/SKILL.md` (+ `skills/en/README.md`). Ordnernamen bleiben deutsch, auch im Englischen.
- `web/` – die Seite: `index.html` (Sprachwähler), `de/index.html`, `en/index.html`, Zips, Plakate, Signet, `LICENSE.txt`, `SHA256SUMS(.sig)`, `allowed_signers`.
- `plakat/` – `bild_ohne_schrift.png` (Bild von Codex, ohne Schrift), `plakat.py` (de), `plakate_en.py` (en), `logos.py` (Signet, Favicon, Querlogo), fertige Plakate.
- `doku/` – `LIESMICH.md` (Programmheft, liegt auch im Gesamt-Zip), Premierenstimmen `kommentar_*.md`, `index_vor_fonts_2026-11-03.html` (Archiv).

## Bauen
- **Zips** (kein Skript, Aufbau wie die vorhandenen): `<name>.zip` / `<name>-en.zip` = `LICENSE.txt` + `<name>/SKILL.md` + `<name>/LICENSE.txt`. Programm-Zip `skill-suite-des-grauens(-en).zip` = alle sechs + `LIESMICH.md` bzw. `README.md`. `suite-des-grauens-gesamt.zip` kommt aus `../zwischenraum/skills/gesamt/`.
- **Plakat:** `python plakat/plakat.py [bild] [ziel]` und `python plakat/plakate_en.py [bild] [ziel]`; ohne Argumente Bild und Ziel = `plakat/`. Zur Probe ein anderes Ziel angeben. Schriften aus `C:/Windows/Fonts/`. Danach von Hand nach `web/` kopieren: A4 als `plakat-a4(-en).png`, Webfassung als `plakat-web(-en).jpg` (die englische ist `*_en-web.jpg`; die deutsche `plakat-web.jpg` stammt nicht aus `plakat.py`, das nur `plakat_klein.jpg` schreibt).
- **Seite:** statisches HTML, keine Build-Kette; nur Google Fonts von außen. Sicherungen `*.vor-*.html` nicht einchecken.

## Querverweise
Zweite Spielzeit `../02-panik` (dontpanic.special.at), dritte `../03-katastrophen` (lostintranslation.special.at), Bühne und Gesamtskill `../zwischenraum` (zwischenraum.special.at). Herkunft: Baustelle `\\nas\Public\dev\skill-suite-des-grauens\` (nur lesen).

## Regeln
- Sprachen: siehe `\\nas\Public\dev\kabarett\WIE_MACH_ICH_SPRACHEN.md`.
- Texte UTF-8 (ohne BOM).
- Jede Seite und jeder Skill auf Deutsch **und** Englisch.
- Keine Religion, keine Politik in Namen und Texten.
- Sitzungsnamen in Skill-Texten nur als Rollen („eine andere Sitzung“), nicht als Namen.
- Vor dem Veröffentlichen schaut der Legal-Agent drüber (KI-Kennzeichnung, Lizenzzeile, Plakate).
- Signatur und Manifest (`SHA256SUMS`, `.sig`) kommen gesammelt am Schluss, nicht je Änderung.
- Nach jedem Schreiben im Ergebnis nachsehen: Datei öffnen, Zip auflisten, Pfad wiederfinden.
