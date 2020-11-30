class Tree:
    """Abstract base class representation a tree structure"""
    
    class Position:
        """An abstraction representing the location of a single element"""
        
        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            """Return if other position represent the same location"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self,other):
            """Return true if other does not represent the same location"""
            return not (self == other)
        
        def root(self):
            """Return position representing the tree root (or None if is empty)"""
            raise NotImplementedError('must be implemented by subclass')
        
        def parents(self, p):
            """Return the position representing p parents (or None if is empty)"""
            raise NotImplementedError('must be implemented by subclass')
        
        def num_childrens(self, p):
            """Return the number of children that position p"""
            raise NotImplementedError('must be implemented by subclass')
        
        def children(self, p):
            """Generate a iteration of position representing p children"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __len__(self):
            """Return the total number of elements in the tree"""
            raise NotImplementedError('must be implemented by subclass')
            
        def is_root(self, p):
            """Return true if position p represent the root tree """
            return self.root() == 0
        
        def is_leap(self, p):
            """Return true if position p does not have any children"""
            return self.num_childrens(p) == 0
        
        def is_empty(self):
            """Return true if tree is empty"""
            return len(self) == 0
        
        def depht(self, p):
            """Return the number of levels separating position p from the root"""
            if self.is_root(p):
                return 0
            else:
                return 1 + self.depht(self.parents(p))
        
        def _height(self,p):
            """Return the height of the subtree rooted at position p"""
            if self.is_leap():
                return 0
            else:
                return 1 + max(self._height(c) for c in self.children(p))