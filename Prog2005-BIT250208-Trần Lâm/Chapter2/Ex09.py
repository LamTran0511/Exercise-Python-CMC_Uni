n = int(input("Nhập số nguyên dương 5 chữ số: "))
while n < 10000 or n > 99999:
    n = int(input("Sai! Nhập số 5 chữ số (10000-99999): "))

max_digit = 0
temp = n
while temp > 0:
    d = temp % 10
    if d > max_digit:
        max_digit = d
    temp //= 10

print(f"Chữ số lớn nhất trong {n} là {max_digit}")
