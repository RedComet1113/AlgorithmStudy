class LinkedQueue:
    class _Node:
        def __init__(self, val=None, next:object=None):
            self.value  = val
            self.next   = next

    def __init__(self):
        self._front    = None
        self._rear     = None
        self._size     = 0

    def enqueue(self, val):
        new = self._Node(val)
        if self._size == 0:
            self._front = self._rear = new
        self._rear.next = new; self._rear = new
        self._size += 1

    def dequeue(self):
        deleted = self._front.value
        self._front = self._front.next
        self._size -= 1
        if self._size == 0:
            self.rear = None
        return deleted
    
    def peek(self):
        return self._front.value
    
    def isEmpty(self):
        return not self._size
    
    def size(self):
        return self._size
    
# queue = LinkedQueue()

# queue.enqueue(2); queue.enqueue(5); queue.enqueue(4) # [2, 5, 4]
# print(queue.size(), end=' ')    # 3
# print(queue.dequeue(), end=' ') # 2
# print(queue.peek(), end=' ')    # 5
# print(queue.dequeue())          # 5
# print(queue.isEmpty())          # False
# print(queue.dequeue())          # 4
# print(queue.isEmpty())          # True