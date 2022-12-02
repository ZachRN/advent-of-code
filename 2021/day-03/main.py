#Advent of Code Day 3 Part One
with open("input.txt", "r") as f:
    Lines = f.readlines()
gamma = list('000000000000')
epsilon = list('000000000000')
for i in range(12):
    x = 0
    for line in Lines:
        if line[i] == "1":
            x += 1
    if (x > 500):
        gamma[i] = '1'
        epsilon[i] = '0'
    else:
        gamma[i] = '0'
        epsilon[i] = '1'
print(int(''.join(gamma),2))
print(int(''.join(epsilon),2))
print(int(''.join(gamma),2) * int(''.join(epsilon),2))
#Advent of Code Day 3 Part Two
Copy = Lines.copy()
for i in range(12):
    one = 0
    zero = 0
    ones = []
    zeros = []
    for line in Copy:
        if line[i] == "1":
            one += 1
            ones.append(line)
        else:
            zero += 1
            zeros.append(line)
    if zero > one:
        Copy = zeros
    else:
        Copy = ones
holdone = Copy[0]
Copy = Lines.copy()
for i in range(12):
    one = 0
    zero = 0
    ones = []
    zeros = []
    for line in Copy:
        if line[i] == "1":
            one += 1
            ones.append(line)
        else:
            zero += 1
            zeros.append(line)
    #print(one)
    #print(zero)
    if one < zero:
        Copy = ones
    else:
        Copy = zeros
    if (len(Copy) == 1):
        break
holdtwo = Copy[0]
# print(holdone)
print(int(holdone,2)) 
#print(holdtwo)  
print(int(holdtwo,2)) 
print(int(holdtwo,2) * int(holdone,2))   