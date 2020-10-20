

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return print(array)


array =  [8, 2, 6, 4, 5,56,78,2,4,67,3]

bubble_sort(array)
    