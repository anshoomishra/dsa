# Min heap Implementation 
from typing import List


def buildheap(arr,i,n):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        buildheap(arr,smallest,n)
    
    
def extract_min(arr:List):
    m = arr[0]
    arr[0] = arr[len(arr)-1]
    
    arr.remove(arr[len(arr)-1])
    buildheap(arr,0,len(arr))
    return m

def decrease_key(arr,i,key):
    
    pass
        

if __name__ == "__main__":
    arr = [10,9,1,2,3,4,11,12,5,6]
    n = len(arr)
    
    for i in range((n//2)-1,-1,-1):
        buildheap(arr,i,len(arr))
    
    print(arr)  
    m = extract_min(arr)
    print(m)
    print(arr) 
    m = extract_min(arr)
    print(m)
    print(arr) 
    m = extract_min(arr)
    print(m)
    print(arr) 
    m = extract_min(arr)
    print(m)
    print(arr) 
    pass

# import collections
# print(dir(collections))