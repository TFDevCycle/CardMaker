from ursina import *                    # Import the ursina engine

class preview():
    def __init__(self, img):
        app = Ursina()                          # Initialise your Ursina app
        cube = Entity(model='cube', scale=(5,7,0), texture=img)
        app.run()                               # Run the app