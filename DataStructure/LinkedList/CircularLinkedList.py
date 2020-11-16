class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Node:
    #Node 
        def __init__(self,data,next):
            self.data = data #Reference to user elements
            self.next = next #Reference to next node

class CircularQueue:
    
    def __init__(self) :
        """Empty queue"""
        self.tail = None
        self.size = 0
    
    def __len__(self):
        """Return the number of elements in queue"""
        return self.size
    
    def is_empty(self):
        """Return true if the queue is empty"""
        return self.size == 0
    
    def first(self):
        """Return the element in front of queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self.tail.next 
        return head.data
    
    def dequeue(self):
        """Remove and return the first element in the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        old_head = self.tail.next 
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = old_head.next 
        self.size -= 1
        return old_head.data 
    
    def enqueue(self,data):
        """Add a element in back of the queue"""
        newNode = Node(data,None)
        if self.is_empty():
            newNode.next = newNode 
        else:
            newNode.next = self.tail.next 
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1
        
    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self.size > 0:
            self.tail = self.tail.next 
            
            
s = CircularQueue()

s.enqueue(1)
s.enqueue(2)
s.rotate()
