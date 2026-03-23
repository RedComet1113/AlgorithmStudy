# 14725. 개미굴 (G3)
# https://www.acmicpc.net/problem/14725

import sys; input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key    = key
        self.next   = []
        self.child  = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, strList:list):
        tmp = self.head

        for s in strList:
            if s not in tmp.child:
                tmp.child[s] = Node(s)
                tmp.next.append(s)
            tmp = tmp.child[s]

    def travel(self, node:Node, depth:int):
        node.next.sort()
        
        if depth != 0:
            print("{}{}".format("--"*(depth-1), node.key))
        
        for n in node.next:
            self.travel(node.child[n],  depth+1)
            
trie = Trie()
qLen = int(input())
for _ in range(qLen):
    trie.insert(input().rstrip().split()[1:])
    

trie.travel(trie.head, 0)