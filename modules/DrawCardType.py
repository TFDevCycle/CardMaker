from CardMaker import *

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
