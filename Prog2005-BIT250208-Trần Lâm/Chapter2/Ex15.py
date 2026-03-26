n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Sai! Nhập số nguyên dương: "))

s = 0
while n > 0:
    s += n % 10
    n //= 10

print("Tổng chữ số =", s)
