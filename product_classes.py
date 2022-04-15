from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    name: str
    price: float

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


@dataclass
class Basket:

    def __init__(self):
        self.basket: List[Product] = []

    def add(self, product: Product):
        self.basket.append(product)
        return self.basket

    def remove(self, product: Product):
        self.basket.remove(product)
        return self.basket

    def count_sum(self):
        sum = 0
        for i in range(0, len(self.basket)):
            sum += self.basket[i].price
        return sum
