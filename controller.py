"""
	A simple tetris game written in Python.
	Uses Pygame library.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
"""
import time
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


grid = Grid()
#grid.print_grid()
sb = ScoreBoard()
sb.print_scoreboard()
active_shape = Shape()
#grid.add_shape(active_shape)
# ---------- Main Program Loop ------------
while not done:
	# --- Main event Loop

	# Checking to see if a key is held down and then move piece
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		grid.move_shape("left")
		grid.draw_shapes()
	if keys[pygame.K_RIGHT]:
		grid.move_shape("right")
		grid.draw_shapes()
	if keys[pygame.K_DOWN]:
		grid.move_shape("down")
		grid.draw_shapes()
	if keys[pygame.K_UP]:
		grid.move_shape("rotate")
		grid.draw_shapes()
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				grid.move_shape("left")
				grid.draw_shapes()
			if event.key == pygame.K_RIGHT:
				grid.move_shape("right")
				grid.draw_shapes()
			if event.key == pygame.K_DOWN:
				grid.move_shape("down")
				grid.draw_shapes()
			if event.key == pygame.K_UP:
				grid.move_shape("rotate")
				grid.draw_shape()

	# --- Game logic

	# if round over create new shape
	# else move shape down
	# check for collisions

	# --- Drawing code should go here

	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	SCREEN.fill(WHITE)

	# Draw the outlines for the Tetris grid
	pygame.draw.aaline(SCREEN, BLACK, [BORDER, WINDOW_HEIGHT - BORDER], [BORDER, BORDER], True)
	pygame.draw.aaline(SCREEN, BLACK, [WINDOW_WIDTH/2, BORDER], [BORDER,BORDER], True)
	for i in range(1,11):
		pygame.draw.aaline(SCREEN, BLACK, [WIDTH_SPACER * i + BORDER, WINDOW_HEIGHT-BORDER], [WIDTH_SPACER * i + BORDER, BORDER], True)
	for i in range(1,21):
		pygame.draw.aaline(SCREEN, BLACK, [WINDOW_WIDTH/2, HEIGHT_SPACER*i + BORDER], [BORDER, HEIGHT_SPACER*i + BORDER], True)
	
	#active_shape.draw_shape()
	#active_shape.move("down")
	sb.print_scoreboard()
	#grid.print_grid()
	grid.draw_shapes()
	grid.move_shape("down")
	# --- Update screen
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)
	time.sleep(0.2)
#	for i in active_shape.get_blocks():
#		if i.get_location()[1] >= 19:
#			active_shape = Shape("K",4,0)
#			grid.add_shape(active_shape)

# Close the window and quit
pygame.quit()