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

    def __len__(self):
        def _iterative_len(node):
            if node is None: return 0

            n = node
            l = 0
            while n is not None:
                n = n._next
                l += 1

            return l

        def _recursive_len(node):
            if node is None: return 0

            return 1 + _recursive_len(node._next)

        l1 = _iterative_len(self._head._next)
        l2 = _recursive_len(self._head._next)
        assert(l2 == l1)

        return l1
    
    def indexOf(self, index):
        def _iterative_indexOf(node, index):
            if index < 0: return None
            
            n = node
            i = 0
            while n is not None and i < index:
                n = n._next
                i += 1
            
            if n is None and i < index: return None

            return n
        
        def _recursive_indexOf(node, index):
            if node is None: return None
            if index == 0: return node

            return _recursive_indexOf(node._next, index - 1)
             
        
        ni = _iterative_indexOf(self._head._next, index)
        nr = _recursive_indexOf(self._head._next, index)
        assert(ni == nr)

        return nr

    def middle(self):
        p = self._head._next
        q = p

        while q is not None and q._next is not None:
            q = q._next._next
            p = p._next

        return p


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

    print(len(l))

    print("#" * 10 + " Middle of List " + "#" * 10)
    m = l.middle()
    assert m._val == 2