def checkWins(player1, player2):
	if player2 == "X": # LOSE ROCK
		if player1 == "A": # ROCk 1
			return (3 + 0) # SCISSORS
		if player1 == "B": # PAPER 2
			return (1 + 0) # ROCK
		if player1 == "C": # SCISSORS 3
			return (2 + 0) # PAPER
	if player2 == "Y": # DRAW PAPER
		if player1 == "A": # ROCk 1
			return (1 + 3) # ROCK
		if player1 == "B": # PAPER 2
			return (2 + 3) # PAPER
		if player1 == "C": # SCISSORS 3
			return (3 + 3) # SCISSORS
	if player2 == "Z": # WIN SCISSORS  HAD STUPID ISSUE, HAD Z SET TO Y ORIGINALLY
		if player1 == "A": # ROCk 1
			return (2 + 6) # PAPER
		if player1 == "B": # PAPER 2
			return (3 + 6) # SCISSORS
		if player1 == "C": # SCISSORS 3
			return (1 + 6) # ROCK
	return (0)

#Advent of Code 2022 Day Two Part Two
with open("input.txt", 'r') as f:
	myinput = f.readlines()

score = 0
for line in myinput:
	answers = line.strip().split(" ")
	player1 = answers[0]
	player2 = answers[1]
	score = score + checkWins(player1, player2)
print(score)
