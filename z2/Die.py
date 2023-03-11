import random
class Die:
	
	def __init__(self, sides):
		self._sides = sides
		self._value = None

	def roll(self):
		self._value = random.randint(1, self._sides)

	def get_value(self):
		return self._value

	def get_sides(self):
		return self._sides

	def __str__(self):
		return "Sides: {}\nValue: {}".format(self._sides, self._value)
	