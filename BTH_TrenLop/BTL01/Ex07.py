class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

sv1 = student('Nguyễn Văn A', 10)
sv2 = student('Nguyễn Văn B', 8)
print(sv1.name,'.Tổng điểm: ',sv1.score)
print(sv2.name,'.Tổng điểm: ',sv2.score)