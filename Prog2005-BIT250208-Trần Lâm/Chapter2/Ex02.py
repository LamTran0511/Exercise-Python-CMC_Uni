#Bài 2
#Yêu cầu: Yêu cầu người dùng nhập vào một số dương và kiểm tra xem số đó có phải là số nguyên tố hay không
def bai02():
    n = int(input('Nhập số dương: '))
    while n <= 0:
        n = int(input('Sai! Nhập lại số dương: '))
    if n < 2:
        print(n, 'Không phải số nguyên tố')
    else:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        print(n, "là số nguyên tố" if is_prime else "không phải số nguyên tố")

bai02()