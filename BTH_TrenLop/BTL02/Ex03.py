name = input("Nhập tên: ")
name = name.strip()
word = name.split()
normalized_name = ""
for i in word:
    normalized_name += i.capitalize() + " "

print("Tên chuẩn:", normalized_name.strip())