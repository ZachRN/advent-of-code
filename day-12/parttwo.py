global_count = 0

def count_total(entry, caves, path, smalls):
    global global_count
    if entry == "end":
        global_count += 1
        return
    if entry == "start":
        return
    path_double = 0
    for pathtaken in smalls:
        if path.count(pathtaken) > 2:
            return
        if path.count(pathtaken) == 2:
            path_double += 1
        if path_double > 1:
            return
    for avail in caves[entry]:
        path.append(avail)
        count_total(avail,caves,path,smalls)
        path.pop()
            
Lines = []
caves = {}
with open("largetest.txt") as f:
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
smalls = []
for unique in UniqueInputs:
    if str(unique).islower() and str(unique) != "end" and str(unique) != "start":
        smalls.append(unique)
#print (caves)
for entry in caves["start"]:
    temp = ["start", entry]
    count_total(entry, caves, temp, smalls)
print(global_count)

#print(caves)
#print(UniqueInputs)