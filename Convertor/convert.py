from tabulate import tabulate


userInputNumber = input('Input number: ')
userInputFormatInput = int(
    input('What is inputted number?(binary - 1; decimal - 2; hexadecimal - 3) '))
userInputFormatOutput = int(input(
    'What is the outputted number?(binary - 1; decimal - 2; hexadecimal - 3) '))


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
			return False
		return True
	elif choice == 2:
		try:
			int(number, 10)
		except ValueError:
			print("Inputted number isn't decimal! (or just don't use decimal point pls)")
			return False
		except:
			print("Something went wrong")
		return True
	elif choice == 3:
		try:
			int(number, 16)
		except ValueError:
			print("Inputted number isn't hexadecimal!")
			return False
		except:
			print("Something went wrong")
		return True
	else:
		print('Error in format, please check it if you have inputted it right.')
		return False


def binaryToDecimal(num):
	listt = [int(i) for i in str(num)]
	listt.reverse()
	finalNumber = 0
	finalString = ""
	finalString2 = ""
	for i in range(len(listt)):
		finalNumber += listt[i]*(2**i)
		finalString += str(listt[i])+"*"+str(2**i)+" + "
		finalString2 += str(listt[i]*(2**i)) + " + "

	print("\n\nResult:")
	print(finalNumber)
	print("\nMethod:")
	print("1)  "+finalString[:-2] + "	- We'll be multiplying the numbers now.")
	print("2)  "+finalString2[:-2] + "			- Now, just the addition left.")
	print("3)  "+str(finalNumber))


def decimalToBinary(num):
	changingNum = int(num)
	endList = []
	endList2 = [['Division by 2', 'Quotient', 'Reminder']]
	while changingNum != 0:
		reminder = changingNum % 2
		changingNum = int((changingNum-reminder)/2)
		endList.insert(0, str(reminder))
		tempList = [str((changingNum-reminder)*2)+"/2", changingNum, reminder]
		endList2.append(tempList)
	
	print("\n\nResult:")
	print("".join(endList))
	print("\nMethod:")
	print(tabulate(endList2, headers='firstrow', tablefmt='fancy_grid'))
	


def Solve(number, choice, output):
	if choice == 1:
		if output == 2:
			binaryToDecimal(number)
		elif output == 3:
			print("d")
	elif choice == 2:
		if output == 1:
			decimalToBinary(number)
		elif output == 3:
			print("d")
	elif choice == 3:
		int(number, 16)
	
if userInputFormatInput == userInputFormatOutput:
	print('Input format cannot be the same as output')
else:
	if checkIfPossible(userInputNumber, userInputFormatInput) == True:
		Solve(userInputNumber, userInputFormatInput, userInputFormatOutput)
