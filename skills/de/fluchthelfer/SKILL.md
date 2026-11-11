---
name: fluchthelfer
description: Spickzettel für Escape-Sequenzen, die ausbüxen - Farbcodes (ESC[32m) in Logs und Dateien, Fortschrittsbalken mit \r, und doppelt und dreifach maskierte Backslashes, wenn ein Text durch PowerShell, Bash, Regex und JSON reist. Lies ihn, wenn in einer Datei oder Ausgabe Zeichen wie ←[0m, ^[[32m, \x1b oder \u001b stehen, wenn ein grep auf eine Werkzeugausgabe nichts findet, obwohl man den Text sieht, wenn ein Log voller halber Zeilen ist, oder wenn du nicht mehr weißt, wie viele Backslashes ein Muster braucht. Optional, kein Pflichtprogramm.
---

# Fluchthelfer

*ESC heißt Flucht. Und manche Zeichen nutzen jede Gelegenheit dazu: Sie
verlassen das Terminal, für das sie gedacht waren, und tauchen in Dateien,
Logs und Vergleichen wieder auf.*

## Farbcodes, die mitgeschrieben werden

Viele Werkzeuge färben ihre Ausgabe mit ANSI-Sequenzen: `ESC [ 32 m` heißt
grün, `ESC [ 0 m` heißt zurück. Im Terminal sieht man Farbe, in einer Datei
sieht man `←[32m`, `^[[32m` oder `\x1b[32m`.

- **Folge:** `grep "fertig"` findet nichts, weil im Text `fer\x1b[1mtig`
  steht. JSON wird ungültig, ein Vergleich schlägt still fehl.
- **Abschalten an der Quelle** (am besten): `NO_COLOR=1` als Umgebungsvariable
  (viele Werkzeuge halten sich daran), `--color=never` bzw. `--no-color`,
  `git -c color.ui=never ...`, in PowerShell 7
  `$PSStyle.OutputRendering = 'PlainText'`.
- **Nachträglich entfernen:**
  ```python
  import re; sauber = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", text)
  ```
  ```bash
  sed -E 's/\x1b\[[0-9;?]*[ -/]*[@-~]//g' log.txt
  ```

## Fortschrittsbalken mit Wagenrücklauf

Ein Fortschrittsbalken schreibt `\r` und überschreibt die Zeile. Im Terminal
sieht man eine Zeile, in der Logdatei stehen hundert halbe. Wer so ein Log
auswertet, nimmt nur den Teil nach dem letzten `\r` jeder Zeile:
`zeile.rsplit("\r", 1)[-1]`. Siehe auch `return-to-sender`.

## Wie viele Backslashes?

Jede Schicht, durch die ein Text reist, frisst eine Maskierung. Zähle die
Schichten von innen nach außen:

| Ziel | im Muster | in einer Python-Zeichenkette | in JSON darum herum |
|---|---|---|---|
| ein wörtlicher Backslash im Regex | `\\` | `r"\\"` oder `"\\\\"` | `"\\\\"` bzw. `"\\\\\\\\"` |
| ein Punkt im Regex | `\.` | `r"\."` | `"\\."` |

Faustregeln:
- **Python:** Muster immer als Rohzeichenkette `r"..."`.
- **PowerShell:** `'einfache'` Anführungszeichen, dann bleibt alles wörtlich;
  Regex-Escapes mit `[regex]::Escape($text)` erzeugen lassen.
- **Bash:** Muster in `'einfache'` Anführungszeichen; `$'...'` nur, wenn man
  wirklich ein Steuerzeichen meint (`$'\t'`, `$'\r'`).
- **JSON** ist immer eine Schicht mehr. Lieber das Objekt im Programm bauen
  und mit `json.dumps` schreiben, als JSON von Hand zu maskieren.

## Die eine Prüfung

Nach dem Schreiben die Datei nach dem ESC-Zeichen durchsuchen:
`grep -c $'\x1b' datei` muss 0 ergeben (PowerShell:
`(Get-Content datei -Raw).Contains([char]27)` muss `False` sein). Und den
Text, den man sucht, im Ergebnis wiederfinden, statt dem Muster zu glauben.

*Geschrieben von Falzbein, 02.11.2026. Geschwister: `slash-n-back`
(Backslashes und Anführungszeichen), `return-to-sender` (Zeilenenden),
`tischlein-deck-dich` (Tabellen).*
