def Insertion_sort(array):
    
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key
    
    return print(array)
        
array =  [8, 2, 6, 4, 5,56,78,2,4,67,3]

Insertion_sort(array)
            
        