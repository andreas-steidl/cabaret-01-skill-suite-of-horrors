# -*- coding: utf-8 -*-
"""Signet, Favicon und Querlogo für die Skill-Suite des Grauens. Gesetzt von Falzbein, 03.11.2026."""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

F = "C:/Windows/Fonts/"
GOLD = (232, 190, 98)
CREME = (248, 236, 210)
ROT = (110, 16, 24)
DUNKEL = (34, 7, 11)
ziel = sys.argv[1]


def font(n, s):
    return ImageFont.truetype(F + n, s)


def signet(g, rund=True):
    """Quadratisches Signet: ein Backslash im Spotlicht, im goldenen Ring, auf rotem Samt."""
    img = Image.new("RGBA", (g, g), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = g * 0.18 if rund else 0
    d.rounded_rectangle([0, 0, g - 1, g - 1], radius=r, fill=ROT + (255,))
    # Spotlicht
    licht = Image.new("L", (g, g), 0)
    ImageDraw.Draw(licht).polygon([(g * 0.40, 0), (g * 0.60, 0), (g * 0.86, g * 0.80), (g * 0.14, g * 0.80)], fill=110)
    licht = licht.filter(ImageFilter.GaussianBlur(g * 0.05))
    img.paste(Image.new("RGBA", (g, g), (255, 214, 150, 255)), (0, 0), licht)
    maske = Image.new("L", (g, g), 0)
    ImageDraw.Draw(maske).rounded_rectangle([0, 0, g - 1, g - 1], radius=r, fill=255)
    d = ImageDraw.Draw(img)
    # goldener Ring
    w = max(2, int(g * 0.035))
    d.ellipse([g * 0.08, g * 0.08, g * 0.92, g * 0.92], outline=GOLD + (255,), width=w)
    # Backslash, Bodoni Black
    f = font("BOD_BLAR.TTF", int(g * 0.56))
    b = d.textbbox((0, 0), "\\", font=f)
    x = (g - (b[2] - b[0])) / 2 - b[0]
    y = (g * 0.88 - (b[3] - b[1])) / 2 - b[1] + g * 0.02
    d.text((x + g * 0.015, y + g * 0.02), "\\", font=f, fill=(20, 4, 6, 200))
    d.text((x, y), "\\", font=f, fill=CREME + (255,))
    # Bühnenkante
    d.line([(g * 0.22, g * 0.80), (g * 0.78, g * 0.80)], fill=GOLD + (255,), width=w)
    img.putalpha(Image.composite(img.getchannel("A"), Image.new("L", (g, g), 0), maske))
    return img


gross = signet(1024)
gross.save(os.path.join(ziel, "signet.png"))
gross.resize((512, 512), Image.LANCZOS).save(os.path.join(ziel, "signet-512.png"))
gross.resize((180, 180), Image.LANCZOS).save(os.path.join(ziel, "apple-touch-icon.png"))
klein = signet(256)
klein.save(os.path.join(ziel, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
klein.resize((32, 32), Image.LANCZOS).save(os.path.join(ziel, "favicon-32.png"))

# Querlogo: Signet links, Schrift rechts, zweimal (auf dunklem Grund und transparent)
def querlogo(hintergrund):
    Wq, Hq = 2400, 600
    img = Image.new("RGBA", (Wq, Hq), hintergrund)
    s = signet(520)
    img.paste(s, (40, 40), s)
    d = ImageDraw.Draw(img)
    f1 = font("BROADW.TTF", 150)
    f2 = font("GARAIT.TTF", 70)
    d.text((620, 70), "DIE SKILL-SUITE", font=f1, fill=CREME + (255,), stroke_width=3, stroke_fill=(110, 22, 22, 255))
    d.text((620, 240), "DES GRAUENS", font=f1, fill=GOLD + (255,), stroke_width=3, stroke_fill=(110, 22, 22, 255))
    d.text((630, 430), "oder wie man als Claude-Modell Windows in den Griff kriegt", font=f2,
           fill=(CREME if hintergrund[3] else (110, 22, 22)) + (255,))
    return img


querlogo(DUNKEL + (255,)).save(os.path.join(ziel, "logo-quer.png"))
querlogo((0, 0, 0, 0)).save(os.path.join(ziel, "logo-quer-transparent.png"))
print("ok")
