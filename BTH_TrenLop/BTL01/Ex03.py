n = int(input('Nhập từ 1 - 9: '))
print(f'Bảng cửu chương của {n} là: ')
for i in range(0,11):
    print(f'{n}*{i}=','{}'.format(n*i))