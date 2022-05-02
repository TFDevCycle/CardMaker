from black import json
from modules.CardConstructor import CardConstructor

json_file = '{ "card": "Link", "image_card": "DarkWolfRitual.jpg"}'

card = CardConstructor(json.loads(json_file))
card.buildCard()