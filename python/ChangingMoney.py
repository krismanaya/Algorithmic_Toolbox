#python 2
import sys 

m = input()

def ChangingMoney(m):
    """count the number of 10s,5s and 1s it takes sum m"""
    loop = True
    count = 0 
    while loop:
        if m >= 10: 
            m -= 10 
            count += 1
        elif m >= 5: 
            m -= 5 
            count += 1
        elif m >= 1: 
            m -= 1
            count += 1
        else: 
            loop = False
    return count
    

sol = ChangingMoney(m)
print sol 
    

    
