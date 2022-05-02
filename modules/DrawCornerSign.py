from CardMaker import *

class DrawCornerSign():
    corner_img = "Cornerdefault.png"
    attribute_path = Image.open(souce_path + path_extras + corner_img)
    attribute_img = attribute_path.resize((20,20),Image.ANTIALIAS)
    area_x = 387
    area_y = 580
    area = area_x, area_y
    image_with_text.paste(attribute_img, area)
