class Account:
	

	def __init__(self, balance = 0):
		self._balance = balance

	def pay(self, amount):
		self._balance+=amount

	def take(self, amount):
		if self._balance<amount:
			print("Nie masz wystarczająco srodków aby wykonać transakcje")
		else:
			self._balance-=amount

	def __str__(self):
		return str(self._balance)

