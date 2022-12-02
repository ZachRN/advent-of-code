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
		sides.append(length * width)
		sides.append(length * height)
		sides.append(height * width)
		sides.sort()

		total_paper += (sides[0] + sides[1] + sides[2]) * 2 + sides[0]
	print(total_paper)

if __name__ == "__main__":
	main_function()