def fillEdge(newList, myinput):
	for x in range(len(newList[0])):
		newList[0][x] = 1
		newList[-1][x] = 1
	for x in range(len(newList)):
		newList[x][0] = 1
		newList[x][-1] = 1
	return (newList)
def checkNorth(newList, myinput):
	for col in range(1, len(myinput[0]) - 1):
		newestMax = int(myinput[0][col])
		for row in range(1, len(myinput) - 1):
			if (int(myinput[row][col]) > newestMax):
				newList[row][col] = 1
				newestMax = int(myinput[row][col])
	return (newList)
def checkSouth(newList, myinput):
	for col in range(1, len(myinput[0]) - 1):
		newestMax = int(myinput[len(myinput) - 1][col])
		row = len(myinput) - 1
		while row > 0:
			if (int(myinput[row][col]) > newestMax):
				# print(row, col)
				newList[row][col] = 1
				newestMax = int(myinput[row][col])
				# print(newestMax)
			row -=1
	return (newList)
def checkEast(newList, myinput):
	for row in range(1, len(myinput[0]) - 1):
		newestMax = int(myinput[row][0])
		for col in range(1, len(myinput) - 1):
			if (int(myinput[row][col]) > newestMax):
				newList[row][col] = 1
				newestMax = int(myinput[row][col])
	return (newList)
def checkWest(newList, myinput):
	for row in range(1, len(myinput[0]) - 1):
		col = len(myinput[row]) - 2
		newestMax = int(myinput[row][col])
		while col > 0:
			if (int(myinput[row][col]) > newestMax):
				newList[row][col] = 1
				newestMax = int(myinput[row][col])
			col -= 1
	return (newList)
				
def run():
	with open("input.txt", 'r') as f:
		myinput = f.readlines()
	newList = []
	for i in range(len(myinput)):
		newList.append([])
		for x in range(len(myinput[0])-1):
			newList[i].append(0)
	newList = fillEdge(newList, myinput)
	newList = checkNorth(newList, myinput)
	newList = checkSouth(newList, myinput)
	newList = checkEast(newList, myinput)
	newList = checkWest(newList, myinput)
	output = 0
	for i in range(len(newList)):
		for x in range(len(newList[i])):
			if newList[i][x] == 1:
				output += 1
		print(newList[i])
	return (output)
print(run())