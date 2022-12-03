def find_letter(answers, strlen):
	seenLetters = {}
	for i in range(0, int(strlen/2)):
		key_string = answers[i]
		if key_string not in seenLetters:
			seenLetters[key_string] = 1
	for i in range(int(strlen/2), strlen):
		key_string = answers[i]
		if key_string in seenLetters:
			return(key_string)
	return (0)

#Advent of Code 2022 Day Three Part one
with open("input.txt", 'r') as f:
	myinput = f.readlines()
output = 0
for line in myinput:
	answers = line.strip()
	strlen = len(answers)
	letter = find_letter(answers, strlen)
	if (ord(str(letter)) >= 97):
		output = output + ord(str(letter)) - 96
	else:
		output = output + ord(str(letter)) - 38
	# output = output + 
# print(ord('A'))
print(output)
