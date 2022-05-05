# from _config import *
from PIL import Image, ImageDraw, ImageFont
import random

from modules.DrawImage import DrawImage
from modules.DrawArtwork import DrawArtwork
from modules.DrawAttribute import DrawAttribute
from modules.DrawLevel import DrawLevel
from modules.sleep import sleeper

serial_id = random.randint(000000000, 999999999)



class CardConstructor:

   config = None
   card_img = None
   card_img_draw = None

   def __init__(self, json_card) -> None:
      self.loadConfig()

      if isinstance(json_card, dict):
         self.json_card = json_card
      
      self.getSources()
   
   def loadConfig(self):
      self.config = {
         'source_path': "img/",
         'path_cards': "cards/",
         'path_img':   "cardimages/",
         'path_attr':   "type/",
         'path_level': "lvl/",
         'i': 0,
         'areas': {
            'card_area': (0,0),
            'img_area':  (51,113),
            'attr_area': (355,29),
            'level_area': (380,76),
            'level_x': 380,
            'level_y': 76,
         },
         'text': {
            'title_xy': (30,28),
            'atk_xy': (265,557),
            'def_xy': (350,557),
            'type_xy': (35,460),
            'desc_xy': (35,480),
            'fontsize48': 48,
            'fontsize23': 23,
            'fontsize15': 15,
            'fontsize12': 14,
            'titleFont': 'fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf',
            'AttrFont': "fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf",
            'DescFont': 'fonts\Yu-Gi-Oh! Matrix Book.ttf',
            'title_color': 'black',
            'title_color_xyz': 'white',
            'text_alignment': 'left'
         }
      }

   def getSources(self):
      self.source_card_path      = self.config['source_path'] + self.config['path_cards'] +'Card-' + self.json_card['card'].lower().replace(' ', '-') + '.png'
      self.attribute_path        = self.config['source_path'] + self.config['path_attr'] + self.json_card['attribute'] + '.png'
      self.level_path            = self.config['source_path'] + self.config['path_level'] + 'Level-Red.png'

      self.image                 = DrawImage(self.json_card['card'], self.config['areas']['card_area'], self.source_card_path).getimage()
      self.source_card1          = DrawImage(self.json_card['card'], self.config['areas']['card_area'], self.source_card_path).getSourceCard()

      self.artwork               = DrawArtwork(self.json_card['image_card'], self.config['areas']['img_area'], self.config['source_path'] + self.config['path_img'] + self.json_card['image_card']).getArtwork()
      
      self.attribute             = DrawAttribute(self.json_card['attribute'], self.config['areas']['attr_area'], self.attribute_path).getAttribute()

      self.level                 = DrawLevel(self.json_card['Level'], self.config['areas']['level_area'], self.level_path).getLevel()

   def setLevel(self):
      for self.config['i'] in range(self.json_card['Level']):
        self.config['areas']['level_x'] = self.config['areas']['level_x'] - 27
        self.area = self.config['areas']['level_x'], self.config['areas']['level_y']
        self.source_card1.paste(self.level, self.area)

   def pasteImages(self):
      self.draw                  = ImageDraw.Draw(self.source_card1) 

      self.source_card1.paste(self.artwork, self.config['areas']['img_area'])
      sleeper(self.image,self.source_card1,"Rendering Artwork")
      self.source_card1.paste(self.attribute, self.config['areas']['attr_area']) 
      sleeper(self.image,self.source_card1,"Rendering Attribute")  


   def writeText(self):
      TitleFont                  = ImageFont.truetype(self.config['text']['titleFont'], self.config['text']['fontsize48'])
      ATKDEFFont                 = ImageFont.truetype(self.config['text']['titleFont'], self.config['text']['fontsize23'])
      AttrFont                   = ImageFont.truetype(self.config['text']['AttrFont'], self.config['text']['fontsize15'])
      DescFont                   = ImageFont.truetype(self.config['text']['DescFont'], self.config['text']['fontsize12'])
      if self.json_card['card'] == "XYZ":
         self.draw.text((self.config['text']['title_xy']), self.json_card['Title'], font=TitleFont, fill=self.config['text']['title_color_xyz'], align=self.config['text']['text_alignment']) 
         sleeper(self.image,self.source_card1,"Rendering Title")     
      else:
         self.draw.text((self.config['text']['title_xy']), self.json_card['Title'], font=TitleFont, fill=self.config['text']['title_color'], align=self.config['text']['text_alignment'])
         sleeper(self.image,self.source_card1,"Rendering Title")
      self.draw.text((self.config['text']['atk_xy']), self.json_card['Atk'], font=ATKDEFFont, fill=self.config['text']['title_color'], align=self.config['text']['text_alignment'])
      self.draw.text((self.config['text']['def_xy']), self.json_card['Def'], font=ATKDEFFont, fill=self.config['text']['title_color'], align=self.config['text']['text_alignment'])
      sleeper(self.image,self.source_card1,"Rendering ATK/DEF")
      self.draw.text((self.config['text']['type_xy']), "[" + self.json_card['Type'] + "]", font=AttrFont, fill=self.config['text']['title_color'], align=self.config['text']['text_alignment'])
      sleeper(self.image,self.source_card1,"Rendering Type")
      self.draw.text((self.config['text']['desc_xy']), self.json_card['Descripton'], font=DescFont, fill=self.config['text']['title_color'], align=self.config['text']['text_alignment'])
      sleeper(self.image,self.source_card1,"Rendering Description")

   def generateCard(self):
      self.getSources()
      self.pasteImages()
      self.writeText()
      self.setLevel()
      print("finished..")


