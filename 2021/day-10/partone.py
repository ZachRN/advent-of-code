with open("input.txt") as f:
    Lines = f.readlines()
total = 0
for line in Lines:
    openers = []
    for character in line:
        if character in ('(', '[', '{', '<'):
            openers.append(character)
        elif character == ')':
            if openers[len(openers) - 1] == '(':
                openers.pop()
            else:
                total += 3
                break
        elif character == ']':
            if openers[len(openers) - 1] == '[':
                openers.pop()
            else:
                total += 57
                break
        elif character == '}':
            if openers[len(openers) - 1] == '{':
                openers.pop()
            else:
                total += 1197
                break
        elif character == '>':
            if openers[len(openers) - 1] == '<':
                openers.pop()
            else:
                total += 25137
                break
print(total)
