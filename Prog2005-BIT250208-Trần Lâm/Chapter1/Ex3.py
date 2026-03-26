a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
if b != 0:
    print('Thương = ', thuong)
else:
    print('Không thể chia cho 0!')

print('Tổng = ', tong)
print('Hiệu = ', hieu)
print('Tích = ', tich)