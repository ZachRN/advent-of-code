def hasall(num, puzzle):
    for character in num:
        if character not in puzzle:
            return (-1)
    return (0)

def solve(line):
    decode = line.split()[:10]
    num_dict = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    for puzzle in decode:
        if len(puzzle) == 2:
            num_dict[1] = puzzle
        elif len(puzzle) == 3:
            num_dict[7] = puzzle
        elif len(puzzle) == 4:
            num_dict[4] = puzzle
        elif len(puzzle) == 7:
            num_dict[8] = puzzle
    for puzzle in decode:
        if len(puzzle) == 6 and hasall(num_dict[4], puzzle) == 0:
            num_dict[9] = puzzle
        elif len(puzzle) == 6 and hasall(num_dict[1], puzzle) == 0:
            num_dict[0] = puzzle
        elif (len(puzzle) == 6):
            num_dict[6] = puzzle
    for puzzle in decode:
        if len(puzzle) == 5 and hasall(num_dict[7], puzzle) == 0:
            num_dict[3] = puzzle
        elif len(puzzle) == 5 and hasall(puzzle, num_dict[6]) == 0:
            num_dict[5] = puzzle
        elif len(puzzle) == 5:
            num_dict[2] = puzzle
    decode = line.split()[11:]
    answer = 0
    for puzzle in decode:
        for i in range(10):
            #I originally counted the Ascii value of the string, and attempted it based on that, however it came back wrong in certain
            #cases, unsure why, look into later however sorting the string and comparing solves theissue
            if sorted(puzzle) == sorted(num_dict[i]):
                answer = (answer * 10) + i
                break
    return (int(answer))

with open("input.txt", "r") as f:
    Lines = f.readlines()
running_total = 0
for line in Lines:
    running_total += solve(line)
print(running_total)