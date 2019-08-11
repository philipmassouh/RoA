def heapify(heap, root):
	newRoot = root
	leftChild = 2*root+1
	rightChild = 2*root+2
	if leftChild < len(heap) and heap[leftChild] > heap[newRoot]:
		newRoot = leftChild
	if rightChild < len(heap) and heap[rightChild] > heap[newRoot]:
		newRoot = rightChild
	if root!=newRoot:
		heap[root],heap[newRoot]=heap[newRoot],heap[root]
		heapify(heap,newRoot)

def heapSort(heap):
	for i in range(len(heap), -1, -1):
		heapify(heap, i)
	answer = []
	while(len(heap)>1):
		answer.insert(len(answer),heap[0])
		heap[0],heap[-1]=heap[-1],heap[0]
		heap.pop()
		heapify(heap, 0)
	return answer
