#advent of code day 5 part one
def display_array(numbers):
    for line in numbers:
        print(line)
def fill_line(x1, y1, x2, y2, board):
    if x1 != x2:
        if (x1 <= x2):
            while (x1 <= x2):
                board[x1][y1] = int(board[x1][y1]) + 1
                x1 += 1
        else:
            while (x2 <= x1):
                board[x2][y2] = int(board[x2][y2]) + 1
                x2 += 1
    else:
        if (y1 <= y2):
            while (y1 <= y2):
                board[x1][y1] = int(board[x1][y1]) + 1
                y1 += 1
        else:
            while (y2 <= y1):
                board[x2][y2] = int(board[x2][y2]) + 1
                y2 += 1
    return (board)
def count_board(board):
    count = 0
    for row in board:
        for number in row:
            if (int(number) > 1):
                count += 1
    return (count)

with open("input.txt", "r") as f:
    Lines = f.readlines()
numbers = []
for line in Lines:
    numbers.append(line.replace(",", " ").split())
board = [[0 for x in range(1000)] for y in range(1000)]
for row in numbers:
    if (row[0] == row[3] or row[1] == row[4]):
        board = fill_line(int(row[0]), int(row[1]), int(row[3]), int(row[4]), board)
points = count_board(board)
#display_array(board)
print(points)
