from constants import *;
from shape import Shape

class Grid(object):
	"""
	Main class to keep track and update all objects in the grid.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	grid = []
	new = []

	def __init__(self):

		# Initialize the grid as a 20 x 10 2d list
		# "O" denotes an empty spot, "X" denotes an occupied spot
		for i in range (0,20):
			new = []
			for j in range (0,10):
				new.append("O")
			self.grid.append(new)
				
	def add_shape(self, shape):
		"""Add a shape to the grid"""
		for i in shape.get_blocks():
			if not self.collide(shape):
				self.grid[i.get_location()[0]][i.get_location()[1]] = "X"

	def collide(self,shape,direction = ""):
		""" Return if shape will collide if moved one step toward direction """
		if direction == "":
			for i in shape.get_blocks():
				if i.get_location()[0] < 0 or i.get_location()[0] > 9 or i.get_location()[1] < -1 or i.get_location()[1] > 19 or self.grid[i.get_location()[0]][i.get_location()[1]] == "X":
					return True
		elif direction == "right":
			pass
		elif direction == "left":
			pass
		elif direction == "right":
			pass
		return False
	def print_grid(self):
		"""Print the grid in an easy to understand format with the "O" and "X" of each spot. This function is only used for debugging"""
		for i in self.grid:
			print " ".join(i)
		