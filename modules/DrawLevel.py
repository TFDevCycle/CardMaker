from PIL import Image, ImageDraw

class DrawLevel():
   def __init__(self, level, area, level_image) -> None:
      self.level = level
      self.area = area
      self.level_image = Image.open(level_image).convert('RGBA')
      self.level_image = self.level_image.resize((25,25),Image.ANTIALIAS)

   def getLevel(self):
      return self.level_image