
def linear(array,value):
    
    for index,element in enumerate(array):
        if element == value:
            return print(f'Item found in the index {index}, the value is {element}')
    return None

        

data = [1,45,46,42,56]

linear(data , 46)