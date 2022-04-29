from turtle import onclick
from cv2 import CAP_PROP_DC1394_MAX
from ursina import *
from Deck_config import Cards, pos1, pos2, CardNumberHand, ExtraDeck
from random import * 

app = Ursina()
rotation_resetter = Entity()


class Card:
   global card
   def __init__(self,var,  position, texture):
         self.var = var
         self.position = position
         self.texture = texture
   def CardCreate(var, position, texture):
      var = Entity(parent=rotation_resetter, model='cube', scale=(0,2,1.5), position=position, texture=texture)
      var.rotation_y = 90

class Start():
      global pos1
      global pos2
      CardNumberHand = CardNumberHand + 1
      Name = "Card" + str(CardNumberHand)
      print(CardNumberHand)
      for ii in range(5):
            ii+1
            i = randint(0, 2)
            pos1 = pos1 + 1.5
            Card.CardCreate(Name ,position=(pos1,pos2), texture=Cards[i])

class Stats():
      DeckNum = str(len(Cards))
      ExtraDeckNum = str(len(ExtraDeck))
      DeckNumText = "Deck: " + DeckNum
      ExtraDeckNumText = "Extra-Deck: " + ExtraDeckNum
      DeckNumber = Text(text=DeckNumText, position=(-0.85,0.40))
      ExtraDeckNumber = Text(text=ExtraDeckNumText,position=(-0.85,0.45))

def input(key):
   global pos1
   global pos2
   global Card1
   global Card2
   global CardNumberHand

   if held_keys['r']:
      CardNumberHand = CardNumberHand + 1
      Name = "Card" + str(CardNumberHand)
      print(Name)
      i = randint(0, 2)
      pos1 = pos1 + 1.5
      Card.CardCreate(Name ,position=(pos1,pos2), texture=Cards[i])
   if held_keys['f']:
      CardNumberHand = CardNumberHand + 1
      Name = "Card" + str(CardNumberHand)
      pos1 = pos1 + 1.5
      Card.CardCreate(Name ,position=(pos1,pos2), texture=ExtraDeck[0])
   if held_keys['q']:
         '''Card1.disable()'''
app.run()