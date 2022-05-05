import json
from modules.CardConstructor import CardConstructor

with open('CardCreator.json', 'r') as f:
  json_file = json.load(f)

card1 = CardConstructor(json_file)
card1.generateCard()