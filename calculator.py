#this is a program for a basic numerical calculator
class Calculator:
	def __init__ (self,a,b):
		self.a=a
		self.b=b

	#this is the add method
	def add(self):
		return self.a+self.b

	#this is the subtract method
	def subtract(self):
		return self.a-self.b
	#this is the multiplication method
	def multiply(self):
		return self.a*self.b
	#this is the division method
	def division(self):
		return self.a/self.b
	def __repr__(self):
		return "calculator('{}','{}')".format(self.a,self.b)
	def __str__(self):
		pass


num1=Calculator(1,2)
print (num1)