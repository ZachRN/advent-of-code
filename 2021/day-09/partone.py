def check_surrond(f, x, y):
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
            return (int(f[x][y]) + 1)
    except:
        pass
    try:
        if (int(f[x][y]) < int(f[x][y+1])):
            return (int(f[x][y]) + 1)
    except:
        pass
    try:
        if (int(f[x][y]) < int(f[x-1][y])):
            return (int(f[x][y]) + 1)
    except:
        pass
    try:
        if(int(f[x][y]) < int(f[x+1][y])):
            return (int(f[x][y]) + 1)
    except:
        pass
    return (0)
    
with open("input.txt", "r") as f:
    lines = f.readlines()
x = 0
y = 0
counter = 0
while y in range(len(lines)):
    x = 0
    while x in range(len(lines[y])):
        counter += int(check_surrond(lines, y, x))
        x += 1
    y += 1
print(counter)


