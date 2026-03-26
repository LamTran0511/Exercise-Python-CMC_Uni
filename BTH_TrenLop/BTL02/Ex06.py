class Product:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value > 0:
            self._price = value
        else:
            print("Price phải > 0")

    def __str__(self):
        return f"Product price: {self._price}"