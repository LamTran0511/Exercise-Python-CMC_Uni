import numpy as np
import matplotlib.pyplot as plt


# Bai1
def bai1():
    xeploai = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
    soluong = [25, 10, 12, 4, 1]

    plt.bar(xeploai, soluong)
    plt.title("Kết quả học tập của lớp")
    plt.xlabel("Xếp loại")
    plt.ylabel("Số học sinh")
    plt.show()

# Bai2
def bai2():
    x = np.linspace(-5, 5, 400)
    y1 = x**2
    y2 = x**3

    plt.plot(x, y1, color="blue", label="y = x^2")
    plt.plot(x, y2, color="red", label="y = x^3")
    plt.title("So sánh hai hàm số y = x^2 và y = x^3")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

# Bai3
def bai3():
    san_pham = ["A", "B", "C", "D", "E"]
    phan_tram = [30, 25, 15, 20, 10]

    plt.pie(phan_tram, labels=san_pham, autopct="%1.1f%%", startangle=90)
    plt.title("Tỷ lệ doanh số của 5 sản phẩm")
    plt.show()
