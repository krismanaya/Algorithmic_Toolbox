#python2
import sys

arr = map(int,raw_input().strip().split(' '))

"""prints the largest number in a list."""

def largest_number(list): 
    app = []
    count = len(list)
    while count > 0: 
        maximum = max(list)
        app.append(maximum)
        list.remove(maximum)
        count -= 1
    return app

sol = largest_number(arr)
for x in sol: 
	print x,
