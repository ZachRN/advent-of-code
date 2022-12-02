from pickle import FALSE


def main_function():
	with open("input.txt", 'r') as f:
		data = f.readline()

	x = 0
	y = 0
	robot_x = 0
	robot_y = 0
	visited_locations = {}
	visited_locations_robot = {}
	key_string = str(x) + str(y)
	visited_locations[key_string] = 1
	visited_locations_robot[key_string] = 1
	Robot = False
	for character in data:
		if Robot is False:
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
			elif key_string not in visited_locations_robot:
				visited_locations[key_string] = 1	
			Robot = True
		else:
			if character == '^':
				robot_y += 1
			elif character == 'v':
				robot_y -= 1
			elif character == '<':
				robot_x -= 1
			elif character == '>':
				robot_x += 1
			key_string = str(robot_x) + str(robot_y)
			if key_string in visited_locations_robot:
				visited_locations_robot[key_string] += 1
			elif key_string not in visited_locations:
				visited_locations_robot[key_string] = 1	
			Robot = False

	# print(visited_locations)
	print(len(visited_locations))
	print(len(visited_locations_robot))
	print(len(visited_locations_robot) + len(visited_locations) - 1) #minus one cause 0,0

if __name__ == "__main__":
	main_function()