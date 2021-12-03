import statistics
from statistics import mode
with open("binary_diag_day3.txt") as f:
	data = [line.strip() for line in f]

def common(data):
	new_data =[]
	for i in range(len(data[0])):
		new_data.append([])
		for elem in data:
			new_data[i].append(str(elem[i]))
	most_common =[]
	least_common =[]

	for elem in new_data:
		most_common += max(set(elem), key=elem.count)
		least_common += min(set(elem), key=elem.count)
	return most_common

def oxygen(data):
	for i in range(len(data[0])):
		to_remove=[]
		for elem in data:

			if elem[i]!=common(data)[i]:
				to_remove.append(elem)
		data = [elem for elem in data if elem not in to_remove]
		if len(data)==1:
			break
	return data[0]

with open("binary_diag_day3.txt") as f:
	other_data = [line.strip() for line in f]
def co2(data):
	for i in range(len(data[0])):
		to_remove=[]
		for elem in data:

			if elem[i]==common(data)[i]:
				to_remove.append(elem)
		data = [elem for elem in data if elem not in to_remove]
		if len(data)==1:
			break
	return data[0]


print('oxygenwynik', oxygen(data))
print('co2wynik', co2(other_data))
oxygen = int(oxygen(data), 2)
print('oxygen', oxygen)
co2 = int(co2(other_data), 2)
print('co2', co2)
print('solution',oxygen*co2)
# print(f'solution {int(oxygen[0], 2)*int(co2[0],2)}')