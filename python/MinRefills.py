#python 2


def MinRefills(x,n,L):
    """x = array A = x_0 <= x_2 <=  ... <= x_n <= x_n+1 = B
    n = x_n position in the array 
    L = distance car can travel without refuiling""" 
    
    numRefills = 0 
    currentRefills = 0 
    while currentRefills <= n: 
        lastRefill = currentRefills
        while (currentRefills <= n and x[currentRefills + 1] - x[lastRefill] <= L): 
            currentRefills +=1
        if currentRefills <= n: 
            numRefills +=1
        print numRefills
        if currentRefills == lastRefill: 
            return "IMPOSSIBLE"
    return numRefills
