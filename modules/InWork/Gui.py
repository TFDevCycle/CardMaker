import PySimpleGUI as sg
from PIL import Image, ImageFont, ImageDraw
import re
import os
import textwrap
from string import ascii_letters
import colorama
import main

class CardGenerator():
    def __init__(self):
        sg.theme('darkPurple6')
        self.arrays()
        self.layout()
        self.functions()

    def arrays(self):
        self.card=['Normal','Effect','Ritual','Fusion','Synchro','XYZ','Pendulum','Link','Token','Trap','Spell']
        self.attribute=['Dark','Divine','Earth','Empty','Fire','Light','Spell','Time','Trap','Void','Wind']
        self.level=['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
        self.menu= [['Settings', ['&Exit']],
                        ['&Help', ['&About..']],]

    def layout(self):
    # Define the window's contents
        self.layout = [
                    [sg.Text(size=18, text='Card')],
                    [sg.Text("Card:       "),
                    sg.InputOptionMenu(values=self.card, size=30, default_value="Effect")],
                    [sg.Text("Title:        "),
                    sg.Input(size=35)],
                    [sg.Text("Artwork:   "),
                    sg.Input(tooltip="", size=35, default_text="Placeholder")],
                    [sg.Text("Attribute:  "),
                    sg.InputOptionMenu(size=30, values=self.attribute, default_value="Empty")],
                    [sg.Text("Level:       "),
                    sg.InputOptionMenu(values=self.level, size=30, default_value="0")],
                    [sg.Text("ATK/DEF:"),
                    sg.Input(size=17),
                    sg.Input(size=16)],
                    [sg.Text("Type:       "),
                    sg.Input(size=14),
                    sg.Text("  /  "),
                    sg.Input(size=14)],
                    [sg.Text("Desc:      "),
                    sg.Input(size=35)],  
                    [sg.Text(size=18, text='Link')],
                    [sg.HSeparator()], 
                    [sg.Checkbox(text=""),
                    sg.Checkbox(text=""),
                    sg.Checkbox(text="")],
                    [sg.Checkbox(text=""),
                    sg.Text("      "),
                    sg.Checkbox(text="")],            
                    [sg.Checkbox(text=""),
                    sg.Checkbox(text=""),
                    sg.Checkbox(text="")],           
                    [sg.Text(size=18, text='Pendel')],
                    [sg.HSeparator()],
                    [sg.Input(size=5),
                    sg.Multiline(size=(35,5), no_scrollbar=True),
                    sg.Input(size=5)],
                    [sg.Text("Save Path")],
                    [sg.HSeparator()],
                    [sg.FolderBrowse(size=40, button_text='Save Path', key=30)],
                    [sg.HSeparator(color='black', pad=(5,10))],
                    [sg.Button('Generate', size=40)],
                    ]
        self.window = sg.Window('CardCreator',default_element_size=(12, 1), icon=r"modules\In Work\icon.ico",layout=self.layout)      # Part 3 - Window Defintion

    def functions(self):

        self.event, self.values = self.window.read()

        if self.event in (None, 'Generate'):
            self.source_card_path      = "img/cards/card-" + self.values[0].lower().replace(' ', '-') + '.png'
            self.attribute_path      = "img/type/" + self.values[3].replace(' ', '-') + '.png'
            if self.values[0] == "XYZ":
                self.level_path      = "img\lvl\Level-black.png"
            else:
                self.level_path      = "img\lvl\Level-red.png"
            self.card_image = Image.open(self.source_card_path).convert('RGBA')
            self.finishCard = Image.new('RGBA', self.card_image.size, (255,255,255,0))
            self.finishCard = self.card_image.resize((421,614),Image.ANTIALIAS)
            self.draw                  = ImageDraw.Draw(self.finishCard)

            self.level_image = Image.open(self.level_path).convert('RGBA')
            self.level_image = self.level_image.resize((25,25),Image.ANTIALIAS)

            self.level_x = 380
            self.i = 0
            for self.i in range(int(self.values[4])):
                    self.level_x = self.level_x - 27
                    area = self.level_x, 76
                    self.finishCard.paste(self.level_image, area)



            self.art_image = Image.open("img/cardimages/" + self.values[2] + ".png").convert('RGBA')
            if self.values[0] == "Pendulum":
                self.art_image = self.art_image.resize((367,273),Image.ANTIALIAS)
                self.finishCard.paste(self.art_image, (27,110))
            else:
                self.art_image = self.art_image.resize((320,320),Image.ANTIALIAS)
                self.finishCard.paste(self.art_image, (51,113))
            self.attribute_image = Image.open(self.attribute_path).convert('RGBA')
            self.attribute_image = self.attribute_image.resize((40,40),Image.ANTIALIAS)
            self.finishCard.paste(self.attribute_image, (355,29))
            self.out  = Image.alpha_composite(self.card_image,self.finishCard)
            self.out.save("tmpout.png")    

            if self.values[0] == "Link":
                
                self.tmpout = Image.alpha_composite(self.out, self.finishCard)
                self.linklevel = 0
                if self.values[11] == True:
                    self.linkTM_image = "LM-TopLefta.png"
                    self.linklevel = self.linklevel + 1
                else:
                    self.linkTM_image = "LM-TopLeft-false.png"

                area_lx = 35
                area_ly = 95
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

                if self.values[12] == True:
                    self.linkTM_image = "LM-Top.png"
                    self.linklevel = self.linklevel + 1
                else:
                    self.linkTM_image = "LM-Top-false.png"
                
                area_lx = 163
                area_ly = 89
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

                if self.values[13] == True:
                    self.linkTM_image = "LM-TopRight.png"
                    self.linklevel = self.linklevel + 1
                else:
                    self.linkTM_image = "LM-TopRight-false.png"
                
                area_lx = 345
                area_ly = 95
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

                if self.values[14] == True:
                    linkTM_image = "LM-Left.png"
                    self.linklevel = self.linklevel + 1
                else:
                    linkTM_image = "LM-Left-false.png"
                
                area_lx = 25
                area_ly = 225
                area = area_lx, area_ly
                link_file = Image.open("img/linkarrow/" + linkTM_image)
                self.finishCard.paste(link_file, area)

                if self.values[15] == True:
                    linkTM_image = "LM-Right.png"
                    self.linklevel = self.linklevel + 1
                else:
                    linkTM_image = "LM-Right-false.png"
                
                area_lx = 370
                area_ly = 225
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

                if self.values[16] == True:
                    self.linkTM_image = "LM-BottomLeft.png"
                    self.linklevel = self.linklevel + 1
                else:
                    self.linkTM_image = "LM-BottomLeft-false.png"

                area_lx = 35
                area_ly = 406
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

                if self.values[17] == True:
                    self.linkTM_image = "LM-Bottom.png"
                    self.linklevel = self.linklevel + 1
                else:
                    self.linkTM_image = "LM-Bottom-false.png"

                area_lx = 163
                area_ly = 430
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

                if self.values[18] == True:
                    self.linkTM_image = "LM-BottomRight.png"
                    self.linklevel = self.linklevel + 1
                else:
                    self.linkTM_image = "LM-BottomRight-false.png"

                area_lx = 345
                area_ly = 405
                area = area_lx, area_ly
                self.link_file = Image.open("img/linkarrow/" + self.linkTM_image)
                self.finishCard.paste(self.link_file, area)

            self.card_image = Image.open("tmpout.png").convert('RGBA')
            os.remove("tmpout.png")

            self.TitleFont  = ImageFont.truetype('fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf', 48)
            self.ATKDEFFont                 = ImageFont.truetype('fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf', 23)
            self.AttrFont                   = ImageFont.truetype('fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf', 15)
            self.AttrFont1                  = ImageFont.truetype('fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf', 16)
            self.PendelFont                 = ImageFont.truetype('fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf', 22)
            self.DescFont                   = ImageFont.truetype('fonts\Yu-Gi-Oh! Matrix Book.ttf', 14)

            self.title = self.draw.text((30,28), self.values[1], font=self.TitleFont, fill='black')
            self.type = self.draw.text((35,460), "[" + self.values[7] + "/" + self.values[8] + "]", font=self.AttrFont, fill='black')
            self.avg_char_width = sum(self.DescFont.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
            self.max_char_count = int(self.card_image.size[0] * 1.125 / self.avg_char_width)

            self.text = textwrap.fill(text=self.values[9], width=self.max_char_count, break_long_words=True)
            self.desc = self.draw.text((35,480), self.text, font=self.DescFont, fill='black')
            self.atk = self.draw.text((265,557), self.values[5], font=self.ATKDEFFont, fill='black')

            if self.values[0] == "Pendulum":
                self.avg_char_width = sum(self.PendelFont.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
                self.max_char_count = int(self.card_image.size[0] / self.avg_char_width)
                self.text = textwrap.fill(self.text, width=70, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None)
                self.pendell = self.draw.text((37,420), self.values[18], font=self.PendelFont, fill='black')
                self.pendeldesc = self.draw.text((65,387), self.text, font=self.DescFont, fill='black')
                self.pendelr = self.draw.text((370,420), self.values[20], font=self.PendelFont, fill='black')

            if self.values[0] == "Link":
                self.defe = self.draw.text((375,557), str(self.linklevel), font=self.AttrFont1, fill='black')
            else:    
                self.defe = self.draw.text((350,557), self.values[7], font=self.ATKDEFFont, fill='black')
            self.out  = Image.alpha_composite(self.card_image,self.finishCard)
            self.out.show()

            if self.values[30] == "":
                self.values[30] = "C:\#CMD-Skript\Github\CardMaker\output"
                self.file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", self.values[2]).replace(" ", "_")+'.png'
                self.out.save(self.values[30] + "/" + self.file_name)
                img = self.values[30] + "/" + self.file_name
                main.preview(img)
            else:
                self.file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", self.values[2]).replace(" ", "_")+'.png'
                self.out.save(self.values[30] + "/" + self.file_name)
                if "InWork" in self.values[30]:
                    img = self.file_name
                else:
                    img = self.values[30] + "/" + self.file_name
                main.preview(img)
        elif self.event == 'About..':
            self.documentation.read()
            self.window.read()
        elif self.event == 'Exit':
            self.window.close()
        # Do something with the information gathered
CardGenerator()