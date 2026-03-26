import array
a = array.array('i', [1, 3, 5, 8, 9, 2, 4, ])

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap sau khi đã tìm xong min
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort(a))

