#python2
import sys 

a,b = map(int,raw_input().split())
"""given two integers a,b compute the lcm(a,b)"""
def gcd(a,b):
    if b == 0: 
        return a
    a_prime = a % b 
    return gcd(b,a_prime)

def lcd(a,b): 
    return (a*b)/gcd(a,b)

sol = lcd(a,b)
print sol