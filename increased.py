with open("data.txt") as f:
	data = [int(line.strip()) for line in f]


def increased(numbers):
	increased = 0
	for i in range(0, len(numbers)-2):
		if numbers[i+1]>numbers[i]:
			increased+=1
	return increased

print(increased(data))
