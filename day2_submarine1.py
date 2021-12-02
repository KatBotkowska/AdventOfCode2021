with open("submarine_data.txt") as f:
	data = [line.strip().split() for line in f]

#print(data)
def submarine(directions):
	horizontal = 0
	depth = 0
	for direction in directions:
		if direction[0] == 'forward':
			horizontal += int(direction[1])
		elif direction[0] == 'up':
			depth-=int(direction[1])
		else:
			depth+=int(direction[1])
	return f'horizontal {horizontal}, depth {depth}, final position {horizontal*depth}'

print(submarine(data))
