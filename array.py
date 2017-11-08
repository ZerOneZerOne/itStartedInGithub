#this is a code space used for practising array programs learnt in data structures

#an empty array is created to store the further programs
#this is a function that asks for the numbr of elements of an array
#an it also asks one by one what are the elements
#nd finally adds them to the array
shaunak=[]
def arrBas():
	#to accept n numbers and enter them into an array
	print("enter the number of elements")
	n=input()
	for i in range (1,n+1):
		print("enter value for array element"+str(i))
		element=input()
		shaunak.append(element)
	
#this program finds the mean of the scanned array
arrBas()
Sum=sum(i for i in shaunak)
mean=float(Sum/n)
print(mean)