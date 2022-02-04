from _config import *
from PIL import Image, ImageDraw, ImageFont
import os
import re

'''
@Author: DevCycle
@Version: 0.3
@new: Added Classes
'''

# Your Card Infos
Title       = "Fire Dragon"
Attribute   = "Void"
Level       = 6
Type        = "[Dragon / Effect]"
Description = "The Ultimate Power"
Attack      = "2400"
Defense     = "2000"

class DrawImage():
    global image_with_text
    global image
    global draw

    source_card = "Card-effect.png"
    image = Image.open(souce_path + source_card).convert('RGBA')
    image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
    draw = ImageDraw.Draw(image_with_text)
    image_width = image.size[0]
    image_height = image.size[1]

    print("Source Image: " + source_card)

class DrawLevelImage():
    level_image = "Level-Red.png"
    level_file = Image.open(souce_path + level_image)
    level_file.resize((8,8),Image.ANTIALIAS)
    for i in range(Level):
        area_x = area_x - 27
        area = area_x, area_y
        image_with_text.paste(level_file, area) 

class DrawImageCard():
    image_card = "firedragon.jpg"
    area = 51, 113 

    card_image = Image.open(souce_path + image_card)
    card = card_image.resize((320,320),Image.ANTIALIAS)
    image_with_text.paste(card, area)
    print("Card Image: " + image_card + "\n")

class DrawText():
    title_x = 0
    title_y = 0
    type_x = 0
    type_y = 0
    desc_x = 0
    desc_y = 0
    title_x = 30
    title_y = 28 
    type_x = 35
    type_y = 463
    desc_x = 35
    desc_y = 483
    atk_x = 265
    atk_y = 559
    def_x = 350
    def_y = 559
    fontsize -= 1

    font = ImageFont.truetype(fontfile1, fontsize)
    font1 = ImageFont.truetype(fontfile3, fontsize1)
    font2 = ImageFont.truetype(fontfile1, fontsize2)
    font3 = ImageFont.truetype(fontfile1, fontsize3)

    print("Final font size: ",fontsize)

    draw.text((title_x, title_y), Title, font=font, fill=txt_color, align=text_alignment)
    draw.text((type_x, type_y), Type, font=font1, fill=txt_color, align=text_alignment)
    draw.text((desc_x, desc_y), Description, font=font2, fill=txt_color, align=text_alignment)
    draw.text((atk_x, atk_y), Attack, font=font3, fill=txt_color, align=text_alignment)
    draw.text((def_x, def_y), Defense, font=font3, fill=txt_color, align=text_alignment)

class DrawCardType():
    if Attribute == "Void":
        attribute_image = "Void.png"
        attribute_path = Image.open(souce_path + attribute_image)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_path, area)
    elif Attribute == "Time":
        attribute_image = "Time.png"
        attribute_path = Image.open(souce_path + attribute_image)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_path, area)  

out = Image.alpha_composite(image, image_with_text)
out.show()

file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", Title).replace(" ", "_")+'.png'
out.save(os.path.join(output_dir, file_name))

