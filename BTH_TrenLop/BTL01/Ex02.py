import math
a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
print(f'Lũy thừa của {a} là: ','{:.2f}'.format(a*a))
print(f'Lũy thừa của {b} là: ','{:.2f}'.format(b*b))
print(f'Căn bậc 2 của {a} là: ','{:.2f}'.format(math.sqrt(a)))
print(f'Căn bậc 2 của {b} là: ','{:.2f}'.format(math.sqrt(b)))
print(f'Chia lấy phần nguyên của {a} và {b} là: ','{:.2f}'.format((a//b)))
print(f'Chia lấy phần dư của {a} và {b} là: ','{:.2f}'.format((a%b)))
print(f'Chia lấy phần nguyên của {b} và {a} là: ','{:.2f}'.format((b//a)))
print(f'Chia lấy phần dư của {b} và {a} là: ','{:.2f}'.format((b%a)))

