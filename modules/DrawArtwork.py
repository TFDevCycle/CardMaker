from PIL import Image

class DrawArtwork():
   def __init__(self, artwork, artarea, art_image) -> None:
      self.artwork = artwork
      self.artarea = artarea
      self.art_image = Image.open(art_image).convert('RGBA')
      self.art_image1 = self.art_image.resize((320,320),Image.ANTIALIAS)

   def getArtwork(self):
      return self.art_image1