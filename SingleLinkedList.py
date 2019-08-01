class SingleLinkedList(object):
    class Node(object):
        def __init__(self, val):
            self._val = val
            self._next = None
    
    def __init__(self):
        self._head = SingleLinkedList.Node(None)

    def insert(self, node):
        node._next = self._head._next
        self._head._next = node
    
    def search(self, val):
        def _iterative_search(node, val):
            if node is None: return None
            n = node
            while n is not None:
                if n._val == val: return n
                n = n._next
            
            return None
        
        def _recursive_search(node, val):
            if node is None: return None
            
            if node._val == val: return node
            return _recursive_search(node._next, val)
        
        ni = _iterative_search(self._head._next, val)
        nr = _recursive_search(self._head._next, val)

        assert(ni == nr)
        return ni

    def delete(self, node):
        if node is None: return

        n = self._head
        while n is not None:
            if n._next == node: break
            n = n._next
        
        if n is None: return
        
        n._next = node._next
        node._next = None
        del node

if __name__ == "__main__":
    print("Testing SingleLinkedList")

    print("#" * 10 + " Insert / Search / Delete " + "#" * 10)

    l = SingleLinkedList()
    
    n = SingleLinkedList.Node(3)
    l.insert(n)
    
    n = SingleLinkedList.Node(2)
    l.insert(n)
    
    n = SingleLinkedList.Node(1)
    l.insert(n)
    
    n = SingleLinkedList.Node(0)
    l.insert(n)

    n2 = l.search(2)
    assert(n is not None)
    
    n0 = l.search(0)
    assert(n is not None)
    
    n3 = l.search(3)
    assert(n is not None)
    
    l.delete(n2)
    l.delete(n0)
    l.delete(n3)