# from _config import *
from PIL import Image, ImageDraw
import random

from modules.DrawImage import DrawImage
from modules.DrawImageCard import DrawImageCard
serial_id = random.randint(000000000, 999999999)



class CardConstructor:

   config = None
   card_img = None

   def __init__(self, json_card) -> None:
      self.loadConfig()

      if isinstance(json_card, dict):
         self.json_card = json_card
      
      self.getSources()
   
   def loadConfig(self):
      self.config = {
         'souce_path': "img/",
         'path_cards': "cards/",
         'areas': {
            'img_area': (51,113)
         }
      }

   def getSources(self):
      self.source_card = DrawImage(self.json_card['card']).getSourceCard()
      print(self.source_card)

   def generateCard(self):
      self.image = Image.open(self.config['souce_path'] + self.config['path_cards'] + self.source_card).convert('RGBA')
      image_with_text = Image.new('RGBA', self.image.size, (255,255,255,0))
      self.card_image = ImageDraw.Draw(image_with_text)

   def generateImageCard(self, card, area):
      self.card_image = DrawImageCard(card, self.config['areas']['img_area'], self.image).getImage()
      self.image.paste(self.card_image, area)
 
   def buildCard(self):
      self.generateCard()
      self.generateImageCard(self.card_img, self.config['areas']['img_area'])      
      out = Image.alpha_composite(self.card_img, self.card_img)
      out.show()  
