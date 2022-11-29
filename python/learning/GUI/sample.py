from ursina import *

#application.development_mode = False

app = Ursina()      #makes window

#window.exit_button.enabled = False
#window.fps_counter.enabled = False
#window.cog_button.enabled = False
#window.fullscreen = True
#window.borderless = False

lst = [1,2,3]

def menu(lst):
    menu_lst = []
    for evnt in lst:
        menu_lst.append(Button(
            parent = scene,
            model = 'quad',
            color = color.cyan,
            text = str(evnt),
        ))
    return menu_lst

index = 0

def draw_menu(lst):
    global index
    lst = menu(lst)
    
#entity = Entity(model = 'cube',   #('quad','circle','sphere')
#                color = color.orange,  #color.rgb(r,g,b)
#                texture = 'white cube',
#                scale = (2,3,4),  #scale = number; equal scale
#                position = (3,2,1))

#txt = Text(text = "Test Text",
#           color = color.rgb(255,255,255),
#           scale = 2)

def update():           #automatically called
    menu(lst)                #your code

app.run()