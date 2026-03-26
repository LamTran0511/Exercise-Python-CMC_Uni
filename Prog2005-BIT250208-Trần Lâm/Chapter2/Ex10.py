def sum_1_to_n(n):
    if n == 1:
        return 1
    return n + sum_1_to_n(n - 1)

n = int(input("Nhập n (>=1): "))
while n < 1:
    n = int(input("Sai! Nhập n >= 1: "))

print("Tổng =", sum_1_to_n(n))
