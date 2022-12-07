def add_dir(dirDict, folder):
	if folder not in dirDict:
		dirDict.update({folder: 0})
	return (dirDict)

def run():
	with open("input.txt", 'r') as f:
		myinput = f.readlines()
	dirDict = {}
	dirList = []
	level = 0
	for line in myinput:
		parse = line.strip("\n").split(" ")
		if parse[1] == "cd":
			if parse[2] == "..":
				dirList.pop()
				level -= 1
				continue
			level += 1
			if (parse[2] == "/"):
				dirList.append("/")
				dirDict = add_dir(dirDict, "/")
				continue
			dirList.append(dirList[-1] + parse[2])
			dirDict = add_dir(dirDict, dirList[-1])
		elif parse[0].isnumeric():
			for value in dirList:
				# print(value, parse[0])
				dirDict[value] += int(parse[0], base=10)
	output = 0
	for item in dirDict:
		if dirDict[item] < 100000:
			output = output + dirDict[item]
	return (output)

print(run())