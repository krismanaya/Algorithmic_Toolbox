#python2

import sys

"""add two integers. Test function"""
def aplusb(a,b): 
	return a+b 
a, b = map(int, raw_input().split())
solution = aplusb(a,b)

print solution
