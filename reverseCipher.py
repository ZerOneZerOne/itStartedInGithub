#this is a program of the reverse cipher
print('Welcome,Do you want to encrypt or decrypt a reverse cipher')
answer=raw_input('To encrypt press e and to decrypt press d:')
#this block of code runs the encryption algorithm
if answer=='e':
	message = raw_input('Message to be encrypted: ')
	encrypted=""
	i=len(message)-1
	while i>=0:
		encrypted=encrypted+message[i]
		i=i-1
	print(encrypted)
#this block of code runs the decryption algoritm
else:
	message = raw_input('Message to be decrypted: ')
	decrypted=""
	i=len(message)-1
	while i>=0:
		decrypted=decrypted+message[i]
		i=i-1
	print(decrypted)



