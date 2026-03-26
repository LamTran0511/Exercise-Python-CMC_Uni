nums = input("Nhập các số nguyên, cách nhau bởi dấu cách: ")
numbers = list(map(int, nums.split()))
max_number = max(numbers)
print("Số lớn nhất trong danh sách là:", max_number)