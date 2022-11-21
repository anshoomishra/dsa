def selection_sort(array):
    for i in range(len(array)):
        mn_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[mn_index]:
                mn_index = j
        array[i],array[mn_index] = array[mn_index],array[i]
    return array

if __name__ == "__main__":
    array = [4,3,2,1,5,6,7]
    print(selection_sort(array))