#this program is a ceaser cipher

print("This is the ceaser cipher.\nDo You want to encode a message or decode a message")
print("To encode your message press e to decode a messge press d")
mode=raw_input()
if mode=="e":
#this is the ceaser cipher encoder
	original=raw_input("Enter the message you want to encode:")
	encrypted=""
	print("enter a number between 0 & 26 including 0 & 26 which will be the encryption key")
	key=input()
	i=0
	while i<len(original):
		#to handle the wraping around
		if ord(original[i])>len(original):
			Ascii=ord(original[i])+key-len(original)
		elif ord(original[i])<0:
			Ascii=ord(original[i])+key+len(original)
		else:
			Ascii=ord(original[i])+key
		encrypted = encrypted + chr(Ascii)
		i=i+1
	print(encrypted)
elif mode=='d':
#this is the ceaser cipher decoder
	encrypted=raw_input("Enter the message that you want to decode:")
	decrypted=""
	print("Enter the key according to which you want to decode your text")
	key=input()
	i=0
	while i<len(encrypted):
		#to handle the wraping around
		if ord(encrypted[i])>len(encrypted):
			Ascii=ord(encrypted[i])-key-len(encrypted)
		elif ord(encrypted[i])<0:
			Ascii=ord(encrypted[i])-key+len(encrypted)
		else:
			Ascii=ord(encrypted[i])-key
		encrypted = encrypted + chr(Ascii)
		i=i+1
	print(decrypted)