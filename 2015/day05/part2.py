def main_function():
	with open("input.txt", 'r') as f:
		data = f.readlines()
	for line in data:
		i = 0
		visited_locations = {}
		length = len(line)
		while i < length - 1:
			j = 0
			while j < length - 1:
					
	# print(visited_locations)
	print(len(visited_locations))

if __name__ == "__main__":
	main_function()