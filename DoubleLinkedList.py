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

    def reverse(self):
        def _iterative_reverse(head):
            if head is None: return

            p = head._next
            q = p._next
            while p is not None:
                # Reverse node (node is not first one or last one)
                # Reverse first should also set its *new next* to be None which previously point to head node
                # Reverse last one should also set it "new prev" to point to head which previouly point to None
                p._next, p._prev = p._prev, p._next
                # First one become last one
                if p._next == head: p._next = None

                if q is not None:
                    p = q
                    q = q._next
                else:
                    # Last one now is pointed by head
                    p._prev = head
                    head._next = p
                    break

        def _recursive_reverse(head):
            def __reverse_traversal(node, cb):
                if node is None:
                    return
                __reverse_traversal(node._next, cb)
                cb(node)

            def __swapDoubleLinkedNode(node):
                # First node, update its prev to be None, because after reversing, this is the last node in list
                if node._prev == head: node._prev = None
                # Last node, update its next (will be prev after reversing) to point to head
                if node._next == None:
                    node._next = head
                    head._next = node
                # Reversing nodes in the middle is easy
                node._prev, node._next = node._next, node._prev

            __reverse_traversal(self._head, __swapDoubleLinkedNode)

        # _iterative_reverse(self._head)
        _recursive_reverse(self._head)

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

    # l.delete(n0)
    # l.delete(n2)
    # l.delete(n3)
    # l.delete(n4)

    # n1 = l.search(1)
    # print(n1._val)

    # n4 = l.search(4)
    # print(n4)

    # l.delete(n2)
    # l.delete(n3)

    print("#" * 10 + " Reverse list " + "#" * 10)
    l.reverse()

    n = None
    print("End")