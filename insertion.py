import random
def insertionSort(a):
	b = []
	while len(a) > 0:
		value = a.pop()
		i = 0
		while i < len(b) and value > b[i]:
			i+=1
		b.insert(i, value)
	print(b)

#Generate Random Numbers
n = int(input("Enter the number of elements to generate: "))
r = int(input("Enter the the range of the elements: "))
a = []
for x in range(n):
	a.append(random.randint(0,r))

insertionSort(a)
