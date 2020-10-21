from random import randint

def QuickSort(array):
    
    if len(array) < 2:
        return array
    
    low, same, hight = [],[],[]
    
    pivot = array[randint(0, len(array) - 1)]
    
    
    
    for i in array:
        
        if i < pivot:
            low.append(i)
        if i == pivot:
            same.append(i)
        if  i > pivot:
            hight.append(i)
        
    return QuickSort(low) + same + QuickSort(hight)



array =  [8, 2, 6, 4, 5,56,78,2,4,67,3]

print(QuickSort(array))