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
        'l' : (0, -1),
        'r' : (0, 1),
        'u' : (-1, 0),
        'd' : (1, 0)
    }
    
    MOVING = True
    RECT = None
    DIR = None
    SPEED = 10.8
    
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
        self.CLOCK = pygame.time.Clock()
        
        locs = [ (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) ]
        
        for i in range(8):
            index = locs[random.randint(0,8-i)]
            self.BOARD[index[0]][index[1]] = str(i+1)
            self.RECTS[index[0]][index[1]] = pygame.Rect(( 24 + index[0]*108, 44 + index[1]*108),( 100, 100 ))
            locs.remove(index)
        
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
    
    def direction (self, i, j):
        if i < 3 and self.BOARD[i+1][j] == ' ':
            return 'd'
        elif i > -1 and self.BOARD[i-1][j] == ' ':
            return 'u'
        elif j > -1 and self.BOARD[i][j-1] == ' ':
            return 'l'
        elif j < 3 and  self.BOARD[i][j+1] == ' ':
            return 'r'

    def index(self, x, y):
        i = j = -1
        if 24 < x < 124:
            i = 0
        elif 132 < x < 232:
            i = 1
        elif 240 < x < 340:
            i = 2
        if 44 < y < 144:
            j = 0
        elif 152 < y < 252:
            j = 1
        elif 260 < y < 360:
            j = 2
        return i,j

    def move(self):
        if self.RECT == None:
            self.MOVING = False
            return
        if self.direction(self.index(self.RECT.left, self.RECT.top)) != self.DIR:
            
        
           
if __name__ == "__main__":
    Game(364,384,"Eight Puzzle")