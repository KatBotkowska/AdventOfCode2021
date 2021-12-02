with open("submarine_data.txt") as f:
	data = [line.strip().split() for line in f]

#print(data)
def submarine2(directions):
	horizontal = 0
	depth = 0
	aim = 0
	for direction in directions:
		if direction[0] == 'forward':
			horizontal += int(direction[1])
			depth +=aim*int(direction[1])
		elif direction[0] == 'up':
			aim-=int(direction[1])
		else:
			aim+=int(direction[1])
	return f'horizontal {horizontal}, depth {depth}, aim {aim}, final position {horizontal*depth}'

print(submarine2(data))
