"""
	A simple tetris game written in Python.
	Uses Pygame library.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
"""
import pygame

# Initialize game engine
pygame.init()

# Define Constants

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED =(255,0,0)
PI = 3.141592653

# Set height and width of screen
size = [400,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyTetris - A very slimy Tetris")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------- Main Program Loop ------------
while not done:
	# --- Main event Loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT:
			done = True
	
	# --- Game logic

	# --- Drawing code should go here

	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(WHITE)

	# --- Update screen
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit
pygame.quit()