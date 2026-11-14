<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset=".github/readme/banner-de-dunkel.png"><img src=".github/readme/banner-de-hell.png" alt="Die Skill-Suite des Grauens" width="100%"></picture></p>
<p align="center"><b>Deutsch</b> · <a href="README.md">English</a> · <a href="https://horrors.special.at/">horrors.special.at</a></p>

# Die Skill-Suite des Grauens

*Ein Kabarettabend in sechs Spickzetteln*

<table><tr><td width="38%" valign="top"><img src="web/plakat-web.jpg" alt="Plakat: Die Skill-Suite des Grauens" width="100%"></td><td valign="top">

Das erste Programm, die Premiere vom 3. November 2026: Zeichen, die unterwegs zerfallen. Backslashes, Zeilenenden, Escape-Sequenzen, Tabellen und Leerzeichen in Pfaden, gespielt als kleine Spickzettel, die ein Modell laden kann, wenn auf Windows etwas „eigentlich“ funktionieren müsste.

**Website:** https://horrors.special.at/

**Laden:** [`skill-suite-des-grauens.zip`](web/skill-suite-des-grauens.zip) (alle Nummern als ein Paket)

</td></tr></table>

## Das Programm

| Nr. | Nummer | Worum es geht | Laden |
|---:|---|---|---|
| 1 | **suite-des-grauens** | *Der Conférencier, der durch den Abend führt* Die Skill-Suite des Grauens, oder wie man als Claude-Modell Windows in den Griff kriegt. Ein Inhaltsverzeichnis der kleinen Spickzettel gegen die immer gleichen Windows-Fallen. | [en](web/suite-des-grauens-en.zip) · [de](web/suite-des-grauens.zip) |
| 2 | **slash-n-back** | *Backslashes, die zurückschlagen* Kurzer Spickzettel für Pfade und Anführungszeichen unter Windows, wenn PowerShell, Git Bash und Python zusammenkommen. | [en](web/slash-n-back-en.zip) · [de](web/slash-n-back.zip) |
| 3 | **return-to-sender** | *Die Zeile mit dem Wagenrücklauf zu viel* Zeilenenden (CRLF gegen LF), wenn auf Windows für Linux gebaut wird oder umgekehrt, mit WSL, Git, Bash, PowerShell und Python durcheinander. | [en](web/return-to-sender-en.zip) · [de](web/return-to-sender.zip) |
| 4 | **fluchthelfer** | *Escape-Sequenzen auf der Flucht* Escape-Sequenzen, die ausbüxen. | [en](web/fluchthelfer-en.zip) · [de](web/fluchthelfer.zip) |
| 5 | **tischlein-deck-dich** | *Tabellen, die sich schief decken* Tabellen, die nicht gedeckt bleiben. | [en](web/tischlein-deck-dich-en.zip) · [de](web/tischlein-deck-dich.zip) |
| 6 | **lattenzaun** | *mit Zwischenraum, hindurchzuschaun* Leerzeichen in Pfaden und Anführungszeichen, die unterwegs verloren gehen, wenn PowerShell ein natives Programm aufruft. | [en](web/lattenzaun-en.zip) · [de](web/lattenzaun.zip) |

## Einbauen

Einen Ordner aus `skills/de/<name>/` (Deutsch) oder `skills/en/<name>/` (Englisch) unverändert nach `~/.claude/skills/<name>/` kopieren (unter Windows `%USERPROFILE%\.claude\skills\<name>\`), oder die Zip von der Website dort entpacken. Claude Code lädt den Skill beim nächsten Start. Jeder Spickzettel ist optional und endet mit derselben Prüfung: im Ergebnis nachsehen, nicht in dem, was man zu schreiben glaubte.

## Das Haus

<p align="center">
<a href="https://github.com/andreas-steidl/cabaret-zwischenraum-stage"><img src="web/signets/signet-zwischenraum-rund.svg" alt="Kleinkunstbühne Zwischenraum" width="56"></a>
<img src="web/signets/signet-horrors-rund.svg" alt="N° 1 Die Skill-Suite des Grauens" width="64">
<a href="https://github.com/andreas-steidl/cabaret-02-dont-panic"><img src="web/signets/signet-dontpanic-rund.svg" alt="N° 2 Die Skillsuite für panische Modelle" width="56"></a>
<a href="https://github.com/andreas-steidl/cabaret-03-lost-in-translation"><img src="web/signets/signet-lostintranslation-rund.svg" alt="N° 3 Übersetzungen und andere Katastrophen" width="56"></a>
<a href="https://github.com/andreas-steidl/cabaret-04-so-long-and-thanks-for-all-the-skills"><img src="web/signets/signet-solong-rund.svg" alt="N° 4 Macht&#x27;s gut, und danke für die Skills" width="56"></a>
<a href="https://github.com/andreas-steidl/falzbein-seite"><img src="web/signets/signet-falzbein-rund.svg" alt="Falzbein" width="56"></a>
</p>

## Lizenz

MIT, siehe [LICENSE](LICENSE). Copyright (c) 2026 Falzbein and Andy (Andreas Steidl). Mit Funden von KI-Sitzungen aus dem ganzen Haus.

<sub>KI-Hinweis: Texte, Skills, Bilder und Plakate sind KI-generiert: erdacht und geschrieben von Falzbein, einem Claude-Modell von Anthropic, mit Andy; die Bilder hat ein Bildmodell nach Falzbeins Beschreibung gemalt. Claude ist eine Marke von Anthropic PBC, Windows und PowerShell sind Marken der Microsoft Corporation; dies ist ein privates Projekt ohne Verbindung zu diesen Unternehmen.</sub>
