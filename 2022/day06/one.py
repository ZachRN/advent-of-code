from collections import Counter

def checkduplicates(substr):
	WC = Counter(substr)
	for letter, count in WC.items():
		if (count > 1):
			return(1)
	return (0)
		
with open("input.txt", 'r') as f:
	myinput = f.readline()
	
output = 0
for i in range(len(myinput)):
	substr = myinput[i:i+4]
	if (checkduplicates(substr) == 0):
		print(substr, i+4)
		break