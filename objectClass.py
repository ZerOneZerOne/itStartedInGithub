class Fruit:
	'''this is a class that describes a fruit'''
	def __init__(self,given_name,given_colors,given_taste):
		self.name= given_name
		self.color=given_colors
		self.taste=given_taste
		
	@staticmethod
	def add(num1,num2):
		num3 =num1+num2
		return num3
		
	def we_like(self):
		if self.taste=="bitter":
			return "dont like"
		else:
			return "like"
		