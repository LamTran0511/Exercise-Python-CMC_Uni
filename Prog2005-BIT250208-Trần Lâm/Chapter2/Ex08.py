n = int(input("Nhập số dương: "))
if n < 0:
    n = int(input("Sai! Nhập số dương: "))
else:
    lenght_n = len(str(n))
    for i in range(0, lenght_n):
        m = n % 10
        print(m, end=' ')
        n //= 10


