# Bai01:
def selection_sort_desc(arr):
    a = arr[:]
    n = len(a)
    step = 0

    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            step += 1
            if a[j] > a[max_idx]:
                max_idx = j

        if max_idx != i:
            a[i], a[max_idx] = a[max_idx], a[i]
            step += 1

    return a, step


def bubble_sort_desc(arr):
    a = arr[:]
    n = len(a)
    step = 0

    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            step += 1
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                step += 1
                swap = True

        if not swap:
            break

    return a, step


data = [5, 1, 9, 2, 8, 3, 7]

sel_sort, sel_step = selection_sort_desc(data)
bub_sort, bub_step = bubble_sort_desc(data)

print("Danh sách ban đầu:", data)
print("Selection Sort (giảm dần):", sel_sort)
print("Tổng bước Selection Sort:", sel_step)
print("Bubble Sort (giảm dần):", bub_sort)
print("Tổng bước Bubble Sort:", bub_step)


# Bai02:
def bai02_1():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = [x for x in n if x % 2 == 0]
    print('Các số lẻ là: ', a)


def bai02_2():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = list(filter(lambda x: x % 2 != 0, n))
    print('Các số lẻ là: ', a)
