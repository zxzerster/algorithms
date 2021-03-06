class BinarySearchTree:
    class Node:
        def __init__(self, val):
            self._left = None
            self._right = None
            self._val = val

    def __init__(self):
        self._root = None

    def insert(self, node):
        if node is None: return

        if self._root is None:
            self._root = node
            return

        BinarySearchTree._recursive_insert(self._root, node)
    
    def delete(self, node):
        if node is None: return

        # case 1: node doesn't have any children
        if node._left is None and node._right is None:
            p = self._parent(node)
            if p is None:
                # node is the rrot
                self._root = None
            else:
                if p._left == node: p._left = None
                else: p._right = None 
                del node
            return
        
        # case 2: node has only 1 child, no matter left or right
        if node._left is None:
            # node has only right child
            p = self._parent(node)
            if p is None:
                n = self._root
                self._root = node._right
                del n
                return
            if p._left == node:
                p._left = node._right
            else:
                p._right = node._right
            del node
            return
            
        if node._right is None:
            # node has only left child
            p = self._parent(node)
            if p is None:
                n = self._root
                self._root = node._left
                del n
                return
            if p._left == node:
                p._left = node._left
            else:
                p._right = node._left
            return

        # case 3: node has both left / right child
        
        # step 1: find successor of node, we use this successor to replace the deleted one
        s = self.successor(node)
        parent = self._parent(node)

        # step 2: because s will replace node, its right sub tree will become parent's left sub tree
        # also notice that this successor will have no left sub tree, or it won't be a successor, think about this

        # put s' right child to its parent's left first
        self._parent(s)._left = s._right

        # replace node with its successor
        s._right = node._right
        s._left = node._left

        # node's parent is None means node is root of this tree
        if parent == None:
            parent = self._root
            self._root = s
            del node
            return

        # if node isn't root, then, we need figure out like we did before, attach it to parent (left or right)
        if parent._left == node:
            parent._left = s
        else:
            parent._right = s

        del node
        return

    def root(self):
        return self._root

    def min(self, node):
        if node is None: return None

        n = node
        while n is not None:
            p = n
            n = n._left

        return p

    def max(self, node):
        if node is None: return None

        n = node
        while n is not None:
            p = n
            n = n._right

        return p

    def successor(self, node):
        if node is None: return None

        #  case 1: node is max itself, there will be no successor for max node
        # O(h) h -> height of tree
        r = self.max(self._root)
        if r == node: return None

        # case 2: node is not max node, and have right sub-tree, successor will be
        # min of right sub-tree
        # O(h)
        if node._right is not None:
            return self.min(node._right)

        # case 3: node is not max node, and doesn't have right sub-tree, successor will be
        # nearest parent whoes first sub-left child is node

        # because we don't have parent pointer in each node, we have to search the nearest "left parent"
        # from top to bottom
        # left parent -> means node is the left child of parent
        # O(h)
        n = self._root
        while n is not node:
            if node._val < n._val:
                lp = n
                n = n._left
            else:
                n = n._right

        return lp

    # O(h)
    def predecessor(self, node):
        if node is None: return None

        # case 1: if node is minimum node, there will be no predecessor
        # O(h) h -> height of tree
        r = self.min(self._root)
        if r == node: return None

        # case 2: if node isn't minimum node, and has left sub-tree, predecessor will be
        # max of left sub-tree
        # O(h)
        if node._left is not None:
            return self.max(node._left)

        # case 3: if node isn't minimum node, and doesn't have left sub-tree, predecessor will be
        # nearest right parent whoese first right sub-right left is node
        # right parent -> means node is the right child of parent
        # O(h)
        n = self._root
        while n is not node:
            if node._val < n._val:
                n = n._left
            else:
                rp = n
                n = n._right

        return rp

    def breadthFirstTraversal(self, cb=None):
        from collections import deque

        if self._root is None: return

        q = deque()
        q.appendleft(self._root)

        while len(q) > 0:
            n = q.pop()
            if n._left is not None:
                q.appendleft(n._left)
            if n._right is not None:
                q.appendleft(n._right)

            if cb is not None:
                cb(n)

    def depthFirstTraversal(self, cb=None):
        BinarySearchTree._depthFirstTraversal(self._root, cb)

    def _parent(self, node):
        if node is None: return None

        n = self._root
        p = None
        while n is not node:
            if n == node: break

            p = n
            if node._val < n._val:
                n = n._left
            else:
                n = n._right

        return p

    @staticmethod
    def _depthFirstTraversal(node, cb=None):
        if node is None: return

        if node._left is not None:
            BinarySearchTree._depthFirstTraversal(node._left, cb)

        if node._right is not None:
            BinarySearchTree._depthFirstTraversal(node._right, cb)

        if cb is not None:
            cb(node)

    @staticmethod
    def _recursive_insert(root, node):
        if node._val < root._val:
            if root._left is not None:
                BinarySearchTree._recursive_insert(root._left, node)
            else:
                root._left = node
        else:
            if root._right is not None:
                BinarySearchTree._recursive_insert(root._right, node)
            else:
                root._right = node

    @staticmethod
    def _iteraitve_insert(root, node):
        n = root
        p = n

        while n is not None:
            p = n
            if node._val < n._val:
                n = n._left
            else:
                n = n._right

        # Find insertion place, do insertion
        if node._val < p._val:
            p._left = node
        else:
            p._right = node


if __name__ == "__main__":
    print("Test BinarySearchTree")

    print("#" * 10 + " Insert / Search / Delete " + "#" * 10)
    t = BinarySearchTree()

    n = BinarySearchTree.Node(8)
    t.insert(n)
    n8 = n

    n = BinarySearchTree.Node(4)
    t.insert(n)
    n4 = n

    n = BinarySearchTree.Node(3)
    t.insert(n)
    n3 = n

    n = BinarySearchTree.Node(15)
    t.insert(n)
    n15 = n

    n = BinarySearchTree.Node(11)
    t.insert(n)
    n11 = n

    n = BinarySearchTree.Node(19)
    t.insert(n)
    n19 = n

    n = BinarySearchTree.Node(13)
    t.insert(n)
    n13 = n

    n = BinarySearchTree.Node(17)
    t.insert(n)
    n17 = n

    n = BinarySearchTree.Node(23)
    t.insert(n)
    n23 = n

    print("#" * 10 + " Min / Max " + "#" * 10)
    m1 = t.min(t.root())
    m2 = t.max(t.root())

    assert(m1._val == 3)
    assert(m2._val == 23)

    m1 = None
    m2 = None

    print("#" * 10 + " Successor / Predecessor " + "#" * 10)
    # case 1: max node donesn't have a successor
    s = t.successor(n23)
    p = t.predecessor(n3)
    assert(s is None)
    assert(p is None)
    # case 2: node has right sub-tree
    s = t.successor(n15)
    p = t.predecessor(n8)
    assert(s._val == 17)
    assert(p._val == 4)

    # case 3: node only has left sub-tree
    s = t.successor(n4)
    p = t.predecessor(n11)
    assert(s._val == 8)
    assert(p._val == 8)

    print("#" * 10 + " Delete (standalone) " + "#" * 10)

    print("#" * 10 + " Traversal (breadthfirst / depthfirst) " + "#" * 10)
    t.breadthFirstTraversal()

    del m1
    del m2
    del n
    del n8
    del n4
    del n3
    del n15
    del n11
    del n19
    del n13
    del n17
    del n23
    print("End") #break