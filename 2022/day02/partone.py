def checkWins(player1, player2):
	if player2 == "X":
		if player1 == "A": # ROCK 1
			return (1 + 3)
		if player1 == "B":
			return (1 + 0)
		if player1 == "C":
			return (1 + 6)
	if player2 == "Y": #PAPER 2
		if player1 == "A":
			return (2 + 6)
		if player1 == "B":
			return (2 + 3)
		if player1 == "C":
			return (2 + 0)
	if player2 == "Z": # SCISSORS 3
		if player1 == "A":
			return (3 + 0)
		if player1 == "B":
			return (3 + 6)
		if player1 == "C":
			return (3 + 3)
	return (0)

#Advent of Code 2022 Day Two Part One
with open("input.txt", 'r') as f:
	myinput = f.readlines()

score = 0
for line in myinput:
	answers = line.strip().split(" ")
	# print (answers)
	player1 = answers[0]
	player2 = answers[1]
	score = score + checkWins(player1, player2)
print(score)
