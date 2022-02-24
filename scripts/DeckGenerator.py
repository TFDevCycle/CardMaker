
from ursina import *

app = Ursina()
rotation_resetter = Entity()

Card1 = Entity(parent=rotation_resetter, model='cube', scale=(0,2,1.5), position=(-3,-4), texture="output/UndeathUnderworld/Undeath_Yugi.png")
Card2 = Entity(parent=rotation_resetter, model='cube', scale=(0,2,1.5), position=(-1.5,-4), texture="output/UndeathUnderworld/Ultimate_Black_Hole.png")
Card3 = Entity(parent=rotation_resetter, model='cube', scale=(0,2,1.5), position=(0,-4), texture="output/Template__Monster.png")
Card4 = Entity(parent=rotation_resetter, model='cube', scale=(0,2,1.5), position=(1.5,-4), texture="output/UndeathUnderworld/Guard_of_Hell.png")
Card5 = Entity(parent=rotation_resetter, model='cube', scale=(0,2,1.5), position=(3,-4), texture="output/UndeathUnderworld/Dragon_of_Hell.png")
def input(key):
   if held_keys['1']:
      Card1.scale   =(0,6,4)
      Card1.position=(0,0,1)

   else:
      Card1.scale   =(0,2,1.5)
      Card1.position=(-3,-4 ,0)

   if held_keys['2']:
      Card2.scale   =(0,6,4)
      Card2.position=(0,0,1)

   else:
      Card2.scale   =(0,2,1.5)
      Card2.position=(-1.5,-4,0)

   if held_keys['3']:
      Card3.scale   =(0,6,4)
      Card3.position=(0,0,1)

   else:
      Card3.scale   =(0,2,1.5)
      Card3.position=(0,-4,0)

   if held_keys['4']:
      Card4.scale   =(0,6,4)
      Card4.position=(0,0,1)

   else:
      Card4.scale   =(0,2,1.5)
      Card4.position=(1.5,-4,0)

   if held_keys['5']:
      Card5.scale   =(0,6,4)
      Card5.position=(0,0,1)

   else:
      Card5.scale   =(0,2,1.5)
      Card5.position=(3,-4,0)

def update():
   Card1.rotation_y = 90
   Card2.rotation_y = 90
   Card3.rotation_y = 90
   Card4.rotation_y = 90
   Card5.rotation_y = 90

app.run()