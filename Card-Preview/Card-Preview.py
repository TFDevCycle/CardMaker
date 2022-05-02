from torch import tile
from ursina import *
from _config import i, Cards
app = Ursina()


rotation_resetter = Entity()

cube = Entity(parent=rotation_resetter, model='cube', scale=(0,6,4), texture=Cards[0])

class tetu1:
    
    def tetuback():
        global i 
        i = i - 1
        if i == -8:
            i = 0
        print(i)
        print("Success")
        cube.texture = Cards[i]

    def tetunext():
        global i 
        i = i + 1
        if i == 8:
            i = 0
        print(i)
        print("Success")
        cube.texture = Cards[i]

button  = Button(text="<", scale=(0.2,0.1), position=(-0.75,0))
button1 = Button(text=">", scale=(0.2,0.1), position=(0.75,0))
button.on_click = tetu1.tetuback
button1.on_click = tetu1.tetunext

def update():
    rotation_resetter.rotation_y += 40 * time.dt

    cube.rotation = cube.world_rotation
    rotation_resetter.rotation = (0,0,0)

EditorCamera()

app.run()