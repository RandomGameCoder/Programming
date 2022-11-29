from ursina import *

#application.development_mode = False

app = Ursina()      #makes window

#window.exit_button.enabled = False
#window.fps_counter.enabled = False
#window.cog_button.enabled = False
#window.fullscreen = True
#window.borderless = False

entity = Entity(model = 'cube',   #('quad','circle','sphere')
                color = color.orange,  #color.rgb(r,g,b)
                texture = 'white cube',
                scale = (2,3,4),  #scale = number; equal scale
                position = (3,2,1))

txt = Text(text = "Test Text",
           color = color.rgb(255,255,255),
           scale = 2)

def update():           #automatically called
    pass                #your code

app.run()           #runs window
