Lines = []
with open("input.txt") as f:
    for line in f:
        Lines.append(list(map(int, line.strip())))
temp = [[0] * len(line) * 5 for x in range(len(line) * 5)]
x = 0
while x in range(len(Lines)):
    y = 0
    while y in range(len(Lines[0])):
        temp[x][y] = Lines[x][y]
        y += 1
    x += 1
x = 100
while x in range(len(temp)):
    y = 0
    while y in range(len(Lines[0])):
        temp[x][y] = temp[x - 100][y] % 9 + 1
        y += 1
    x += 1
x = 0
while x in range(len(temp)):
    y = 100
    while y in range(len(temp[0])):
        temp[x][y] = temp[x][y-100] % 9 + 1
        y += 1
    x += 1
for line in temp:
    print(line)
string_ints = [str(inte) for inte in temp]
str_of_ints ="\n".join(string_ints)
str_of_ints = str_of_ints.replace(",","")
str_of_ints = str_of_ints.replace(" ","")
str_of_ints = str_of_ints.replace("[","")
str_of_ints = str_of_ints.replace("]","")
with open("bigmap.txt", "w") as f:
    f.writelines(str_of_ints)
print(len(temp[0]))
