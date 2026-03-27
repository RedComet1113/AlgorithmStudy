from completeBinaryTree import CompleteBinaryTree as CBT

class MaxHeap(CBT):
    def __init__(self, arr:list=[]):
        super().__init__(arr)
        self.__buildHeap()

    def __swap(self, idx:int, jdx:int):
        if idx >= self._size or jdx >= self._size:
            raise IndexError
        
        self._tree[idx], self._tree[jdx] = self._tree[jdx], self._tree[idx]

    def __siftDown(self, idx:int):
        while not self.isLeaf(idx):
            maxIdx = self.lChild(idx, True)
            if self.hasRChild(idx) and self._tree[self.rChild(idx, True)] > self._tree[maxIdx]:
                maxIdx = self.rChild(idx, True)

            if(self._tree[maxIdx] <= self._tree[idx]):
                return
            
            self.__swap(idx, maxIdx)
            idx = maxIdx

    def __buildHeap(self):
        for i in range(self._size//2 - 1, -1, -1):
            self.__siftDown(i)

    # update
    def insert(self, val):
        self._tree.append(val)
        self._size += 1
        self.__buildHeap()

    def pop(self):
        if self._size == 0: raise Exception("inexist")
        self._size -= 1
        ret = self._tree.pop()
        self.__buildHeap()

        return ret

    # utils
    def maxItem(self):
        return self._tree[0]
    
    def popMax(self):
        self.__swap(0, self._size - 1)
        ret = self.pop()
        self.__buildHeap()
        return ret

# maxHeap = MaxHeap([2, 3, 1, 4])
# print(maxHeap.popMax())
# maxHeap.insert(7); print(maxHeap.maxItem())