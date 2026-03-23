# 5670. 휴대폰 자판 (P4)
# https://www.acmicpc.net/problem/5670

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

    def cnt2in(self, string):
        tmp = self.head

        cnt = 0
        for ch in string:
            if tmp.key == None:
                cnt += 1
            elif len(tmp.child) > 1 or tmp.value is not None:
                cnt += 1
            tmp = tmp.child[ch]

        return cnt
    
import sys; input = sys.stdin.readline

while True:
    try:
        strs = []; trie = Trie()

        tmp = input()
        if tmp == "": break
        size = int(tmp)
        for _ in range(size):
            tmp = input().rstrip()
            strs.append(tmp)
            trie.insert(tmp)

        res = 0
        for q in strs:
            res += trie.cnt2in(q)
        print("{:.2f}".format(res/len(strs)))
    except:
        break