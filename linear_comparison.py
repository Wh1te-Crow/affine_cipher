from fractions import gcd

def reverse_modulo(first,second):
	arr = [1,0,0,1]
	#the result is the expression (result,x,y): result = first*x+second*y
	while second!=0:
		fraction,remainder = divmod(first,second)
		first,second=second,remainder
		arr = [arr[2],arr[3],(arr[0]-fraction*arr[2]),(arr[1]-fraction*arr[3])]
	return (first,arr[0],arr[1])
'''
	ax ≡ b(mod n)
	a1*x ≡ b1 (mod n1), a = a1*d, b = b1*d, n = n1*d
'''
def solving_linear_comparisons(a,b,n):
	d= gcd(a,n)
	if (d==1):
		rezult = (reverse_modulo(a,n)[1]*b)%n
	else:
		if (b%d != 0):
			rezult = False
		else:
			
			a1, b1, n1 = a/d, b/d, n/d
			x0 = (reverse_modulo(a1,n1)[1]*b1)
			rezult = []
	
			for i in range(0,d):
				rezult.append((x0+i*n)%n)
	return rezult

#print(solving_linear_comparisons(10,7,23))
'''
a = [1,1,2,3,2,5]
a=tuple(set(a))
print(a)
'''
#print(reverse_modulo(3,26)[1])