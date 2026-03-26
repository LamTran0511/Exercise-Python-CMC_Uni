#Yêu cầu: Yêu cầu người dùng nhập vào một số trong
#khoảng từ 1 đến 9, sau đó hiển thị bảng cửu chương của số đó từ 1 đến 9
n = int(input('Nhập từ 1 đến 9: '))
while n < 1 or n > 9:
    n = int(input("Lỗi! nhập lại số từ 1 đến 9: "))

for i in range(1, 11):
    nhan = n*i
    print(n, 'x', i, '=',nhan)
