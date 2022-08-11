from main import Product, Basket
import pytest

honor_phone = Product('HONOR 8X', 18000)
iphone_phone = Product('IPHONE X', 125000)
xiaomi_phone = Product('XIAOMI 10X SUPER MEGA ULTRA Z', 50)

test_sum = [([Product('Чак-чак', 1500), Product('IPHONE X', 125000), Product('XIAOMI 10X SUPER MEGA ULTRA Z', 50)], 126550)]

@pytest.mark.parametrize('products_a, summa', test_sum)
def test_basket(products_a, summa):
    basket = Basket()
    for prod in products_a:
        basket.add(prod)

    assert summa == basket.count_sum()

test_title = [([Product('HONOR 8X', 18000)], 'HONOR 8X'), ([Product('XIAOMI 10X SUPER MEGA ULTRA Z', 50)], 'XIAOMI 10X SUPER MEGA ULTRA Z')]

@pytest.mark.parametrize('name, price', test_title)
def test_name(name, price):
    product = Product(name, price)

    assert product.name == name

test_price = [([Product('HONOR 8X', 18000)], 18000), ([Product('XIAOMI 10X SUPER MEGA ULTRA Z', 50)], 50)]

@pytest.mark.parametrize('name, price', test_price)
def test_price(name, price):
    product = Product(name, price)

    assert product.price == price

test_to_add = [([honor_phone, iphone_phone, xiaomi_phone],
             [honor_phone, iphone_phone], xiaomi_phone)]

@pytest.mark.parametrize('products_a, products_b, products_c', test_to_add)
def test_add_bask(products_a, products_b, products_c):
    basket = Basket(products_b)
    basket.add(products_c)

    assert basket.basket == products_a

test_to_remove = [([honor_phone, iphone_phone, xiaomi_phone],
            [honor_phone, iphone_phone], xiaomi_phone)]

@pytest.mark.parametrize('products_a, products_b, products_c', test_to_remove)
def test_bask_rem(products_a, products_b, products_c):
    basket = Basket(products_a)
    basket.remove(products_c)
    assert basket.basket == products_b