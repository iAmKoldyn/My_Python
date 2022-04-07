from product_classes import Basket, Product
import pytest


tests = [('banana', 10.0), ('bread', 20.0)]

def test_field():
    bread = Product('banana', 10.0)
    assert bread.name == 'banana'


@pytest.mark.parametrize('name, price', tests)
def test_name(name: str, price: float):
    alt = Product(name, price)
    assert alt.name == name


@pytest.mark.parametrize('name, price', tests)
def test_price(name: str, price: float):
    alt = Product(name, price)
    assert alt.price == price


test_1 = [([Product('banana', 10.0), Product('bread', 40.0), Product('eggs', 50.0)], 'add')]

@pytest.mark.parametrize('product, str', test_1)
def test_add(product: Product, str: str):
    basket_1 = Basket()
    for p in product:
        basket_1.add(p)
        assert str == basket_1.add(p)

test_2 = [([Product('banana', 10.0), Product('bread', 40.0), Product('eggs', 50.0)], 'remove')]

@pytest.mark.parametrize('product, str', test_2)
def test_remove(product: Product, str: str):
    basket_2 = Basket()
    for p in product:
        basket_2.add(p)
    assert str == basket_2.remove(p)


test_3 = [([Product('banana', 10.0), Product('bread', 40.0), Product('eggs', 50.0)], 100.0)]

@pytest.mark.parametrize('product, str', test_3)
def test_summ(product: Product, str: float):
    basket_3 = Basket()
    for p in product:
        basket_3.add(p)
    assert str == basket_3.count_sum()
