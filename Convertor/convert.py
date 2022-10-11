userInputNumber = input('Input number: ')
userInputFormatInput = int(input('What is inputted number?(binary - 1; decimal - 2; hexadecimal - 3) '))
userInputFormatOutput = int(input('What is the outputted number?(binary - 1; decimal - 2; hexadecimal - 3) '))
def checkIfPossible(number, choice):
	if choice == 1:
		try:
			int(number)
		except ValueError:
			print("Inputted number isn't number")
		except:
			print("Something went wrong") 
		possible = '10'
		found = False
		for n in number:
			if n not in possible:
				found = True
				break
			else:
				continue
		if found == True:
			print("Inputted number isn't binary!")
	elif choice == 2:
		try:
			int(number, 10)
		except ValueError:
			print("Inputted number isn't decimal! (or just don't use decimal point pls)")
		except:
			print("Something went wrong") 
	elif choice == 3:
		try:
			int(number, 16)
		except ValueError:
			print("Inputted number isn't hexadecimal!")
		except:
			print("Something went wrong")
	else:
		return print('Error in format, please check it if you have inputted it right.')

def binaryToDecimal(num):
	listt = [int(i) for i in str(num)]
	listt.reverse()
	finalNumber = 0
	finalString = ""
	for i in range(len(listt)):
		finalNumber += listt[i]*(2**i)
		finalString += str(listt[i]) + str("*2") + "^" + str(i) + "+"

	print("\n\nResult:")
	print(finalNumber)
	print("\nMethod:")
	print(finalString[:-1])


def Solve(number, choice, output):
	if choice == 1:
		if output == 2:
			binaryToDecimal(number)
		elif output == 3:
			print("xd")
	elif choice == 2:
		int(number, 10)
	elif choice == 3:
		int(number, 16)
	

if userInputFormatInput == userInputFormatOutput:
	print('Input format cannot be the same as output')
else:
	checkIfPossible(userInputNumber, userInputFormatInput)
	Solve(userInputNumber, userInputFormatInput, userInputFormatOutput)


