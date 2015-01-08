from constants import *;
from shape import Shape
from scoreboard import ScoreBoard

class Grid(object):
	"""
	Main class to keep track and update all objects in the grid.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	grid = []			 # Internal representation of the grid
	shapes = []	         # List of shapes that are already settled
	active_shape = None  # Current shape being moved
	sb = ScoreBoard()	 # Keeps track of score and level
	def __init__(self):

		# Initialize the grid as a 20 x 10 2d list
		# "O" denotes an empty spot, "X" denotes an occupied spot
		for i in range (0,10):
			new = []
			for j in range (0,20):
				new.append("O")
			self.grid.append(new)
		self.active_shape = Shape()
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

	def check_grid(self):
		"""Check if any row is full, if so call delete_row()"""
		for i in reversed(range(0,20)):
			full_row = 0
			for j in reversed(range(0,10)):
				if self.grid[j][i] == "X":
					full_row += 1
			if full_row == 10:
				self.delete_row(i)
				self.sb.add_score(10)
				print "Score: ", self.sb.get_score()
				self.check_grid()

	def delete_row(self,row):
		"""Removes all blocks in given row and moves every block above it down one unit"""
		for shape in self.shapes:
			blocks = shape.get_blocks()
			# Check to see which blocks match current row and delete them
			to_delete = [x for x in shape.get_blocks() if x.get_location()[1] == row]
			for block in to_delete:
				shape.remove_block(block)
			to_move = [x for x in shape.get_blocks() if x.get_location()[1] < row]
			# Check to see which blocks are above the current row and move them down one unit
			for block in to_move:
				block.move(block.get_location()[0],block.get_location()[1]+1)
		self.update_grid()

	def move_shape(self,direction):
		"""Main function used to move or rotate a shape in the grid"""
		if direction == "right":
			if not self.collide(direction):
				self.active_shape.move(direction)
		elif direction == "left":
			if not self.collide(direction):
				self.active_shape.move(direction)
		elif direction == "down":
			if not self.collide(direction):
				self.active_shape.move(direction)
			else:
				# At top - Game Over

				# At bottom - new shape
				self.add_shape(self.active_shape)
				self.active_shape = Shape()
				#time.sleep(0.1)
				self.check_grid()
				self.update_grid()

		elif direction == "rotate":
			print "Trying to rotate"
		else:
			return "Error: Invalid direction in grid - move_shape()"
		self.update_grid()

	def collide(self, direction = ""):
		""" Return if active_shape will collide if moved one step toward direction """
		if direction == "":
			for i in self.active_shape.get_blocks():
				if i.get_location()[0] < 0 or i.get_location()[0] > 9 or i.get_location()[1] < -1 or i.get_location()[1] > 19 or self.grid[i.get_location()[0]][i.get_location()[1]] == "X":
					return True
		elif direction == "left":
			for i in self.active_shape.get_outer_blocks(direction):
				if self.active_shape.out_of_bounds(direction) or self.grid[i.get_location()[0]-1][i.get_location()[1]] == "X":
					return True
		elif direction == "right":
			for i in self.active_shape.get_outer_blocks(direction):
				if self.active_shape.out_of_bounds(direction) or self.grid[i.get_location()[0]+1][i.get_location()[1]] == "X":
					return True
		elif direction == "down":
			for i in self.active_shape.get_outer_blocks(direction):
				if self.active_shape.out_of_bounds(direction) or self.grid[i.get_location()[0]][i.get_location()[1]+1] == "X":
					return True
		elif direction == "rotate":
			print "Trying to rotate"
			pass
		return False
	def draw_shapes(self):
		for i in self.shapes:
			i.draw_shape()
		self.active_shape.draw_shape()
	def print_grid(self):
		"""Print the grid in an easy to understand format with the "O" and "X" of each spot. This function is only used for debugging"""
		for i in self.grid:
			print " ".join(i)
		