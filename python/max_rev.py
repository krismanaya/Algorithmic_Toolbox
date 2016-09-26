#python2
import sys 

n = input() 
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' ')) 


def max_rev(a,b,n): 
	sum_max_rev = []
	count = 0 
	while count < n:
		if n == 1: 
			return a[0]*b[0]
		else:
			max_a = max(a)
			max_b = max(b)
			sum_max_rev.append((max_a*max_b))
			a.remove(max_a)
			b.remove(max_b)
			count += 1
	return sum(sum_max_rev)

sol = max_rev(a,b,n)
print sol 