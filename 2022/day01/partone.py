#Advent of Code 2022 Day One
with open("input.txt", 'r') as f:
	myinput = f.readlines()
current = 0
highest = 0
for line in myinput:
	if line[0] == '\n':
		if current > highest:
			highest = current
		current = 0
	else:
		current = current + int(line)
print(highest)