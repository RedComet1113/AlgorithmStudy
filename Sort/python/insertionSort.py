def swap(arr:list, i:int, j:int):
    if i >= len(arr) or j >= len(arr): raise IndexError
    arr[i], arr[j] = arr[j], arr[i]

# 인덱스 순으로 정렬
def insertionSort(arr:list):
    size = len(arr); cmp = swp = 0
    for i in range(1, size):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            swap(arr, j, j-1); j -= 1
            cmp += 1; swp += 1
        if j != 0: cmp += 1
    return [cmp, swp]

arr = [3, 1, 5, 4, 2]; print(arr, end = "")

stat = insertionSort(arr)

print(" ->", arr)
print(f"\n비교 : {stat[0]} 회\n교환 : {stat[1]} 회")