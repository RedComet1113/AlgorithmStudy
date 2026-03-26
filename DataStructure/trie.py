class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.value = val
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        tmp = self.head

        for ch in string:
            if ch not in tmp.child:
                tmp.child[ch] = Node(ch)
            tmp = tmp.child[ch]

        tmp.value = string

    def search(self, string):
        tmp = self.head

        for ch in string:
            if ch in tmp.child:
                tmp = tmp.child[ch]
            else:
                return False
            
        if tmp.value is not None:
            return True
        return False
        

strBox = Trie()
strBox.insert("apple")
strBox.insert("juice")

print(strBox.search("banana"))
print(strBox.search("juice"))
print(strBox.search("app"))