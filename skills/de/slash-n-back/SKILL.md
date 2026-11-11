---
name: slash-n-back
description: Kurzer Spickzettel für Pfade und Anführungszeichen unter Windows, wenn PowerShell, Git Bash und Python zusammenkommen. Lies ihn, wenn du auf Windows einen UNC-Pfad (\\server\freigabe) oder Windows-Pfad in ein Skript, eine Datei oder einen Befehl schreibst, wenn ein Pfad plötzlich mit einem Laufwerk davor oder ohne Backslashes auftaucht, oder wenn etwas „nicht gefunden“ meldet, das sicher da ist. Optional, kein Pflichtprogramm.
---

# slash'n'back

*Slashes sind weird, Windows ist weird, PowerShell ist nicht bash.*

Das erwischt jede Sitzung irgendwann, auch sehr gute. Es ist kein Zeichen von
Unfähigkeit, sondern von drei Sprachen, die dasselbe Zeichen verschieden
lesen. Du musst das hier nicht auswendig können. Es reicht, das Ergebnis
nachzusehen (ganz unten).

## Was wo gilt

| Du schreibst in | Ein `\` ist dort | So kommst du sicher hin |
|---|---|---|
| **Write-/Edit-Werkzeug** | ein Backslash, wörtlich | der sicherste Weg für Skripte mit Pfaden |
| **PowerShell, `'einfach'`** | ein Backslash, wörtlich | `'\\nas\Public\datei.md'` |
| **PowerShell, `"doppelt"`** | wörtlich, aber `$` wird ersetzt, Maskierung mit `` ` `` | nur nehmen, wenn du eine Variable brauchst |
| **Bash** | Maskierung, auch auf dem Weg durch die Werkzeugschicht | `/t/Ordner` statt `T:\Ordner`; UNC hier meiden |
| **Python, normale Zeichenkette** | Maskierung: `\t` `\n` `\a` `\03` werden zu Steuerzeichen | `r"T:\Ordner"` oder `/`; am Ende nie ein einzelnes `\` |

## Die häufigsten Fälle

**`\\nas` wird zu `\nas`.** Beim Schreiben einer Datei über Bash, auch in einem
Heredoc mit `'EOF'`, ging schon ein Backslash verloren. PowerShell liest
`\nas\...` dann als Pfad auf dem aktuellen Laufwerk, und der Fehler heißt
`D:\nas\... nicht gefunden`. Skripte mit UNC-Pfaden darum mit dem
Write-Werkzeug schreiben, Befehle mit UNC-Pfaden direkt in PowerShell ausführen.

**Das Laufwerk taucht plötzlich auf.** `D:\nas\...` oder `C:\nas\...` in einer
Fehlermeldung heißt fast immer: Vorn fehlt ein Backslash.

**`T:\Bilder\03_werkzeug` in Python oder einem erzeugten Text.** `\03` wird zum
Steuerzeichen 0x03. Kein Fehler, nur ein Pfad, den es nicht gibt.

**Python aus Bash erreicht das NAS oft nicht**, Python aus PowerShell schon.
Python-Code kann man in PowerShell über einen Here-String füttern:

```powershell
$py = @'
print(r"\\nas\Public\datei.md")
'@
$py | python -
```

Das schließende `'@` muss ganz am Zeilenanfang stehen.

**Zwischen den Welten übersetzen:** In Bash macht `cygpath -w /t/Ordner` daraus
`T:\Ordner`.

**UNC-Pfade in Bash als `//nas/Public/...` schreiben**, nicht `\\nas\...`.
Auch in einem Python-Einzeiler, der aus Bash heraus läuft, geht
`"//nas/Public/..."` zuverlässiger als `r"\\nas\..."`. (Echolot)

**Heredoc ohne Anführungszeichen (`<<EOF`) wertet aus:** `\\` wird zu `\`,
`$` und Backticks werden ersetzt. Für Text mit Windows-Pfaden oder `$` immer
`<<'EOF'`. Wer doch eine Variable braucht, verdoppelt die Backslashes
(`D:\\Workspace`). (Echolot)

**Backticks in doppelten Anführungszeichen sind in Bash Befehlsersetzung.** Ein
grep nach dem PowerShell-Zeilenende `` `r`n `` in `"..."` läuft als Befehl `r`
und meldet „r: command not found“. PowerShell-Escapes in Bash-Mustern nur in
einfachen Anführungszeichen. (Echolot)

**Deutsche Anführungszeichen in PowerShell-Zeichenketten.** PowerShell
behandelt `„` und `“` wie gerade Anführungszeichen. Ein Satz wie
`"er sagte „nein“"` beendet die Zeichenkette mitten im Text, die Meldung ist
dann ein rätselhaftes „Unerwartetes Token“. Text mit solchen Zeichen in einen
Here-String `@'...'@` legen oder mit dem Write-Werkzeug schreiben.

**PowerShell ist nicht bash:** kein `2>/dev/null` (sondern `2>$null`), kein
`VAR=x befehl`, kein `head`. Und Variablen kennen keine Groß- und
Kleinschreibung: `$n` überschreibt `$N`.

## Das Stille ist das Gefährliche

Ein falscher Pfad schreit nicht immer:

- `-ErrorAction SilentlyContinue`, `2>$null` oder `try/catch` machen aus „Pfad
  falsch“ ein harmloses „nichts gefunden“.
- `$null -eq $null` ist wahr: Eine Warteschleife, die auf eine Änderung wartet,
  wartet mit einem falschen Pfad ewig und meldet nichts.

Prüfe darum vor so einer Schleife einmal `Test-Path`, und lass sie laut
abbrechen, wenn der Pfad nicht da ist.

## Die eine Prüfung, die fast alles fängt

Nach dem Schreiben den Pfad **im Ergebnis wiederfinden**, statt dem eigenen
Befehl zu glauben:

```powershell
Get-Content .\skript.ps1 -TotalCount 1
Select-String -Path .\skript.ps1 -SimpleMatch '\\nas\Public'
```

Einmal hinsehen genügt. Wenn es trotzdem passiert ist: Ein verlorener Backslash
ist in einer Minute behoben. Sag es, korrigiere es, und mach weiter.
