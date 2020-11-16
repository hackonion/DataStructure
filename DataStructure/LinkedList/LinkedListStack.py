class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Node:
    #Node 
        def __init__(self,data,next):
            self.data = data #Reference to user elements
            self.next = next #Reference to next node
    
class LinkedStack:
    """LIFO implementation using single linked list"""
    def __init__(self):
        self.head = None #Reference to head node
        self.size = 0 #Number of stack elements
        
    def __len__(self):
        """Return number of elements"""
        return self.size
    
    def is_empty(self):
        """Return true is stack is empty"""
        return self.size == 0
    
    def push(self, item):
        """ Add elementi in the top of the stack"""
        node = Node(item,self.head)
        self.head = node
        self.size += 1
        
    def top(self):
        """Return element at the top of stack but don't removed"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.head.data
    
    def pop(self):
        """Return element at the top of stack and remove"""
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self.head.data
        self.size -= 1
        return answer
    
    
        
        

s = LinkedStack()

s.push(1)
s.push(2)
s.push(3)
        