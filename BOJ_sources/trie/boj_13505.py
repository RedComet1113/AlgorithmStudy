# 13505. 두 수 XOR (P3)
# https://www.acmicpc.net/problem/13505

class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.value = val
        self.child = [None, None]

class BinaryTrie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, num:int):
        tmp = self.head
        for i in range(29, -1, -1):
            bit = (num >> i) & 1
            if tmp.child[bit] == None:
                tmp.child[bit] = Node(bit)
            tmp = tmp.child[bit]

        tmp.value = num

    def xorMax(self, num:int):
        tmp = self.head
        for i in range(29, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if tmp.child[1] != None:
                    tmp = tmp.child[1]
                else:
                    tmp = tmp.child[0]
            else:
                if tmp.child[0] != None:
                    tmp = tmp.child[0]
                else:
                    tmp = tmp.child[1]

        return num ^ tmp.value
    
import sys; input = sys.stdin.readline

trie = BinaryTrie()
size = int(input()); arr = list(map(int, input().split()))
for num in arr:
    trie.insert(num)

xorMax = 0
for num in arr:
    tmp = trie.xorMax(num)
    if tmp > xorMax:
        xorMax = tmp

print(xorMax)