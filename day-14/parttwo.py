def initial_pairing(poly, commands, all_pairings):
    glue = ""
    x = 0
    while x in range(len(poly) - 1):
        glue = str(poly[x]) + str(poly[x + 1])
        if glue in commands:
            all_pairings[glue] += 1
        x += 1
        

with open("input.txt") as f:
    Lines = f.readlines()
poly = Lines[0].strip()
commands = {}
x = 2
while x in range(len(Lines)):
    temp = Lines[x].strip().split(" -> ")
    if temp[0] not in commands:
        commands[temp[0]] = temp[1]
    x += 1
#print(commands)
total_occurence = {}
for i in poly:
    if i in total_occurence:
        total_occurence[i] += 1
    else:
        total_occurence[i] = 1
all_pairings = {}
for i in commands:
    if str(i) not in all_pairings:
        all_pairings[str(i)] = 0
temp_pairings = all_pairings.copy()
clear_pairings = all_pairings.copy()
initial_pairing(poly, commands, all_pairings)
#print(all_pairings)
for i in range(40):
    for x in all_pairings:
        if all_pairings[x] > 0:
            insert = commands[x]
            first_half = x[0] + insert
            second_half = insert + x[1]
            # print(first_half,second_half, x[0], x[1], insert)
            # print(all_pairings[x])
            temp_pairings[first_half] += int(all_pairings[x])
            temp_pairings[second_half] += int(all_pairings[x])
            if insert not in total_occurence:
                total_occurence[insert] = 0
            total_occurence[insert] += int(all_pairings[x])
    all_pairings = temp_pairings.copy()
    temp_pairings = clear_pairings.copy()
small = total_occurence["N"]
big = total_occurence["N"]
for i in total_occurence:
    if int(total_occurence[i]) < int(small):
        small = total_occurence[i]
    elif int(total_occurence[i]) > int(big):
        big = total_occurence[i]
print(all_pairings)
print(big - small)

