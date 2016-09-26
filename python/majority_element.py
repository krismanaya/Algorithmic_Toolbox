#python2 
import sys
n = int(input())
arr = map(int,raw_input().strip().split(' '))


def majority_element_naive(arr,n):
    arr_n = sorted(arr)
    for i in range(0,len(arr_n)-1): 
        if arr.count(arr[i]) > n // 2: 
            return 1
    return 0 

def majority_element(arr,low=0,high=None):
    new_arr = sorted(arr)
    high = len(arr)-1 if high is None else high
    mid = (low+high)/2
    while low <= high:
        mid = (low+high)/2
        if new_arr.count(new_arr[low]) > len(arr)/2: 
            return 1 
        if new_arr.count(new_arr[high]) > len(arr)/2: 
            return 1
        else: 
            low+=mid
            high-=mid
    return 0

sol = majority_element(arr)
print sol