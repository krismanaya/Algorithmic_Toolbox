#python2
A = map(int,raw_input.strip().split(' ')) 
B = map(int,raw_input.strip().split(' '))
n = int(input)


#Naive Algorithm for multiplying polynomail O(n^2)
#ex: A = [3,4], B = [1,2], n = 2
def multipoly(A,B,n): 
    product = (2*(n-1))*[0] # creates the size of the product
    for i in range(0,n):
        for j in range(0,n):
            product[i+j] += A[i]*B[j]
    return product #ouputs the coefficients of the product

sol = multipoly(A,B,n)
print sol

#Naive Divide and Conquer Algorithm 
#$\sum_{i=0}^{log_{2}n}4^{i}k\frac{n/2^{i}} = \theta{n^{2}}$ 
#Order \theta(n^2) still the same. 
#same example
def multipoly2(A,B,a_l,b_l,n): 
	#a_l is the first coeficcient in A 
	#b_l is the first coefiicient in B
	R = (2*(n-1))*[0]
	if n == 1: 
		R[0] = A[a_l]*B[b_l]
		return R  
	R[0:n-1] = multipoly2(A,B,n/2,a_l,b_l) #split the array
	R[n:2*n-1] = multipoly2(A,B,n/2,a_l+n/2,b_l+n/2) #split the array 
	D_0E_1 = multipoly2(A,B,n/2,a_l,b_l + n/2) #multiply A,B split
	D1_E_0 = multipoly2(A,B,n/2,a_l+n/2,b_l) #multiply A,B split
	R[n/2:n+(n/2-2)] += D_1E_0 + D_0E_1 #sum the split
	return R 

#Divide and Conquer Algorithm of order \theta(n^{1.58})




