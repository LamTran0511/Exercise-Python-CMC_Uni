def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Nhập n (>=0): "))
while n < 0:
    n = int(input("Sai! Nhập n >= 0: "))

print(n,'! ' '=', factorial(n))
