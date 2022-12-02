#Advent of Code 2022 Day One
with open("input.txt", 'r') as f:
	myinput = f.readlines()

current = 0
highest = 0
highesttwo = 0
highestthree = 0
for line in myinput:
	# print(line)
	if line[0] == '\n':
		if current > highest:
			highestthree = highesttwo
			highesttwo = highest
			highest = current
		elif current > highesttwo:
			highestthree = highesttwo
			highesttwo = current
		elif current >highestthree:
			highestthree = current
		current = 0
	else:
		current = current + int(line, 10)
print(highest + highestthree + highesttwo)