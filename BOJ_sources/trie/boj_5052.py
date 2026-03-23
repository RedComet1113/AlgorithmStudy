# 5052. 전화번호 목록 (G4)
# https://www.acmicpc.net/problem/5052

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
        return string

    def hasPrefix(self, string):
        tmp = self.head

        for ch in string[:-1]:
            if ch in tmp.child:
                tmp = tmp.child[ch]
                if tmp.value is not None:
                    return True
        return False
    
import sys; input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    size = int(input())
    phoneNum = []; trie = Trie()
    for _ in range(size):
        phoneNum.append(trie.insert(input().rstrip()))
        
    flag = False
    for num in phoneNum:
        if trie.hasPrefix(num):
            print("NO"); flag = True; break
    if not flag:
        print("YES")