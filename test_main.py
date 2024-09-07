import pytest
from main import Category, Product


@pytest.fixture
def test_category():
    return Category('Сок', 'Натуральный, без сахара', ['Яблочный', 'Персиковый', 'Апельсиновый'])


def test_init_category(test_category):
    assert test_category.title == 'Сок'
    assert test_category.description == 'Натуральный, без сахара'
    assert test_category.products == ['Яблочный', 'Персиковый', 'Апельсиновый']
    assert test_category.total_category == 1
    assert test_category.total_unique == 3


@pytest.fixture
def test_product():
    return Product('Сок', 'Полезный и вкусный', '119.99', '80')


def test_init_product(test_product):
    assert test_product.title == 'Сок'
    assert test_product.description == 'Полезный и вкусный'
    assert test_product.price == '119.99'
    assert test_product.quantity == '80'
