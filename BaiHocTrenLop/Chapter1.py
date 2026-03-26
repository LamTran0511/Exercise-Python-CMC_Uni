def bai1():
    a = int(36)
    b = float(3.6)
    c = str('Hello')

    print("a =", a)
    print("b =", b)
    print("c =", c)


def bai2():
    Pi = 3.14
    r = float(5)
    chuvi = 2 * Pi * r
    print("chuvi =", chuvi)


def bai3():
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


def bai4():
    def sum_two_numbers(a, b):
        return a + b

    print(sum_two_numbers(1, 2))


def bai5():
    name = 'Trần Lâm'
    age = 18
    average_score = 8.3
    age_next_year = age + 1
    doubled_score = average_score * 2

    print("Tên: ", name)
    print("Tuổi: ", age)
    print("Điểm trung bình: ", average_score)
    print("Tuổi sang năm: ", age_next_year)
    print("Điểm nhân đôi: ", doubled_score)


def bai6():
    def is_even(n):
        return n % 2 == 0

    print(is_even(2))
    print(is_even(3))


def bai7():
    a = float(input("Nhập số: "))
    b = float(input("Nhập số: "))
    c = float(input("Nhập số: "))

    maxval = max(a, b, c)
    print("Số lớn nhất = ", maxval)


def bai8():
    def greet(name="Student"):
        print(f"Hello, {name}!")

    greet()
    greet("Hoàng Linh")


def bai9():
    age = int(input("Nhập tuổi: "))

    if 1 <= age <= 120:
        print("Tuổi hợp lệ.")
    else:
        print("Tuổi không hợp lệ (chỉ nhận 1 đến 120).")


def bai10():
    s = input("Nhập chuỗi: ")
    count_a = s.count('a')
    print("Số lần 'a' xuất hiện:", count_a)


def bai11():
    c = float(input("Nhập nhiệt độ (°C): "))
    f = c * 9 / 5 + 32
    print(f"{c:.2f}°C = {f:.2f}°F")


def bai12():
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))

    bmi = weight / (height * height)
    print(f"BMI = {bmi:.2f}")


def bai13():
    try:
        a = int(input("Nhập số nguyên a: "))
        b = int(input("Nhập số nguyên b: "))

        result = a / b
        print("Kết quả phép chia:", result)

    except ValueError:
        print("Lỗi: Bạn phải nhập số nguyên!")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")


def bai14():
    import math

    x = float(input("Nhập một số: "))

    if x < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm!")
    else:
        print("Căn bậc hai là:", math.sqrt(x))


def bai15():
    students = []

    for i in range(1, 4):
        print(f"\n--- Nhập sinh viên {i} ---")
        name = input("Tên: ")
        toan = float(input("Điểm Toán: "))
        ly = float(input("Điểm Lý: "))
        hoa = float(input("Điểm Hóa: "))

        avg = (toan + ly + hoa) / 3
        students.append((name, avg))

    print("\nKẾT QUẢ:")
    for name, avg in students:
        print(f"{name}: Điểm trung bình = {avg:.2f}")


# Tạo thêm menu cho dễ chạy
while (True):
    print("\n----------Menu----------")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("5. Bài 5")
    print("6. Bài 6")
    print("7. Bài 7")
    print("8. Bài 8")
    print("9. Bài 9")
    print("10. Bài 10")
    print("11. Bài 11")
    print("12. Bài 12")
    print("13. Bài 13")
    print("14. Bài 14")
    print("15. Bài 15")
    print("16. Thoát chương trình.")
    x = int(input("Chọn bài tập: "))
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
            bai6()
    elif x == 7:
            bai7()
    elif x == 8:
            bai8()
    elif x == 9:
            bai9()
    elif x == 10:
            bai10()
    elif x == 11:
                bai11()
    elif x == 12:
                bai12()
    elif x == 13:
                bai13()
    elif x == 14:
                bai14()
    elif x == 15:
                bai15()
    elif x == 16:
        print("Thoát chương trình")
        break
    else:
        print("Lỗi không có chức năng")
