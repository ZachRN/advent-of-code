with open("input.txt", "r") as f:
    Lines = f.readlines()
School = Lines[0].split(",")
AllFish = ([0 for x in range(10)])
for fish in School:
    AllFish[int(fish)] += 1
for i in range(256):
    tempNew = AllFish[0]
    for x in range(9):
        AllFish[x] = AllFish[x + 1]
    AllFish[6] += tempNew
    AllFish[8] = tempNew
print(sum(AllFish))
print(AllFish)