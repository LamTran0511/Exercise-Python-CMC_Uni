# BIT250208-Trần Lâm
# Bai 01:
class Product():
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError('Giá trị phải lớn hơn 0: ')

    def __str__(self):
        return f"{self.price}"
# Bai 02:
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split(' ')
        return cls(name, int(age))

    def __str__(self):
        return f"{self.name} {self.age}"
a = Person.from_string('Long 18')
print(a)
# Bai 03:
class Animal():
    def sound(self):
        print("sound")
class Dog(Animal):
    def sound(self):
        print("Tiếng chó sủa")
dongvat =Animal()
dongvat.sound()
cho =Dog()
cho.sound()
