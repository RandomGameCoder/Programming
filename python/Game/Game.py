import pygame, sys

# initialize pygame
pygame.init()

class Game:
    
    # Game variables
    FRAME_RATE = 120
    # get display info
    DISPLAY_INFO = pygame.display.Info()
    
    DEBUG = False
    
    
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
        
        self.start()
    
    
    def set_framerate(self, framerate: int):
        """ sets the maximum framerate for the window

        Args:
            framerate (int): The new frame rate to be set
        """
        self.FRAME_RATE = framerate
    
    def game_loop(self):
        """ The game loop of the game

        Returns:
            None: When the game is exited
        """
        dt = 0
        
        # main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F10:
                        self.toggle_debug()
                    self.keypressed(event.key)
                elif event.type == pygame.KEYUP:
                    self.keyreleased(event.key)
            
            # game update
            self.update(dt)
            
            # clear screen
            self.WINDOW.fill("black")
            
            # render
            self.render(self.WINDOW)
            
            # reflect the render on the window
            pygame.display.flip()
            
            # calculating delta time
            dt = self.CLOCK.tick(self.FRAME_RATE) / 1000
    
    def show_debug(self):
        if not self.DEBUG:
            return None
        # render debug info
    
    def start(self):
        """ Starts the game loop
        """
        self.game_loop()
        
        sys.exit()
    
    def keypressed(self, key):
        """ Handles the event when a key is pressed
        This function is to be overridden with the game's input handling

        Args:
            key (pygame key): The pressed key is passed onto this method
        """

        pass
    
    def keyreleased(self, key):
        """ Handles the event when a key is released
        This function is to be overridden with the game's input handling

        Args:
            key (pygame key): The released key is passed onto this method
        """

        pass
    
    def exit(self):
        """ Quits the window
        """
        pygame.quit()
    
    def update(self, dt: float):
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
        pass
    
    
    
    def toggle_debug(self):
        self.DEBUG = not self.DEBUG

class Sim(Game):
    TITLE = "SIMULATION"
    
    GRID_WIDTH = 0
    GRID_HEIGHT = 0
    CELL_WIDTH = 0
    CELL_HEIGHT = 0
    
    SHOW_GRID = True
    
    def __init__(self, g_width: int, g_height: int, c_width: int, c_height: int):
        """_summary_

        Args:
            g_width (int): The number of columns of cells to fit in the window
            g_height (int): The number of rows of cells to fit in the window
            c_width (int): The width of one cell in pixels
            c_height (int): The height of one cell in pixels
        """
        # initialising the game values
        self.GRID_WIDTH = g_width
        self.GRID_HEIGHT = g_height
        self.CELL_WIDTH = c_width
        self.CELL_HEIGHT = c_height
        
        # calculating the window's width and height
        width = self.CELL_WIDTH * self.GRID_WIDTH
        height = self.CELL_HEIGHT * self.GRID_HEIGHT
        
        # initialising the window
        super().__init__(width, height, title = self.TITLE)
    
    def render(self, window):
        if self.SHOW_GRID:
            for i in range(1,self.GRID_WIDTH):
                pygame.draw.line(window, (255,255,255), (i*self.CELL_WIDTH, 0), (i*self.CELL_WIDTH, self.CELL_HEIGHT * self.GRID_HEIGHT))
            for i in range(1,self.GRID_HEIGHT):
                pygame.draw.line(window, (255,255,255), (0, i*self.CELL_HEIGHT),(self.CELL_WIDTH * self.GRID_WIDTH, i*self.CELL_HEIGHT))
                    
if __name__ == "__main__":
    new = Sim(128,128,5,5)