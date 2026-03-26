from tokenize import String

s = input("Nhập chuỗi ký tự: ")
ch = input('Nhập ký tự cần đếm: ')
dem = 0
for i in s:
    if i ==  ch:
        dem += 1
print('Số lần ký tự xuất hiện = ',dem)
#Bài 5

#Yêu cầu: Yêu cầu người dùng nhập vào một chuỗi và một ký tự,
# sau đó đếm xem ký tự đó xuất hiện bao nhiêu lần trong chuỗi.