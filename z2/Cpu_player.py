from Player import Player

class Cpu_player(Player):
	
	def __init__(self):
		Player.__init__(self)

	def decide_want_stil_play(self):
		if self._score>16:
			self._still_playing = False
		else:
			self._still_playing = True