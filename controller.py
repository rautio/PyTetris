"""
	A simple tetris game written in Python.
	Uses Pygame library.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
"""
import pygame
from shape import Shape
from block import Block
from constants import *;

# Initialize game engine
pygame.init()

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

	# if round over create new shape
	# else move shape down
	# check for collisions

	# --- Drawing code should go here

	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(WHITE)

	# Testing draw_block function
	#block1 = Block(GREEN,50,50)
	#block1.draw_block(screen)
	# --- Update screen
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit
pygame.quit()