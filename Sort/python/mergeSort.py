def mergeSort(arr:list):
    if(len(arr) <= 1): return arr
    m = len(arr)//2
    return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))

def merge(l:list, r:list):
    i = j = 0
    lSize = len(l); rSize = len(r)
    res = []

    while i < lSize and j < rSize:
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    while i < lSize:
        res.append(l[i]); i += 1
    while j < rSize:
        res.append(r[j]); j += 1

    return res

print(mergeSort([4, 1, 5, 2, 6, 7, 9, 3, 10, 8]))