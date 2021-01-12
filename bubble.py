def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort([1, 6, 7, 3, 2, 4, 5, 0, 0, 3, 2, 1, 6, 9]))
