import random

print("This will populate and counting-sort an array according to input parameters.")

# Populate the list to be sorted
n = int(input("Enter the size of the array to be sorted: "))
r = int(input("Enter the range of numbers to be generated and inserted: "))
a = []
for x in range(n):
	a.append(random.randint(0,r))

# Create and populate data structure for counts
index = [0 for j in range(n)]
for x in a:
	index[x] += 1
i = 1;
while i < len(index):
	index[i] += index[i-1]
	i+=1

# Create and populate output
f = [0 for i in range(len(a))]
for i in range(len(a)):
	f[index[a[i]]-1] = a[i]
	index[a[i]] -= 1

# Print list to check
print(f)
