"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def sample_items():
    item1 = Item("Item1", 10.0, 5)
    item2 = Item("Item2", 15.0, 3)
    item3 = Item("Item3", 20.0, 2)
    return item1, item2, item3

def test_calculate_total_price(sample_items):
    item1, item2, item3 = sample_items
    assert item1.calculate_total_price() == 50.0
    assert item2.calculate_total_price() == 45.0
    assert item3.calculate_total_price() == 40.0

def test_apply_discount(sample_items):
    item1, item2, item3 = sample_items

    item1.apply_discount()
    assert item1.price == 10.0

    item2.pay_rate = 0.9
    item2.apply_discount()
    assert item2.price == 13.5

    item3.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 16.0
