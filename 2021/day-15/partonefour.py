from timeit import default_timer as timer
import heapq
import math

def findMin(Lines):
    lowest_path = [[math.inf] * len(row) for row in Lines]
    lowest_path[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    while True:
        _, x, y = heapq.heappop(queue)
        lowest = lowest_path[x][y]
        if x == len(Lines) - 1 and y == len(Lines[0]) - 1:
            return lowest
        for newX, newY in ((x + 1, y),(x, y + 1),(x - 1, y),(x, y - 1)):
            if newX not in range(len(Lines)) or newY not in range(len(Lines[0])):
                continue
            new_lowest = lowest + int(Lines[newX][newY])
            if new_lowest < lowest_path[newX][newY]:
                lowest_path[newX][newY] = new_lowest
                heapq.heappush(queue, (new_lowest,newX,newY))

start = timer()
Lines = []
with open("bigmap.txt") as f:
    for line in f:
        Lines.append(line.strip())
Lines = [list(map(int, line.strip())) for line in Lines]
print(findMin(Lines))
end = timer()
print(end - start)
