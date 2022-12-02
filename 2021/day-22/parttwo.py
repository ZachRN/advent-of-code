with open("input.txt") as f:
    Lines = f.readlines()
OnRange = []
for line in Lines:
    ToDo = line.strip().replace(" ",",").split(",")
    x = ToDo[1].split(".")
    y = ToDo[2].split(".")
    z = ToDo[3].split(".")
    x_min = int(x[0][2:])
    x_max = int(x[2]) + 1
    y_min = int(y[0][2:])
    y_max = int(y[2]) + 1
    z_min = int(z[0][2:])
    z_max = int(z[2]) + 1
    if ToDo[0] == "on":
        value = 1
    else:
        value = 0
    Temp = []
    for area in OnRange:
        #print(area)
        if (x_min < area[0][1] and x_max > area[0][0]) and (y_min < area[1][1] and y_max > area[1][0]) and (z_min < area[2][1] and z_max > area[2][0]):
            if area[0][0] < x_min:
                slicer = [[area[0][0],x_min],[area[1][0],area[1][1]],[area[2][0],area[2][1]], area[3]]
                area[0][0] = x_min
                Temp.append(slicer)
            if area[0][1] > x_max:
                slicer = [[x_max,area[0][1]],[area[1][0],area[1][1]],[area[2][0],area[2][1]], area[3]]
                area[0][1] = x_max
                Temp.append(slicer)
            if area[1][0] < y_min:
                slicer = [[area[0][0],area[0][1]],[area[1][0],y_min],[area[2][0],area[2][1]], area[3]]
                area[1][0] = y_min
                Temp.append(slicer)
            if area[1][1] > y_max:
                slicer = [[area[0][0],area[0][1]],[y_max,area[1][1]],[area[2][0],area[2][1]], area[3]]
                area[1][1] = y_max
                Temp.append(slicer)
            if area[2][0] < z_min:
                slicer = [[area[0][0],area[0][1]],[area[1][0],area[1][1]],[area[2][0],z_min], area[3]]
                area[2][0] = z_min
                Temp.append(slicer)
            if area[2][1] > z_max:
                slicer = [[area[0][0],area[0][1]],[area[1][0],area[1][1]],[z_max,area[2][1]], area[3]]
                area[2][1] = z_max
                Temp.append(slicer)
        else:
            Temp.append(area)
    Temp.append([[x_min, x_max], [y_min, y_max], [z_min, z_max], value])
    OnRange = Temp
Total = 0
for area in OnRange:
    if area[3] == 1:
        Total += (area[0][1] - area[0][0]) * (area[1][1] - area[1][0]) * (area[2][1] - area[2][0])
print(Total)
#print(OnRange)
#print("yo")
