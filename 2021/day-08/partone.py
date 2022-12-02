with open("input.txt", "r") as f:
    Lines = f.readlines()
count = 0
for line in Lines:
    temp = line.split()[11:]
    for encode in temp:
        if len(encode) in (2, 4, 3, 7):
            count += 1
print(count)