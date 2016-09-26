#python2 
import sys

a, b = map(int, raw_input().split())
"""compute the gcd of a,b >= 0 using Euclid's algorithm"""
def gcd(a,b): 
	if b == 0: 
		return a
	a_prime = a % b
	return gcd(b,a_prime)
sol = gcd(a,b)
print sol 
