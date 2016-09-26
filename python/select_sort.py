#pyhon2 

arr = map(int,raw_input.strip().split(' ')) 

#Selection Sort: 
#ex arr = [8,4,2,5,2]
#greedy method
def select_sort(arr): 
	n = len(arr)
	new_arr = []
	count = 0 
	while count < n: 
		min_num = min(arr)
		new_arr.append(min_num)
		arr.remove(min_num)
		count += 1 
	return new_arr
sol = select_sort(arr)
print sol 

#Selection Sort: 
#ex arr = [8,4,2,5,2]
#running time O(n^2)
def select_sort_swap(arr):
	n = len(arr) 
	for i in range(0,n): 
		minIndex = i
		for j in range(i+1,n): 
			if arr[j] < arr[minIndex]: 
				minIndex = j
		arr[i],arr[minIndex] = arr[minIndex],arr[i]
	return arr 
sol = selec_sort_swap(arr)
print sol


def merge_sort(arr): 
	pass 