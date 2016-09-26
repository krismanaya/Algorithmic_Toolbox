# Uses python3
import sys

def binary_search(a,x,low=0,high=None):
     high = len(a)-1 if high is None else high
     if high < low: 
         return - 1 
     mid = low + (high-low)//2
     if x == a[mid]:
         return mid
     elif x < a[mid]: 
         return binary_search(a,x,low,mid-1)
     else: 
         return binary_search(a,x,mid+1,high)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x),end = ' ')


def binary_search(arr,key,low=0,high=None):
     high = len(arr)-1 if high is None else high
     if high < low: 
         return - 1 
     mid = low + (high-low)//2
     if key == arr[mid]:
         return mid
     elif key < arr[mid]: 
         return binary_search(arr,key,low,mid-1)
     else: 
         return binary_search(arr,key,mid+1,high)

