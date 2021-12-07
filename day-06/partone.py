with open("input.txt", "r") as f:
    Lines = f.readlines()
School = Lines[0].split(",")
for i in range(80):
    ArraySize = len(School)
    for fish in range(ArraySize):
        School[fish] = int(School[fish]) - 1
        if School[fish] == -1:
            School[fish] = 6
            School.append(8)
print(len(School))