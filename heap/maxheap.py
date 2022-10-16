# Min heap Implementation 
def buildheap(arr,i,n):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        buildheap(arr,largest,n)
    
    

        

if __name__ == "__main__":
    arr = [10,9,1,2,3,4,11,12,5,6]
    n = len(arr)
    print(len(arr))
    for i in range((n//2)-1,-1,-1):
        buildheap(arr,i,len(arr))
    print(arr)   
    pass
