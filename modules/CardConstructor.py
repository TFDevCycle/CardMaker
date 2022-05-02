# from _config import *
from PIL import Image, ImageDraw
import random

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
      pass
      # self.source_card = DrawImage(self.json_card['card']).getSourceCard()
      # print(self.source_card)
