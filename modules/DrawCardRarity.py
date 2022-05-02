from CardMaker import *

class DrawCardRarity():

   def __init__(self, p_image_with_text) -> None:
      self.image_with_text = p_image_with_text

      tmpout = Image.alpha_composite(image, self.image_with_text)
      tmpout.save("tmpout.png")
      if rarity == "Shatterfoil":
         card_border = Image.open(souce_path + path_rarity + "Shatter.png")
         self.image_with_text.paste(card_border)
         print("Card Rarity: Shatterfoil Rare")    
      elif rarity == "Mosaic":
         card_border = Image.open(souce_path + path_rarity + "Mosaic.png")
         self.image_with_text.paste(card_border)
         print("Card Rarity: Mosaic Rare")  
      elif rarity == "Secret":
         area = 51, 113 
         card_image = Image.open(souce_path + path_rarity + "Secret.png")
         card = card_image.resize((320,320),Image.ANTIALIAS)
         self.image_with_text.paste(card, area)
         print("Card Rarity: Secret Rare")    
      else:
         print("Card Rarity: None")

