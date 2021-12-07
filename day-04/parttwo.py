def display_board(arr):
    for line in arr:
        print(line)


def SumBoard(board):
    totalSum = 0
    for line in board:
        for number in line:
            if int(number) != -1:
                totalSum += int(number)
    return (totalSum)

def checkboard(board):
    x = 0
    y = 0
    while x < 5:
        y = 0
        while y < 5:
            if board[x][y] != -1:
                break
            y += 1
        if y == 5:
            return (1)
        x += 1
    x = 0
    y = 0
    while y < 5:
        x = 0
        while x < 5:
            if board[x][y] != -1:
                break
            x += 1
        if x == 5:
            return (1)
        y += 1
    return (-1)
def board_search(arr, Call, x, dead_board):
    if x == 100:
        return (dead_board)
    y = 0
    while y < 5:
        z = 0
        while z < 5:
            if int(arr[x][y][z]) == int(Call):
                 arr[x][y][z] = -1
                 if (checkboard(arr[x]) == 1):
                    dead_board.append(x)
                    return (dead_board)
            z += 1
        y += 1
    return (dead_board)

def play_bingo(arr, CallOrder):
    dead_board = []
    i = 0
    while i < len(CallOrder):
        x = 0
        while x < 100:
            while x in dead_board:
                x += 1
            dead_board = board_search(arr, CallOrder[i], x, dead_board)
            if len(dead_board) == 100:
                print(CallOrder[i])
                print(dead_board)
                return (x, CallOrder[i])
            x += 1
        i += 1
    return (0, 0)


with open("input.txt", "r") as f:
    Lines = f.readlines()
CallOrder = Lines[0].split(",")
arr = []
CountLines = 0
for line in Lines:
    CountLines += 1
Count = 2
ArrayTraverse = 0
while (Count < CountLines):
    arr.append([])
    y = 0
    while (y < 5):
        arr[ArrayTraverse].append(Lines[Count].split())
        y += 1
        Count += 1
    Count += 1
    ArrayTraverse += 1
x, Call = play_bingo(arr, CallOrder)
display_board(arr[x])
print(x)
print(Call)
totalSum = SumBoard(arr[x])
print(totalSum)
print(int(Call) * int(totalSum))