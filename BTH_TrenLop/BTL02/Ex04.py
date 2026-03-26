text = input("Nhập chuỗi: ")

upper = lower = digit = special = space = vowel = consonant = 0

vowels = "aeiouAEIOU"

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

    if char.isdigit():
        digit += 1

    if char.isspace():
        space += 1

    if char.isalpha():
        if char in vowels:
            vowel += 1
        else:
            consonant += 1
    elif not char.isdigit() and not char.isspace():
        special += 1

print("Chữ hoa:", upper)
print("Chữ thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
print("Khoảng trắng:", space)
print("Nguyên âm:", vowel)
print("Phụ âm:", consonant)