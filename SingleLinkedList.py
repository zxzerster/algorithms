class SingleLinkedList(object):
    class Node(object):
        def __init__(self, val):
            self._val = val
            self._next = None
    
    def __init__(self):
        self._head = SingleLinkedList.Node(None)

if __name__ == "__main__":
    print("Testing SingleLinkedList")