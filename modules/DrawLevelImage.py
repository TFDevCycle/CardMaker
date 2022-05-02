from CardMaker import*

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
