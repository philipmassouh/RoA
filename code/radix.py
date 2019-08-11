import random

def countingSort(inp, exp):
	# Initialize the count and output structures.
	out = [0] *	len(inp)
	cnt = [0] * 10 # This is a radix sort subroutine so we only need 0-9.
	# Populate the count array.
	for x in inp:
		idx = x/exp
		cnt[int(idx % 10)] += 1
	# Sum those bad boys up
	for i in range(1,10):
		cnt[i] += cnt[i-1]
	# Populate the output array.
	i = n-1
	while i>=0:
		idx = inp[i]/exp
		out[cnt[int(idx%10)] - 1] = inp[i]
		cnt[int(idx%10)] -=1
		i-=1
	# Copy values over
	for i in range(0, len(inp)):
		inp[i] = out[i]

def radixSort(a):
	print("This will populate and radix-sort an array according to input parameters.")
	# Find the maximum value in the input.
	max1 = a[0]
	for x in range(len(a)):	
		if max1 < a[x]:
			max1 = a[x]
	# Counting sort for every digit
	exp = 1
	while max1/exp > 0:
		countingSort(a, exp)
		exp *= 10


# Populate the list to be sorted
n = int(input("Enter the size of the array to be sorted: "))
v = int(input("Enter non-inclusive max value of random numbers to be inserted: "))
a = []
for x in range(n):
	a.append(random.randint(0,v))

radixSort(a)
print(a)
