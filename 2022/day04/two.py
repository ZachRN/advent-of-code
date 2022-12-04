#Advent of Code 2022 Day Four Part one
with open("input.txt", 'r') as f:
	myinput = f.readlines()
output = 0
for line in myinput:
	elves = line.strip().split(",")
	elfrange1 = elves[0].split("-")
	elfrange2 = elves[1].split("-")

	onemin = int(elfrange1[0])
	onemax = int(elfrange1[1])
	twomin = int(elfrange2[0])
	twomax = int(elfrange2[1])

	if (twomin in range(onemin, onemax+1) or twomax in range(onemin, onemax+1)):
		output += 1
		continue
	if (onemin in range(twomin,twomax+1) or onemax in range(twomin, twomax+1)):
		output += 1
		continue
print(output)
