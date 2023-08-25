import pygame

class Game:
    
    def __init__(self, window_width, window_height, title = "Untitled"):
        # initialize pygame
        pygame.init()
        
        # setting up window
        self.WINDOW = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption(title)
        
        # game loop
        self.__game_loop()
    
    def __game_loop(self):
        # main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    return None
                elif event.type == pygame.KEYDOWN:
                    self.keypressed(event.key)
    
    def keypressed(self, key):
        # automatically called at time of execution, the key value is automatically passed
        # need to be overidden
        pass
    
    def exit(self):
        pygame.quit()
    
    def update(self):
        # function to override
        pass
    
    def render(self):
        # function to override
        pass
                    
if __name__ == "__main__":
    new = Game(800, 600)
    