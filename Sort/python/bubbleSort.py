def swap(arr:list, i:int, j:int):
    if i >= len(arr) or j >= len(arr): raise IndexError
    arr[i], arr[j] = arr[j], arr[i]

# 최댓값 먼저 정렬
def bubbleSort(arr:list):
    size = len(arr); cmp = swp = 0
    for i in range(size-1):
        for j in range(size-i-1):
            cmp += 1
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1); swp += 1
    return [cmp, swp]

arr = [3, 1, 5, 4, 2]; print(arr, end = "")

stat = bubbleSort(arr)

print(" ->", arr)
print(f"\n비교 : {stat[0]} 회\n교환 : {stat[1]} 회")