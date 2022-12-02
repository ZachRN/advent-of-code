count = 0
with open("input.txt") as f:
    for line in f:
        for encode in line.split()[11:]:
            if len(encode) in (2,3,4,7):
                count += 1
print(count)