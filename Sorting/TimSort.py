from Merge_sort import merge


def insert_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    
    for i in range(left + 1, right + 1):
       
        key_item = array[i]
        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array



def timSort(array):
    min_run = 32
    n = len(array)
    
    for i in range(0,n,min_run):
        insert_sort(array,i,min((i + min_run -1),n - 1))
        size = min_run
        
        while size < n:
            for start in range(0,n,size * 2):
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n-1))
                
                merged_array = merge(
                    left=array[start:midpoint + 1],
                    right=array[midpoint + 1:end + 1])
                array[start:start + len(merged_array)] = merged_array
            size *= 2
    return array


array =  [8, 2, 6, 4, 5,56,78,2,4,67,3]

print(timSort(array))