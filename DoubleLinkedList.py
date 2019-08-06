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

if __name__ == "__main__":
    print("Test DoubleLinkedList")
    
    l = DoubleLinkedList()
    
    print("#" * 10 + " Insert / Search / Delete " + "#" * 10)
    n = DoubleLinkedList.Node(2)
    l.insert(n)
    
    n = DoubleLinkedList.Node(1)
    l.insert(n)
    
    n = DoubleLinkedList.Node(0)
    l.insert(n)
    
    n = None
    print("End") 