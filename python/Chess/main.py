global board
board = [
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','','']
]

layout = [
    ['r','k','b','k','q','b','k','r'],
    ['p','p','p','p','p','p','p','p'],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    ['p','p','p','p','p','p','p','p'],
    ['r','k','b','k','q','b','k','r']
]

class Piece:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.poss_sqrs = []
    
    def possible_sqrs(self):
        dirs = [
            (0,-1),(1,0),
            (1,-1),(0,1),
            (-1,0),(1,1),
            (-1,1),(-1,-1)
        ]
        for n in range(1,7):
            for chord in dirs:
                loc = (self.x + chord[0]*n,self.y + chord[1]*n)
                if not 0<loc[0]<8 or not 0<loc[1]<8:
                    continue
                self.poss_sqrs.append(loc)
        print(self.poss_sqrs)

class Queen(Piece):
    def __init__(self,*args):
        super().__init__(*args)

class Rook(Piece):
    def __init__(self,*args):
        super().__init__(*args)
        
    def possible_sqrs(self):
        dirs = [
            (0,-1),(1,0),
            (0,1),(-1,0)
        ]
        for n in range(1,7):
            for chord in dirs:
                loc = (self.x + chord[0]*n,self.y + chord[1]*n)
                if not 0<loc[0]<8 or not 0<loc[1]<8:
                    continue
                self.poss_sqrs.append(loc)
        print(self.poss_sqrs)

class Bishop(Piece):
    def __init__(self,*args):
        super().__init__(*args)
        
    def possible_sqrs(self):
        dirs = [
            (1,-1),(1,1),
            (-1,1),(-1,-1)
        ]
        for n in range(1,7):
            for chord in dirs:
                loc = (self.x + chord[0]*n,self.y + chord[1]*n)
                if not 0<loc[0]<8 or not 0<loc[1]<8:
                    continue
                self.poss_sqrs.append(loc)
        print(self.poss_sqrs)

class Knight(Piece):
    def __init__(self,*args):
        super().__init__(*args)
        
    def possible_sqrs(self):
        dirs = [
            (1,-3),(1,3),
            (-1,-3),(-1,3),
            (3,1),(3,-1),
            (-3,1),(-3,-1)
        ]
        for chord in dirs:
            loc = (self.x + chord[0],self.y + chord[1])
            if not 0<loc[0]<8 or not 0<loc[1]<8:
                continue
            self.poss_sqrs.append(loc)
        print(self.poss_sqrs)

r = Knight(4,4,'Black')
r.possible_sqrs()