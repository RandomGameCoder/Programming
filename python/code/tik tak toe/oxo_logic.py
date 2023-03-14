import os, random,oxo_data

def newGame():
    return list(" "*9)

def saveGame(game):
    oxo_data.saveGame(game)

def restoreGame():
    try:
        game=oxo_data.restoreGame()
        if len(game)==9:
            return game
        else: return newGame()
    except IOError:
        return newGame()

def _generateMove(game):
    options=[i for i in range(len(game))
             if game[i]==" "]
    return random.choice(options)

def _isWinningMove(game):
    wins= ((0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for a,b,c in wins:
        chars = game[a]+game[b]+game[c]
        if chars =='XXX' or chars =='OOO':
            return True
    return False

def userMove(game,cell):
    if game[cell]!=' ':
        raise ValueError('Invalid cell')
    else:
        game[cell]='X'
    if _isWinningMove(game):
        return 'X'
    else:
        return ''

def computerMove(game):
    cell=_generateMove(game)
    if cell==-1:
        return 'D'
    game[cell]='O'
    if _isWinningMove(game):
        return 'O'
    else:
        return ''

def test():
    result=''
    game=newGame()
    while not result:
        print(game)
        try:
            result=userMove(game,_generateMove(game))
        except ValueError:
            print("Oops, that sholdn't happen")
        if not result:
            result=computerMove(game)
        if not result: continue
        elif result=='D':
            print("its a draw")
        else:
            print("the winner is",result)
        print(game)

if __name__=="__main__":
    test()
            
    
