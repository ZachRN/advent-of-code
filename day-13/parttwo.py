def fold_up(board, fold):
	subtraction = 1
	hold = fold
	while fold in range(len(board)):
		for x in range(len(board[fold])):
			if (hold - subtraction > -1) and (hold + subtraction < len(board)):
				if str(board[hold + subtraction][x]) == "#":
					board[hold - subtraction][x] = board[hold + subtraction][x]
				board[hold + subtraction][x] = "."
		subtraction += 1
		fold += 1
	fold -= 1
	while fold >= hold:
		board.pop(fold)
		fold -= 1
def fold_left(board, fold):
	hold = fold
	for y in range(len(board)):
		fold = hold
		subtraction = 1
		while fold in range(len(board[y])):
			if (hold - subtraction > -1) and (hold + subtraction < len(board[y])):
				if str(board[y][hold + subtraction]) == "#":
					board[y][hold - subtraction] = board[y][hold + subtraction]
				board[y][hold + subtraction] = "#"
			subtraction += 1
			fold += 1
	temp = fold - 1
	for y in range(len(board)):
		fold = temp
		while fold >= hold:
			board[y].pop(fold)
			fold -= 1

def print_board(board):
	for line in board:
		for character in line:
			print(character, end ="")
		print()

cords = []
folds = []
with open("input.txt") as f:
	for line in f:
		if line[0].isnumeric():
			cords.append(line.strip().split(','))
		elif line[0] == "f":
			folds.append(line.strip().replace("=", " ").split(" "))
max_x = 0
max_y = 0
for in_set in cords:
	if int(in_set[0]) > max_x:
		max_x = int(in_set[0])
	elif int(in_set[1]) > max_y:
		max_y = int(in_set[1])
board = [["." for x in range(max_x + 1)] for y in range(max_y + 1)]
for in_set in cords:
	board[int(in_set[1])][int(in_set[0])] = '#'
for fold in folds:
	if str(fold[2]) == "y":
		fold_up(board, int(fold[3]))
	elif str(fold[2]) == "x":
		fold_left(board, int(fold[3]))
	break
count = 0
for line in board:
	count += line.count("#")
print(count)