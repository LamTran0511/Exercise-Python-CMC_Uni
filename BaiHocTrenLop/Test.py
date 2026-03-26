# from os import name
#
# info = 'Trần Lâm - BIT250208 - 05/11/2007 .'
# arr = info.split('-')
# upd = info.split('.')
# for i in arr:
#  print(i)
# print(info.split('-'))
#
# print(info.upper())
# print(info.lower())
#
# print(info.find("5"))
# print(info.rfind("5"))
#
# print(info[0:5])
# print(info[5:9])
# print(info[-1:])
#
# upd1 = "- CMCU"
# upd1 = upd1.join(upd)
# print(upd1)
#
# matrix = [
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
# ]
# for row in matrix:
#  print(matrix)
# try:
#  x = int(input("Nhập số nguyên: "))
#  if x >= 0:
#   print('Số nguyên dương.')
#  else:
#   print('Số nguyên âm.')
# except ValueError:
#  print("Lỗi cú pháp")

# s = input("Nhập chuỗi: ")
# ch = input("Nhập 1 ký tự cần đếm: ")
#
# while len(ch) != 1:
#     ch = input("Sai! Nhập đúng 1 ký tự: ")
#
# count = 0
# for c in s:
#     if c == ch:
#         count += 1
#
# print(f"Ký tự '{ch}' xuất hiện {count} lần")

# def student():
#     student = get_student()
#     if student[0] == "LamTran":
#         student[1] == "PhuTho"
#     print(f'{student[0]} from {student[1]}')
# def get_student():
#     name = input("Nhap ten: ")
#     address = input("Nhap que quan: ")
#     return [name, address]
#
# def Data():
#     student = {'name': 'Alice', 'age': 20,
#                'grades': {'math': 90, 'science': 85}}
#     print(student['name'],student['age'])
#     print(student['grades']['math'],
#           student['grades']['science'])

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name, house)
#
# def main():
#     student = Student.get()
#     print(student)
#
# if __name__ == "__main__":
#     main()

# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts
#
#     def __str__(self):
#         return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

#SẮP XẾP:
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
numbers = [5,6,2,1,3]
print(bubble_sort(numbers))

def luuFile():
    file = open('csdlsinhvien.txt', 'w', encoding='utf-8')
    file.writelines("sv01;Trần Minh Tuấn;8.7\n")
    file.writelines("sv02;Lê Thị Hồng;9.2\n")
    file.writelines("sv03;Phạm Văn An;7.8\n")
    file.writelines("sv04;Ngô Thị Mai;8.0\n")
    file.close()
luuFile()

def docFile():
    file = open('csdlsinhvien.txt', 'r', encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()
docFile()

