import oxo_logic
import tkinter
import tkinter.messagebox as mb

menu=["start new game",
      "resume game",
      "help",
      "quit"]

def getMenuChoice(aMenu):
    if not aMenu:
        raise ValueError('no menu content')
    while True:
        print('\n\n')
        for index, item in enumerate(aMenu, start=1):
            print(index,'\t',item)
            try:
                choice=int(input("\nchoose a menu option:"))
                if 1<=choice<=len(aMenu):
                    return choice
                else:
                    print('choose a number between 1 and ',len(aMenu))
            except ValueError:
                print("choose the number of a menu option")

def main():
    print(getMenuChoice(menu))
    getMenuChoice([])

if __name__=="__main__":
    main()

def startGame():
    return oxo_logic.neeGame()

def resumeGame():
    return oxo_logic.restoreGame()

def displayHelp():
    print('''
    Start new game : sarts a new game of tic tac toe
    Resume game: restores the last saved game and commences play
    quit: quits the application
    ''')

def quit():
    print('goodbye')
    raise SystemExit

def executeChoice(choice):
    dispatch=[startGame,resumeGame,displayHelp,quit]
    game=dispatch[choice-1]()
    if game:
        pass

def main():
    top=tkinter.Tk()
    top.withdraw()
    while True:
        choice=getMenuChoice(menu)
        executeChoice(choice)

def printGame(game):
    display='''
     1 | 2 | 3    {} | {} | {}
     ---------    ---------=--
     4 | 5 | 6    {} | {} | {}
     ---------    ------------
     7 | 8 | 9    {} | {} | {}'''
    print(display.format(*game))

def playGame(game):
    result=""
    while not result:
        printGame(game)
        choice=input("Cell[1-9 or q to quit]:")
        if choice.lower()[0]=='q':
            save=mb.askyesno('save game','Save game before quiting?')       
            if save:
                oxo_logic.saveGame(game)
            quit()
        else:
            try:
                cell=int(choice)-1
                if not (0<=cell<=8):
                    raise ValueError
            except ValueError:
                print("choose a number between 1 and 9 or 'q' to quit")
                continue

            try:
                result=oxo_logic.userMove(game,cell)
            except ValueError:
                mb.showerror('Invalid cell','Choose an empty cell')
                continue
            if not result:
                result=oxo_logic.computerMove(game)
            if not result:
                continue
            elif result=='D':
                printGame(game)
                mb.showinfo('result','its a draw')
            else:
                printGame(game)
                mb.showinfo('result','winner is {}'.format(result))
