"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
@pytest.fixture

def item1():
    return Item("Смартфон", 10000, 20)

def test_item_init(item1):
    """Функция, которая тестирует конструктор"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20

def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_item_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 10000.0