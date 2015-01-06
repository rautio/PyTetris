import pygame

# Define Constants

WHITE = (255,255,255)
BLACK = (0,0,0)

# Shape colors defined according to standardization set by The Tetrics Company
CYAN = (0,240,255)
BLUE = (0,0,255)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
LIME = (100,255,0)
MAGENTA = (230,40,180)
RED =(255,0,0)
SHAPES = ["I","J","L","O","S","T","Z"]
PI = 3.141592653

WINDOW_HEIGHT = 600 
WINDOW_WIDTH = 600
BORDER = 50
WIDTH_SPACER = (WINDOW_WIDTH/2-BORDER)/10
HEIGHT_SPACER = (WINDOW_HEIGHT - 2*BORDER)/20
# Set width and height of screen
SIZE = [WINDOW_WIDTH+BORDER,WINDOW_HEIGHT+BORDER]
SCREEN = pygame.display.set_mode(SIZE)
