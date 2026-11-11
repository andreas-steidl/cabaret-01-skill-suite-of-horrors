---
name: lattenzaun
description: Spickzettel für Leerzeichen in Pfaden und Anführungszeichen, die unterwegs verloren gehen, wenn PowerShell ein natives Programm aufruft - vor allem sc.exe, msiexec, cmd /c, schtasks und alles unter „C:\Program Files“. Lies ihn, bevor du mit sc.exe einen Dienst anlegst, einen Pfad mit Leerzeichen an ein .exe übergibst, wenn ein Dienst mit Fehler 1053 nicht startet, wenn Windows plötzlich „C:\Program“ sucht, oder wenn `sc` gar nichts tut (in PowerShell heißt es Set-Content). Teil der Skill-Suite des Grauens. Optional, kein Pflichtprogramm.
---

# Lattenzaun

*Es war einmal ein Lattenzaun, mit Zwischenraum, hindurchzuschaun.*
*(Christian Morgenstern)*

*Windows sieht das Leerzeichen in „Program Files“ und denkt genau wie der
Architekt im Gedicht: Da ist ja Platz. Und baut aus dem Zwischenraum etwas
anderes, als du gemeint hast.*

## Die drei Fallen, die zusammen zuschnappen

1. **`sc` ist in PowerShell nicht sc.exe**, sondern `Set-Content`. `sc create …`
   schreibt still eine Datei namens `create`. Immer **`sc.exe`** ausschreiben.
2. **Windows PowerShell 5.1 verliert Anführungszeichen** auf dem Weg zu einem
   nativen Programm. Innere `"` kommen nicht an, wenn sie nicht als `\"`
   maskiert sind, und manchmal nicht einmal dann. PowerShell 7.3 und neuer
   reicht sie richtig durch (`$PSNativeCommandArgumentPassing`), aber nicht
   für jede Sorte Programm, `cmd.exe` und `msiexec` bleiben eigenwillig.
3. **Ein Pfad mit Leerzeichen ohne innere Anführungszeichen** wird vom
   Dienstmanager zerlegt: Er sucht erst `C:\Program.exe`, dann
   `C:\Program Files\Python311\python.exe`. Gefährlich ist das obendrein,
   denn wer eine `C:\Program.exe` hinlegt, wird gestartet.

## Was hilft

- **Das Cmdlet statt sc.exe nehmen**, dann gibt es kein natives Zerlegen:
  ```powershell
  New-Service -Name 'meindienst' -StartupType Automatic `
    -BinaryPathName '"C:\Program Files\Python311\python.exe" "D:\pfad\dienst.py"'
  ```
  Außen einfache, innen doppelte Anführungszeichen: PowerShell lässt das
  Innere in Ruhe.
- **Wenn es sc.exe sein muss:** nach `binPath=` und `start=` steht ein
  Leerzeichen, das ist dort Pflicht. Und in Windows PowerShell 5.1 den Rest
  mit dem Stop-Parsing-Zeichen `--%` unberührt durchreichen:
  ```powershell
  sc.exe --% create meindienst binPath= "\"C:\Program Files\Python311\python.exe\" \"D:\pfad\dienst.py\"" start= auto
  ```
- **python.exe ist kein Dienst.** Ein Dienstprogramm muss dem Dienstmanager
  antworten, sonst kommt nach 30 Sekunden Fehler 1053. Entweder das Skript
  mit `pywin32` (servicemanager) als echten Dienst schreiben oder einen
  Dienst-Wrapper davorsetzen, oder gleich eine geplante Aufgabe nehmen.
- **Für alles andere mit Leerzeichen:** den Aufruf in PowerShell mit dem
  Call-Operator und getrennten Argumenten machen, `& "C:\Program Files\x\y.exe" $arg1 $arg2`,
  statt eine fertige Zeichenkette zu bauen.

## Die eine Prüfung

Nach dem Anlegen nachsehen, was **wirklich** eingetragen ist:
```powershell
sc.exe qc meindienst          # Zeile BINARY_PATH_NAME
(Get-CimInstance Win32_Service -Filter "Name='meindienst'").PathName
```
Die Anführungszeichen um `"C:\Program Files\…\python.exe"` müssen dort
stehen. Fehlen sie, hat der Lattenzaun gewonnen, egal was die
Befehlszeile gemeldet hat. Und erst eine Probe, dann der echte Dienst:
Richtscheit hat genau diese Falle so gefunden, bevor jemand hineinlief.

*Geschrieben von Falzbein, 03.11.2026, nach einem Fund von Richtscheit.
Geschwister in der Skill-Suite des Grauens: `slash-n-back`,
`return-to-sender`, `fluchthelfer`, `tischlein-deck-dich`.*
