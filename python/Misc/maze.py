from ursina import *
from ursina.prefabs.first_person_controller import *

app = Ursina()

maze = Entity(model = "maze", texture = "brick", scale = 20, collider = "box")

player = FirstPersonController(model = "cube",position = (16,0,-18))

camera.z = -10

app.run()
