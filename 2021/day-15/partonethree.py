from timeit import default_timer as timer
def findMin(Lines):
    Unexplored = []
    Unexplored.append([0, 0, 0])
    dirs = [(1, 0), (0, 1)]
    while True:
        #print("-------------")
        Unexplored.sort(key=lambda x: x[2])
        #print(Unexplored)
        #print("-------------")
        ToExplore = Unexplored[0]
        x, y = Unexplored[0][0], Unexplored[0][1]
        if x == len(Lines) - 1 and y == len(Lines[0]) -1:
            break
        Unexplored.pop(0)
        cost = int(ToExplore[2])
        for area in dirs:
            newX, newY = x + area[0], y + area[1]
            if newX <= len(Lines) - 1 and newY <= len(Lines[0]) - 1:
                newCost = int(Lines[newX][newY]) + cost
                found = False
                for node in Unexplored:
                    if node[0] == newX and node[1] == newY:
                        found = True
                        if newCost < int(node[2]):
                            node[2] = newCost
                        break
                if found == False:
                    Unexplored.append([newX, newY, newCost])
    #print(ToExplore)
    print(ToExplore[2])
    print("Broke out")       

start = timer()
Lines = []
with open("input.txt") as f:
    for line in f:
        Lines.append(line.strip())
#print(len(Lines[0]))
findMin(Lines)
end = timer()
print(end - start)
#Test.txt timer = 0.0015259170000000016
#Input.txt timer = 64.75377462499999