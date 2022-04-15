from product_classes import *
import pytest


tests = [('banana', 10.0), ('bread', 20.0)]

def test_field():
    bread = Product('bread', 10.0)
    assert bread.name == 'bread'


@pytest.mark.parametrize('name, price', tests)
def test_name(name: str, price: float):
    alt = Product(name, price)
    assert alt.name == name


@pytest.mark.parametrize('name, price', tests)
def test_price(name: str, price: float):
    alt = Product(name, price)
    assert alt.price == price


test_1 = [([Product('banana', 50.0), Product('bread', 20.0), Product('eggs', 100.0)], [Product('banana', 50.0)])]

@pytest.mark.parametrize('basket, str', test_1)
def test_add(basket: List[Product], str : List[Product]):
    basket_1 = Basket()
    for p in basket:
        basket_1.add(p)
    is_equal = True
    for p1, p2 in zip(str, basket_1.basket):
        if not (p1.name == p2.name and p1.price == p2.price):
            is_equal = False
            break
    assert is_equal

    
test_2 = [([Product('banana', 10.0), Product('bread', 40.0), Product('eggs', 50.0)], [Product('banana', 50.0)])]

@pytest.mark.parametrize('basket, str', test_2)
def test_remove(basket: List[Product], str : List[Product]):
    basket_2 = Basket()
    for p in basket:
        basket_2.add(p)
        basket_2.remove(p) 
    is_equal = True
    for p1, p2 in zip(str, basket_2.basket):
        if not (p1.name == p2.name and p1.price == p2.price):
            is_equal = False
            break
    assert is_equal

test_3 = [([Product('banana', 10.0), Product('bread', 40.0), Product('eggs', 50.0)], 100.0)]

@pytest.mark.parametrize('product, str', test_3)
def test_summ(product: Product, str: float):
    basket_3 = Basket()
    for p in product:
        basket_3.add(p)
    assert str == basket_3.count_sum()
