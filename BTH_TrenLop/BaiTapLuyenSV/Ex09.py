import matplotlib.pyplot as plt

mon_the_thao = ["Bóng đá", "Bóng rổ", "Bóng chuyền", "Cầu lông", "Bơi lội"]
so_hoc_sinh = [9, 6, 5, 7, 4]
plt.bar(mon_the_thao, so_hoc_sinh)
plt.title("Số lượng học sinh theo môn thể thao yêu thích")
plt.xlabel("Môn thể thao")
plt.ylabel("Số lượng học sinh")
plt.show()