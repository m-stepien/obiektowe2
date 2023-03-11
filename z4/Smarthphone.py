class Smarthphone:
	
	def __init__(self,manufacturer,model,price):
		self._manufacturer=manufacturer
		self._model=model
		self._price=price

	def get_manufacturer(self):
		return self._manufacturer

	def get_model():
		return self._model

	def get_price():
		return self._price

	def set_manufacturer(self, manufacturer):
		self._manufacturer = manufacturer

	def set_model(self, model):
		self._model = model

	def set_price(self, price):
		self._price = price

	def show_manufacturer(self, manufacturer):
		print(self._manufacturer)

	def show_model(self, model):
		print(self._model)

	def show_price(self, price):
		print(self._price)

	def __str__(self):
		return "manufacturer: {}\nmodel: {}\nprice: {}".format(self._manufacturer, self._model, self._price)

