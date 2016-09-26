#python2
import partition

arr = map(int,raw_input().strip().split(' '))

def quick_sort(arr,l=0,r=None): 
	r = len(arr)-1 if r is None else r
	if l >= r: 
		return None
	else: 
		m = partion(arr,l,r)
		quick_sort(arr,l,m-1)
		quick_sort(arr,m+1,r)

sol = quick_sort(arr)
print sol