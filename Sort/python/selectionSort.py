def swap(arr:list, i:int, j:int):
    if i >= len(arr) or j >= len(arr): raise IndexError
    arr[i], arr[j] = arr[j], arr[i]

# 최솟값 먼저 정렬
def selectionSort(arr:list):
    size = len(arr); cmp = swp = 0
    for i in range(size-1):
        minIdx = i
        for j in range(i+1, size):
            cmp += 1
            if arr[j] < arr[minIdx]: minIdx = j
        swp += 1
        swap(arr, i, minIdx)
    return [cmp, swp]

arr = [3, 1, 5, 4, 2]; print(arr, end = "")

stat = selectionSort(arr)

print(" ->", arr)
print(f"\n비교 : {stat[0]} 회\n교환 : {stat[1]} 회")