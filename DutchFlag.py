def DutchFlagAlgo(a, size_arr):
    low, mid, high = 0, 0, size_arr - 1
    while mid <= high:
        if a[mid] == 'r':
            a[low], a[mid] = a[mid], a[low]
            mid += 1
            low += 1
        elif a[mid] == 'w':
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

arr = ['r', 'w', 'w', 'r', 'w', 'b', 'w', 'b', 'r', 'r', 'r', 'w']
arr_size = len(arr)
arr = DutchFlagAlgo(arr, arr_size)
print(arr)
