class Player:
	def __init__(self):
		self._score = 0
		self._still_playing = True
		self._block = False

	def add_to_score(self, num):
		self._score+=num

	def get_score(self):
		return self._score

	def block_playing(self):
		self._block = True

	def get_block(self):
		return self._block

	def get_still_playing(self):
		return self._still_playing

	def decide_want_stil_play(self):
		result = input("Do you want roll die?\n1. yes\n2. no\n")
		if result=='1':
			self._still_playing = True
		else:
			self._still_playing = False