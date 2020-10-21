
def merge(left, righ):
    
    result = []
    index_left = index_right = 0
    
    if len(left) == None:
        return righ
    
    if len(righ) == None:
        return left
    while len(result) < len(left) + len(righ):
        
        if left[index_left] <= righ[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(righ[index_right])
            index_right += 1
            
        if index_right == len(righ):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += righ[index_right:]
            break
        
    return result

def merge_sort(array):
    
    mid = len(array)//2
    
    if len(array) < 2:
        return array
    
    return merge( left=merge_sort(array[:mid]),
                 righ=merge_sort(array[mid:]))

array =  [8, 2, 6, 4, 5,56,78,2,4,67,3]

merge_sort(array)


    
    
        