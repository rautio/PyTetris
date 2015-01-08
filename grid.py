from constants import *;
from shape import Shape

class Grid(object):
	"""
	Main class to keep track and update all objects in the grid.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	grid = []			 # Internal representation of the grid
	shapes = []	         # List of shapes that are already settled
	active_shape = None  # Current shape being moved

	def __init__(self):

		# Initialize the grid as a 20 x 10 2d list
		# "O" denotes an empty spot, "X" denotes an occupied spot
		for i in range (0,10):
			new = []
			for j in range (0,20):
				new.append("O")
			self.grid.append(new)
		newshape = Shape()
		self.active_shape = newshape
		self.update_grid()
				
	def add_shape(self, shape):
		"""Add a shape to the grid"""
		self.shapes.append(shape)
		self.update_grid()
	def update_grid(self):

		self.grid = []
		# Clear the grid
		for i in range (0,10):
			new = []
			for j in range (0,20):
				new.append("O")
			self.grid.append(new)

		# Draw "X"s where any stopped shape is
		for shape in self.shapes:
			for i in shape.get_blocks():
				if not i.out_of_bounds():
					self.grid[i.get_location()[0]][i.get_location()[1]] = "X"

		# Draw "X"s where the current active shape is
		for i in self.active_shape.get_blocks():
			if not i.out_of_bounds():
				self.grid[i.get_location()[0]][i.get_location()[1]] = "X"

	def move_shape(self,direction):
		"""Main function used to move or rotate a shape in the grid"""
		if direction == "right":
			if not self.collide(self.active_shape,direction):
				self.active_shape.move(direction)
		elif direction == "left":
			if not self.collide(self.active_shape,direction):
				self.active_shape.move(direction)
		elif direction == "down":
			if not self.collide(self.active_shape,direction):
				self.active_shape.move(direction)
				self.update_grid()
				self.print_grid()
		elif direction == "rotate":
			pass
		else:
			pass

	def collide(self,shape,direction = ""):
		#TODO: Need to change shape to self.active_shape
		""" Return if shape will collide if moved one step toward direction """
		if direction == "":
			for i in shape.get_blocks():
				if i.get_location()[0] < 0 or i.get_location()[0] > 9 or i.get_location()[1] < -1 or i.get_location()[1] > 19 or self.grid[i.get_location()[0]][i.get_location()[1]] == "X":
					return True
		elif direction == "right":
			for i, blocks in enumerate(shape.get_blocks()):
				if i != len(shape.get_blocks())-1 and blocks[i+1].get_location()[0] == blocks[i].get_location()[0]+1:
					pass
				elif i.get_location()[0] > 9 or self.grid[i.get_location()[0]+1][i.get_location()[1]] == "X":
					return True
		elif direction == "left":
			pass
		elif direction == "down":
			for i in shape.get_outer_blocks(direction):
				if shape.out_of_bounds(direction) or self.grid[i.get_location()[0]][i.get_location()[1]+1] == "X":
					return True
		return False
	def draw_shapes(self):
		for i in self.shapes:
			i.draw_shape()
		self.active_shape.draw_shape()
	def print_grid(self):
		"""Print the grid in an easy to understand format with the "O" and "X" of each spot. This function is only used for debugging"""
		for i in self.grid:
			print " ".join(i)
		