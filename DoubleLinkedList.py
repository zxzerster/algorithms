class DoubleLinkedList(object):
    class Node(object):
        def __init__(self, val):
            self._val = val
            self._prev = None
            self._next = None
    
    def __init__(self):
        self._head = DoubleLinkedList.Node(None)
    
    def insert(self, node):
        if node is None: return
        
        node._prev = self._head
        node._next = self._head._next
        self._head._next = node
        if node._next is not None:
            node._next._prev = node

    def delete(self, node):
        if node is None: return
        if node._next is None and node._prev is None: return

        node._prev._next = node._next
        if node._next is not None:
            node._next._prev = node._prev
        node._next = None
        node._prev = None
        del node._val

    def search(self, val):
        n = self._head._next
        while n is not None:
            if n._val == val: return n
            n = n._next

        return None

if __name__ == "__main__":
    print("Test DoubleLinkedList")

    l = DoubleLinkedList()

    print("#" * 10 + " Insert / Search / Delete " + "#" * 10)
    n = DoubleLinkedList.Node(4)
    l.insert(n)
    n4 = n

    n = DoubleLinkedList.Node(3)
    l.insert(n)
    n3 = n

    n = DoubleLinkedList.Node(2)
    l.insert(n)
    n2 = n

    n = DoubleLinkedList.Node(1)
    l.insert(n)

    n = DoubleLinkedList.Node(0)
    l.insert(n)
    n0 = n

    l.delete(n0)
    l.delete(n2)
    l.delete(n3)
    l.delete(n4)

    n1 = l.search(1)
    print(n1._val)

    n4 = l.search(4)
    print(n4)

    l.delete(n2)
    l.delete(n3)

    n = None
    print("End")