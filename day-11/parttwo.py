def check_flash(new_Lines, y, x):
	if new_Lines[y][x] != 10:
		return 0, new_Lines
	new_Lines[y][x] += 1
	if y > 0 and x > 0: #Top Left
		if new_Lines[y - 1][x - 1] < 10:
			new_Lines[y - 1][x - 1] += 1
	if y > 0: # Top
		if new_Lines[y - 1][x] < 10:
			new_Lines[y - 1][x] += 1
	if x > 0: # Left
		if new_Lines[y][x - 1] < 10:
			new_Lines[y][x - 1] += 1
	if x < 9: # Right
		if new_Lines[y][x + 1] < 10:
			new_Lines[y][x + 1] += 1
	if y < 9: # Bottom
		if new_Lines[y + 1][x] < 10:
			new_Lines[y + 1][x] += 1
	if y < 9 and x > 0: #Bottom Left
		if new_Lines[y + 1][x - 1] < 10:
			new_Lines[y + 1][x - 1] += 1
	if y < 9 and x < 9: #Bottom Right
		if new_Lines[y + 1][x + 1] < 10:
			new_Lines[y + 1][x + 1] += 1
	if y > 0 and x < 9: #Top Right
		if new_Lines[y - 1][x + 1] < 10:
			new_Lines[y - 1][x + 1] += 1
	return 1, new_Lines

def flash_amount(new_Lines):
	increasing = 1
	while increasing > 0:
		increasing = 0
		for y in range(len(new_Lines)):
			for x in range(len(new_Lines[y])):
				temp, new_Lines = check_flash(new_Lines, y, x)
				increasing += temp
	counter = 0
	for y in range(len(new_Lines)):
		for x in range(len(new_Lines)):
			if new_Lines[y][x] > 9:
				new_Lines[y][x] = 0
				counter += 1
	for y in range(len(new_Lines)):
		for x in range(len(new_Lines)):
			if new_Lines[y][x] != 0:
				return False, new_Lines
	return True, new_Lines


with open("input.txt") as f:
	Lines = f.readlines()
	new_Lines = []
	i = 0
	for line in Lines:
		new_Lines.append([])
		for num in line:
			if num == '\n':
				break
			new_Lines[i].append(int(num))
		i += 1
counter = 0
done = False
while not done:
	for y in range(len(new_Lines)):
		for x in range(len(new_Lines[y])):
			new_Lines[y][x] += 1
	done, new_Lines = flash_amount(new_Lines)
	counter += 1
print(counter)
