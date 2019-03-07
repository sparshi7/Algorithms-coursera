f = open('Quicksort.txt')
li = []
c=0
for line in f:
	li.append(int(line))
	c+=1
# li=[3,8,2,5,1,4,7,6]
global count
count=0
def ChoosePivot(A, n):

	#swap pivot with first element

	#choose first element as pivot
	# A[0] = A[0]

	#choose last element as pivot
	# A[0], A[n-1] = A[n-1], A[0]

	#choose median of first, middle and last element as pivot
	if (n%2==0):
		ind=(n//2-1)
	else:
		ind=(n//2)
	arr= [A[0],A[ind], A[n-1]]
	arr.sort()
	if arr[1]==A[ind]:
		A[0], A[ind] = A[ind], A[0]
	elif arr[1]==A[n-1]:
		A[0], A[n-1] = A[n-1], A[0]

def Partition(A, n):
	p = A[0]
	i = 1
	j=1
	while(j<n):
		if A[j]<p:
			A[j], A[i] = A[i], A[j]
			i=i+1
		j=j+1
	A[0], A[i-1] = A[i-1], A[0]
	return i-1

def Quicksort(A, n):
	if n<=1:
		return
	ChoosePivot(A,n)
	#Partition A around p
	partition=Partition(A,n)
	global count
	count+=n-1
	Quicksort(A[:partition], partition)
	Quicksort(A[partition+1:], n-partition-1)
	

Quicksort(li, len(li))
print('The number of comparisons required is', count)