import math
a = [5,7,8,-2,11,13,9,10]
b = []
c = []
d = []
tong = 0
dem = 0

print("Chuỗi của từng số là:")
for x in a:
    print(x)

for y in a:
    if y % 2 == 0 and y > 0 :
        b.append(y)
print('Các số chẵn dương là: ', b)

for z in a:
    if z < 0:
        c.append(z)
print('Các số âm là: ', c)

for i in a:
    if i > 0:
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0:
                break
            else:
                d.append(i)
print('Các số nguyên tố là: ', d)

for i in a:
    tong += i
    dem += 1
print('Giá trị trung bình = ', tong/dem)
    