def partition(arr,m,n):
    i = m-1

    for j in range(m,n):
        if arr[j] <= arr[n]:
            i+=1
            
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[n] = arr[n],arr[i+1]
    return i+1


def quick_sort(arr,low,high):
    if low < high:
        partion_index = partition(arr,low,high)

        quick_sort(arr,low,partion_index-1)
        quick_sort(arr,partion_index+1,high)

if __name__ == "__main__":

    arr = [10,11,9,8,7,12,2,3,6,7,4,1,5]
    quick_sort(arr,0,len(arr)-1)
    print(arr)
    
