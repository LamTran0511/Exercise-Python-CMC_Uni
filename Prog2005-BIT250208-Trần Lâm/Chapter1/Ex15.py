students = []

for i in range(1, 4):
    print(f"\n--- Nhập sinh viên {i} ---")
    name = input("Tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))

    avg = (toan + ly + hoa) / 3
    students.append((name, avg))

print("\nKẾT QUẢ:")
for name, avg in students:
    print(f"{name}: Điểm trung bình = {avg:.2f}")
