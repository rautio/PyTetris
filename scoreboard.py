from constants import *;

class Scoreboard(object):
	"""
	A class to keep track of score and level.

	Oskari Rautiainen
	oskari.rautiainen@gmail.com
	"""
	def __init__(self):
		self.score = 0
		self.lvl = 1
	def get_score(self):
		return self.score
	def get_lvl(self):
		return self.lvl
	def add_score(self,num):
		self.score += num
		return self.score
	def next_level(self):
		self.lvl += 1