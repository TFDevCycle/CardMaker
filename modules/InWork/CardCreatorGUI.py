import PySimpleGUI as sg
from PIL import Image, ImageFont, ImageDraw
import re
import os
import textwrap
from string import ascii_letters
                    # Part 1 - The import
card=['Normal','Effect','Ritual','Fusion','Synchro','XYZ','Pendulum','Link','Token','Trap','Spell']
attribute=['Dark','Divine','Earth','Empty','Fire','Light','Spell','Time','Trap','Void','Wind']
level=['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
menu= [['Settings', ['&Exit']],
                        ['&Help', ['&About..']],]


class GUI():
    def __init__(self) -> None:
        pass
    

    def gui():
        layout = [  
            [sg.Text("Card:       "),
            sg.InputOptionMenu(values=card, size=30, default_value="Effect", key=0)],
            [sg.Text("Title:        "),
            sg.Input(size=35, key=1)],
            [sg.Text("Artwork:   "),
            sg.Input(tooltip="", size=35, default_text="Placeholder", key=2)],
            [sg.Text("Attribute:  "),
            sg.InputOptionMenu(size=30, values=attribute, default_value="Empty", key=3)],
            [sg.Text("Level:       "),
            sg.InputOptionMenu(values=level, size=30, default_value="0", key=4)],
            [sg.Text("ATK/DEF:"),
            sg.Input(size=17, key=5),
            sg.Input(size=16, key=6)],
            [sg.Text("Type:       "),
            sg.Input(size=14, key=7),
            sg.Text("  /  "),
            sg.Input(size=14, key=8)],
            [sg.Text("Desc:      "),
            sg.Input(size=35, key=9)],  
            [sg.Text(size=18, text='Link')],
            [sg.HSeparator()], 
            [sg.Checkbox(text="", key=10),
            sg.Checkbox(text="", key=11),
            sg.Checkbox(text="", key=12)],
            [sg.Checkbox(text="", key=13),
            sg.Text("      "),
            sg.Checkbox(text="", key=14)],            
            [sg.Checkbox(text="", key=15),
            sg.Checkbox(text="", key=16),
            sg.Checkbox(text="", key=17)],           
            [sg.Text(size=18, text='Pendel')],
            [sg.HSeparator()],
            [sg.Input(size=5, key=18),
            sg.Multiline(size=(35,5), no_scrollbar=True, key=19),
            sg.Input(size=5, key=20)],
            [sg.Text("Save Path")],
            [sg.HSeparator()],
            [sg.FolderBrowse(size=40, button_text='Save Path', key=21)],
            [sg.HSeparator(color='black', pad=(5,10), key=22)],
            [sg.Button('Generate', size=40)], ]

        doc_layout =[ [sg.Text('Created and Coded from DevCycle', size=30)]]
        # Define the window's contents
       
        # Create the window
        window = sg.Window('CardCreator',default_element_size=(12, 1), icon=r"modules\In Work\icon.ico", layout=layout)      # Part 3 - Window Defintion
        documentation = sg.Window('About..',size=(230, 50), default_element_size=(12, 1),icon=r"modules\In Work\icon.ico", layout=doc_layout)

        # Display and interact with the Window
        event, values = window.read()

        if event in (None, 'Generate'):
            source_card_path      = "img/cards/card-" + values[0].lower().replace(' ', '-') + '.png'
            attribute_path      = "img/type/" + values[3].replace(' ', '-') + '.png'
            if values[0] == "XYZ":
                level_path      = "img\lvl\Level-black.png"
            else:
                level_path      = "img\lvl\Level-red.png"
            card_image = Image.open(source_card_path).convert('RGBA')
            finishCard = Image.new('RGBA', card_image.size, (255,255,255,0))
            finishCard = card_image.resize((421,614),Image.ANTIALIAS)
            draw                  = ImageDraw.Draw(finishCard)

            level_image = Image.open(level_path).convert('RGBA')
            level_image = level_image.resize((25,25),Image.ANTIALIAS)

            level_x = 380
            i = 0
            for i in range(int(values[4])):
                    level_x = level_x - 27
                    area = level_x, 76
                    finishCard.paste(level_image, area)



            art_image = Image.open("img/cardimages/" + values[2] + ".png").convert('RGBA')
            if values[0] == "Pendulum":
                art_image = art_image.resize((367,273),Image.ANTIALIAS)
                finishCard.paste(art_image, (27,110))
            else:
                art_image = art_image.resize((320,320),Image.ANTIALIAS)
                finishCard.paste(art_image, (51,113))
            attribute_image = Image.open(attribute_path).convert('RGBA')
            attribute_image = attribute_image.resize((40,40),Image.ANTIALIAS)
            finishCard.paste(attribute_image, (355,29))
            out  = Image.alpha_composite(card_image,finishCard)
            out.save("tmpout.png")    

            if values[0] == "Link":
                
                tmpout = Image.alpha_composite(out, finishCard)
                linklevel = 0
                if values[10] == True:
                    linkTM_image = "LM-TopLefta.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-TopLeft-false.png"

                area_lx = 35
                area_ly = 95
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[11] == True:
                    linkTM_image = "LM-Top.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-Top-false.png"
                
                area_lx = 163
                area_ly = 89
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[12] == True:
                    linkTM_image = "LM-TopRight.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-TopRight-false.png"
                
                area_lx = 345
                area_ly = 95
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[13] == True:
                    linkTM_image = "LM-Left.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-Left-false.png"
                
                area_lx = 25
                area_ly = 225
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[14] == True:
                    linkTM_image = "LM-Right.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-Right-false.png"
                
                area_lx = 370
                area_ly = 225
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[15] == True:
                    linkTM_image = "LM-BottomLeft.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-BottomLeft-false.png"

                area_lx = 35
                area_ly = 406
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[16] == True:
                    linkTM_image = "LM-Bottom.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-Bottom-false.png"

                area_lx = 163
                area_ly = 430
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

                if values[17] == True:
                    linkTM_image = "LM-BottomRight.png"
                    linklevel = linklevel + 1
                else:
                    linkTM_image = "LM-BottomRight-false.png"

                area_lx = 345
                area_ly = 405
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                finishCard.paste(link_file, area)

            card_image = Image.open("tmpout.png").convert('RGBA')
            os.remove("tmpout.png")

            TitleFont  = ImageFont.truetype('fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf', 48)
            ATKDEFFont                 = ImageFont.truetype('fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf', 23)
            AttrFont                   = ImageFont.truetype('fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf', 15)
            AttrFont1                  = ImageFont.truetype('fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf', 16)
            PendelFont                 = ImageFont.truetype('fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf', 22)
            DescFont                   = ImageFont.truetype('fonts\Yu-Gi-Oh! Matrix Book.ttf', 14)

            title = draw.text((30,28), values[1], font=TitleFont, fill='black')
            type = draw.text((35,460), "[" + values[7] + "/" + values[8] + "]", font=AttrFont, fill='black')
            avg_char_width = sum(DescFont.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
            max_char_count = int(card_image.size[0] * 1.145 / avg_char_width)

            text = textwrap.fill(text=values[9], width=max_char_count, break_long_words=True)
            desc = draw.text((35,480), text, font=DescFont, fill='black')
            atk = draw.text((265,557), values[5], font=ATKDEFFont, fill='black')

            if values[0] == "Pendulum":
                avg_char_width = sum(PendelFont.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
                max_char_count = int(card_image.size[0] / avg_char_width)
                text = textwrap.fill(text, width=70, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None)
                pendell = draw.text((37,420), values[18], font=PendelFont, fill='black')
                pendeldesc = draw.text((65,387), text, font=DescFont, fill='black')
                pendelr = draw.text((370,420), values[20], font=PendelFont, fill='black')

            if values[0] == "Link":
                defe = draw.text((375,557), str(linklevel), font=AttrFont1, fill='black')
            else:    
                defe = draw.text((350,557), values[7], font=ATKDEFFont, fill='black')
            out  = Image.alpha_composite(card_image,finishCard)
            out.show()

            if values[9] == "":
                pass
            else:
                file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", values[2]).replace(" ", "_")+'.png'
                out.save(values[10] + "/" + file_name)
        elif event == 'About..':
            documentation.read()
            window.read()
        elif event == 'Exit':
            window.close()
        # Do something with the information gathered
