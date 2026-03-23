# 16934. 게임 닉네임 (G3)
# https://www.acmicpc.net/problem/16934

class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
        self.dup = {}

    def spanningName(self, string):
        tmp = self.head
        if string in self.dup:
            self.dup[string] += 1
        else:
            self.dup[string] = 1

        isEnd = False; idx = 0
        for ch in string:
            if ch not in tmp.child:
                tmp.child[ch] = Node(ch)
                if not isEnd:
                    isEnd = True
            tmp = tmp.child[ch]
            if not isEnd:
                idx += 1
        
        if not isEnd:
            if self.dup[string] == 1:
                return string
            else:
                return "{0}{1}".format(string, self.dup[string])
        return string[:idx+1]
    
import sys; input = sys.stdin.readline

size = int(input()); trie = Trie()
for _ in range(size):
    print(trie.spanningName(input().rstrip()))