n = int(input("Nhập n (số lượng số Fibonacci): "))
while n <= 0:
    n = int(input("Sai! Nhập n > 0: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
