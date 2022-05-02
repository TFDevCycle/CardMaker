from CardMaker import *

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

    if card == "Link":
        Defense = str(linkLevel)
        draw.text((375, def_y), Defense, font=font3, fill=desc_color, align=text_alignment)
