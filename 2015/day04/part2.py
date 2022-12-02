import hashlib

def main_function():
	with open("input.txt", 'r') as f:
		data = f.readline()
	save = data
	lowest_number = 0
	while (True):
		data = save
		data = data + str(lowest_number)
		hashed = hashlib.md5(data.encode('utf-8')).hexdigest()
		if hashed.startswith("000000"):
			break
		lowest_number += 1
	print(lowest_number)

if __name__ == "__main__":
	main_function()