class CompleteBinaryTree:
    def __init__(self, arr:list=[]):
        self._tree = arr
        self._size = len(arr)

    # return items
    def parent(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self._size:    raise IndexError
        if idx == 0:                        raise Exception("inexist")
        
        if retIdx: return (idx-1)//2
        return self._tree[(idx-1)//2]
    
    def lChild(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self._size:    raise IndexError
        if idx >= self._size//2:            raise Exception("inexist")

        if retIdx: return 2*idx + 1
        return self._tree[2*idx + 1]
    
    def rChild(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self._size:    raise IndexError
        if idx >= (self._size - 1)//2:      raise Exception("inexist")

        if retIdx: return 2*idx + 2
        return self._tree[2*idx + 2]

    def lSibling(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self._size:    raise IndexError
        if idx & 1 == 1:                    raise Exception("inexist")

        if retIdx: return idx - 1
        return self._tree[idx - 1]

    def rSibling(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self._size:           raise IndexError
        if idx & 1 == 0 or idx + 1 >= self._size:  raise Exception("inexist")

        if retIdx: return idx + 1
        return self._tree[idx + 1]

    # update
    def insert(self, val):
        self._tree.append(val)
        self._size += 1

    def pop(self):
        if self._size == 0: raise Exception("inexist")
        self._size -= 1
        return self._tree.pop()

    def update(self, idx:int, val):
        if idx < 0 or idx >= self._size: raise IndexError

        self._tree[idx] = val
        return val

    # traversal
    def preOrderTraversal(self):
        return self.__preTrav()
    def __preTrav(self, idx:int=0, res:list=[]):
        res.append(self._tree[idx])
        if self.hasLChild(idx): self.__preTrav(self.lChild(idx, True), res)
        if self.hasRChild(idx): self.__preTrav(self.rChild(idx, True), res)

        return res
    
    def postOrderTraversal(self):
        return self.__postTrav()
    def __postTrav(self, idx:int=0, res:list=[]):
        if self.hasLChild(idx): self.__postTrav(self.lChild(idx, True), res)
        if self.hasRChild(idx): self.__postTrav(self.rChild(idx, True), res)
        res.append(self._tree[idx])

        return res
    
    def inOrderTraversal(self):
        return self.__inTrav()
    def __inTrav(self, idx:int=0, res:list=[]):
        if self.hasLChild(idx): self.__inTrav(self.lChild(idx, True), res)
        res.append(self._tree[idx])
        if self.hasRChild(idx): self.__inTrav(self.rChild(idx, True), res)

        return res

    # utils
    def size(self):
        return self._size
    
    def isLeaf(self, idx:int):
        if idx < 0 or idx >= self._size: raise IndexError
        
        if idx < self._size//2:
            return False
        return True
    
    def hasLChild(self, idx:int):
        if idx < 0 or idx >= self._size: raise IndexError
        
        if idx < self._size//2: return True
        return False
    
    def hasRChild(self, idx:int):
        if idx < 0 or idx >= self._size: raise IndexError

        if idx < (self._size - 1)//2: return True
        return False
    
# cbt = CompleteBinaryTree([4, 7, 3, 1, 2, 6, 5])
# print(cbt.preOrderTraversal())
# print(cbt.postOrderTraversal())
# print(cbt.inOrderTraversal())