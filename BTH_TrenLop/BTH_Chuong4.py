# Bai 1
def bai01():
    student = ("Trần Lâm", 18, 8.6)
    name, age, gpa = student
    print("Tên:", name)
    print("Tuổi:", age)
    print("Điểm TB:", gpa)


# Bai 2
def bai02():
    student = {'Lâm': {8.6, 9.0, 8, 7}}

    def tinhdiemtb(n):
        return sum(n) / len(n)

    for name, n in student.items():
        diemtb = tinhdiemtb(n)
    print('Điểm trung bình của học sinh là = ', diemtb)


# Bai 3
def bai03():
    class car:
        def __init__(self, brand, year):
            self.brand = brand
            self.year = year

    car01 = car('Honda', 2025)
    print('Hãng xe', car01.brand)
    print('Năm sản xuất', car01.year)


# Bai 4
def bai04():
    class student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    s1 = student('Lâm', 10)
    s2 = student('Long', 9)
    if s1.score > s2.score:
        print(s1.name, 'lớn hơn', s2.name)
    else:
        print(s1.name, 'bé hơn', s2.name)


# Bai 5
def bai05():
    class student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    def display(self):
        print(f"Tên: {self.name} | Điểm: {self.score}")

    s1 = student('Lâm', 10)
    s2 = student('Long', 9)
    if s1.score > s2.score:
        print(s1.name, 'lớn hơn', s2.name)
    else:
        print(s1.name, 'bé hơn', s2.name)


# Bai 6
def bai06():
    class Student:
        def __init__(self, name, score):
            if not (0 <= score <= 10):
                raise ValueError("Điểm phải nằm trong khoảng 0 đến 10!")
            self.name = name
            self.score = score

        def display(self):
            print(f"Tên: {self.name} | Điểm: {self.score}")

    s1 = Student('Lâm', 10)
    s2 = Student('Long', 9)
    if s1.score > s2.score:
        print("Học sinh có điểm bé hơn là: ")
        s2.display()
    elif s1.score == s2.score:
        print("Cả 2 học sinh bằng điểm nhau")
    else:
        print("Học sinh có điểm lớn hơn là: ")
        s1.display()


# Bai 7
def bai07():
    class Person:
        def __init__(self, age):
            if age <= 0:
                raise ValueError("Tuổi phải lớn hơn 0!")
            self.age = age

    p1 = Person(20)
    print("Tuổi:", p1.age)


while True:
    print("\n----------Menu----------")
    print("1. Bai 1")
    print("2. Bai 2")
    print("3. Bai 3")
    print("4. Bai 4")
    print("5. Bai 5")
    print("6. Bai 6")
    print("7. Bai 7")
    print("8. Thoát")
    x = int(input("Chọn chức năng: "))
    if x == 1:
        bai01()
    elif x == 2:
        bai02()
    elif x == 3:
        bai03()
    elif x == 4:
        bai04()
    elif x == 5:
        bai05()
    elif x == 6:
        bai06()
    elif x == 7:
        bai07()
    elif x == 8:
        print("Thoát chương trình")
        break
    else:
        print("Lỗi không có chức năng")
