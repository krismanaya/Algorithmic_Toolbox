#python2
import random
import partition 


def randomize_quick_sort(arr,l=0,r=None): 
	r = len(arr) - 1 if r is None else r
	if l >= r: 
		return None 
	else: 
		k = random.randit(l,r)
		arr[l],arr[k] = arr[k],arr[l]
		m = partition(arr,l,r) 
		randomize_quick_sort(arr,l,m-1)
		randomize_quick_sort(arr,m+1,r)
