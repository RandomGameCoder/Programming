from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(Entity):
    def __init__(self,**kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)

app = Ursina()

ground = Entity(model = "plane",scale = 20,texture = "white_cube",texture_scale=(20,20,20),collider ="mesh")

EditorCamera()

app.run()
