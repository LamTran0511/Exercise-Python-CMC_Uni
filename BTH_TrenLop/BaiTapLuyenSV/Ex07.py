def thong_ke_tuple(data):
    trung_binh = sum(data) / len(data)
    lon_nhat = max(data)
    nho_nhat = min(data)
    return trung_binh, lon_nhat, nho_nhat
numbers = (4, 8, 2, 10, 6)
tb, ln, nn = thong_ke_tuple(numbers)
print("Trung bình cộng:", tb)
print("Giá trị lớn nhất:", ln)
print("Giá trị nhỏ nhất:", nn)