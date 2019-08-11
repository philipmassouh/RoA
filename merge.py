import random
# Used to merge the two halves.
def merge(ar,l,r):
	a=b=c=0
	while a<len(l) and b<len(r):
		if l[a] < r[b]:
			ar[c] = l[a]
			a+=1
		else:
			ar[c] = r[b]
			b+=1
		c+=1
	while a < len(l):
		ar[c] = l[a]
		c+=1
		a+=1
	while b < len(r):
		ar[c] = r[b]
		c+=1
		b+=1

# Recursively dividies array until size is one.
def mergeSort(a):
	if len(a)>1:
		l=a[:len(a)//2]
		r=a[len(a)//2:]
		mergeSort(l)
		mergeSort(r)
		merge(a,l,r)

# Test code
r = int(input("Enter the range of the elements to be randomly generated: "))
n = int(input("Enter the size of the array in which to generate said elements: "))
a =[]
for x in range(n):
	a.append(random.randint(0,r))
print(a)
c = int(input("Enter zero to sort and display, anything else to quit: "))
mergeSort(a)
print(a)
