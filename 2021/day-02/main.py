#Advent of Code Day Two Part One
with open("input.txt", "r") as f:
    Lines = f.readlines()
depth = 0
horizontal = 0
for line in Lines:
    if line.startswith("forward"):
        horizontal += int(line[8:])
    elif line.startswith("up"):
        depth -= int(line[2:])
    elif line.startswith("down"):
        depth += int(line[4:])
print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Multiplied: " + str((depth * horizontal)))
#Advent of Code Day Two Part Two
depth = 0
horizontal = 0
aim = 0
for line in Lines:
    if line.startswith("forward"):
        horizontal += int(line[8:])
        depth += int(line[8:]) * aim
    elif line.startswith("up"):
        aim -= int(line[2:])
    elif line.startswith("down"):
        aim += int(line[4:])
print("Aim: +" + str(aim))
print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Multiplied: " + str((depth * horizontal)))