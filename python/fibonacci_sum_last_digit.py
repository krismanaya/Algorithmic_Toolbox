#python 2

import sys

n = int(input())
"""this function is too slow."""
def sum_fibonnaci(n): 
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        F = (n+1) * [0]
        F[0] = 0
        F[1] = 1
        for i in range(2,n+1):
            F[i] = F[i-1] + F[i-2]
        return sum(F)

def sum_last_digit(n):
    if n < 4: 
        return sum_fibonnaci(n)
    else: 
        return sum_fibonnaci(n) % 10

sol = sum_last_digit(n)
print sol