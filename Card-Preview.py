from ursina import *

app = Ursina()

rotation_resetter = Entity()
cube = Entity(parent=rotation_resetter, model='cube', scale=(2,3,0), texture='output/Fire_Dragon.png')


def update():
    rotation_resetter.rotation_y += 100 * time.dt

    cube.rotation = cube.world_rotation
    rotation_resetter.rotation = (0,0,0)

EditorCamera()

app.run()