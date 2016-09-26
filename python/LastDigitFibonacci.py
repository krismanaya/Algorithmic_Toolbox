#python2
import sys 

n = int(input())

def last_digit_fib(n): 
	"""compute the last digit of the nth fibonacci term."""
	if n == 0: 
		return 0
	if n == 1: 
		return 1
	else: 
		F = (n+1)*[0]
		F[0] = 0
		F[1] = 1
		for i in range(2,n+1): 
			F[i] = (F[i-1] + F[i-2]) % 10 
			F.append(F[i])
		return F[-1]

sol = last_digit_fib(n)
print sol 