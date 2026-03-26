import math

x = float(input("Nhập một số: "))

if x < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm!")
else:
    print("Căn bậc hai là:", math.sqrt(x))
