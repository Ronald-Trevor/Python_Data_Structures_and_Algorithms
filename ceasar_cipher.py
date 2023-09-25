plain_text = input("Enter text to encrypt:")
shift_key = int(input("Enter shift value:"))

def encrypt(plain_text, shift_key):
	result = ""

	for i in range(len(plain_text)):
		ch = plain_text[i]
		#Encrypt uppercase
		if ch.isupper():
			result += chr(( ord(ch) + shift_key - 65) % 26 + 65)
		#Encrypt lowercase
		else:
			result += chr( (ord(ch) + shift_key - 97) % 26 + 97)

	return result

print(encrypt(plain_text, shift_key))
cipher_text = input("Enter cipher text to decrypt:")
shift_key = int(input("Enter shift key:"))

def decrypt(cipher_text, shift_key):
	plain_text = ""

	for i in range(len(cipher_text)):
		ch = cipher_text[i]
		if ch.isalpha():
			if ch.isupper():
				plain_text += chr((ord(ch)-shift_key-65)%26+65)
			else:
				plain_text += chr((ord(ch)-shift_key-97)%26+97)

	return plain_text

print(decrypt(cipher_text,shift_key))
