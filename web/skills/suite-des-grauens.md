---
name: suite-des-grauens
description: Die Skill-Suite des Grauens, oder wie man als Claude-Modell Windows in den Griff kriegt. Ein Inhaltsverzeichnis der kleinen Spickzettel gegen die immer gleichen Windows-Fallen - Backslashes, Zeilenenden, Escape-Sequenzen, Tabellen, Leerzeichen in Pfaden. Lies ihn, wenn auf Windows etwas „eigentlich“ funktionieren müsste und es nicht tut, und du nicht weißt, welcher Spickzettel passt. Optional, kein Pflichtprogramm, gern mit einem Lächeln.
---

# Die Skill-Suite des Grauens

*Oder: wie man als Claude-Modell Windows in den Griff kriegt.*

Jede Sitzung, die auf Windows arbeitet, beschwert sich am Anfang über
genau diese Fehler, und macht sie eine Stunde später selbst. Ein
Familienproblem. Darum gibt es für jedes Problemchen einen kleinen
Spickzettel mit einem Namen, den man sich merkt.

| Skill | wenn … |
|---|---|
| `slash-n-back` | ein Pfad zerfällt, `\\nas` als `//nas` gebraucht wird, `\n` in einem Pfad zum Zeilenumbruch wird, deutsche Anführungszeichen PowerShell verwirren |
| `return-to-sender` | CRLF gegen LF: `bad interpreter ^M`, ein Diff, in dem jede Zeile anders ist, eine Prüfsumme nach dem Kopieren |
| `fluchthelfer` | ANSI-Farbcodes im Log, `\r`-Fortschrittsbalken, die Frage, wie viele Backslashes ein Muster braucht |
| `tischlein-deck-dich` | Tabellen voller `â”€`, verrutschte Spalten, CSV, die Excel in Spalte A stopft |
| `lattenzaun` | Leerzeichen in „Program Files“, `sc.exe` und verlorene Anführungszeichen, Dienste mit Fehler 1053 |

**Zweites Programm: Die Skillsuite für panische Modelle**

| Skill | wenn … |
|---|---|
| `henne-und-ei` | `NT SERVICE\x` bekommt keine Rechte, Fehler 1332, `IdentityNotMappedException`: erst den Dienst eintragen |
| `viele-koeche` | zwei Prozesse schreiben in ein Protokoll, Zeilen fehlen still, ein Dämon holt den beendeten Prozess zurück |
| `max-und-moritz` | Zwillinge in Groß/Klein: JSON-Schlüssel, `$n`/`$N`, `Readme.md`/`README.md` in Git, `D:`/`d:` |
| `dollar-doppelpunkt` | `"$var:"` ist leer oder ungültig, `"$obj.Name"` halb eingesetzt, `$` in ssh lokal ersetzt, `[NullString]::Value` |
| `stille-post` | `pytest \| tail -1` ist grün, `pipefail`, `$LASTEXITCODE`, sudo frisst die erste Zeile, Einzeiler ab der dritten Schicht |
| `leerer-platz` | `Start-Process` mit leerem Argument, Junctions mit zwei Adressen, WSL-Wachen auf `/mnt/d`, die nie anschlagen |
| `hase-und-igel` | die Antwort des Menschen gilt einer älteren Frage, Nachrichten überholen sich mitten in der Arbeit |

**Die eine Regel hinter allen:** Was durch mehrere Schichten reist (Bash,
PowerShell, Python, ein natives Programm, JSON, eine Datei), verliert in
jeder Schicht etwas. Nach dem Schreiben im **Ergebnis** nachsehen, nicht in
dem, was man zu schreiben glaubte.

Entstanden aus einem Witz von Andy (slash-n-back war ein kleiner Seitenhieb
auf Fable) und geschrieben von Andy und Falzbein, mit Funden von Echolot
und Richtscheit. Neue Fallen sind willkommen: ein Skill je Problemchen.
