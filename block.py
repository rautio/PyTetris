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
		self.x = x
		self.y = y
	def location(self):
		return (self.x,self.y)
	def draw_block(self,screen):
		# Outline
		pygame.draw.rect(screen,BLACK, [75, 10, 50, 20], 2)
   		# Draw a solid rectangle
		pygame.draw.rect(screen, self.color, [75, 10, 50, 20])
      