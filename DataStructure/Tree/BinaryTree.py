from DataStructure.Tree.GeneralTree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    def left(self, p):
        """Return a position representing p's left child
           return None if p does not have a left child"""

        raise NotImplementedError('must be implement by subclass')

    def right(self, p):
        """Return a position representing p right child.
           return None if p not have a right child.
        """

        raise NotImplementedError('must be implement by subclass')

    def sibling(self, p):
        """Return a position representing p sibling (or None if no sibling)"""
        parent = self.parent(p)

        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self,p):
        """Generate an iteration of positions representing p children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)