# Bài 2: Yêu cầu người dùng nhập một số nguyên, sau đó kiểm tra và in ra số đó có phải là số nguyên tố hay không.
n = int(input("Nhập số nguyên tố: "))

if n < 2:
    print("Đây ko phải số nguyên tố")
else:
    la_so_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
