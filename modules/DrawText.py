from CardMaker import *

class DrawText():
    print("Final font size: ",fontsize)

    if card == "XYZ":
        draw.text((title_x, title_y), Title, font=TitleFont1, fill=title_color_xyz, align=text_alignment)
        draw.text((type_x, type_y), Type, font=AttrFont1, fill=desc_color, align=text_alignment)
        draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color_xyz, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color_xyz, align=text_alignment)
        draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color_xyz, align=text_alignment)

    elif card == "Trap":
        desc_y = desc_y - 20
        draw.text((title_x, title_y), Title, font=TitleFont1, fill=title_color, align=text_alignment)
        draw.text((type_x, type_y), Type, font=AttrFont1, fill=desc_color, align=text_alignment)
        draw.text((desc_x, desc_y), Description, font=DescFont1, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color, align=text_alignment)
        draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color, align=text_alignment)            
    
    elif card == "Spell":
        desc_y = desc_y - 20
        draw.text((title_x, title_y), Title, font=TitleFont1, fill=title_color, align=text_alignment)
        draw.text((desc_x, desc_y), Description, font=DescFont1, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color, align=text_alignment)
        draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color, align=text_alignment)

    elif card == "Link":
        draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), "", font=font4, fill=title_color, align=text_alignment)
    else:
        draw.text((title_x, title_y), Title, font=TitleFont1, fill=title_color, align=text_alignment)
        draw.text((type_x, type_y), Type, font=AttrFont1, fill=desc_color, align=text_alignment)
        draw.text((desc_x, desc_y), Description, font=DescFont1, fill=desc_color, align=text_alignment)
        draw.text((serial_x, serial_y), str(serial_id), font=font4, fill=title_color, align=text_alignment)
        draw.text((atk_x, atk_y), Attack, font=font3, fill=desc_color, align=text_alignment)
        draw.text((auflage_x, auflage_y), auflage, font=font4, fill=title_color, align=text_alignment)
        draw.text((def_x, def_y), Defense, font=font3, fill=desc_color, align=text_alignment)
        draw.text((card_id_x, card_id_y), card_id, font=font4, fill=title_color, align=text_alignment)
