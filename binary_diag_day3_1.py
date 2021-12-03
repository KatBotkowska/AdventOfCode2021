import statistics
from statistics import mode
with open("binary_diag_day3.txt") as f:
	data = [line.strip() for line in f]


def binary_diag_1(data):
	new_data=[]
	gamma_rate=''
	epsilon_rate=''
	for i in range(len(data[0])):
		new_data.append([])
		for elem in data:
			new_data[i].append(str(elem[i]))
	for elem in new_data:
		# most_common = mode(elem)
		most_common = max(set(elem), key=elem.count)
		less_common = min(set(elem), key=elem.count)
		gamma_rate +=most_common
		epsilon_rate+=less_common
	return int(gamma_rate,2) * int(epsilon_rate,2)


print(binary_diag_1(data))
