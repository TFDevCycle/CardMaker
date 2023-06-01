import json
from modules.CardConstructor import CardConstructor
import modules.InWork.CardCreatorGUI as CardCreator
 
inp_typ = "JSON"
if inp_typ == "JSON":
  with open('CardCreator.json', 'r') as f:
    json_file = json.load(f)

  '''

  if json_file['aktion'] == 'new':
    with open('data/' + json_file["Title"] + '.json', 'w') as f:
      u = json.dumps(json_file, indent=4)
      f.write(u)
      
  elif json_file['aktion'] == 'open':
    with open('data/' + json_file['Cardname'] + '.json', 'r') as u:
      json_file = json.load(u)

  '''

  card1 = CardConstructor(json_file)
  card1.generateCard()

elif inp_typ == "GUI":
  CardCreator.GUI()