def display_board(arr):
    for line in arr:
        print(line)
    print()

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
            if arr[x][y] != -1:
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
    return (0)

def play_bingo(arr, CallOrder):
    x = 0
    for Call in CallOrder:
        x = 0
        for board in arr:
            y = 0
            for line in board:
                z = 0
                for number in line:
                    if int(number) == int(Call):
                        arr[x][y][z] = -1
                        if (checkboard(arr[x]) == 1):
                            return (x, Call)
                    z += 1
                y += 1
            x += 1
    return (-1)
                        


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
#print(arr[0][0][2])
x, Call = play_bingo(arr, CallOrder)
if x >= 0:
    display_board(arr[x])
    print(Call)
    totalSum = SumBoard(arr[x])
    print(totalSum)
    print(int(Call) * int(totalSum))