#python2 

arr = map(int,raw_input().strip().split(' ')) 

def partition(arr,l=0,r=None): 
	r = len(arr)-1 if r is None else r
	x = arr[l]
	j = l 
	for i in range(l+1,r): 
		if arr[i] <= x: 
			j += 1
			arr[j],arr[i] = arr[i],arr[j]
	arr[l],arr[j] = arr[j],arr[l]
	return j

sol = partition(arr)
print sol
