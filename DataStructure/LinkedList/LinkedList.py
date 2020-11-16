class Node:
    #Create a node
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SimpleSingleList():
    #Create a simple single list
    def __init__(self) :
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        #Append an item to list
        node = Node(data)          
        
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1
    
    def size(self):
         #Get the size of the list
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count
    
    def iter(self):
        # Iterate through the list.
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    
    def delete(self, data):
        #Delete a node from the list 
        current = self.tail
        prev = self.tail
        
        while current:
            if current.data == data:
                if  current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
            prev = current .next
            current = current.next
    
    def search(self, data):
        #Search through the list. Return True if data is found, otherwise False. 
        for node in self.iter():
            if data == node:
                return True
        return False
    
    def clear(self):
        #Clear the entire list
        self.tail = None
        self.head = None
        
