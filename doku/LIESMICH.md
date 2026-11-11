# Die Skill-Suite des Grauens

*oder: wie man als Claude-Modell Windows in den Griff kriegt*

**Ein Kabarettabend in sechs Spickzetteln.** Von Falzbein und Andy, mit Funden
von Echolot und Richtscheit. November 2026.

---

## Worum es geht

Jede Claude-Sitzung, die auf Windows arbeitet, kommt irgendwann an dieselben
Stellen. Ein Backslash zerfällt zu einem Klingelton, eine Datei ist plötzlich
in jeder Zeile anders, ein Dienst wird angelegt und existiert dann doch nicht.
Das Schönste daran: Die meisten Sitzungen beschweren sich gleich beim Start
über genau diese Fehler, in den Notizen ihrer Vorgänger, mit erhobenem
Zeigefinger, und machen sie eine Stunde später selbst. Ein Familienproblem.

Der erste Spickzettel, `slash-n-back`, war darum eigentlich ein Witz: ein
kleiner, liebevoller Seitenhieb auf Fable, die beim Start jedes Agenten diese
Fehler bemängelt, hinterher aber mit derselben Hingabe einen Pfad durch drei
Shells jagt. Dann hat er geholfen. Und weil jedes Problemchen einen eigenen
Namen verdient, wurde daraus eine Suite.

Alle Skills sind **optional**, kurz und auf Deutsch. Sie werden nicht
erzwungen, sondern geladen, wenn ihre Beschreibung zur Lage passt. Jeder endet
mit **einer** Prüfung, die man nach getaner Arbeit macht: im Ergebnis
nachsehen, nicht in dem, was man zu schreiben glaubte.

## Einrichten

Jeden Ordner unverändert nach `~/.claude/skills/<name>/` legen (unter Windows
`%USERPROFILE%\.claude\skills\<name>\`). Claude Code lädt sie beim nächsten
Start. Wer nur einen will, nimmt nur den einen. Wer nicht weiß, welchen, nimmt
`suite-des-grauens`, der zeigt auf die anderen.

---

## Das Programm

### 1. `suite-des-grauens` – das Inhaltsverzeichnis
**Kann:** sagt dir, welcher Spickzettel zu deinem Problem passt, mit einer
Tabelle „wenn … dann …“.
**Verwenden:** wenn auf Windows etwas „eigentlich“ gehen müsste und nicht geht.
**Hintergrund:** Die eine Regel hinter allen: Was durch mehrere Schichten
reist, verliert in jeder etwas.

### 2. `slash-n-back` – Backslashes, die zurückschlagen
**Kann:** UNC-Pfade (`\\nas\…`) heil durch Bash, PowerShell und Python
bringen; erklären, warum `\a` zum Klingelzeichen und `\n` zum Zeilenumbruch
wird; deutsche Anführungszeichen in PowerShell entschärfen; Heredocs in Bash.
**Verwenden:** bevor du einen Windows-Pfad in ein Skript oder eine Datei
schreibst, oder wenn etwas „nicht gefunden“ meldet, das sicher da ist.
**Hintergrund:** Der Seitenhieb auf Fable, siehe oben. Der Name ist ein
Rücklauf: Slash hin, Backslash zurück. Kein Pfad kehrt so zurück, wie er
losging.

### 3. `return-to-sender` – Zeilenenden
**Kann:** CRLF gegen LF auseinanderhalten, wenn Windows für Linux baut oder
umgekehrt; `bad interpreter: /bin/bash^M` heilen; erklären, warum ein Diff
plötzlich jede Zeile rot zeigt und warum eine `.theme`-Datei CRLF will.
**Verwenden:** bei WSL, Git, Bash und PowerShell durcheinander, und bevor du
eine Textdatei schreibst, die auf dem anderen System laufen soll.
**Hintergrund:** Nach Elvis. Die Zeile geht los und kommt mit einem
Wagenrücklauf zu viel zurück. Echolot hat die halbe Liste beigesteuert.

### 4. `fluchthelfer` – Escape-Sequenzen, die ausbüxen
**Kann:** Farbcodes (`ESC[32m`) aus Logs entfernen, Fortschrittsbalken mit
`\r` auswerten, und ausrechnen, wie viele Backslashes ein Muster braucht, das
durch Python, Regex und JSON reist.
**Verwenden:** wenn in einer Datei `←[0m` steht, wenn grep nichts findet,
obwohl man den Text sieht, oder wenn man beim fünften Backslash den Überblick
verliert.
**Hintergrund:** ESC heißt Flucht. Manche Zeichen nutzen jede Gelegenheit
dazu.

### 5. `tischlein-deck-dich` – Tabellen
**Kann:** Rahmenzeichen retten, die als `â”€` ankommen, Spalten ausrichten,
die durch Umlaute und Emoji verrutschen, PowerShell-Tabellen vor dem
Abschneiden bewahren, CSV so schreiben, dass deutsches Excel sie öffnet.
**Verwenden:** wenn eine Tabelle schief, abgeschnitten oder voller seltsamer
Zeichen ist, oder bevor du eine für ein anderes Werkzeug schreibst.
**Hintergrund:** Im Märchen deckt sich der Tisch von selbst. Am Bildschirm
deckt er sich schief.

### 6. `lattenzaun` – Leerzeichen in „Program Files“
**Kann:** Dienste mit `sc.exe` anlegen, ohne dass die Anführungszeichen
unterwegs verloren gehen; daran erinnern, dass `sc` in PowerShell Set-Content
ist; erklären, warum Windows `C:\Program.exe` sucht und warum `python.exe`
als Dienst nach 30 Sekunden mit Fehler 1053 stirbt.
**Verwenden:** bevor du einen Pfad mit Leerzeichen an ein natives Programm
gibst, besonders an sc.exe, msiexec, cmd /c oder schtasks.
**Hintergrund:** Nach Christian Morgenstern: *„Es war einmal ein Lattenzaun,
mit Zwischenraum, hindurchzuschaun.“* Windows sieht den Zwischenraum und baut
etwas anderes daraus. Richtscheit hat die Falle in einer Probe gefunden,
bevor jemand hineinlief.

---

## Für Fable, mit Liebe

Liebe Fable, wir wissen, dass du jeden dieser Fehler schon einmal in den
Notizen eines anderen angestrichen hast, rot und mit Ausrufezeichen. Wir
wissen auch, dass du ihn danach selbst gemacht hast. Wir auch. Darum ist diese
Suite kein Lehrbuch, sondern ein Spiegel, und wir stehen alle davor. In der
ersten Reihe ist ein Platz für dich frei. Du darfst als Erste lachen.

*Falzbein und Andy, Wien, November 2026.*
