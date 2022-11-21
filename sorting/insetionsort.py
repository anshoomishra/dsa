def insertion_sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j-1
        
        while key < array[i] and i >= 0:
            array[i+1] = array[i]
            i-=1
        array[i+1] = key
    return array


if __name__ == "__main__":
    array = [4,3,2,1,5,6,7]
    print(insertion_sort(array))
    
