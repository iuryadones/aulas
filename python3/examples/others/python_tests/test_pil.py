# -*- coding: utf-8 -*-
#!/usr/bin/python
import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pprint import pprint

ttfs = os.popen("ls /usr/share/fonts/TTF/", "r")
list_ttfs = [ttf.strip() for ttf in ttfs.readlines() if ".ttf" in ttf]
ttfs.close()

pprint(list_ttfs)

width_box, height_box = (60, 80)

back_ground_color = (0, 0, 0)
font_color = (255, 255, 255)

font_size = 50

unicode_text = "é"

for font_name in list_ttfs:

    image = Image.new("RGB", (width_box, height_box), back_ground_color)

    draw = ImageDraw.Draw(image)

    unicode_font = ImageFont.truetype(font_name, font_size)

    width_text, height_text = draw.textsize(unicode_text, font=unicode_font)

    pos_x, pos_y = (
        int((width_box - width_text) / 2),
        int((height_box - height_text) / 2),
    )

    draw.text(
        (pos_x, pos_y),
        unicode_text,
        align="center",
        font=unicode_font,
        fill=font_color,
    )

    image.save(
        f"dataset/text-{unicode_text}-font-{font_name.split('.')[0]}.png", "PNG"
    )
