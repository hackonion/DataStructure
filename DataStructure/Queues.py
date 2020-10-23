class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class queues():
    def_capacity = 10 #Define the capacity for new queues
    
    
    def __init__(self):    
        """ Created empty queues """
        self.data = [None] * queues.def_capacity
        self.size = 0
        self.front = 0
        
    def __len__(self):
        """ Return size of queues """
        return self.size
    
    def is_empty(self):
        """ Return true is queues is empty """
        return self.size == 0
    
    def first(self):
        """ Return the element in front of queues """
        if self.is_empty():
            raise Empty("Is empty")
        return self.data[self.front]
    
    def dequeue(self):
        """ Return and remove the first element of queues """
        if self.is_empty():
            raise Empty('Is empty')
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value
    
    def enqueue(self,item):
        """ Add elements to back of queue."""
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self._front + self.size) % len(self.data)
        self.data[avail] = item
        self.size += 1
    
    def resize(self,cap):
        """ Resize to the capacity of queue. """
        old = self.data = [None] * cap
        walk = self.front
        
        for k in range(self.resize):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0
    
    