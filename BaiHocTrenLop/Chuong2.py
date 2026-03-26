
def so_nguyen():
 x = int(input("Nhập số nguyên: "))
 if x == 0:
    print("Xin hãy nhập lại ")
 else:
    print("Giá trị X = ",x)

def vong_lap():
    x = int(input('Nhập số vòng lặp')) # Rút x = int vào input
    for i in range(0, x):
        print(i, end=", ")

def tong():
    tong = 0
    x = int(input('Viết số nguyên: '))
    for i in range(0, x):
        tong += i
        print("Tổng = ",tong)

def factorial(n):
    n = int(input("Nhập số nguyên: "))
    if n < 1:
        return 1
    return n * factorial(n-1)


while(True):
    print("----------Menu----------")
    print("1. Số nguyên")
    print("2. Vòng lặp")
    print("3. Tính tổng")
    print("4. Thoát")
    x = int(input("Chọn chức năng: "))
    if x == 1:
        so_nguyen()
    elif x == 2:
            vong_lap()
    elif x == 3:
            tong()
    elif x == 4:
        print("Thoát chương trình")
        break
    else:
        print("Lỗi không có chức năng")
