# 10815. 숫자 카드 (S5)
# https://www.acmicpc.net/problem/10815

def mergeSort(arr):
    if len(arr) <= 1: return arr
    m = len(arr)//2
    return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))

def merge(l, r):
    i = j = 0
    lSize = len(l); rSize = len(r)
    
    res = []
    while i < lSize and j < rSize:
        if l[i] < r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    while i < lSize:
        res.append(l[i]); i += 1
    while j < rSize:
        res.append(r[j]); j += 1

    return res

def binarySearch(arr, val):
    l = 0; r = len(arr)-1
    while l <= r:
        m = (l+r)//2
        if(val == arr[m]):  return 1
        elif(val < arr[m]): r = m-1
        else:               l = m+1
    return 0

import sys; input = sys.stdin.readline;

cSize = int(input())
card = mergeSort(list(map(int, input().split())))
qSize = int(input())
query = list(map(int, input().split()))

for q_i in query:
    print(binarySearch(card, q_i), end=' ')

# cSize = int(input())
# card = set(map(int, input().split()))
# qSize = int(input())
# query = list(map(int, input().split()))

# for q_i in query:
#     print(1 if q_i in card else 0, end=' ')