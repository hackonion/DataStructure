class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    
    """Created empty stack"""
    def __init__(self):

        self.data = []
        
    def __len__(self):
        """Return the number of elements"""
        return len(self.data)
    
    def is_empty(self):
        """Return True  if stack is empty"""
        return len(self.data) == 0
    
    def push(self,x):
        """Add element x to the top of stack"""
        self.data.append(x)
    
    def top(self):
        """ Return the element at the top of the stack."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]
    
    def pop(self):
        """ Remove and return the element from the top of the stack."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop() #Remove last item from list
    

    