class Sach:
    def __init__(self, ten, tac_gia):
        self.ten = ten
        self.tac_gia = tac_gia

    def __str__(self):
        return f"Tên sách: {self.ten}, Tác giả: {self.tac_gia}"
sach1 = Sach("Dế Mèn Phiêu Lưu Ký", "Tô Hoài")
print(sach1)