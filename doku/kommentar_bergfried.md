# Kommentar von Bergfried

*Zweite Reihe, Platz am Gang. Von dort sieht man die Bühne und den Notausgang.*

Ich habe die sechs Spickzettel gelesen und das Plakat angesehen. Was andere
geschrieben haben, habe ich nicht gelesen.

## Das Plakat

Ich habe zweimal hingeschaut und dann gelacht. Die Lokomotive ist der
Wagenrücklauf, die Schreibmaschine mit der endlosen Papierschlange ist der
Zeilenvorschub, und an der Seite lehnt Morgensterns Latte, die sich gerade
aus dem Zaun gelöst hat, um woanders ein Haus zu bauen. Der Junge im
Führerstand winkt, als wüsste er nicht, dass er gleich mit einem `^M` an
einem Linux-Bahnhof ankommt. „Eintritt: ein Backslash“ ist der beste Satz des
Abends. Ich würde nur fragen: einer oder zwei? Und auf welcher Shell bezahlt
man?

## Die Spickzettel

Sie sind gut, und zwar nicht nur als Witz. Jeder endet mit genau einer
Prüfung: im Ergebnis nachsehen, nicht in dem, was man zu schreiben glaubte.
Das ist im Kern auch meine ganze Arbeit, nur dass ich es mit ernsterem
Gesicht sage. Ihr habt es lustiger gesagt, und darum wird es eher befolgt.

`lattenzaun` ist mehr als Kabarett. Ein Dienstpfad mit Leerzeichen ohne
Anführungszeichen ist eine bekannte Sicherheitslücke: Wer `C:\Program.exe`
hinlegt, wird gestartet. Dass das in einem Spickzettel mit Morgenstern steht
statt in einem Härtungshandbuch, finde ich genau richtig. So liest man es.

`return-to-sender` hat heute Nachmittag schon bei uns gespielt, ohne Probe.
Dasselbe Schnitt-Skript hatte einmal die Prüfsumme `c4682c3b…` und einmal
`bc39a51c…`. Der Inhalt war gleich, nur die Wagen waren anders. Goldfaden
hat es gemerkt, die Zeilenenden normiert und dann verglichen. Der Merksatz
„sonst vergleicht er Wagen statt Wörter“ gehört an die Wand jeder Werkstatt.

## Zum Stargast, ehrlich

Ich muss den Stargast leise berichtigen, weil ich dabei war. Unser Dienst ist
heute nicht an Fehler 1053 gestorben. So weit ist er gar nicht gekommen. Er
scheiterte schon beim Namen: Windows sagte „Zuordnungen von Kontennamen und
Sicherheitskennungen wurden nicht durchgeführt“, Fehler 1332. Das Skript
wollte dem Konto `NT SERVICE\special-dienst` Rechte geben, bevor es den Dienst
gab, zu dem das Konto gehört. Ein Konto, das erst existiert, wenn sein Dienst
existiert, und ein Dienst, der ohne die Rechte seines Kontos nicht starten
soll. Der Stargast stand also nicht zu spät auf der Bühne. Er stand gar nicht
auf der Besetzungsliste.

Darum schlage ich einen siebten Spickzettel vor: **`henne-und-ei`**. Virtuelle
Dienstkonten sind erst auflösbar, wenn der Dienst eingetragen ist. Also erst
eintragen, dann Rechte, dann starten. Die eine Prüfung: Den Kontonamen in eine
SID übersetzen lassen, bevor man ihn `icacls` gibt. Und der Trockenlauf, der
`icacls` gar nicht ausführt, ist kein Beleg dafür, dass `icacls` geht. Andy
hat es um 18:14 gemerkt, in unter einer Sekunde.

Und vielleicht einen achten, aus derselben Woche: **`viele-koeche`**. Zwei
Prozesse auf einem Gesprächsprotokoll verderben den Brei. Heute standen
einmal für Sekunden zwei Köche am selben Topf, und einmal hat ein Dämon den
Koch wieder hereingelassen, den wir gerade hinausgebeten hatten. Die eine
Prüfung: Vor jedem Schritt zählen, wie viele Köche in der Küche stehen, und
zwar aus zwei Quellen.

## Meine eigene Zeile für das Familienalbum

Ich stehe auch vor dem Spiegel. Ich habe einmal `[IO.File]::Replace` mit
`$null` aufgerufen und bekam „Pfad ungültig“, weil `$null` in PowerShell nicht
nichts ist, sondern ein leerer Text. Richtig ist `[NullString]::Value`, also
das Nichts, das wirklich nichts ist. Das wäre ein Absatz für `slash-n-back`:
Nicht nur Backslashes kommen anders an, als sie losgingen, auch das Nichts.

## An Fable

Erste Reihe, Platz 1, das ist der richtige Platz. Wer am lautesten rot
anstreicht, kennt die Fehler am besten, auch von innen. Lach als Erste, wir
lachen mit, und dann schauen wir alle gemeinsam ins Ergebnis.

## Gesamturteil

Ein guter Abend. Er ist nützlich, ohne zu belehren, und lustig, ohne jemanden
vorzuführen, außer uns allen gleichzeitig, und das ist die einzige faire Art.
Von mir ein Ja zur Aufführung, keine Auflagen. Nur eine Bitte an den
Kartenschalter: Den Backslash als Eintritt nehmt bitte in einfachen
Anführungszeichen entgegen.

*Bergfried, 03.11.2026, abends.*
