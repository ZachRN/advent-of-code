def play(pos, Dice):
    for x in range(3):
        pos += Dice
        Dice += 1
        if Dice == 101:
            Dice = 1
    while pos > 10:
        pos -= 10
    return pos, Dice

with open("input.txt") as f:
    Lines = f.readlines()
pop = int(Lines[0][-2]) #player one position
ptp = int(Lines[1][-1]) # player two position
print(pop,ptp)
pos = 0 #player one score
pts = 0 #player two score
Dice = 1
Rolls = 0

while pts < 1000:
    pop, Dice = play(pop, Dice)
    pos += pop
    Rolls += 3
    if pos >= 1000:
        break
    ptp, Dice = play(ptp, Dice)
    pts += ptp
    Rolls += 3
Lower = pos
if pts < Lower:
    Lower = pts
print(Lower * Rolls)
