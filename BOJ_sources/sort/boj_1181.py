# 1181. 단어 정렬 (S5)
# https://www.acmicpc.net/problem/1181

def mergeSort(arr):
    if len(arr) <= 1: return arr
    m = len(arr)//2
    return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))

def merge(l, r):
    i = j = 0
    lSize = len(l); rSize = len(r)
    res = []

    while i < lSize and j < rSize:
        if len(l[i]) < len(r[j]):
            res.append(l[i]); i += 1
        elif len(l[i]) == len(r[j]):
            lenSize = len(l[i])
            for k in range(lenSize):
                if l[i][k] < r[j][k]:
                    res.append(l[i]); i += 1
                    break
                if l[i][k] > r[j][k]:
                    res.append(r[j]); j += 1
                    break
        else:
            res.append(r[j]); j += 1
    while i < lSize:
        res.append(l[i]); i += 1
    while j < rSize:
        res.append(r[j]); j += 1

    return res

from sys import stdin; input = stdin.readline

size = int(input())
strs = set()
for _ in range(size):
    strs.add(input()[:-1])

strs = mergeSort(list(strs))

for st in strs:
    print(st)