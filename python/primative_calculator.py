#python2 
import sys 


n = int(input())

d = {}
count = 0 
def prim_calc(n): 
    if n == 1: 
        return 1,-1
    if d.get(n) is not None: 
        return d[n]
    ans = (prim_calc(n-1)[0]+1,n-1)
    
    if n % 2 == 0: 
        ret = prim_calc(n//2)
        if ans[0] > ret[0]:
            ans = (ret[0]+1, n//2)
    
    if n%3 == 0: 
        ret = prim_calc(n//3)
        if ans[0] > ret[0]: 
            ans = (ret[0]+1,n//3)
    
    d[n] = ans
    return ans

def print_solution(n):
    ans = []
    while prim_calc(n)[1] != -1: 
        ans.append(n)
        n = prim_calc(n)[1]
    ans.append(1)
    ans.reverse()
    print len(ans) - 1
    for x in ans:
        print x,

def solve(n):
    if n == 1: 
        print n-1 
        print n 
    else:  
        for i in range(1,n): 
            prim_calc(i)[0]
        print_solution(n)
        

 
solve(n)


