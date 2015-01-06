import pygame
from constants import *;

class Block(object):
	"""
	A class to store information about each block of a shape.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	def __init__(self,color,x,y):
		self.x = x
		self.y = y
		self.color = color
	def move(self,x,y):
		"""Change x and y locations to inputs x and y"""
		self.x = x
		self.y = y
	def get_location(self):
		"""Return a list (x,y) of the coordinates of the block"""
		return (self.x,self.y)
	def draw_block(self):
		"""Draw the block only if it is within bounds of the 20 x 10 grid"""
		if(self.x >=0 and self.x <=9 and self.y >=0 and self.y <= 19):
			# Outline
			pygame.draw.rect(SCREEN,BLACK, [self.x * WIDTH_SPACER + 1 + BORDER, self.y * HEIGHT_SPACER + 1 + BORDER, WIDTH_SPACER-1, HEIGHT_SPACER-1], 1)
	   		# Draw a solid rectangle
			pygame.draw.rect(SCREEN, self.color, [self.x * WIDTH_SPACER + 2 + BORDER, self.y * HEIGHT_SPACER + 2 + BORDER, WIDTH_SPACER-3, HEIGHT_SPACER-3])
	    