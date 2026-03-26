class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # gán qua setter

    def __str__(self):
        return f"{self.name} from {self.address}"

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value not in ["PT", "HN", "VN"]:
            raise ValueError("Lỗi địa chỉ!")
        self._address = value


def get_student():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    return Student(name, address)


def main():
    student = get_student()
    print(student)


if __name__ == "__main__":
    main()
