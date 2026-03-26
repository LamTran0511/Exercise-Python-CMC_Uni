a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
while a < 0 or b < 0:
    print("Lỗi! nhập lại số nguyên dương: ")
while b != 0:
    a, b = b, a % b
print("Ước lượng chung = ", a)