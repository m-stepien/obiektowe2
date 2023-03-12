class Remote:
	

	def __init__(self, chanel, volume):
		self._chanel = chanel
		self._volume = volume

	@property
	def chanel(self):
		return self._chanel

	@chanel.setter
	def chanel(self, chanel):
		if type(chanel) == int and chanel >0 and chanel <1000:
			self._chanel = chanel

	@property
	def volume(self):
		return self._volume

	@volume.setter
	def volume(self, volume):
		if type(volume) == int and volume>0 and volume <=20:
			self._volume=volume
