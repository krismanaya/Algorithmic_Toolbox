#python2 
import sys 

n,W = map(int, raw_input().strip().split(' '))
weights = []
v = []
w = []
for i in range(n): 
	v_i,w_i = map(int, raw_input().strip().split(' '))
	v.append(v_i)
	w.append(w_i)

def fractional_knapsack(W,v,w,n):
	A = n*[0]
	V = 0 
	i = 0
	weights = []
	for j in range(0,n): 
		weights.append(v[j]/w[j])
		weight = sorted(weights)
	if n == 1: 
		while i < n:
			if W == 0: 
				return round(V,4)
			b = min(w[i],W)
			V = V + b*(v[0]/float(w[0]))
			w[i] = w[i] - b
			A[i] = A[i] + b 
			W = W - b 
			i+=1 
		return round(V,4)
	else: 
		while i < n:
			a = min(w[j],W)
			if W == 0: 
				return round(V,4)
			V = V + a*(weight[-(i+1)]) 
			w[i] = w[i] - a
			A[i] = A[i] + a 
			W = W - a
			i += 1 
	return round(V,4)

sol = fractional_knapsack(W,v,w,n)
print sol

