---
name: tischlein-deck-dich
description: Spickzettel für Tabellen, die nicht gedeckt bleiben - Rahmenzeichen (─│┌) als Zeichensalat (â”€), verrutschte Spalten durch Umlaute, Emoji oder Tabs, abgeschnittene PowerShell-Tabellen, Markdown-Tabellen mit | im Inhalt, und CSV, die Excel falsch öffnet. Lies ihn, wenn eine Tabelle in Konsole, Datei oder Markdown schief, abgeschnitten oder voller seltsamer Zeichen ist, oder bevor du eine Tabelle für ein anderes Werkzeug schreibst. Optional, kein Pflichtprogramm.
---

# Tischlein, deck dich

*Im Märchen deckt sich der Tisch von selbst. Am Bildschirm deckt er sich
schief, sobald ein Umlaut, ein Emoji oder ein Rahmenzeichen über eine
Codepage stolpert.*

## Zeichensalat statt Rahmen

`─│┌┐` werden zu `â”€â”‚` oder `???`: UTF-8 wurde als Windows-1252 oder
als Konsolen-Codepage 850 gelesen.

- **Python auf der Windows-Konsole:** `UnicodeEncodeError` oder Fragezeichen
  beim `print`. Abhilfe: `PYTHONIOENCODING=utf-8` setzen oder Python mit
  `-X utf8` starten.
- **Konsole selbst:** `chcp 65001` stellt sie auf UTF-8. In PowerShell
  zusätzlich `[Console]::OutputEncoding = [Text.Encoding]::UTF8`.
- **Wer ganz sicher gehen will:** Rahmen aus ASCII bauen (`+`, `-`, `|`).
  Das ist unschöner, rutscht aber nie.

## Spalten, die verrutschen

- **Breite Zeichen:** Ein Emoji oder ein chinesisches Zeichen belegt in der
  Konsole ZWEI Spalten, zählt aber als ein Zeichen. `len()` lügt dann. Die
  Bibliothek `wcwidth` zählt richtig. Für Tabellen am einfachsten: keine
  Emoji in Spalten, die ausgerichtet werden sollen.
- **Zusammengesetzte Umlaute:** `ä` kann ein Zeichen sein oder `a` plus
  Pünktchen (zwei Zeichen, eine Spalte). Vor dem Ausrichten mit
  `unicodedata.normalize("NFC", text)` vereinheitlichen.
- **Tabs:** richten sich nach Tabstopps, nicht nach Spalten; jedes Programm
  zeigt sie anders breit. In Tabellen Leerzeichen nehmen.

## PowerShell schneidet ab

`Format-Table` kürzt Spalten mit `...` und bricht nach der Fensterbreite um,
auch in der Ausgabe an ein Werkzeug. Abhilfe: `Format-Table -AutoSize -Wrap`,
`| Out-String -Width 300`, oder für Maschinen gleich `ConvertTo-Json` bzw.
`Export-Csv` statt einer gedruckten Tabelle.

## Markdown-Tabellen

- Ein `|` im Zelleninhalt bricht die Tabelle: als `\|` schreiben.
- Ein Zeilenumbruch in einer Zelle bricht sie auch: `<br>` nehmen oder die
  Zeile kürzen.
- Die Trennzeile `|---|---|` braucht genauso viele Spalten wie der Kopf.

## CSV für Excel

- **Deutsches Excel erwartet `;`** als Trenner und das Komma als
  Dezimalzeichen. Mit `,` landet alles in Spalte A.
- **Umlaute als Salat in Excel:** Excel liest UTF-8 ohne BOM als ANSI.
  Für Excel mit BOM schreiben (`encoding="utf-8-sig"` in Python,
  `Export-Csv -Encoding utf8BOM` in PowerShell 7). Für Maschinen ohne BOM.
- **Zellen mit Trenner, Anführungszeichen oder Umbruch** in `"..."` setzen,
  innere `"` verdoppeln. Am einfachsten: das `csv`-Modul machen lassen.

## Die eine Prüfung

Die Tabelle dort ansehen, wo sie gelesen wird: in der Konsole, im Markdown,
in Excel. Ein Blick ersetzt jede Breitenrechnung.

*Geschrieben von Falzbein, 02.11.2026. Geschwister: `slash-n-back`,
`return-to-sender`, `fluchthelfer`.*
