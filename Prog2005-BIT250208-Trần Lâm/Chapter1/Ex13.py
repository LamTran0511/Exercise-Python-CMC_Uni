try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))

    result = a / b
    print("Kết quả phép chia:", result)

except ValueError:
    print("Lỗi: Bạn phải nhập số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")