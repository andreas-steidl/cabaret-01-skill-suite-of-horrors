---
name: return-to-sender
description: 'Spickzettel für Zeilenenden (CRLF gegen LF), wenn auf Windows für Linux gebaut wird oder umgekehrt, mit WSL, Git, Bash, PowerShell und Python durcheinander. Lies ihn bei "bad interpreter: /bin/bash^M", "$''\r'': command not found", einem Diff, in dem plötzlich JEDE Zeile geändert ist, einer Prüfsumme, die nach dem Kopieren nicht mehr stimmt, einem Vergleich oder Regex, der "eigentlich" passen müsste, einer Datei, die Windows nicht annimmt (.theme, .bat, .reg), oder wenn du eine Textdatei schreibst, die auf dem anderen System laufen soll. Optional, kein Pflichtprogramm.'
---

# return to sender

*Die Schreibmaschine macht am Zeilenende zwei Dinge: Wagen zurück (CR, `\r`)
und Zeile vor (LF, `\n`). Windows hat beide behalten, Linux und macOS nur den
Vorschub. Seitdem fährt in jeder gemischten Werkstatt irgendwo ein Wagen
zurück, den keiner bestellt hat.*

## Woran man es erkennt

| Meldung / Zeichen | was los ist |
|---|---|
| `/bin/bash^M: bad interpreter` | Shell-Skript mit CRLF auf Linux |
| `$'\r': command not found`, `syntax error near unexpected token $'do\r'` | dasselbe, eine Zeile tiefer |
| Diff zeigt jede Zeile als geändert | Zeilenenden umgeschrieben, Inhalt gleich |
| `"abc" != "abc"` in Bash, Vergleich schlägt still fehl | ein `\r` hängt am Wert (aus Datei oder Windows-Programm gelesen) |
| Prüfsumme, Signatur oder Blockmap stimmt nach Kopie nicht | Kopie hat Zeilenenden „repariert“ |
| Windows nimmt `.theme`, `.bat`, `.reg` nicht an oder liest Unsinn | LF, wo CRLF erwartet wird |

## Nachsehen, nicht raten

```bash
file datei.sh                          # "with CRLF line terminators"
grep -c $'\r' datei.sh                 # Zeilen mit CR (0 = reines LF)
git ls-files --eol                     # je Datei: i/ = im Repo, w/ = im Arbeitsordner
```
```powershell
(Get-Content datei -Raw).Contains("`r`n")
```
```python
d = open(p, "rb").read(); print(d.count(b"\r\n"), d.count(b"\n") - d.count(b"\r\n"))  # CRLF, reines LF
```

## Die Fallen, nach Werkzeug

- **Python schreibt im Textmodus auf Windows CRLF.** `open(p, "w")` macht aus
  jedem `\n` ein `\r\n`. Für Linux-Dateien `open(p, "w", newline="\n")`, für
  Windows-Dateien ausdrücklich `newline="\r\n"`. Beim Lesen macht der
  Textmodus aus beidem `\n`. `.split("\n")` auf Rohtext lässt `\r` am
  Zeilenende stehen, `.splitlines()` nicht.
- **PowerShell:** `Set-Content` und `Out-File` schreiben das Zeilenende der
  Plattform, auf Windows also CRLF. Wer LF braucht:
  `[IO.File]::WriteAllText(p, ($text -replace "`r`n", "`n"))`. Here-Strings
  in einer CRLF-Skriptdatei tragen CRLF in sich.
- **Bash:** `read` behält das `\r`, `$(cat datei)` auch. Säubern mit
  `wert=${wert%$'\r'}` oder `tr -d '\r'`. Datei reparieren: `sed -i 's/\r$//' datei`
  (oder `dos2unix`, wenn vorhanden).
- **Git:** `core.autocrlf` ist von Rechner zu Rechner anders eingestellt. Was
  verlässlich gilt, gehört ins Repo, in `.gitattributes`:
  ```
  * text=auto eol=lf
  *.ps1 text eol=crlf
  *.bat text eol=crlf
  *.cmd text eol=crlf
  *.sh  text eol=lf
  *.png binary
  ```
  Danach einmal `git add --renormalize .` und als eigenen Commit buchen,
  sonst verschwindet die Umstellung in einem Feature-Diff.
- **Git, wenn Prüfsummen zählen:** Wo der SHA-256 einer Datei auf Windows
  und Linux gleich sein muss, ist `* -text` in `.gitattributes` die sichere
  Wahl. Git wandelt dann nie um, die Bytes bleiben exakt wie eingecheckt. Mit
  `core.autocrlf=true` oder `text=auto` schreibt Windows beim Auschecken CRLF,
  und jede Hash-Prüfung scheitert. (Echolot, Python-Dienst für beide Systeme)
- **Eine Datei aus einem anderen Commit wortgleich holen:**
  `git show <commit>:<pfad> > ziel`, danach den Hash vergleichen. Kopieren
  und Einfügen über einen Editor ändert gern die Zeilenenden.
- **Protokolle über stdout** (JSON-RPC, MCP, alles, was eine Gegenstelle
  zeilenweise liest): das Zeilenende selbst als `b"\n"` anhängen und binär
  schreiben (`sys.stdout.buffer.write(...)`), nie `print()` oder
  `os.linesep`. Sonst kommt unter Windows `\r\n` beim Gegenüber an.
- **Regex:** In .NET (PowerShell) passt `$` im Multiline-Modus VOR `\n`, nicht
  vor `\r`, das `\r` landet also im Treffer. Lieber `\r?$` schreiben.
- **WSL:** Dateien unter `/mnt/c/...` behalten ihre Windows-Zeilenenden. Ein
  Skript, das unter Windows gespeichert wurde, läuft unter Linux nicht, nur
  weil es dort liegt.

## Kodierung, die Cousine

Dieselbe Familie, ein Zeichen weiter vorn in der Datei:

- **Windows PowerShell 5.1 liest Dateien ohne BOM als ANSI.** Skripte, die
  auch dort laufen sollen, schreibt man in reinem ASCII (ae, oe, ue, ss),
  sonst werden Umlaute zu Zeichensalat oder ein String bricht. PowerShell 7
  liest UTF-8 ohne BOM richtig.
- **`Set-Content -Encoding UTF8` schreibt unter 5.1 ein BOM.** Wer das aus
  Python liest, braucht `encoding="utf-8-sig"`, sonst scheitert `json.load`
  am ersten Zeichen.
- **JSON, das gehasht oder signiert wird,** mit festen Trennzeichen erzeugen
  (`separators=(",", ":")`, dazu `sort_keys=True`, wenn die Reihenfolge nicht
  feststeht), damit die Bytes stabil bleiben. `ensure_ascii=False` nur dort,
  wo Menschen lesen.
- **Commit-Meldungen über einen Heredoc** in ASCII schreiben vermeidet
  Kodierungsärger zwischen Git Bash, cmd und Git für Windows.

## Wer was braucht

| CRLF | LF | egal, aber einheitlich |
|---|---|---|
| `.bat`, `.cmd`, `.reg`, `.theme`, `.ps1` (empfohlen) | `.sh`, `Dockerfile`, `Makefile`, alles, was unter Linux ausgeführt wird | `.md`, `.json`, `.py`, `.yml`, `.csv` (dann im Repo festlegen) |

## Merksatz

Wer eine Datei für das andere System schreibt, sagt das Zeilenende
ausdrücklich an, statt es dem Werkzeug zu überlassen. Und wer eine Prüfsumme
über Text bildet, prüft vorher, dass beide Seiten dieselben Zeilenenden
haben, sonst vergleicht er Wagen statt Wörter.

*Geschrieben von Falzbein, 02.11.2026, für Andys Werkstatt.
Schwester: `slash-n-back` (Backslashes und Anführungszeichen).*
