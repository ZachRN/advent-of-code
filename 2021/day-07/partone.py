with open("input.txt", "r") as f:
	positions = list(map(int, f.readline().split(",")))

BestPosition = 0
BestFuelUsage = 0
for i in range(800):
	FuelUsage = 0
	for number in positions:
		FuelUsage += abs((number - i))
	if FuelUsage < BestFuelUsage or BestFuelUsage == 0:
		BestFuelUsage = FuelUsage
		BestPosition = i
print("Fuel Usage: " + str(BestFuelUsage))
print("Best Position: " + str(BestPosition))