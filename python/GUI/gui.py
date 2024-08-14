import pygame, sys

# initialize pygame
pygame.init()

class Game:
    
    # Game variables
    FRAME_RATE = 120
    
    DEBUG = False
    
    
    def __init__(self, title = "Untitled"):
        """ Initialises the game variables and creates the window

        Args:
            window_width (int): The width of the window
            window_height (int): The height of the window
            title (str, optional): Sets the window title. Defaults to "Untitled".
        """        
        
        # setting up window
        self.WINDOW = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
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