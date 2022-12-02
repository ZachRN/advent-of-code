def main_function():
	with open("input.txt", 'r') as f:
		data = f.readlines()
	total_paper = 0
	for present in data:
		dimensions = present.split('x')

		length = int(dimensions[0])
		width = int(dimensions[1])
		height = int(dimensions[2])

		sides = []
		sides.append(length)
		sides.append(height)
		sides.append(width)
		sides.sort()

		total_paper += (sides[0] * sides[1] * sides[2]) +  ((sides[0] + sides[1]) * 2)
	print(total_paper)

if __name__ == "__main__":
	main_function()