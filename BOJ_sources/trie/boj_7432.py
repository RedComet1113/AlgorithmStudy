# 7432. 디스크 트리 (G3)
# https://www.acmicpc.net/problem/7432

class Node:
    def __init__(self, key):
        self.key    = key
        self.next   = []
        self.child  = {}

class Directory:
    def __init__(self):
        self.head = Node(None)

    def insert(self, dir:str):
        dir = list(dir.split('\\'))

        tmp = self.head
        for f in dir:
            if f not in tmp.child:
                tmp.child[f] = Node(f)
                tmp.next.append(f)
            tmp = tmp.child[f]

    def printDirectory(self, node:Node, depth:int=0):
        node.next.sort()

        if depth != 0:
            print("{}{}".format(' '*(depth-1), node.key))

        for n in node.next:
            self.printDirectory(node.child[n], depth+1)

import sys; input = sys.stdin.readline

disc = Directory()
dirLn = int(input())
for _ in range(dirLn):
    disc.insert(input().rstrip())

disc.printDirectory(disc.head)