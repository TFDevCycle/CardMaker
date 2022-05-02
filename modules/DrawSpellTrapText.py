from CardMaker import *

class DrawSpellTrapText():
    stText_x = 275
    stText_y = 77

    if card == "Trap":
        if cardkind == "Counter":
            draw.text((stText_x, stText_y), "[Trap     ]", font=AttrFont1, fill=title_color, align=text_alignment)
            cardkind_img = "Counter.png"
            symbol_path = Image.open(souce_path + path_symbol + cardkind_img)
            symbol_img = symbol_path.resize((17,17),Image.ANTIALIAS)
            stArea = stText_x + 50, stText_y + 1
            image_with_text.paste(symbol_img, stArea)
        if cardkind == "Continuous":
            draw.text((stText_x, stText_y), "[Trap     ]", font=AttrFont1, fill=title_color, align=text_alignment)
            cardkind_img = "Continuous.png"
            symbol_path = Image.open(souce_path + path_symbol + cardkind_img)
            symbol_img = symbol_path.resize((17,17),Image.ANTIALIAS)
            stArea = stText_x + 50, stText_y + 1
            image_with_text.paste(symbol_img, stArea)
        if cardkind == "":
            stText_x = 280
            stText_y = 77
            draw.text((stText_x, stText_y), "[Trap Card]", font=AttrFont1, fill=title_color, align=text_alignment)

    elif card == "Spell":
        if cardkind == "Counter":
            stText_x = 280
            stText_y = 77
            draw.text((stText_x, stText_y), "[Spell Card    ]", font=AttrFont1, fill=title_color, align=text_alignment) 
        if cardkind == "Continuous":
            draw.text((stText_x, stText_y), "[Spell Card    ]", font=AttrFont1, fill=title_color, align=text_alignment)
            cardkind_img = "Continuous.png"
            symbol_path = Image.open(souce_path + path_symbol + cardkind_img)
            symbol_img = symbol_path.resize((17,17),Image.ANTIALIAS)
            stArea = stText_x + 55, stText_y + 1
            image_with_text.paste(symbol_img, stArea)
        if cardkind == "":
            stText_x = 280
            stText_y = 77
            draw.text((stText_x, stText_y), "[Spell Card]", font=AttrFont1, fill=title_color, align=text_alignment)
