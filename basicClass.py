#this is a pythonic way to all the programs of sem 3 oopm
class student:

	def __init__(self,name,surname,roll):
		self.name=name
		self.surname = surname
		self.roll=roll
		self.mail = name + "." + surname +"@djsce.in"
	def printDetails(self):
		print(self.name)
		print(self.surname)
		print(self.roll)
		print(self.mail)
		
s1 = student("shaunak","galvankar",11)
s2 = student("jatin","dalvi",4)
s3 = student("chirag","gada",10)

print (s1.printDetails())
print (s2.printDetails())
print (s3.printDetails())


