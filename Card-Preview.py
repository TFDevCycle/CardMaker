from ursina import *

app = Ursina()

rotation_resetter = Entity()
cube = Entity(parent=rotation_resetter, model='cube', scale=(0,6,4), texture='output/Fire_Dragon.png')
button  = Button(text="Back", scale=(0.2,0.1), position=(-0.75,0))
button1 = Button(text="Next", scale=(0.2,0.1), position=(0.75,0))
def update():
    rotation_resetter.rotation_y += 50 * time.dt

    cube.rotation = cube.world_rotation
    rotation_resetter.rotation = (0,0,0)

EditorCamera()

app.run()