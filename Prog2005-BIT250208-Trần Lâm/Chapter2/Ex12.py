n = int(input("Nhập n (>=1): "))
while n < 1:
    n = int(input("Sai! Nhập n >= 1: "))

s = 0
for i in range(1, n + 1, 2):
    s += i

print("Tổng số lẻ =", s)
