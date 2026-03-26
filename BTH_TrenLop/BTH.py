#Bt 1
def bai1():
    n = int(input("Nhập số nguyên: "))
    if n > 0:
        print("Số nguyên dương = ", n)
    elif n == 0:
        print("N bằng 0", n)
    else:
        print("Số nguyên âm", n)

def bai2():
    for i in range(1, 11):
        print(i)

def bai3():
    x = int(input("Nhập số nguyên dương: "))
    tong = 0
    for i in range(0, x):
        tong += i
    print(tong)

def bai4():
    x = int(input("Nhập số nguyên: "))
    if x%2 == 0:
        print("Chẵn")
    else:
        print("Lẻ")

def bai5():
    for i in range(2, 21):
        if i % 2:
            continue
        print(i)

while(True):
    print("\n----------Menu----------")
    print("1. Kiểm tra số nguyên âm/dương")
    print("2. Chạy từ 1-10")
    print("3. Tính tổng")
    print("4. Chẵn lẻ")
    print("5. Chạy từ 2-20 cách 2")
    print("6. Thoát")
    x = int(input("Chọn chức năng: "))
    if x == 1:
            bai1()
    elif x == 2:
            bai2()
    elif x == 3:
            bai3()
    elif x == 4:
            bai4()
    elif x == 5:
            bai5()
    elif x == 6:
        print("Thoát chương trình")
        break
    else:
        print("Lỗi không có chức năng")