def checkNorth(myinput, row, col):
	treeSize = int(myinput[row][col])
	totalTrees = 0
	row -= 1
	while (row >= 0):
		totalTrees += 1
		if int(myinput[row][col]) >= treeSize:
			break
		row -= 1
	return (totalTrees)
def checkSouth(myinput, row, col):
	treeSize = int(myinput[row][col])
	totalTrees = 0
	row += 1
	while (row < len(myinput)):
		totalTrees += 1
		if int(myinput[row][col]) >= treeSize:
			break
		row += 1
	return (totalTrees)
def checkEast(myinput, row, col):
	treeSize = int(myinput[row][col])
	totalTrees = 0
	col -= 1
	while (col >= 0):
		totalTrees += 1
		if int(myinput[row][col]) >= treeSize:
			break
		col -= 1
	return (totalTrees)
def checkWest(myinput, row, col):
	treeSize = int(myinput[row][col])
	totalTrees = 0
	col += 1
	while (col < (len(myinput[0]) - 1)):
		totalTrees += 1
		if int(myinput[row][col]) >= treeSize:
			break
		col += 1
	return (totalTrees)
def run():
	with open("input.txt", 'r') as f:
		myinput = f.readlines()
	highestTreeScore = 0
	for row in range(len(myinput)):
		curTreeScore = 0
		for col in range(len(myinput[0]) - 1):
			north = checkNorth(myinput, row, col)
			south = checkSouth(myinput, row, col)
			east = checkEast(myinput, row, col)
			west = checkWest(myinput, row, col)
			curTreeScore = north * south * east * west
			if curTreeScore > highestTreeScore:
				print(row, col , north, south ,east, west, myinput[row][col])
				highestTreeScore = curTreeScore
	return (highestTreeScore)
print(run())