with open("data.txt") as f:
	data = [int(line.strip()) for line in f]

new_data = [sum(data[i:i+3]) for i in range(len(data)-1)]

def increased_2(numbers):
	increased = 0
	for i in range(0, len(numbers)-2):
		if numbers[i+1]>numbers[i]:
			increased+=1
	return increased

print(increased_2(new_data))
