from constants import *;

class ScoreBoard(object):
	"""
	A class to keep track of score and level.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	def __init__(self):
		self.score = 0
		self.lvl = 1

	def get_score(self):
		"""Return current score"""
		return self.score

	def get_lvl(self):
		"""Return current level"""
		return self.lvl

	def add_score(self,num):
		"""Add num to the score"""
		self.score += num
		return self.score

	def next_level(self):
		"""Iterate the level by one"""
		self.lvl += 1
	def print_scoreboard(self):
		"""Print the scoreboard to the game screen"""
		pygame.draw.aaline(SCREEN, BLACK, [WINDOW_WIDTH/2 + BORDER,BORDER], [WINDOW_WIDTH, BORDER], True)