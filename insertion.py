import random
def insertionSort(a):
	b = []
	while len(a) > 0:
		value = a.pop()
		i = 0
		while i < len(b) and value > b[i]:
			i+=1
		b.insert(i, value)
	return b
