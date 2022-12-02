def main_function():
	with open("input.txt", 'r') as f:
		data = f.readline()
	floor = 0
	for character in data:
		if character == '(':
			floor += 1
		elif character == ')':
			floor -= 1
	print(floor)

if __name__ == "__main__":
	main_function()