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

    def hasLoop(self):
        def _hashable_loop_detector(node):
            nodes = set()

            while node is not None:
                if node in nodes: return True

                nodes.add(node)
                node = node._next

            return False

        def _iterative_loop_detector(node):
            p = node
            q = node

            while q is not None and q._next is not None:
                q = q._next._next
                p = p._next

                if p == q: return True

            return False

        loop1 = _hashable_loop_detector(self._head._next)
        loop2 = _iterative_loop_detector(self._head._next)

        assert(loop1 == loop2)
        return loop2

    def loopLength(self):
        def _iterative_loop_detector(node):
            p = node
            q = node

            while q is not None and q._next is not None:
                q = q._next._next
                p = p._next

                if p == q: return p

            return None

        p = _iterative_loop_detector(self._head._next)
        q = p
        len = 0
        while p is not None:
            p = p._next
            len += 1
            if p == q: return len

        return None

    def isPalindrome(self):
        from collections import deque
        stack = deque()

        n = self._head._next
        while n is not None:
            stack.append(n)
            n = n._next

        n = self._head._next
        while n is not None:
            p = stack.pop()
            if p._val != n._val: return False
            n = n._next

        return True

    def swap(self, node1, node2):
        if node1 is None or node2 is None: return
        if node1 == node2: return

        def _prevNode(head, node):
            p = head
            while p._next is not None:
                if p._next == node: return p
                p = p._next

        p1 = _prevNode(self._head, node1)
        p2 = _prevNode(self._head, node2)
        if node1._next != node2 and node2._next != node1:
            p1._next = node1._next
            p2._next = node2._next

            node2._next = p1._next
            p1._next = node2
            node1._next = p2._next
            p2._next = node1
        else:
            if node1._next == node2:
                node1._next = node2._next
                p1._next = node2
                node2._next = node1
                return
            if node2._next == node1:
                node2._next = node1._next
                p2._next = node1
                node1._next = node2
                return

if __name__ == "__main__":
    print("Testing SingleLinkedList")

    print("#" * 10 + " Insert / Search / Delete " + "#" * 10)

    l = SingleLinkedList()

    n = SingleLinkedList.Node(4)
    l.insert(n)
    n4 = n
    
    n = SingleLinkedList.Node(3)
    l.insert(n)
    
    n = SingleLinkedList.Node(2)
    l.insert(n)
    n2 = n
    
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
    
    # l.delete(n2)
    # l.delete(n0)
    # l.delete(n3)

    print(len(l))

    print("#" * 10 + " Middle of List " + "#" * 10)
    m = l.middle()
    print(m._val)
    assert m._val == 2

    print("#" * 10 + " Loop detects " + "#" * 10)
    looped1 = l.hasLoop()
    l1 = l.loopLength()

    n4._next = n2
    # n = None
    # n4 = None
    # n2 = None

    looped2 = l.hasLoop()
    l2 = l.loopLength()

    assert(looped1 == False)
    assert(l1 is None)
    assert(looped2 == True)
    assert(l2 == 3)

    print("#" * 10 + " Palindrome detector " + "#" * 10)
    pl = SingleLinkedList()

    n = SingleLinkedList.Node(4)
    pl.insert(n)

    n = SingleLinkedList.Node(3)
    pl.insert(n)

    n = SingleLinkedList.Node(2)
    pl.insert(n)

    n = SingleLinkedList.Node(1)
    pl.insert(n)

    n = SingleLinkedList.Node(2)
    pl.insert(n)

    n = SingleLinkedList.Node(3)
    pl.insert(n)

    n = SingleLinkedList.Node(4)
    pl.insert(n)

    palindrome1 = pl.isPalindrome()
    n4._next = None
    n4 = None
    n2 = None
    palindrome2 = l.isPalindrome()

    print("palindrome1: %r,  palindrome2: %r" % (palindrome1, palindrome2))
    assert(palindrome1)
    assert(palindrome2 is False)

    print("#" * 10 + " Swap nodes " + "#" * 10)
    pl1 = SingleLinkedList()

    n = SingleLinkedList.Node(4)
    pl1.insert(n)

    n = SingleLinkedList.Node(3)
    pl1.insert(n)
    n3 = n

    n = SingleLinkedList.Node(2)
    pl1.insert(n)
    n2 = n

    n = SingleLinkedList.Node(1)
    pl1.insert(n)
    n1 = n

    n = SingleLinkedList.Node(2)
    pl1.insert(n)

    n = SingleLinkedList.Node(3)
    pl1.insert(n)

    n = SingleLinkedList.Node(4)
    pl1.insert(n)

    # swap two continues nodes
    pl1.swap(n3, n2)

    # swap two same nodes
    # pl1.swap(n3, n3)

    # swap two seperate nodes
    # pl1.swap(n3, n1)
    print("Check swap nodes result on python Tutor!")

    print("End")