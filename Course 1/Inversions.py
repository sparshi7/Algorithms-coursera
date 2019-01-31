f=open('IntegerFile.txt')
li=[]
for line in f:
	li.append(int(line))
# li=[1, 3, 5, 2, 4, 6]
# li = [6,5,4,3,2,1]
def SortandCountInv(A):
	if(len(A)==1):
		return list(A), 0
	D=[]
	count=0
	B, x=SortandCountInv(list(A[:len(A)//2]))
	C, y=SortandCountInv(list(A[len(A)//2:]))
	i=0
	j=0
	for k in range(len(A)):
		if i!=len(B) and j!=len(C):	
			if(B[i]<=C[j]):
				D.append(B[i])
				i+=1
			else:
				count+=(len(B)-i)
				D.append(C[j])
				j+=1
		else:
			break
	if(i==len(B)):
		D[k:]=C[j:]
	else:
		D[k:]=B[i:]
	return list(D), x+y+count
D, count=SortandCountInv(list(li))
print('Number of Inversions =', count)