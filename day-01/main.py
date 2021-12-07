#Part one Advent of Code 2021 Day One
with open("input.txt", 'r') as f:
	Lines = f.readlines()
increase = 0
total = 0
last = 0
for line in Lines:
	total = total + 1
	new = int(line, base=10)
	if new > last:
		increase = increase + 1
	last = new
print(increase - 1)
#Part Two Advent of Code 2021 Day One
SumIncrease = 0
SumOne = 0
SumTwo = 0
Spot = 4
while (Spot <= total):
	SumOne = int(Lines[Spot - 2],base=10) + int(Lines[Spot - 3],base=10) + int(Lines[Spot - 4],base=10)
	SumTwo = int(Lines[Spot - 1],base=10) + int(Lines[Spot - 2], base=10) + int(Lines[Spot - 3], base=10)
	if SumTwo > SumOne:
		SumIncrease = SumIncrease + 1
	Spot = Spot + 1
print(SumIncrease)
#Part Two Done Another Way
SumTwo = 0
for i in range(1997):
	if int(Lines[i]) < int(Lines[i + 3]):
		SumTwo += 1
print(SumTwo)
