#example: https://stackoverflow.com/questions/57227611/price-of-items-using-classes-in-python

from typing import List

class Product:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Basket:

    def __init__(self):
        self.basket: List[Product] = []

    def add(self, product: Product):
        self.basket.append(product)
        return 'add'

    def remove(self, product: Product):
        self.basket.remove(product)
        return 'remove'

    def count_sum(self):
        sum = 0
        for i in range(0, len(self.basket)):
            sum += self.basket[i].price
        return sum
