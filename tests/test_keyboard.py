import pytest
from src.keyboard import Keyboard

@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard_creation(keyboard):
    expected_str = "Dark Project KD87A"
    assert str(keyboard) == expected_str, f"Expected: {expected_str}, Actual: {str(keyboard)}"
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'

def test_change_language(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'

    keyboard.change_lang()
    assert keyboard.language == 'EN'

def test_invalid_lang(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'

def test_keyboard_repr(keyboard):
    assert repr(keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"
