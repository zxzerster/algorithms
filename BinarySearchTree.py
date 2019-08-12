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

    n = BinarySearchTree.Node(4)
    t.insert(n)

    n = BinarySearchTree.Node(3)
    t.insert(n)

    n = BinarySearchTree.Node(15)
    t.insert(n)

    n = BinarySearchTree.Node(11)
    t.insert(n)

    n = BinarySearchTree.Node(19)
    t.insert(n)

    n = None
    print("End") #break