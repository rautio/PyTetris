from constants import *;

class Shape(object):
	"""
	A class to store information about each shape.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	def __init__ (self,form,x,y):
		self.blocks = []
		if(form == "I"):
			# [][][][]
			blocks.append(Block(color,x,y))
		elif(form == "J"):
			# [][][]
			#     []
			pass
		elif(form == "L"):
			# [][][]
			# []
			pass
		elif(form == "O"):
			# [][]
			# [][]
			pass
		elif(form == "S"):
			#   [][]
			# [][]
			pass
		elif(form == "T"):
			# [][][]
			#   []
			pass
		elif(form == "Z"):
			# [][]
			#   [][]
			pass
	def move(self,direction):
		if direction == "left":
			self.x -= 1
		elif direction == "right":
			self.x += 1
		elif direction == "down":
			self.y += 1
		elif direction == "up":
			# This should never really be used...
			self.y -= 1
		else:
			return "Error: Not an appropriate direction"
		
