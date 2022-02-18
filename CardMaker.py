from _config import *
from PIL import Image, ImageDraw, ImageFont
import os
import re

'''
@Author: DevCycle
@Version: 0.3
@new: Added Classes

@important
 •
'''

# Your Card Infos
card        = "Trap"
image_card  = "Placeholder.png"

auflage     = "1. Auflage"
card_id     = "UU01-DE001"

Title       = "Template - Trap"
Attribute   = "Trap"

title_color = "black"
desc_color  = "black"

Level       = 0
lvlcolor    = "red"

Type        = "[Trap]"
Description = "Descrption"

Attack      = ""
Defense     = ""

class DrawImage():
    global image_with_text
    global image
    global draw

    if card == "Effect":
        source_card = "Card-effect.png"
        image = Image.open(souce_path + path_cards + source_card).convert('RGBA')
        image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
        draw = ImageDraw.Draw(image_with_text)
        image_width = image.size[0]
        image_height = image.size[1]
        print("Source Image: " + source_card)
    elif card == "Trap":
        source_card = "Card-trap.png"
        image = Image.open(souce_path + path_cards + source_card).convert('RGBA')
        image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
        draw = ImageDraw.Draw(image_with_text)
        image_width = image.size[0]
        image_height = image.size[1]
        print("Source Image: " + source_card)
    elif card == "Spell":
        source_card = "Card-spell.png"
        image = Image.open(souce_path + path_cards + source_card).convert('RGBA')
        image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
        draw = ImageDraw.Draw(image_with_text)
        image_width = image.size[0]
        image_height = image.size[1]
        print("Source Image: " + source_card)
    elif card == "XYZ":
        source_card = "Card-xyz.png"
        image = Image.open(souce_path + path_cards + source_card).convert('RGBA')
        image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
        draw = ImageDraw.Draw(image_with_text)
        image_width = image.size[0]
        image_height = image.size[1]
        print("Source Image: " + source_card)
    elif card == "Synchro":
        source_card = "Card-synchro.png"
        image = Image.open(souce_path + path_cards + source_card).convert('RGBA')
        image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
        draw = ImageDraw.Draw(image_with_text)
        image_width = image.size[0]
        image_height = image.size[1]
        print("Source Image: " + source_card)

class DrawLevelImage():
    if lvlcolor == "red":
        level_image = "Level-Red.png"
        level_file = Image.open(souce_path + path_lvl + level_image)
        lvl_img = level_file.resize((25,25),Image.ANTIALIAS)
        for i in range(Level):
            area_x = area_x - 27
            area = area_x, area_y
            image_with_text.paste(lvl_img, area)
    elif lvlcolor == "blue":
        level_image = "Level-Blue.png"
        level_file = Image.open(souce_path + path_lvl + level_image)
        lvl_img = level_file.resize((25,25),Image.ANTIALIAS)
        for i in range(Level):
            area_x = area_x - 27
            area = area_x, area_y
            image_with_text.paste(lvl_img, area)  
    elif lvlcolor == "green":
        level_image = "Level-Green.png"
        level_file = Image.open(souce_path + path_lvl + level_image)
        lvl_img = level_file.resize((25,25),Image.ANTIALIAS)
        for i in range(Level):
            area_x = area_x - 27
            area = area_x, area_y
            image_with_text.paste(lvl_img, area)  

class DrawImageCard():
    area = 51, 113 

    card_image = Image.open(souce_path + path_cardimg + image_card)
    card = card_image.resize((320,320),Image.ANTIALIAS)
    image_with_text.paste(card, area)
    print("Card Image: " + image_card + "\n")

class DrawText():
    title_x = 30
    title_y = 28 
    type_x = 35
    type_y = 463
    auflage_x = 45
    auflage_y = 440
    card_id_x = 300
    card_id_y = 440
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
    font4 = ImageFont.truetype(fontfile1, fontsize4)

    print("Final font size: ",fontsize)

    draw.text((title_x, title_y), Title, font=font, fill=title_color, align=text_alignment)
    draw.text((type_x, type_y), Type, font=font1, fill=desc_color, align=text_alignment)
    draw.text((desc_x, desc_y), Description, font=font2, fill=desc_color, align=text_alignment)
    draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
    draw.text((def_x, def_y), Defense, font=font3, fill=desc_color, align=text_alignment)
    draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color, align=text_alignment)
    draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color, align=text_alignment)

class DrawCardType():
    if Attribute == "Void":
        attribute_image = "Void.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area)
    elif Attribute == "Time":
        attribute_image = "Time.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area)
    elif Attribute == "Trap":
        attribute_image = "Trap.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area)
    elif Attribute == "Spell":
        attribute_image = "Spell.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area) 
    elif Attribute == "Wind":
        attribute_image = "Wind.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area) 
    elif Attribute == "Light":
        attribute_image = "Light.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area)    
    elif Attribute == "Fire":
        attribute_image = "Fire.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area) 
    elif Attribute == "Earth":
        attribute_image = "Earth.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area) 
    elif Attribute == "Divine":
        attribute_image = "Divine.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area)
    elif Attribute == "Dark":
        attribute_image = "Dark.png"
        attribute_path = Image.open(souce_path + path_type + attribute_image)
        attribute_img = attribute_path.resize((40,40),Image.ANTIALIAS)
        area_x = 355
        area_y = 29
        area = area_x, area_y
        image_with_text.paste(attribute_img, area)

class CornerSign():
    corner_img = "Cornerdefault.png"
    attribute_path = Image.open(souce_path + path_extras + corner_img)
    attribute_img = attribute_path.resize((20,20),Image.ANTIALIAS)
    area_x = 387
    area_y = 580
    area = area_x, area_y
    image_with_text.paste(attribute_img, area)

out = Image.alpha_composite(image, image_with_text)
out.show()

file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", Title).replace(" ", "_")+'.png'
out.save(os.path.join(output_dir, file_name))

