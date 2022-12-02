import hashlib

def main_function():
	with open("input.txt", 'r') as f:
		data = f.readlines()
	total = 0
	for line in data:
		if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
			continue
		vowels = line.count('a')
		vowels += line.count('e')
		vowels += line.count('i')
		vowels += line.count('o')
		vowels += line.count('u')
		if (vowels < 3):
			continue
		i = 1
		while i < len(line):
			if line[i] == line[i-1]:
				total += 1
				break
			i += 1
	print(total)

if __name__ == "__main__":
	main_function()