global_count = 0

def count_total(entry, caves, path):
    global global_count
    for avail in caves[entry]:
        if str(avail) == "start":
            continue
        if str(avail) == "end":
            path.append(str(avail))
            print(path)
            path.pop()
            global_count += 1
        elif str(avail).isupper() or avail not in path:
            path.append(avail)
            count_total(avail, caves, path)
            path.pop()

Lines = []
caves = {}
with open("input.txt") as f:
    for line in f:
        Lines.append(line.strip().split("-"))
UniqueInputs = []
for line in Lines:
    for cave in line:
        if cave not in UniqueInputs:
            UniqueInputs.append(cave)
for unique in UniqueInputs:
    hasend = 0
    temp = []
    for line in Lines:
        if unique == line[0]:
            if(line[1] == "end"):
                hasend = 1
                continue
            temp.append(line[1])
        elif unique == line[1]:
            if(line[0] == "end"):
                hasend = 1
                continue
            temp.append(line[0])
    #print(temp)
    if hasend == 1:
        temp.append("end")
    caves[unique] = temp
#print (caves)
for entry in caves["start"]:
    temp = ["start", entry]
    count_total(entry, caves, temp)
print(global_count)

#print(caves)
#print(UniqueInputs)