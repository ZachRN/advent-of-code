def check_surrond(f, x, y, map_cords):
    if f[x][y] == "\n":
        return (0)
    try:
        if (int(f[x][y]) > int(f[x][y-1])):
            return (0)
    except:
        pass
    try:
        if (int(f[x][y]) > int(f[x][y+1])):
            return (0)
    except:
        pass
    try:
        if (int(f[x][y]) > int(f[x-1][y])):
            return (0)
    except:
        pass
    try:
        if(int(f[x][y]) > int(f[x+1][y])):
            return(0)
    except:
        pass
    
    try:
        if (int(f[x][y]) < int(f[x][y-1])):
            map_cords.append(x)
            map_cords.append(y)
            return (0)
    except:
        pass
    try:
        if (int(f[x][y]) < int(f[x][y+1])):
            map_cords.append(x)
            map_cords.append(y)
            return (0)
    except:
        pass
    try:
        if (int(f[x][y]) < int(f[x-1][y])):
            map_cords.append(x)
            map_cords.append(y)
            return (0)
    except:
        pass
    try:
        if(int(f[x][y]) < int(f[x+1][y])):
            map_cords.append(x)
            map_cords.append(y)
            return (0)
    except:
        pass
    return (0)
def fill_thy_map(map_cords, lines):
    fill_map = [[0 for x in range(102)] for y in range(102)]
    x = 0
    while x < len(fill_map[0]):
        fill_map[0][x] = 9
        x += 1
    y = 0
    while y < len(fill_map):
        fill_map[y][0] = 9
        fill_map[y][len(fill_map[y])-1] = 9
        y += 1
    y -= 1
    x = 0
    while x < len(fill_map[y]):
        fill_map[y][x] = 9
        x += 1
    navigator = 0
    while navigator < len(map_cords) - 1:
        fill_map[map_cords[navigator] + 1][map_cords[navigator + 1] + 1] = 1
        navigator += 2
    y = 0
    for line in lines:
        x = 0
        for test in line:
            if test == '\n':
                break
            if int(test) == 9:
                fill_map[y + 1][x + 1] = 9
            x += 1
        y += 1
    return (fill_map)
def flood_find(fill_map, y, x):
    total_fill = []
    total_fill.append(y)
    total_fill.append(x)
    filled = 1
    while filled > 0:
        filled = 0
        navigator = 0
        while navigator < len(total_fill) - 1:
            if fill_map[total_fill[navigator] + 1][total_fill[navigator + 1]] not in (9, 1):
                fill_map[total_fill[navigator] + 1][total_fill[navigator+1]] = 1
                total_fill.append(total_fill[navigator] + 1)
                total_fill.append(total_fill[navigator+1])
                filled += 1
            if fill_map[total_fill[navigator] - 1][total_fill[navigator + 1]] not in (9, 1):
                fill_map[total_fill[navigator] - 1][total_fill[navigator+1]] = 1
                total_fill.append(total_fill[navigator] - 1)
                total_fill.append(total_fill[navigator+1])
                filled += 1
            if fill_map[total_fill[navigator]][total_fill[navigator + 1] + 1] not in (9, 1):
                fill_map[total_fill[navigator]][total_fill[navigator+1] + 1] = 1
                total_fill.append(total_fill[navigator])
                total_fill.append(total_fill[navigator+1] + 1)
                filled += 1
            if fill_map[total_fill[navigator]][total_fill[navigator+ 1] - 1] not in (9, 1):
                fill_map[total_fill[navigator]][total_fill[navigator + 1] - 1] = 1
                total_fill.append(total_fill[navigator])
                total_fill.append(total_fill[navigator+1] - 1)
                filled += 1
            navigator += 2
    return (len(total_fill) / 2), fill_map
def find_largest(answers):
    a = 0
    b = 0
    c = 0
    for elements in answers:
        if elements > a:
            c = b
            b = a
            a = elements
        elif elements > b:
            c = b
            b = elements
        elif elements > c:
            c = elements
    print (a,b,c)
    return (a,b,c)

def count_flood(fill_map, map_cords):
    answers = []
    navigator = 0
    while navigator < len(map_cords) - 1:
        to_append, fill_map = flood_find(fill_map,map_cords[navigator],map_cords[navigator+1])
        answers.append(to_append)
        navigator += 2
    for line in fill_map:
        print (line)
    print(answers)
    a,b,c = find_largest(answers)
    return (a * b * c)
        
with open("input.txt", "r") as f:
    lines = f.readlines()
x = 0
y = 0
counter = 0
map_cords = []
basinx = 0
basiny = 0
while y in range(len(lines)):
    x = 0
    while x in range(len(lines[y])):
        check_surrond(lines, y, x, map_cords)
        x += 1
    y += 1
fill_map = fill_thy_map(map_cords, lines)
answer = count_flood(fill_map, map_cords)
print(answer)
#print(map_cords)
#print(counter)


