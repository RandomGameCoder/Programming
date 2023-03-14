import tkinter as tk
import tkinter.messagebox as mb
import oxo_logic

top=tk.Tk()

def evNew():
    status['text']="New game"
    game2cells(oxo_logic.newGame())

def evResume():
    status['text']="Continue Playing"
    game=oxo_logic.restoreGame()
    game2cells(game)

def evSave():
    game=cells2game()
    oxo_logic.saveGame(game)

def evExit():
    if status['text'] in ["New game","Continue Playing","Playing game"]:
        if mb.askyesno("EXIT","do you want to save the game before quitting?"):
            evSave()
            raise SystemExit
    top.quit()

def evHelp():
    mb.showinfo("help",'''
    File->New: starts a new game
    File->Resume: restores the last saved game and commences play
    File->Save: saves current game
    File->Exit: exits, prompts to save current game
    Help->About: shows information about the program
    Help->Programmer: shows information about the programmer''')

def evAbout():
    mb.showinfo("About","This is a tic-tac-toe game programmed by two programmers.")

def evAuthor():
    mb.showinfo("PROGRAMMER",'''
    creator: Mohammed Aban A

    programmers: Mohammed Aban A,
                 Govind S Sarath
    ''')
    
def buildMenu(parent):
    menus=(
        ("File",( ("New",evNew),
                  ("resume",evResume),
                  ("save",evSave),
                  ("exit",evExit))),
        ("help",( ("help",evHelp),
                  ("about",evAbout),
                  ("Programmer",evAuthor)))
        )
    menubar=tk.Menu(parent)
    for menu in menus:
        m=tk.Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0],command=item[1])
        menubar.add_cascade(label=menu[0],menu=m)

    return menubar

def game2cells(game):
    table=board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            table.grid_slaves(row=row,column=col)[0]['text']=game[3*row+col]

def cells2game():
    values=[]
    table=board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            values.append(table.grid_slaves(row=row,column=col)[0]['text'])
    return values

def evClick(row,col):
    if status['text']=="Game over":
        mb.showerror("Game Over","Game Over")
        return

    game=cells2game()
    index=(3*row)+col
    result=oxo_logic.userMove(game,index)
    game2cells(game)

    if not result:
        result=oxo_logic.computerMove(game)
        game2cells(game)
    if result=="D":
        mb.showinfo("Draw","Its a draw")
        status['text']="Game over"
    else :
        if result=="X" or result=="O":
            mb.showinfo("Result","The winner is : {}".format(result))
            status['text']="Game over"

def buildBoard(parent):
    outer=tk.Frame(parent,border=2,relief="sunken")
    inner=tk.Frame(outer)
    inner.pack()

    for row in range(3):
        for col in range(3):
            cell=tk.Button(inner,text=" ",width='5',height='2',
                           command=lambda r=row, c=col:evClick(r,c))
            cell.grid(row=row, column=col)
    return outer

mbar=buildMenu(top)
top["menu"]=mbar

board=buildBoard(top)
board.pack()
status=tk.Label(top,text="Playing game",border=0,
                background="lightblue",foreground='red')
status.pack(anchor="s",fill="x",expand=True)

tk.mainloop()
