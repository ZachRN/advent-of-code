shortest_path = 0
def path_find(board, cords):
    global shortest_path
    x = 0
    y = 0
    if cords[len(cords)-1][0] > 0 or cords[len(cords)-1][1] > 0:
        y = cords[len(cords)-1][0]
        x = cords[len(cords)-1][1]
    temp = 0
    for cord in cords:
        if cord[0] == y and cord[1] == x:
            temp += 1
        if temp == 2:
            return
    if x == 9 and y == 9:
        count = 0
        for cord in cords:
            count += int(cord[2])
        if shortest_path == 0:
            shortest_path = count
        elif count < shortest_path:
            print(count)
            shortest_path = count
        return 
    if y > 0:
        cords.append([(y - 1), (x), board[y - 1][x]])
        path_find(board, cords)
        cords.pop()
    if x > 0:
        cords.append([(y), (x - 1), board[y][x - 1]])
        path_find(board, cords)
        cords.pop()
    if y < 9:
        cords.append([(y + 1), (x), board[y + 1][x]])
        path_find(board, cords)
        cords.pop()
    if x < 9:
        cords.append([(y), (x + 1), board[y][x + 1]])
        path_find(board, cords)
        cords.pop()
Lines = []
with open("test.txt") as f:
    for line in f:
        Lines.append(line.strip())
cords = []
cords.append([0,0,1])
path_find(Lines, cords)
print(shortest_path)