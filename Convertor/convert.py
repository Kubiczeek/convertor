from tabulate import tabulate
import os
clear = lambda: os.system('cls')
clear()

userInputNumber = input('Input number: ')
userInputFormatInput = int(
    input('What is inputted number?(binary - 1; decimal - 2; hexadecimal - 3) '))
userInputFormatOutput = int(input(
    'What is the outputted number?(binary - 1; decimal - 2; hexadecimal - 3; all - 5) '))

cheatSheet = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
cheatSheet2 = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

def getKey(value, dictionary):
    for k, v in dictionary.items():
        if value == v:
            return k
 
    return "No key??!?!?!?!!??!?!?!!?"

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
	return finalNumber

def binaryToHex(num):
	inputList = [int(i) for i in str(num)]
	while len(inputList) % 4 != 0:
		inputList.insert(0, 0)
	spacedList = []
	spacedString = ""
	spacedString2 = ""
	finalString = ""
	for i in range(0, len(inputList), 4):
		spacedList.append(inputList[i:i+4])
	for i in range(len(spacedList)):
		tempSum = 0
		for j in range(len(spacedList[i])):
			tempInt = int(spacedList[i][j])*(2**(4-j-1))
			tempSum += tempInt
			if j == 3:
				finalString += cheatSheet[tempSum]
	for i in range(len(spacedList)):
		tempSum = 0
		for j in range(len(spacedList[i])):
			tempInt = int(spacedList[i][j])*(2**(4-j-1))
			tempSum += tempInt
			spacedString += "".join(str(spacedList[i][j]))
			if j == 3:
				spacedString += "  "
				spacedString2 += cheatSheet[tempSum]
				spacedString2 += "	"
	
	print("\n\nResult:")
	print(finalString)
	print("\nMethod:")
	print("1)   " + spacedString)
	print("2)   " + spacedString2)
	return finalString


def decimalToBinary(num):
	changingNum = int(num)
	endList = []
	endList2 = [['Division by 2', 'Result', 'Reminder']]
	while changingNum != 0:
		reminder = int(changingNum % 2)
		endList.insert(0, str(reminder))
		tempList = [str(changingNum)+"/2", str((changingNum-reminder)/2), reminder]
		changingNum = int((changingNum-reminder)/2)
		endList2.append(tempList)
	
	print("\n\nResult:")
	print("".join(endList))
	print("\nMethod:")
	print(tabulate(endList2, headers='firstrow', tablefmt='grid'))
	return "".join(endList)

def decimalToHex(num):
	changingNum = int(num)
	endList = []
	endList2 = [['Division by 16', 'Result', 'Reminder', 'That is']]
	while changingNum != 0:
		reminder = int(changingNum % 16)
		endList.insert(0, str(cheatSheet[reminder]))
		tempList = [str(changingNum)+"/16", str((changingNum-reminder)/16), reminder, cheatSheet[reminder]]
		changingNum = int((changingNum-reminder)/16)
		endList2.append(tempList)
	
	print("\n\nResult:")
	print("".join(endList))
	print("\nMethod:")
	print(tabulate(endList2, headers='firstrow', tablefmt='grid'))
	return "".join(endList)


def hexToBinary(num):
	inputList = [*num]
	endList = []
	spacedString = ""
	spacedString2 = ""
	for i in range(len(inputList)):
		endList.append(cheatSheet2[inputList[i]])
		spacedString += inputList[i]
		spacedString2 += cheatSheet2[inputList[i]] + " "

	print("\n\nResult:")
	print("".join(endList))
	print("\nMethod:")
	print("1)	" + spacedString)
	print("2)	" + spacedString2)
	print("3)	" + "".join(endList))
	return "".join(endList)

def hexToDecimal(num):
	inputList = [*num]
	betterList = []
	for i in range(len(inputList)):
		betterList.insert(0,int(getKey(inputList[i], cheatSheet)))
	finalNumber = 0
	finalString = ""
	finalString2 = ""
	for i in range(len(betterList)):
		finalNumber += betterList[i]*(16**i)
		finalString += str(betterList[i])+"*"+str(16**i)+" + "
		finalString2 += str(betterList[i]*(16**i)) + " + "

	print("\n\nResult:")
	print(finalNumber)
	print("\nMethod:")
	print("1)  "+finalString[:-2])
	print("2)  "+finalString2[:-2])
	print("3)  "+str(finalNumber))
	return finalNumber
	

def outputAll(num1, num2, num3):
	clear()
	print("\nAnswer:\n")
	print("Bin: "+ num1)
	print("Dec: "+ num2)
	print("Hex: "+ num3)
	print("Ascci: "+ chr(int(num2)))


def Solve(number, choice, output):
	if choice == 1:
		if output == 2:
			binaryToDecimal(number)
		elif output == 3:
			binaryToHex(number)
		elif output == 5:
			outputAll(number, str(binaryToDecimal(number)), str(binaryToHex(number)))
	elif choice == 2:
		if output == 1:
			decimalToBinary(number)
		elif output == 3:
			decimalToHex(number)
		elif output == 5:
			outputAll(str(decimalToBinary(number)), number, str(decimalToHex(number)))
	elif choice == 3:
		if output == 1:
			hexToBinary(number)
		elif output == 2:
			hexToDecimal(number)
		elif output == 5:
			outputAll(str(hexToBinary(number)), str(hexToDecimal(number)), str(number))
	
if userInputFormatInput == userInputFormatOutput:
	print('Input format cannot be the same as output')
else:
	if checkIfPossible(userInputNumber, userInputFormatInput) == True:
		Solve(userInputNumber, userInputFormatInput, userInputFormatOutput)
