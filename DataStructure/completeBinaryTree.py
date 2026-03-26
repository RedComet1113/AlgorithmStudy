class CompleteBinaryTree:
    def __init__(self, arr:list=[]):
        self.__tree = arr
        self.__size = len(arr)

    # return items
    def parent(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self.__size: raise IndexError
        
        if retIdx: return (idx-1)//2
        return self.__tree[(idx-1)//2]
    
    def lChild(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self.__size: raise IndexError
        if 2*idx + 1 >= self.__size: raise Exception("inexist")

        if retIdx: return 2*idx + 1
        return self.__tree[2*idx + 1]
    
    def rChild(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self.__size: raise IndexError
        if 2*idx + 2 >= self.__size: raise Exception("inexist")

        if retIdx: return 2*idx + 2
        return self.__tree[2*idx + 2]

    def lSibling(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self.__size: raise IndexError
        if idx & 1 == 1: raise Exception("inexist")

        if retIdx: return idx - 1
        return self.__tree[idx - 1]

    def rSibling(self, idx:int, retIdx:bool=False):
        if idx < 0 or idx >= self.__size: raise IndexError
        if idx & 1 == 0 or idx + 1 >= self.__size: raise("inexist")

        if retIdx: return idx + 1
        return self.__tree[idx + 1]

    # update
    def insert(self, val):
        self.__tree.append(val)
        self.__size += 1

    def update(self, idx:int, val):
        if idx < 0 or idx >= self.__size: raise IndexError

        self.__tree[idx] = val
        return val

    # traversal
    def preOrderTraversal(self):
        return self.__preTrav()
    def __preTrav(self, idx:int=0, res:list=[]):
        res.append(self.__tree[idx])
        if self.hasLChild(idx): self.__preTrav(self.lChild(idx, True), res)
        if self.hasRChild(idx): self.__preTrav(self.rChild(idx, True), res)

        return res
    
    def postOrderTraversal(self):
        return self.__postTrav()
    def __postTrav(self, idx:int=0, res:list=[]):
        if self.hasLChild(idx): self.__postTrav(self.lChild(idx, True), res)
        if self.hasRChild(idx): self.__postTrav(self.rChild(idx, True), res)
        res.append(self.__tree[idx])

        return res
    
    def inOrderTraversal(self):
        return self.__inTrav()
    def __inTrav(self, idx:int=0, res:list=[]):
        if self.hasLChild(idx): self.__inTrav(self.lChild(idx, True), res)
        res.append(self.__tree[idx])
        if self.hasRChild(idx): self.__inTrav(self.rChild(idx, True), res)

        return res

    # utils
    def size(self):
        return self.__size
    
    def hasLChild(self, idx:int):
        if idx < 0 or idx >= self.__size: raise IndexError
        
        if 2*idx + 1 >= self.__size: return False
        return True
    
    def hasRChild(self, idx:int):
        if idx < 0 or idx >= self.__size: raise IndexError

        if 2*idx + 2>= self.__size: return False
        return True
    
cbt = CompleteBinaryTree([4, 7, 3, 1, 2, 6, 5])
print(cbt.preOrderTraversal())
print(cbt.postOrderTraversal())
print(cbt.inOrderTraversal())