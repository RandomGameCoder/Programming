import pygame, sys, random

# initialize pygame
pygame.init()

class Game:
    
    BOARD = [
        [ '1', '2', '3' ],
        [ '4', '5', '6' ],
        [ '7', '8', ' ' ]
    ]
    
    RECTS = [
        [ None, None, None ],
        [ None, None, None ],
        [ None, None, None ]
    ]
    
    MOVES = {
        'l' : (-1, 0),
        'r' : (1, 0),
        'u' : (0, -1),
        'd' : (0, 1),
        None : (0, 0)
    }
    
    MOVING = True
    RECT = None
    DIR = None
    SPEED = 10.8
    
    CLICKED = 0
    
    def __init__(self, window_width: int, window_height: int, title: str = "Untitled"):
        """ Initialises the game variables and creates the window

        Args:
            window_width (int): The width of the window
            window_height (int): The height of the window
            title (str, optional): Sets the window title. Defaults to "Untitled".
        """        
        
        # setting up window
        self.WINDOW = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption(title)
        self.FONT = pygame.font.SysFont("Segoe UI", 60)
        self.CLOCK = pygame.time.Clock()
        
        locs = [ (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) ]
        
        for i in range(8):
            index = locs[random.randint(0,8-i)]
            self.BOARD[index[0]][index[1]] = str(i+1)
            self.RECTS[index[0]][index[1]] = pygame.Rect(( 24 + index[1]*108, 44 + index[0]*108),( 100, 100 ))
            locs.remove(index)
        
        print(self.RECTS)
        self.BOARD[locs[0][0]][locs[0][1]] = ' '
        
        self.start()
    
    def game_loop(self):
        """ The game loop of the game

        Returns:
            None: When the game is exited
        """
        
        
        # main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    return None
            
            # game update
            self.update()
            
            self.CLICKED = pygame.mouse.get_pressed()[0]
            
            if self.CLICKED == 1:
                i,j = self.index(*pygame.mouse.get_pos())
                if i != -1 and j != -1:
                    self.RECT = self.RECTS[i][j]
                    self.DIR = self.direction(i,j)
                    self.MOVING = True
            
            if self.MOVING:
                # clear screen
                self.WINDOW.fill((69, 48, 14))
                
                # render
                self.render(self.WINDOW)
                
                self.move()
            
            # reflect the render on the window
            pygame.display.flip()
    
    def start(self):
        """ Starts the game loop
        """
        self.game_loop()
        
        sys.exit()
    
    def exit(self):
        """ Quits the window
        """
        pygame.quit()
    
    def update(self):
        """ Method to update the game variables
        This function is to be overridden with the game's update code

        Args:
            dt (float): The offset time between each frame. Multiplied with values to get a consistent speed in any frame rate  
        """
        pass
    
    def render(self, window):
        """ Method to render the game visuals
        This function is to be overridden with the game's render
        """
        for i in self.RECTS:
            for j in i:
                if j == None:
                    continue
                pygame.draw.rect(window, (171, 112, 17), j)
        
        for r in self.BOARD:
            for c in r:
                if c == ' ':
                    continue
                i = self.BOARD.index(r)
                j = r.index(c)
                x = self.RECTS[i][j].left
                y = self.RECTS[i][j].top
                textsurface = self.FONT.render('  '+c, False, "black")
                window.blit(textsurface, (x,y))
    
    def direction (self, i, j):
        if i < 2 and self.BOARD[i+1][j] == ' ':
            return 'd'
        elif i > 0 and self.BOARD[i-1][j] == ' ':
            return 'u'
        elif j > 0 and self.BOARD[i][j-1] == ' ':
            return 'l'
        elif j < 2 and  self.BOARD[i][j+1] == ' ':
            return 'r'
        return None

    def index(self, x, y):
        i = j = -1
        if 24 < x < 124:
            j = 0
        elif 132 < x < 232:
            j = 1
        elif 240 < x < 340:
            j = 2
        if 44 < y < 144:
            i = 0
        elif 152 < y < 252:
            i = 1
        elif 260 < y < 360:
            i = 2
        return i,j

    def move(self):
        if self.RECT == None:
            self.MOVING = False
            return
        if self.direction(*self.index(self.RECT.left + 1, self.RECT.top + 1)) != self.DIR:
            i,j = self.index(self.RECT.left + 1, self.RECT.top + 1)
            self.DIR = self.direction(i,j)
            mov = self.MOVES[self.DIR]
            self.BOARD[i][j], self.BOARD[i+mov[0]][j+mov[1]] = self.BOARD[i+mov[0]][j+mov[1]], self.BOARD[i][j]
            self.RECTS[i][j], self.RECTS[i+mov[0]][j+mov[1]] = self.RECTS[i+mov[0]][j+mov[1]], self.RECTS[i][j]
            self.MOVING = False
            return
        #i,j = self.index(self.RECT.left + 1, self.RECT.top + 1)
        mov = self.MOVES[self.DIR]
        print(mov)
        self.RECT.move_ip(mov[0]*self.SPEED, mov[1]*self.SPEED)
        
        
           
if __name__ == "__main__":
    Game(364,384,"Eight Puzzle")