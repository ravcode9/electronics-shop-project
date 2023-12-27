import pytest
from src.phone import Phone
from src.item import Item

def test_phone_from_item():
    phone = Phone("Samsung Galaxy", 800, 3, 1)
    assert isinstance(phone, Item)

def test_phone_add_with_item():
    phone = Phone("Samsung Galaxy", 800, 3, 1)
    item = Item("Headphones", 50, 2)
    result = phone + item
    assert result == 5

def test_addition_phones():
    phone1 = Phone("Samsung Galaxy", 800, 3, 1)
    phone2 = Phone("iPhone X", 1000, 2, 2)
    result = phone1 + phone2
    assert result == 5

def test_valid_value():
    phone = Phone("Samsung Galaxy", 800, 3, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test__invalid_value():
    phone = Phone("Samsung Galaxy", 800, 3, 1)
    with pytest.raises(ValueError):
        phone.number_of_sim = 0

def test_invalid_type():
    phone = Phone("Samsung Galaxy", 800, 3, 1)
    with pytest.raises(ValueError):
        phone.number_of_sim = "invalid"
