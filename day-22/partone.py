with open("input.txt") as f:
    Lines = f.readlines()
grid = [[[0 for x in range(100)] for y in range(100)] for z in range(100)]
for line in Lines:
    ToDo = line.strip().replace(" ",",").split(",")
    x = ToDo[1].split(".")
    y = ToDo[2].split(".")
    z = ToDo[3].split(".")
    x_min = int(x[0][2:]) + 50
    y_min = int(y[0][2:]) + 50
    z_min = int(z[0][2:]) + 50
    x_max = int(x[2]) + 50
    y_max = int(y[2]) + 50
    z_max = int(z[2]) + 50
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            for z in range(z_min, z_max+1):
                if ToDo[0] == "on":
                    grid[x][y][z] = 1
                else:
                    grid[x][y][z] = 0
counter = 0
for x in range(100):
    for y in range(100):
        for z in range(100):
            if grid[x][y][z] == 1:
                counter += 1
print(counter)