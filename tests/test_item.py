"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item_init(item1):
    """Функция, которая тестирует конструктор"""

    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


def test_item_calculate_total_price(item1):
    """Функция, которая тестирует функцию calculate_total_price"""

    assert item1.calculate_total_price() == 200000


def test_item_apply_discount(item1):
    """Функция, которая тестирует функцию apply_discount"""

    item1.apply_discount()
    assert item1.price == 10000.0


def test_instantiate_from_csv():
    """Функция, которая тестирует функцию instantiate_from_csv"""

    Item.instantiate_from_csv()
    assert len(Item.all) != 0


def test_string_to_number():
    """Функция, которая тестирует функцию string_to_number"""

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.6') == 5


def test__repr__(item1):
    """Функция, которая тестирует функцию __repr__"""
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__(item1):
    """Функция, которая тестирует функцию __str__"""
    assert str(item1) == 'Смартфон'


def test__add__(item1):
    """Функция, которая тестирует функцию __add__"""
    assert item1 + item1 == 40
