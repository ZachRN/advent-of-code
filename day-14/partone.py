with open("test.txt") as f:
    Lines = f.readlines()
poly = Lines[0].strip()
commands = []
x = 2
while x in range(len(Lines)):
    commands.append(Lines[x].strip().split(" -> "))
    x += 1
for i in range(1):
    x = 0
    while x in range(len(poly) - 1):
        for command in commands:
            if str(poly[x]) + str(poly[x + 1]) == str(command[0]):
                x += 1
                poly = poly[:x] + command[1] + poly[x:]
                break
        x += 1
all_letters = {}
for i in poly:
    if i in all_letters:
        all_letters[i] += 1
    else:
        all_letters[i] = 1
small = all_letters["N"]
big = all_letters["N"]
print(all_letters)
for i in all_letters:
    if int(all_letters[i])< int(small):
        small = all_letters[i]
    elif int(all_letters[i]) > int(big):
        big = all_letters[i]
#print(big - small)
#print(all_letters)
print(poly)