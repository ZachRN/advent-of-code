def main_function():
	with open("input.txt", 'r') as f:
		data = f.readline()
	floor = 0
	basement = 0
	for character in data:
		if character == '(':
			floor += 1
		elif character == ')':
			floor -= 1
		basement += 1
		if floor < 0:
			break
	print(basement)
	
if __name__ == "__main__":
	main_function()