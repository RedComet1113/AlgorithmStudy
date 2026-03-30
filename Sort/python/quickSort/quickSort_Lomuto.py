def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr:list):
    return qSort(arr, 0, len(arr)-1)

def qSort(arr:list, p:int, r:int):
    if p < r:
        q = partition(arr, p, r)
        qSort(arr, p, q-1)
        qSort(arr, q+1, r)

def partition(arr:list, p:int, r:int):
    piv = arr[r]; i = p - 1
    for j in range(p, r):
        if arr[j] <= piv:
            i += 1; swap(arr, i, j)
    swap(arr, i+1, r)
    return i+1

arr = [7, 3, 4, 1, 10, 5, 8, 9, 2, 6]; quickSort(arr)
print(arr)