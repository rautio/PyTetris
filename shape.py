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
		x = 4
		y = 0
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
	def out_of_bounds(self,direction):
		"""Return if the shape will be out of bounds if moved one step towards direciton """
		for i in self.blocks:
			if(i.get_location()[0]-1 < 0 or i.get_location()[0]+1 < 9 or i.get_location()[1] + 1 > 19):
				return false
		return true

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
			for i in reversed(self.blocks):
				if(i.get_location()[1]+1 > 19):
					self.blocks = temp_blocks
					break
				i.move(i.get_location()[0],i.get_location()[1]+1)
		else:
			return "Error: Not an appropriate direction"
	def rotate(self,direction):
		"""Rotate the shape"""
		if direction == "left":
			pass
		elif direction == "right":
			pass
		else:
			return "Error: Not an appropriate direction"
	def get_blocks(self):
		"""Return a list of all blocks in the shape"""
		return self.blocks
	def draw_shape(self):
		"""Draw the shape"""
		for i in self.blocks:
			i.draw_block()
		