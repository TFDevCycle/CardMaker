class DrawImage():

   def __init__(self, card) -> None:

      self.source_card = 'Card-' + card.lower().replace(' ', '-') + '.png'
   
   def getSourceCard(self):
      return self.source_card
