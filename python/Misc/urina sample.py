from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = "Block",          #shape
            color = color.white,        #color
            texture = "white_cube",     #texture, in-built texture
            rotation = Vec3(45,45,45),    #rotation vectors
            position = (-6,-3),          #position from center
            scale = 0.5
            )

class Test_button(Button):   #button sample
    def __init__(self):
        super().__init__(
            parent = scene,     #to make button fit size of scene
            model = "quad",
            texture = "brick",      #in-built texture
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime
            )
    def input(self,key):              #fuction for button
        if self.hovered:
            if key == "left mouse down":
                print("test")

def update():
    if held_keys["a"]:
        cube.rotation_x -= 10 * time.dt
        cube.rotation_y -= 10 * time.dt
        cube.rotation_z -= 10 * time.dt


app = Ursina()

texture = load_texture("pac.png")
square = Entity(model = "quad", texture = texture, position = (5,3))
cube = Test_cube()
but = Test_button()

EditorCamera()

app.run()
