import os.path
game_file=".oxogame.dat"

def _getPath():
    try:
        game_path=os.environ['HOMEPATH'] or os.environ['HOME']
        if not os.path.exists(game_path):
            game_path=os.getcwd()
    except (KeyError,TypeError):
        game_path=os.getcwd()
    return game_path

def saveGame(game):
    path=os.path.join(_getPath(),game_file)
    with open(path,'w') as gf:
        gamestr=''.join(game)
        gf.write(gamestr)

def restoreGame():
    path=os.path.join(_getPath(),game_file)
    with open(path) as gf:
        gamestr=gf.read()
        return list(gamestr)

def test():
    print("Path=",_getpath())
    saveGame(list("XO  XO OX"))
    print(restoreGame())

if __name__=="__main__": test()
