from ast import Return
from _config import *
from Creator import *
from PIL import Image, ImageDraw
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
    global source_card
    global image_height
    global image_width

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

class DrawCardRarity():
    global tmpout
    tmpout = Image.alpha_composite(image, image_with_text)
    tmpout.save("tmpout.png")
    if rarity == "Secret Rare":
        area = 51, 113 
        draw.text((title_x, title_y), Title, font=font, fill="gold", align=text_alignment)
        draw.text((title_x, title_y), Title, font=font, fill="silver", align=text_alignment)
        card_image = Image.open(souce_path + path_rarity + "Secret-Rare.png")
        card = card_image.resize((320,320),Image.ANTIALIAS)
        image_with_text.paste(card, area)
        print("Card Rarity: Secret Rare")
    else:
        print("Card Rarity: None")
class DrawLinkArrow():
    global linkLevel
    linkLevel = 0

    tmpout = Image.alpha_composite(tmpout, image_with_text)
    tmpout.save("tmpout.png")
    if card == "Link":

        if linkField[0][0] == 1:
            linkTM_image = "LM-TopLefta.png"
            linkLevel = linkLevel + 1
        else:
            linkTM_image = "LM-TopLeft-false.png"

        area_lx = 35
        area_ly = 95
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)


        if linkField[0][1] == 1:
            linkTM_image = "LM-Top.png"
            linkLevel = linkLevel + 1
        else:    
            linkTM_image = "LM-Top-false.png"

        area_lx = 163
        area_ly = 89
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)


        if linkField[0][2] == 1:
            linkTM_image = "LM-TopRight.png"
            linkLevel = linkLevel + 1
        else:
            linkTM_image = "LM-TopRight-false.png"
        
        area_lx = 345
        area_ly = 95
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)


        if linkField[1][0] == 1:
            linkTM_image = "LM-Left.png"
            linkLevel = linkLevel + 1
        else:
            linkTM_image = "LM-Left-false.png"
        
        area_lx = 25
        area_ly = 225
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)


        if linkField[1][1] == 1:
            print("Empty")

        if linkField[1][2] == 1:
            linkTM_image = "LM-Right.png" 
            linkLevel = linkLevel + 1 
        else:
            linkTM_image = "LM-Right-false.png"
        
        area_lx = 370
        area_ly = 225
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)


        if linkField[2][0] == 1:
            linkTM_image = "LM-BottomLeft.png"
            linkLevel = linkLevel + 1
        else:
            linkTM_image = "LM-BottomLeft-false.png"

        area_lx = 35
        area_ly = 406
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)

        if linkField[2][1] == 1:
            linkTM_image = "LM-Bottom.png"  
            linkLevel = linkLevel + 1  
        else:
            linkTM_image = "LM-Bottom-false.png"  

        area_lx = 163
        area_ly = 430
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)


        if linkField[2][2] == 1:
            linkTM_image = "LM-BottomRight.png"
            linkLevel = linkLevel + 1
        else:
            linkTM_image = "LM-BottomRight-false.png"
        
        area_lx = 345
        area_ly = 405
        area = area_lx, area_ly
        link_file = Image.open(souce_path + path_linkarrow + linkTM_image)
        image_with_text.paste(link_file, area)

class DrawText():
    print("Final font size: ",fontsize)

    draw.text((title_x, title_y), Title, font=font, fill=title_color, align=text_alignment)
    draw.text((type_x, type_y), Type, font=font1, fill=desc_color, align=text_alignment)
    draw.text((desc_x, desc_y), Description, font=font2, fill=desc_color, align=text_alignment)
    draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color, align=text_alignment)

    if card == "XYZ":
        draw.text((title_x, title_y), Title, font=font, fill=title_color_xyz, align=text_alignment)
        draw.text((type_x, type_y), Type, font=font1, fill=desc_color, align=text_alignment)
        draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color_xyz, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color_xyz, align=text_alignment)
        draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color_xyz, align=text_alignment)

    elif card == "Trap":
        draw.text((title_x, title_y), Title, font=font, fill=title_color, align=text_alignment)
        draw.text((type_x, type_y), Type, font=font1, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color, align=text_alignment)
        draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color, align=text_alignment)            

    elif card == "Link":
        Defense = str(linkLevel)
        draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
        draw.text((375, def_y), Defense, font=font3, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), "", font=font4, fill=title_color, align=text_alignment)
    else:
        draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color, align=text_alignment)
        draw.text((def_x, def_y), Defense, font=font3, fill=desc_color, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color, align=text_alignment)

class DrawSpellTrapText():
    stText_x = 275
    stText_y = 77

    if card == "Trap":
        if cardkind == "Counter":
            draw.text((stText_x, stText_y), "[Trap     ]", font=font1, fill=title_color, align=text_alignment)
            cardkind_img = "Counter.png"
            symbol_path = Image.open(souce_path + path_symbol + cardkind_img)
            symbol_img = symbol_path.resize((17,17),Image.ANTIALIAS)
            stArea = stText_x + 50, stText_y + 1
            image_with_text.paste(symbol_img, stArea)
        if cardkind == "Continuous":
            draw.text((stText_x, stText_y), "[Trap     ]", font=font1, fill=title_color, align=text_alignment)
            cardkind_img = "Continuous.png"
            symbol_path = Image.open(souce_path + path_symbol + cardkind_img)
            symbol_img = symbol_path.resize((17,17),Image.ANTIALIAS)
            stArea = stText_x + 50, stText_y + 1
            image_with_text.paste(symbol_img, stArea)
        if cardkind == "":
            stText_x = 300
            stText_y = 77
            draw.text((stText_x, stText_y), "[Trap]", font=font1, fill=title_color, align=text_alignment)

    elif card == "Spell":
        if cardkind == "Counter":
            stText_x = 300
            stText_y = 77
            draw.text((stText_x, stText_y), "[Spell]", font=font1, fill=title_color, align=text_alignment) 
        if cardkind == "Continuous":
            draw.text((stText_x, stText_y), "[Spell    ]", font=font1, fill=title_color, align=text_alignment)
            cardkind_img = "Continuous.png"
            symbol_path = Image.open(souce_path + path_symbol + cardkind_img)
            symbol_img = symbol_path.resize((17,17),Image.ANTIALIAS)
            stArea = stText_x + 55, stText_y + 1
            image_with_text.paste(symbol_img, stArea)
        if cardkind == "":
            stText_x = 300
            stText_y = 77
            draw.text((stText_x, stText_y), "[Trap]", font=font1, fill=title_color, align=text_alignment)

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

class DrawCornerSign():
    corner_img = "Cornerdefault.png"
    attribute_path = Image.open(souce_path + path_extras + corner_img)
    attribute_img = attribute_path.resize((20,20),Image.ANTIALIAS)
    area_x = 387
    area_y = 580
    area = area_x, area_y
    image_with_text.paste(attribute_img, area)

image = Image.open("tmpout.png").convert('RGBA')
os.remove("tmpout.png")

out = Image.alpha_composite(image, image_with_text)
out.show()  

file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", Title).replace(" ", "_")+'.png'
out.save(os.path.join(output_dir, file_name))

