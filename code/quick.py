def partition(a,l,h):
	p = h
	i = l-1
	for j in range(l,h):
		if a[j] <= a[p]:
			i+=1
			a[i],a[j]=a[j],a[i]
	a[i+1],a[h]=a[h],a[i+1]
	return i+1	

def quickSort(a,l,h):
	if l<h:
		x=partition(a,l,h)
		quickSort(a,l,x-1)
		quickSort(a,x+1,h)

a = [97, 42, 1, 24, 63, 94, 2]
quickSort(a,0,len(a)-1)
print(a)
