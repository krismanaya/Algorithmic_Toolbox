#python 2 

arr = map(float,raw_input().strip().split(' '))

def PointsCoverSorted(arr): 
	"""organize partions into groups at unit length."""
	R = set()
	i = 0 
	while i < len(arr):  
		[l,r] = [arr[i],arr[i] + 1]
		 R.update([l,r])
		i += 1
		while i < len(arr) and arr[i] < r: 
			i += 1 
	return R

sol = PointsCoverSorted(arr)
print sol 