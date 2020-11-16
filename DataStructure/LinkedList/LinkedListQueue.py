class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Node:
        #Node 
        def __init__(self,data,next):
            self.data = data #Reference to user elements
            self.next = next #Reference to next node

class LinkedQueue:
    """FIFO queue implementation using single linked list for storage """
    
    def __init__(self):
        """Create a empty queue """
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        """Return the number of elements in the queue"""
        return self.size
    
    def is_empty(self):
        """Return  true if queue is empty"""
        return self.size == 0
    
    def first(self):
        """Return the element in front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.head.data   
    
    def enqueue(self,data):
        """Add element to back of queue"""        
        newNode = Node(data,None)
        if self.is_empty():
            self.head = newNode
        else:
            self.tail.next  = newNode
        self.tail =newNode
        self.size += 1
        
    def dequeue(self):
        """Remove and return the first element"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answerd = self.head.data
        self.head = self.head.next
        self.head -= 1
        if self.is_empty():
            self.tail = None
        return answerd