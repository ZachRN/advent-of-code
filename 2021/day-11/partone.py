#y - 1 = top
#y + 1 = bottom
#x - 1 = left
#x + 1 = right
#y - 1 x - 1 = top left
#y - 1 x + 1 = top right
#y + 1 x - 1 = bottom left
#y + 1 x + 1 = bottom right
def try_cells_add(Lines, y, x):
	flashIncrease = 0
	if Lines[y][x] != 10:
		return flashIncrease, Lines
	Lines[y][x] += 1
	negx = x
	negy = y
	if x == 0:
		negx = 1
	if y == 0:
		negy = 1
	#print(Lines[y][x])
	try: #Top Cell
		if int(Lines[negy - 1][x]) < 10:
			Lines[negy - 1][x] = int(Lines[negy - 1][x]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Bottom Cell
		if int(Lines[y + 1][x]) < 10:
			Lines[y + 1][x] = int(Lines[y + 1][x]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Left Cell
		if int(Lines[y][negx - 1]) < 10:
			Lines[y][negx - 1] = int(Lines[y][negx - 1]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Right Cell
		if int(Lines[y][x + 1]) < 10:
			Lines[y][x + 1] = int(Lines[y][x + 1]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Top Left Cell
		if int(Lines[negy - 1][negx - 1]) < 10:
			Lines[negy - 1][negx - 1] = int(Lines[negy - 1][negx - 1]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Top Right Cell
		if int(Lines[negy - 1][x + 1]) < 10:
			Lines[negy - 1][x + 1] = int(Lines[negy - 1][x + 1]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Bottom Left Cell
		if int(Lines[y + 1][negx - 1]) < 10:
			Lines[y + 1][negx - 1] = int(Lines[y + 1][negx - 1]) + 1
			flashIncrease += 1
	except:
		pass
	try: # Bottom Right Cell
		if int(Lines[y + 1][x + 1]) < 10:
			Lines[y + 1][x + 1] = int(Lines[y + 1][x + 1]) + 1
			flashIncrease += 1
	except:
		pass
	return flashIncrease, Lines
def find_center_flash(Lines, y, x):
	flashIncrease = 0
	try: #Top Cell
		if Lines[y - 1][x] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Bottom Cell
		if Lines[y + 1][x] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Left Cell
		if Lines[y][x - 1] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Right Cell
		if Lines[y][x + 1] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Top Left Cell
		if Lines[y - 1][x - 1] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Top Right Cell
		if Lines[y - 1][x + 1] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Bottom Left Cell
		if Lines[y + 1][x - 1] >= 10:
			flashIncrease += 1
	except:
		pass
	try: # Bottom Right Cell
		if Lines[y + 1][x + 1] >= 10:
			flashIncrease += 1
	except:
		pass
	if flashIncrease == 8:
		Lines[y][x] = 11
	return Lines

def find_flashes(Lines):
	flashes = 0
	flashIncrease = 1
	temp = 0
	while flashIncrease > 0:
		y = 0
		flashIncrease = -1
		while y in range(len(Lines)):
			x = 0
			while x in range(len(Lines[y])):
				temp, Lines = try_cells_add(Lines, y, x)
				#Lines = find_center_flash(Lines, y, x)
				flashIncrease += temp
				x += 1
			y += 1
		#print(flashIncrease)
	y = 0
	while y in range(len(Lines)):
		x = 0
		while x in range(len(Lines[y])):
			if Lines[y][x] > 9:
				flashes += 1
				Lines[y][x] = 0
			x += 1
		y += 1
	return flashes, Lines

with open("test.txt") as f:
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
#print(new_Lines)
#print(Lines)
i = 0
x = 0
y = 0
total_flashes = 0
while i in range(10):
	y = 0
	while y in range(len(new_Lines)):
		x = 0
		while x in range(len(new_Lines[y])):
			new_Lines[y][x] += 1
			x += 1
		y += 1
	i += 1
	for line in new_Lines:
		print(line)
	print("------")
	flashes, new_Lines = find_flashes(new_Lines)
	for line in new_Lines:
		print(line)
	print("--")
	total_flashes += flashes
print(total_flashes)
