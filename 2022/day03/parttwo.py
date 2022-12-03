def find_common_letter(A, B, C):
	for i in range(0, len(A)):
		if A[i] in B and A[i] in C:
			return A[i]
	return (0)

#Advent of Code 2022 Day Three Part one
with open("input.txt", 'r') as f:
	myinput = f.readlines()
output = 0
i = 0
while i < len(myinput):
	A = myinput[i]
	B = myinput[i + 1]
	C = myinput[i + 2]
	letter = find_common_letter(A,B,C)
	if (ord(str(letter)) >= 97):
		output = output + ord(str(letter)) - 96
	else:
		output = output + ord(str(letter)) - 38
	i += 3
print(output)
