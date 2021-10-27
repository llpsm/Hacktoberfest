import random

chars = "abcdefghijklmnopqrstuvwxyzQWERTYUIOPLKJHGFDSAZXCVBNM1234567890"

password_len = int(input("what length would you like your password to be? "))
password_count = int(input("how many passwords would you like to generate? "))
for x in range(0,password_count):
	password = ""
	for x in range(0,password_len):
		password_char = random.choice(chars)
		password      = password + password_char
	print(password)
