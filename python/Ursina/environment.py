from ursina import Ursina, Entity, color

app = Ursina()

floor = Entity(model = "plane", color = color.white, texture = "white_cube", scale = 10)
floor.position = (0,-2,0)

app.run()

