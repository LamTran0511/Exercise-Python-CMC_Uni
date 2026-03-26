import random

m = int(input("Nhập số hàng M: "))
n = int(input("Nhập số cột N: "))

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)
print("Ma trận vừa tạo:")
for row in matrix:
    print(row)

hang = int(input("Nhập số hàng muốn hiển thị (tính từ 0 đến {}): ".format(m - 1)))
if 0 <= hang < m:
    print("Hàng", hang, "là:", matrix[hang])
else:
    print("Hàng không hợp lệ!")

cot = int(input("Nhập số cột muốn hiển thị (tính từ 0 đến {}): ".format(n - 1)))
if 0 <= cot < n:
    print("Cột", cot, "là:")
    for i in range(m):
        print(matrix[i][cot])
else:
    print("Cột không hợp lệ!")

max_value = matrix[0][0]
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

print("Giá trị lớn nhất trong ma trận là:", max_value)
