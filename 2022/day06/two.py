with open("input.txt", 'r') as f:
	myinput = f.readline()
for i in range(len(myinput)):
	if (len(set(myinput[i:i+14])) == 14):
		print(i + 14)
		break
#day 2 was modified based on advice from asarandi using set
#(though their implementation is still nicer)