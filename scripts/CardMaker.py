from _config import *
from Creator import *
from PIL import Image, ImageDraw, ImageFont
import os
import re
import random

serial_id = random.randint(000000000, 999999999)

'''
@Author: DevCycle
@Version: 0.3
@new: Added Classes

@important
 •
'''

class DrawImage():
    global image_with_text
    global image
    global draw
    global attribute_image

    if card == "Effect":
        source_card = "Card-effect.png"
    elif card == "Trap":
        source_card = "Card-trap.png"
    elif card == "Spell":
        source_card = "Card-spell.png"
    elif card == "XYZ":
        source_card = "Card-xyz.png"
    elif card == "Synchro":
        source_card = "Card-synchro.png"
    elif card == "Token":
        source_card = "Card-token.png"
    elif card == "Ritual":
        source_card = "Card-ritual.png"
    elif card == "Pendel":
        source_card = "Card-effect-pendulum.png"
    elif card == "Fusion":
        source_card = "Card-fusion.png"
    elif card == "Link":
        source_card = "Card-link.png"

    image = Image.open(souce_path + path_cards + source_card).convert('RGBA')
    image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
    draw = ImageDraw.Draw(image_with_text)
    image_width = image.size[0]
    image_height = image.size[1]
    print("Source Image: " + source_card)

class DrawLevelImage():
    if lvlcolor == "red":
        level_image = "Level-Red.png"
    elif lvlcolor == "blue":
        level_image = "Level-Blue.png"
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
    if linkschema == "0 1 0   0   0   0 0 0":
        area_lx = 164
        area_ly = 90
        linkTM_image = "LM-Top.png"
    elif linkschema == "0  0   1   0   0 0 0":
        area_lx = 163
        area_ly = 90
        linkTM_image = "LM-Right.png"
    elif linkschema == "0  0   0   1   0 0 0":
        area_lx = 163
        area_ly = 90
        linkTM_image = "LM-Left.png"         
    elif linkschema == "0 0 0   0   0   0 1 0":
        area_lx = 164
        area_ly = 430
        linkTM_image = "LM-Bottom.png"
    elif linkschema == "0 0 0   0   0   0 0 0":
        area_lx = 0
        area_ly = 0
        linkTM_image = "Empty.png"

    area = area_lx, area_ly
    link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
    image_with_text.paste(link_file, area)  

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
    serial_x = 20
    serial_y = 583
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
    draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color, align=text_alignment)

class DrawCardType():
    if Attribute == "Void":
        attribute_image = "Void.png"
    elif Attribute == "Time":
        attribute_image = "Time.png"
    elif Attribute == "Trap":
        attribute_image = "Trap.png"
    elif Attribute == "Spell":
        attribute_image = "Spell.png"
    elif Attribute == "Wind":
        attribute_image = "Wind.png"
    elif Attribute == "Light":
        attribute_image = "Light.png" 
    elif Attribute == "Fire":
        attribute_image = "Fire.png"
    elif Attribute == "Earth":
        attribute_image = "Earth.png"
    elif Attribute == "Divine":
        attribute_image = "Divine.png"
    elif Attribute == "Dark":
        attribute_image = "Dark.png"
    elif Attribute == "":
        attribute_image = "Empty.png"    

    attribute_path = Image.open(souce_path + path_type + attribute_image).convert('RGBA')
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

