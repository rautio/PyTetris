from constants import *;
from shape import Shape

class Grid(object):
	"""
	Main class to keep track and update all objects in the grid.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	active_shape = None
	grid =[]

	def __init__(self):
		for i in range (0,20):
			self.grid.append("O" * 10)
	def add_shape(self, shape):
		active_shape = shape
	def update(self,direction):
		if direction == "down":
			pass
		elif direction == "left":
			pass
		elif direction == "right":
			pass
		else:
			return "Error: Inappropraite direction"
	def print_grid(self):
		# For testing purposes only
		#for i in self.grid:
		#	print " ".join(i)
		pygame.draw.aaline(SCREEN, BLACK, [BORDER, WINDOW_HEIGHT - BORDER], [BORDER, BORDER], True)
		pygame.draw.aaline(SCREEN, BLACK, [WINDOW_WIDTH/2, BORDER], [BORDER,BORDER], True)
		for i in range(1,11):
			pygame.draw.aaline(SCREEN, BLACK, [WIDTH_SPACER * i + BORDER, WINDOW_HEIGHT-BORDER], [WIDTH_SPACER * i + BORDER, BORDER], True)
		for i in range(1,21):
			pygame.draw.aaline(SCREEN, BLACK, [WINDOW_WIDTH/2, HEIGHT_SPACER*i + BORDER], [BORDER, HEIGHT_SPACER*i + BORDER], True)
