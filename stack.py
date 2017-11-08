class stack:
	def __init__(self):
		self.store = []
		
			
	#this method adds the entered arguement tot the top of the stack	
	def push(self,value):
		self.store .append (value)
	#this method removes a value stored fromm the top of the stack
	def pop(self):
		self.store =self.store[:-1]
	#this method tells us what is the value at the top of the stack 
	def peek (self):
		if self.store:
			return self.store[-1]
		else:
			return None
	#this method returns true if the stack is empty
	def isEmpty(self):
		return len(self)==0
	#this method reverses a stack by putting popping then pushing its elements onto another stack
	def revStack(self):
		pass

print ("enter the values as arguements to be added to the stack")
