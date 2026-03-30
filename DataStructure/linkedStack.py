class LinkedStack:
    class _Node:
        def __init__(self, val=None, next:object=None):
            self.value  = val
            self.next   = next

    def __init__(self):
        self._top  = None
        self._size = 0

    def push(self, val):
        self._top = self._Node(val, self._top)
        self._size += 1
    
    def pop(self):
        deleted = self._top.value
        self._top = self._top.next; self._size -= 1
        return deleted
    
    def peek(self):
        return self._top.value
    
    def isEmpty(self):
        return not self._size
    
    def size(self):
        return self._size
