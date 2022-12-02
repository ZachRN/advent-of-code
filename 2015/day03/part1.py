def main_function():
	with open("input.txt", 'r') as f:
		data = f.readline()
	x = 0
	y = 0
	visited_locations = {}
	key_string = str(x) + str(y)
	visited_locations[key_string] = 1
	for character in data:
		if character == '^':
			y += 1
		elif character == 'v':
			y -= 1
		elif character == '<':
			x -= 1
		elif character == '>':
			x += 1
		key_string = str(x) + str(y)
		if key_string in visited_locations:
			visited_locations[key_string] += 1
		else:
			visited_locations[key_string] = 1	
	# print(visited_locations)
	print(len(visited_locations))

if __name__ == "__main__":
	main_function()