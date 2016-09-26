#python2

import sys 

n = int(input())

"""return the nth fibonacci number."""
def fibonacci(n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1
    else: 
        F = (n+1)*[0]
        F[0] = 0 
        F[1] = 1
        for i in range(2,n+1): 
            F[i] = F[i-1] + F[i-2]
            F.append(F[i])
        return F[-1]

sol = fibonacci(n) 
print sol



    
