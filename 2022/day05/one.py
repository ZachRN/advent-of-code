def findDefault(myList):
	for i in range(8):
		if (myinput[i][1] != ' '):
			myList[0].append(myinput[i][1])
		if (myinput[i][5] != ' '):
			myList[1].append(myinput[i][5])
		if (myinput[i][9] != ' '):
			myList[2].append(myinput[i][9])
		if (myinput[i][13] != ' '):
			myList[3].append(myinput[i][13])
		if (myinput[i][17] != ' '):
			myList[4].append(myinput[i][17])
		if (myinput[i][21] != ' '):
			myList[5].append(myinput[i][21])
		if (myinput[i][25] != ' '):
			myList[6].append(myinput[i][25])
		if (myinput[i][29] != ' '):
			myList[7].append(myinput[i][29])
		if (myinput[i][33] != ' '):
			myList[8].append(myinput[i][33])
	return (myList)

with open("input.txt", 'r') as f:
	myinput = f.readlines()
# 1 = 1; 2 = 5; 3 = 9; 4 = 13; 5 = 17; 6 = 21; 7 = 25; 8 = 29; 9 = 33;
myList = []
for i in range(9):
	myList.append([])
myList = findDefault(myList)
for i in range(10, len(myinput)):
	answers = myinput[i].strip().split()
	move = int(answers[1])
	move_from = int(answers[3]) - 1
	move_to = int(answers[5]) - 1
	for j in range(move):
		element = myList[move_from][0]
		myList[move_from].pop(0)
		myList[move_to].insert(0,element)
for i in range(len(myList)):
	print(myList[i][0], end="")