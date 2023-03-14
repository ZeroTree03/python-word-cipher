import random

#Шифрует строку
def Crypt(WORD):
	RESULT = []
	for i in range(len(WORD)):
		RESULT.append(WORD[i]+"p"+WORD[i])
		a = ""
		for j in range(random.randint(1,2)):
			a += random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","r","s","t","u","v","w","x","y","z"])
		RESULT.append(a)
	return RESULT

#Разшифровует строку
def DeCrypt(WORD):
	CRYPTED_LETTERS = list(WORD)
	RESULT = []
	for i in range(len(CRYPTED_LETTERS)):
		J = CRYPTED_LETTERS[i]
		if J == "p":
			if CRYPTED_LETTERS[i-1] == CRYPTED_LETTERS[i+1]:
				RESULT.append(CRYPTED_LETTERS[i+1])
	return RESULT

#Делает из списка строку
def Str(WORD_SPLIT):
	RESULT_STR = ""
	for i in range(len(WORD_SPLIT)):
		RESULT_STR+=WORD_SPLIT[i]
	return RESULT_STR

#Главный цыкл программы
while True:
	USER_CHOISE = input("Do you wand to crypt (y/n): ")
	if USER_CHOISE == "y":
		WORD_TO_CRYPT = input("Type word to crypt: ")
		print(Str(Crypt(WORD_TO_CRYPT)))
	if USER_CHOISE == "n":
		USER_CHOISE = input("Do you wand to decrypt (y/n): ")

		if USER_CHOISE == "y":
			USER_WORD = input("Enter crypted word: ")
			print(Str(DeCrypt(USER_WORD)))
		if USER_CHOISE == "n":
			pass
