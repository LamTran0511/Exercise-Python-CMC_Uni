# Bai 1:
def bai1():
    while True:
        code = input("Nhập mã sản phẩm: ")
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá sản phẩm: "))
        with open('quanlysanpham', 'a', encoding='utf-8') as file:
            file.write(f"{code};{name};{price}\n")
        print("Đã thêm sản phẩm thành công!\n")

        them = input("Thêm sản phẩm? (y/n): ")
        if them.lower() != "y":
            break
    def modanhsach():
        file = open('quanlysanpham', 'r', encoding='utf-8')
        for line in file:
            print(line)
        file.close()
    modanhsach()
    def sapxep():
        products = []

        with open('quanlysanpham', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    code, name, price = line.split(";")
                    products.append((code, name, float(price)))

        products.sort(key=lambda x: x[2], reverse=True)

        print("\nDanh sách sau khi sắp xếp giảm dần theo giá:")
        for p in products:
            print(f"{p[0]};{p[1]};{p[2]}")
bai1()
#Bai 2:
def bai2():
    def nhapfile():
        with open("numbers.txt", "w", encoding="utf-8") as file:
            file.write("5,6,8,9,-5\n")
            file.write("-9,5,4,7,8\n")
            file.write("6,7,8,3,6,46,7,2,-6,-7\n")
    def docfile():
        with open("numbers.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers = list(map(int, line.split(",")))
                    print("Danh sách:", numbers)
                    so_am = [n for n in numbers if n < 0]
                    print("Số âm:", so_am)
                    print("-" * 30)
    nhapfile()
    docfile()
bai2()
#Bai 3:
from xml.dom import minidom

def doc_xml_dom(filename="employees.xml"):
    def tao_file_xml(filename="employees.xml"):
        content = """<?xml version="1.0" encoding="UTF-8"?>
    <employees>
        <employee>
            <id>1</id>
            <name>Nguyễn Khánh Sơn</name>
        </employee>
        <employee>
            <id>2</id>
            <name>Lê Hoành Sử</name>
        </employee>
        <employee>
            <id>3</id>
            <name>Hồ Trung Thành</name>
        </employee>
    </employees>
    """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    tao_file_xml()
    doc = minidom.parse(filename)
    employees = doc.getElementsByTagName("employee")
    print("Danh sách nhân viên:")
    for emp in employees:
        emp_id = emp.getElementsByTagName("id")[0].firstChild.data.strip()
        name = emp.getElementsByTagName("name")[0].firstChild.data.strip()
        print(f"ID: {emp_id} | Name: {name}")
doc_xml_dom()