from ursina import *

app = Ursina()
tetu = "output/The_Dark_Book.png"


rotation_resetter = Entity()

cube = Entity(parent=rotation_resetter, model='cube', scale=(0,6,4), texture=tetu)

class tetu1:

    def tetu2():
        print("Success")
        cube = Entity(parent=rotation_resetter, model='cube', scale=(0,6,4), texture="output/Fire_Dragon.png")
        cube.enable

button  = Button(text="<", scale=(0.2,0.1), position=(-0.75,0))
button1 = Button(text=">", scale=(0.2,0.1), position=(0.75,0))
button1.on_click = tetu1.tetu2
button1.on_click = cube.disable

def update():
    rotation_resetter.rotation_y += 50 * time.dt

    cube.rotation = cube.world_rotation
    rotation_resetter.rotation = (0,0,0)

EditorCamera()

app.run()