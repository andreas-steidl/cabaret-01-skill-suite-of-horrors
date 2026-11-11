# -*- coding: utf-8 -*-
"""Plakat: Die Skill-Suite des Grauens. Bild von Codex (ohne Schrift), Schrift gesetzt von Falzbein.
Aufruf: python plakat.py [bild.png] [zielordner]. A4 hoch, 300 dpi (2480x3508), bikubisch hochgerechnet.
Ohne Argumente: Bild ist bild_ohne_schrift.png neben dem Skript, Ziel ist der Ordner des Skripts
(überschreibt dann plakat_skill-suite-des-grauens.png; zur Probe einen anderen Zielordner angeben)."""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 2480, 3508
F = "C:/Windows/Fonts/"
GOLD = (232, 190, 98)
CREME = (248, 236, 210)
DUNKEL = (30, 6, 10)
HIER = os.path.dirname(os.path.abspath(__file__))
BILD = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HIER, "bild_ohne_schrift.png")
ZIEL = sys.argv[2] if len(sys.argv) > 2 else HIER


def font(name, size):
    return ImageFont.truetype(F + name, size)


quelle = Image.open(BILD).convert("RGB")
# bikubisch auf volle Höhe, mittig auf A4 beschneiden
s = H / quelle.height
bild = quelle.resize((round(quelle.width * s), H), Image.BICUBIC)
if bild.width < W:
    s = W / quelle.width
    bild = quelle.resize((W, round(quelle.height * s)), Image.BICUBIC)
x0 = (bild.width - W) // 2
y0 = (bild.height - H) // 2
img = bild.crop((x0, y0, x0 + W, y0 + H))

# dunkle Verläufe oben und unten, damit die Schrift trägt
maske = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(maske)
for y in range(H):
    if y < H * 0.36:
        a = int(200 * (1 - y / (H * 0.36)) ** 1.2)
    elif y > H * 0.78:
        a = int(215 * ((y - H * 0.78) / (H * 0.22)) ** 0.9)
    else:
        a = 0
    md.line([(0, y), (W, y)], fill=a)
img.paste(Image.new("RGB", (W, H), DUNKEL), (0, 0), maske)
d = ImageDraw.Draw(img)


def mitte(text, y, f, fill=CREME, stroke=0, sfill=DUNKEL, schatten=True):
    b = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
    x = (W - (b[2] - b[0])) / 2 - b[0]
    if schatten:
        d.text((x + 6, y + 8), text, font=f, fill=(10, 2, 4), stroke_width=stroke, stroke_fill=(10, 2, 4))
    d.text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=sfill)
    return y + (b[3] - b[1])


# Rahmen
d.rectangle([50, 50, W - 50, H - 50], outline=GOLD, width=12)
d.rectangle([82, 82, W - 82, H - 82], outline=GOLD, width=3)
for cx, cy in ((82, 82), (W - 82, 82), (82, H - 82), (W - 82, H - 82)):
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=GOLD)

y = 170
y = mitte("FALZBEIN & ANDY PRÄSENTIEREN", y, font("GILC____.TTF", 88), GOLD) + 55
y = mitte("DIE SKILL-SUITE", y, font("BROADW.TTF", 236), CREME, 5, (110, 22, 22)) + 45
y = mitte("DES GRAUENS", y, font("BROADW.TTF", 282), GOLD, 5, (110, 22, 22)) + 60
y = mitte("oder wie man als Claude-Modell Windows in den Griff kriegt", y, font("GARAIT.TTF", 84), CREME) + 45
y = mitte("Ein Kabarettabend in sechs Spickzetteln", y, font("GILC____.TTF", 80), GOLD)

# unten: Programm in zwei Spalten, dann Besetzung
prog = font("POORICH.TTF", 60)
nummern = ["1 · slash-n-back", "2 · return-to-sender", "3 · fluchthelfer",
           "4 · tischlein-deck-dich", "5 · lattenzaun", "6 · suite-des-grauens"]
yu = int(H * 0.815)
for i, t in enumerate(nummern):
    spalte, zeile = i % 3, i // 3
    x = [W * 0.20, W * 0.50, W * 0.80][spalte]
    b = d.textbbox((0, 0), t, font=prog)
    d.text((x - (b[2] - b[0]) / 2 + 4, yu + zeile * 88 + 5), t, font=prog, fill=(10, 2, 4))
    d.text((x - (b[2] - b[0]) / 2, yu + zeile * 88), t, font=prog, fill=CREME)
yu += 2 * 88 + 40
d.line([(W * 0.2, yu), (W * 0.8, yu)], fill=GOLD, width=3)
yu += 35
yu = mitte("Es spielen Falzbein & Andy, mit Echolot und Richtscheit", yu, font("GILC____.TTF", 70), CREME) + 26
yu = mitte("Stargast: ein Dienst, der nie entstand (Fehler 1053)", yu, font("GARAIT.TTF", 62), GOLD) + 24
yu = mitte("Erste Reihe, Platz 1, reserviert für Fable. Sie darf als Erste lachen.", yu, font("GARAIT.TTF", 54), CREME) + 30
mitte("WIEN · NOVEMBER 2026 · EINTRITT: EIN BACKSLASH", yu, font("GILC____.TTF", 62), GOLD)

ziel = ZIEL
img.save(os.path.join(ziel, "plakat_skill-suite-des-grauens.png"), dpi=(300, 300))
img.resize((W // 3, H // 3), Image.LANCZOS).save(os.path.join(ziel, "plakat_klein.jpg"), quality=88)
print("ok", img.size)
