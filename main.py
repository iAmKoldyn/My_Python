from typing import List


class Product:
    name: str
    price: float

    def __init__(self, name, price):
        self.name, self.price = name, price


class Basket:
    def __init__(self, products=[]):
        self.basket: List[Product] = products

    def count_sum(self):
        return sum([cost.price for cost in self.basket])

    def add(self, product):
        self.basket.append(product)

    def remove(self, name: str):
        self.basket.remove(name)