from constants import *;
from block import Block
from random import randint

class Shape(object):
	"""
	A class to store information about each shape.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	def __init__ (self):
		index = randint(0,6)
		form = SHAPES[index]
		x = START_X
		y = START_Y
		self.blocks = []
		if(form == "I"):
			# [][][][]
			self.blocks.append(Block(CYAN,x,y))
			self.blocks.append(Block(CYAN,x+1,y))
			self.blocks.append(Block(CYAN,x+2,y))
			self.blocks.append(Block(CYAN,x+3,y))
		elif(form == "J"):
			# [][][]
			#     []
			self.blocks.append(Block(BLUE,x,y-1))
			self.blocks.append(Block(BLUE,x+1,y-1))
			self.blocks.append(Block(BLUE,x+2,y-1))
			self.blocks.append(Block(BLUE,x+2,y))
		elif(form == "L"):
			# [][][]
			# []
			self.blocks.append(Block(ORANGE,x,y))
			self.blocks.append(Block(ORANGE,x,y-1))
			self.blocks.append(Block(ORANGE,x+1,y-1))
			self.blocks.append(Block(ORANGE,x+2,y-1))
		elif(form == "O"):
			# [][]
			# [][]
			self.blocks.append(Block(YELLOW,x,y))
			self.blocks.append(Block(YELLOW,x,y-1))
			self.blocks.append(Block(YELLOW,x+1,y))
			self.blocks.append(Block(YELLOW,x+1,y-1))
		elif(form == "S"):
			#   [][]
			# [][]
			self.blocks.append(Block(LIME,x+1,y-1))
			self.blocks.append(Block(LIME,x+2,y-1))
			self.blocks.append(Block(LIME,x,y))
			self.blocks.append(Block(LIME,x+1,y))
		elif(form == "T"):
			# [][][]
			#   []
			self.blocks.append(Block(MAGENTA,x,y-1))
			self.blocks.append(Block(MAGENTA,x+1,y-1))
			self.blocks.append(Block(MAGENTA,x+1,y))
			self.blocks.append(Block(MAGENTA,x+2,y-1))
		elif(form == "Z"):
			# [][]
			#   [][]
			self.blocks.append(Block(RED,x,y-1))
			self.blocks.append(Block(RED,x+1,y-1))
			self.blocks.append(Block(RED,x+1,y))
			self.blocks.append(Block(RED,x+2,y))
	def out_of_bounds(self,direction = ""):
		"""Return True if the shape will be out bounds if moved one step towards direciton, else False if would still be in bounds """
		if direction == "":
			for i in self.blocks:
				if i.out_of_bounds():
					return True
		if direction == "left":
			for i in self.blocks:
				if i.out_of_bounds("left"):
					return True
		elif direction == "right":
			for i in self.blocks:
				if i.out_of_bounds("right"):
					return True
		elif direction == "down":
			for i in self.blocks:
				if i.out_of_bounds("down"):
					return True
		return False

	def move(self,direction):
		"""Move the shape one step toward direction"""
		temp_blocks = self.blocks
		if direction == "left":
			for i in self.blocks:
				if(i.get_location()[0]-1 < 0):
					self.blocks = temp_blocks
					break
				i.move(i.get_location()[0]-1,i.get_location()[1])				
		elif direction == "right":
			for i in reversed(self.blocks):
				if(i.get_location()[0]+1 > 9):
					self.blocks = temp_blocks
					break
				i.move(i.get_location()[0]+1,i.get_location()[1])
		elif direction == "down":
			for i in reversed(self.blocks):
				if(i.get_location()[1]+1 > 19):
					self.blocks = temp_blocks
					break
				i.move(i.get_location()[0],i.get_location()[1]+1)
		elif direction == "rotate":
			x_ = None
			y_ = None
			for i in reversed(self.blocks):
				if x_ == None:
					x_ = i.get_location()[0]
					y_ = i.get_location()[1]
				new_x = i.get_location()[0]-x_
				new_y = i.get_location()[1]-y_
				i.move(x_+new_y, y_-new_x)
			# Check to make sure we're not out of bounds
			x_mod = 0
			for i in reversed(self.blocks):
				if i.get_location()[0] < 0:
					if x_mod < 0-i.get_location()[0]:
						x_mod = 0-i.get_location()[0]
				if i.get_location()[0] > 9:
					if x_mod > 9 - i.get_location()[0]:
						x_mod = 9-i.get_location()[0]
			for i in reversed(self.blocks):
				i.move(i.get_location()[0]+x_mod, i.get_location()[1])
		else:
			return "Error: Not an appropriate direction"

	def get_blocks(self):
		"""Return a list of all blocks in the shape"""
		return self.blocks
	def get_outer_blocks(self,direction):
		"""Return a list of all the blocks with sides not adjacent to other blocks in the direction given"""
		result = []
		if direction == "left":
			for i in self.blocks:
				new_block = i
				for j in self.blocks:
					# Check to see if there is another block with the same y value that is to the left of the current one,
					# if so set that as the outer block. 
					if j.get_location()[1] == new_block.get_location()[1] and j.get_location()[0] < new_block.get_location()[0]:
						new_block = j
				if not new_block in result: 
					result.append(new_block)
		elif direction == "right":
			for i in self.blocks:
				new_block = i
				for j in self.blocks:
					# Check to see if there is another block with the same y value that is to the right of the current one,
					# if so set that as the outer block. 
					if j.get_location()[1] == new_block.get_location()[1] and j.get_location()[0] > new_block.get_location()[0]:
						new_block = j
				if not new_block in result: 
					result.append(new_block)
		elif direction == "down":
			for i in self.blocks:
				new_block = i
				for j in self.blocks:
					# Check to see if there is another block with the same x value that is below the current one,
					# if so set that as the outer block. 
					if j.get_location()[0] == new_block.get_location()[0] and j.get_location()[1] > new_block.get_location()[1]:
						new_block = j
				if not new_block in result: 
					result.append(new_block)
		elif direction == "rotate":
			# Essentially what we want are blocks in the rotate block that aren't in the current one
			x_ = None
			y_ = None
			original = []
			rotated = []
			for i in self.blocks:
				original.append(i.get_location())
			for i in self.blocks:
				if x_ == None:
					x_ = i.get_location()[0]
					y_ = i.get_location()[1]
				new_x = i.get_location()[0]-x_
				new_y = i.get_location()[1]-y_
				rotated.append([x_+new_y, y_-new_x])
			x_mod = 0
			for r in rotated:
				if r[0] < 0:
					if x_mod < 0 - r[0]:
						x_mod = 0 - r[0]
				if r[0] > 9:
					if x_mod > 9 - r[0]:
						x_mod = 9 - r[0]
			final_rotated = []
			for r in rotated:
				final_rotated.append([r[0]+x_mod,r[1]])
			for r in final_rotated:
				match = False
				for o in original:
					if o[0] == r[0] and o[1] == r[1]:
						match = True
				if not match:
					result.append(r)
		else:
			return "Error: Not a valid direction in shape - get_outer_blocks()"
		return result
	def remove_block(self,block):
		"""Remove the given block from the shape"""
		if block in self.blocks:
			self.blocks.remove(block)
		else:
			print("Did not remove block")
	def draw_shape(self):
		"""Draw the shape"""
		for i in self.blocks:
			i.draw_block()
		