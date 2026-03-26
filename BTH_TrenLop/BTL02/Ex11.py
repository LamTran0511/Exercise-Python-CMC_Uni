class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Động vật phát ra âm thanh")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Gâu gâu")
dog1 = Dog("Milu")
print("Tên:", dog1.name)
dog1.sound()