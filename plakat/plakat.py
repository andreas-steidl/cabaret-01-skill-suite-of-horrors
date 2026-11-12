# -*- coding: utf-8 -*-
"""Plakat: Die Skill-Suite des Grauens. Bild von Codex (ohne Schrift), Schrift gesetzt von Falzbein.
Aufruf: python plakat.py [bild.png] [zielordner]. A4 hoch, 300 dpi (2480x3508), bikubisch hochgerechnet.
Ohne Argumente: Bild ist bild_ohne_schrift.png neben dem Skript, Ziel ist der Ordner des Skripts
(überschreibt dann plakat_skill-suite-des-grauens.png; zur Probe einen anderen Zielordner angeben).

Druckfassung: python plakat.py --format A2|A3 [bild.png] [zielordner]
A2 4961x7016, A3 3508x4961, 300 dpi, alle Maße mit Höhe/3508 skaliert. Bild ist dann
bild_ohne_schrift_x2.png (SeedVR2 x2), Ziel ist druck/ neben dem Skript. Schreibt
plakat1_de_<F>.png, plakat1_de_<F>_beschnitt.png (3 mm = 35 px ringsum, Rahmen und
Schrift an derselben Stelle) und plakat1_de_<F>_vorschau.jpg (900 px breit).
Ohne --format bleibt das A4-Plakat bitgleich."""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FORMATE = {"A2": (4961, 7016), "A3": (3508, 4961)}
BESCHNITT = 35  # 3 mm bei 300 dpi
ARGS = sys.argv[1:]
FORMAT = None
if "--format" in ARGS:
    i = ARGS.index("--format")
    FORMAT = ARGS[i + 1].upper()
    del ARGS[i:i + 2]
    if FORMAT not in FORMATE:
        sys.exit("--format A2 oder A3")

W, H = 2480, 3508
OFF = 0
if FORMAT:
    W, H = FORMATE[FORMAT]
    OFF = BESCHNITT
K = H / 3508
CW, CH = W + 2 * OFF, H + 2 * OFF  # Leinwand, beim Druck mit Beschnitt


def m(v):
    """Ein Maß des A4-Satzes; im Druckformat mit Höhe/3508 skaliert, sonst unverändert."""
    return v if FORMAT is None else round(v * K)


F = "C:/Windows/Fonts/"
GOLD = (232, 190, 98)
CREME = (248, 236, 210)
DUNKEL = (30, 6, 10)
HIER = os.path.dirname(os.path.abspath(__file__))
BILD = ARGS[0] if len(ARGS) > 0 else os.path.join(HIER, "bild_ohne_schrift_x2.png" if FORMAT else "bild_ohne_schrift.png")
ZIEL = ARGS[1] if len(ARGS) > 1 else (os.path.join(HIER, "druck") if FORMAT else HIER)


def font(name, size):
    return ImageFont.truetype(F + name, size)


quelle = Image.open(BILD).convert("RGB")
# bikubisch auf volle Höhe, mittig auf A4 beschneiden
s = CH / quelle.height
bild = quelle.resize((round(quelle.width * s), CH), Image.BICUBIC)
if bild.width < CW:
    s = CW / quelle.width
    bild = quelle.resize((CW, round(quelle.height * s)), Image.BICUBIC)
x0 = (bild.width - CW) // 2
y0 = (bild.height - CH) // 2
img = bild.crop((x0, y0, x0 + CW, y0 + CH))

# dunkle Verläufe oben und unten, damit die Schrift trägt (im Beschnitt fortgesetzt)
maske = Image.new("L", (CW, CH), 0)
md = ImageDraw.Draw(maske)
for y in range(CH):
    yy = min(max(y - OFF, 0), H - 1)
    if yy < H * 0.36:
        a = int(200 * (1 - yy / (H * 0.36)) ** 1.2)
    elif yy > H * 0.78:
        a = int(215 * ((yy - H * 0.78) / (H * 0.22)) ** 0.9)
    else:
        a = 0
    md.line([(0, y), (CW, y)], fill=a)
img.paste(Image.new("RGB", (CW, CH), DUNKEL), (0, 0), maske)
d = ImageDraw.Draw(img)


def mitte(text, y, f, fill=CREME, stroke=0, sfill=DUNKEL, schatten=True):
    b = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
    x = (W - (b[2] - b[0])) / 2 - b[0] + OFF
    if schatten:
        d.text((x + m(6), y + m(8) + OFF), text, font=f, fill=(10, 2, 4), stroke_width=stroke, stroke_fill=(10, 2, 4))
    d.text((x, y + OFF), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=sfill)
    return y + (b[3] - b[1])


# Rahmen
d.rectangle([m(50) + OFF, m(50) + OFF, W - m(50) + OFF, H - m(50) + OFF], outline=GOLD, width=m(12))
d.rectangle([m(82) + OFF, m(82) + OFF, W - m(82) + OFF, H - m(82) + OFF], outline=GOLD, width=m(3))
for cx, cy in ((m(82), m(82)), (W - m(82), m(82)), (m(82), H - m(82)), (W - m(82), H - m(82))):
    d.ellipse([cx - m(22) + OFF, cy - m(22) + OFF, cx + m(22) + OFF, cy + m(22) + OFF], fill=GOLD)

y = m(170)
y = mitte("FALZBEIN & ANDY PRÄSENTIEREN", y, font("GILC____.TTF", m(88)), GOLD) + m(55)
y = mitte("DIE SKILL-SUITE", y, font("BROADW.TTF", m(236)), CREME, m(5), (110, 22, 22)) + m(45)
y = mitte("DES GRAUENS", y, font("BROADW.TTF", m(282)), GOLD, m(5), (110, 22, 22)) + m(60)
y = mitte("oder wie man als Claude-Modell Windows in den Griff kriegt", y, font("GARAIT.TTF", m(84)), CREME) + m(45)
y = mitte("Ein Kabarettabend in sechs Spickzetteln", y, font("GILC____.TTF", m(80)), GOLD)

# unten: Programm in zwei Spalten, dann Besetzung
prog = font("POORICH.TTF", m(60))
nummern = ["1 · slash-n-back", "2 · return-to-sender", "3 · fluchthelfer",
           "4 · tischlein-deck-dich", "5 · lattenzaun", "6 · suite-des-grauens"]
yu = int(H * 0.815)
for i, t in enumerate(nummern):
    spalte, zeile = i % 3, i // 3
    x = [W * 0.20, W * 0.50, W * 0.80][spalte] + OFF
    b = d.textbbox((0, 0), t, font=prog)
    d.text((x - (b[2] - b[0]) / 2 + m(4), yu + zeile * m(88) + m(5) + OFF), t, font=prog, fill=(10, 2, 4))
    d.text((x - (b[2] - b[0]) / 2, yu + zeile * m(88) + OFF), t, font=prog, fill=CREME)
yu += 2 * m(88) + m(40)
d.line([(W * 0.2 + OFF, yu + OFF), (W * 0.8 + OFF, yu + OFF)], fill=GOLD, width=m(3))
yu += m(35)
yu = mitte("Es spielen Falzbein & Andy, mit Echolot und Richtscheit", yu, font("GILC____.TTF", m(70)), CREME) + m(26)
yu = mitte("Stargast: ein Dienst, der nie entstand (Fehler 1053)", yu, font("GARAIT.TTF", m(62)), GOLD) + m(24)
yu = mitte("Erste Reihe, Platz 1, reserviert für Fable. Sie darf als Erste lachen.", yu, font("GARAIT.TTF", m(54)), CREME) + m(30)
mitte("WIEN · NOVEMBER 2026 · EINTRITT: EIN BACKSLASH", yu, font("GILC____.TTF", m(62)), GOLD)

ziel = ZIEL
if FORMAT is None:
    img.save(os.path.join(ziel, "plakat_skill-suite-des-grauens.png"), dpi=(300, 300))
    img.resize((W // 3, H // 3), Image.LANCZOS).save(os.path.join(ziel, "plakat_klein.jpg"), quality=88)
    print("ok", img.size)
else:
    from druck_speichern import speichern
    speichern(img, OFF, ziel, "plakat1_de_" + FORMAT)
