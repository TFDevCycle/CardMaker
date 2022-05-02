from PIL import Image

class DrawImageCard():
   def __init__(self, card, area, card_image) -> None:
      self.card = card
      self.area = area
      self.card_image = card_image
      self.card = self.card_image.resize((320,320),Image.ANTIALIAS)

   def getImage(self):
      return self.card_image
