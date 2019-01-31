n1=int(input('Enter first number'))
n2=int(input('Enter second number'))
def Karatsuba(x,y):
	len_x=len(str(x))
	len_y =len(str(y))

	if len_x != 1:
		if len_x%2!=0:
			a=int(x//(10**((len_x+1)//2)))
			b=int(x%(10**((len_x+1)//2)))
		else:
			a=int(x//(10**(len_x//2)))
			b=int(x%(10**(len_x//2)))
	else:
		a=0
		b=x

	if len_y !=1:
		if len_y%2!=0:
			c=int(y//(10**((len_y+1)//2)))
			d=int(y%(10**((len_y+1)//2)))
		else:
			c=int(y//(10**(len_y//2)))
			d=int(y%(10**(len_y//2)))
	else:
		c=0
		d=y
 
	if len(str(a))!=1 and len(str(c))!=1:
		mul1=Karatsuba(a,c)
	else:
		mul1=a*c	

	if len(str(b))!=1 and len(str(d))!=1:
		mul2=Karatsuba(b,d)
	else:		
		mul2=b*d
 	
	mul3=(a+b)*(c+d)
	mul4=mul3-mul1-mul2

	if len_x>=len_y:
		if len_x%2==0:
			return (10**len_x)*mul1+(10**(len_x//2))*mul4+mul2
		else:
			return (10**len_x)*mul1+(10**((len_x+1)//2))*mul4+mul2
	else:
		if len_y%2==0:
			return (10**len_y)*mul1+(10**(len_y//2))*mul4+mul2
		else:
			return (10**len_y)*mul1+(10**((len_y+1)//2))*mul4+mul2

print('Product of ',n1,'and',n2,'is ', int(Karatsuba(n1,n2)))
