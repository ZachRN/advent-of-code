def find_complete(openers, character):
    if character == ')':
        if openers[len(openers) - 1] == '(':
            openers.pop()
            return (1, openers)
        else:
            return (-1, openers)
    elif character == ']':
        if openers[len(openers) - 1] == '[':
            openers.pop()
            return (1, openers)
        else:
            return (-1, openers)
    elif character == '}':
        if openers[len(openers) - 1] == '{':
            openers.pop()
            return (1, openers)
        else:
            return (-1, openers)
    elif character == '>':
        if openers[len(openers) - 1] == '<':
            openers.pop()
            return (1, openers)
        else:
            return (-1, openers)
    return (1, openers)
def find_score(openers):
    total_score = 0
    for character in reversed(openers):
        total_score *= 5
        if character == '(':
            total_score += 1
        elif character == '[':
            total_score += 2
        elif character == '{':
            total_score += 3
        elif character == '<':
            total_score += 4
    return (int(total_score))
with open("input.txt") as f:
    Lines = f.readlines()
scores = []
for line in Lines:
    openers = []
    incomplete = 0
    for character in line:
        if character in ('(', '[', '{', '<'):
            openers.append(character)
        else:
            incomplete, openers = find_complete(openers, character)
        if incomplete == -1:
            break
    if incomplete == 1:
        scores.append(find_score(openers))
print("Unsorted Scores:")
print(scores)
print("Sorted Scores:")
scores.sort()
print(scores)
print("Middle of Scores:")
print(scores[int((len(scores) -1 ) /2)])
