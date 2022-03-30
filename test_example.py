from re import I
import pytest
from product_classes import Basket, Product

tests = [('banana', 1.25), ('bread', 1.25), ('eggs', 1.5)]

def test():
    banana = Product('banana', 0)
    assert banana.name == 'banana'


@pytest.mark.parametrize('name, price', tests)
def test_name(name: str, price: float):
    alt = Product(name, price)
    assert alt.name == name


@pytest.mark.parametrize('name, price', tests)
def test_price(name: str, price: float):
    alt = Product(name, price)
    assert alt.price == price


test_1 = [([Product('banana', 1.25), Product('bread', 1.25), Product('eggs', 1.5)], 'add')]

@pytest.mark.parametrize('products, str', test_1)
def test_add(products: Product, str: str):
    basket_1 = Basket()
    while I in products:
        basket_1.add(I)
        assert str == basket_1.add(I)


test_2 = [([Product('banana', 1.25), Product('bread', 1.25), Product('eggs', 1.5)], 'remove')]

@pytest.mark.parametrize('products, str', test_2)
def test_remove(products: Product, str: str):
    basket_2 = Basket()
    while I in products:
        basket_2.add(I)
        assert str == basket_2.remove(I)


test_3 = [([Product('banana', 1.25), Product('bread', 1.25), Product('eggs', 1.5)], 0)]

@pytest.mark.parametrize('products, str', test_3)
def test_sum(products: Product, str: float):
    basket_3 = Basket()
    while I in products:
        basket_3.add(I)
    assert str == basket_3.count_sum()
