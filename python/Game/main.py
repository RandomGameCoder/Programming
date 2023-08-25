import pygame, Game

class Sim(Game):
    TITLE = "SIMULATION"
    
    GRID_WIDTH = 0
    GRID_HEIGHT = 0
    CELL_WIDTH = 0
    CELL_HEIGHT = 0
    
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
        super().__init__(width, height, self.TITLE)
        