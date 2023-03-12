class Pet:
	def __init__(self, name, hunger=0, tiredness=0):
		self.name = name
		self.hunger = hunger
		self.tiredness = tiredness
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):	
		if len(name)>=3 and name.isalpha():
				self._name = name

	@property
	def mood(self):
		sum = self.hunger + self.tiredness
		if sum<=5:
			return "Szczesliwy"
		elif sum<=10:
			return "Zadowolony"
		elif sum<=15:
			return "Podenerwowany"
		elif sum>15:
			return "Wsciekly"



	def _passage_of_time(self):
		self.hunger+=1
		self.tiredness+=1

	def talk(self):
		self._passage_of_time()
		print(self.mood)

	def eat(self, food=4):
		self._passage_of_time()
		if food>self.hunger:
			self.hunger = 0
		else:
			self.hunger-=food

	def play(self, fun=4):
		self._passage_of_time()
		if fun>self.tiredness:
			self.tiredness = 0
		else:
			self.tiredness-=fun

	def __str__(self):
		return "{}:\nhunger: {}\ntiredness: {}\nmood: {}".format(self.name, self.hunger, self.tiredness, self.mood)