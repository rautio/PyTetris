"""
	A simple tetris game written in Python.
	Uses Pygame library.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
"""
import pygame
from shape import Shape
from block import Block
from grid import Grid
from scoreboard import ScoreBoard
from constants import *;

# Initialize game engine
pygame.init()

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
	SCREEN.fill(WHITE)

	# Testing draw_block function
	#block1 = Block(GREEN,50,50)
	#block1.draw_block(screen)
	grid1 = Grid()
	grid1.print_grid()
	sb = ScoreBoard()
	sb.print_scoreboard()
	block1 = Block(RED,2,2)
	block2 = Block(RED,2,3)
	block3 = Block(RED,3,3)
	#block1.draw_block()
	#block2.draw_block()
	#block3.draw_block()
	shapes = ["I","J","L","O","S","T","Z"]
	for i in shapes:
		shape1 = Shape(i,4, int(shapes.index(i))*2)
		shape1.draw_shape()
	# --- Update screen
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit
pygame.quit()