class SinhVien:
    count = 0

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1

    @classmethod
    def dem_so_doi_tuong(cls):
        return cls.count
sv1 = SinhVien(8)
sv2 = SinhVien(7)
sv3 = SinhVien(9)
print("Số đối tượng đã tạo:", SinhVien.dem_so_doi_tuong())