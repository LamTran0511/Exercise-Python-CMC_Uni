import matplotlib.pyplot as plt

cau_lac_bo = ["CLB Tin học", "CLB Văn nghệ", "CLB Khoa học", "CLB Mỹ thuật", "CLB Tiếng Anh"]
so_hoc_sinh = [8, 6, 5, 4, 7]
plt.bar(cau_lac_bo, so_hoc_sinh)
plt.title("Số lượng học sinh tham gia câu lạc bộ")
plt.xlabel("Tên câu lạc bộ")
plt.ylabel("Số lượng học sinh")
plt.show()