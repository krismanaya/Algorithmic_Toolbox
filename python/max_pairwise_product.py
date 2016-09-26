#python2 
import sys 
"""Compute the maximum pairwise product."""
n = input()
arr = map(int,raw_input().split())

def max_pairwise_product(arr): 
	new_arr = sorted(arr)
	return new_arr[-1]*new_arr[-2]

sol = max_pairwise_product(arr)
print sol 