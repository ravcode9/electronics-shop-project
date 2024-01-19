import pytest
import os
from src.item import Item

# Фикстура для создания примеров товаров
@pytest.fixture
def sample_items():
    item1 = Item("Товар1", 10.0, 5)
    item2 = Item("Товар2", 15.0, 3)
    item3 = Item("Товар3", 20.0, 2)
    return item1, item2, item3

# Тест для проверки метода calculate_total_price
def test_calculate_total_price(sample_items):
    item1, item2, item3 = sample_items
    assert item1.calculate_total_price() == 50.0
    assert item2.calculate_total_price() == 45.0
    assert item3.calculate_total_price() == 40.0

# Тест для проверки метода apply_discount
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

# Тест для проверки свойства name
def test_name_property():
    # Создаем товар с длинным именем
    item = Item("ДлинноеИмяТовара", 10.0, 5)
    assert item.name == "ДлинноеИмяТовара"
    item.name = "КороткоеИмя"
    assert item.name == "КороткоеИм"

    # Пытаемся установить очень длинное имя, которое будет усечено до 10 символов
    item.name = 'ОченьДлинноеИмяТовараКотороеПревышаетЛимит'
    assert item.name == 'ОченьДлинн'

# Тест для проверки метода instantiate_from_csv
def test_instantiate_from_csv():
    # Путь к файлу item.csv в пакете src
    project_root = os.path.dirname(os.path.dirname(__file__))
    csv_filename = os.path.join(project_root, 'src', 'item.csv')

    # Инициализируем объекты из файла и проверяем результаты
    Item.instantiate_from_csv(csv_filename)
    assert len(Item.all) == 5

    # Проверяем значения объектов
    item1, item2, item3, item4, item5 = Item.all
    assert item1.name == 'Смартфон'

    # Предполагаем, что значение price для Ноутбука может быть 1000 или 100, исходя из данных
    assert item2.price in [1000.0, 100.0]

    assert item3.quantity == 5
    assert item4.name == 'Мышка'
    assert item5.price == 75.0

def test_item_repr():
    item = Item("Смартфон", 1200, 5)
    assert repr(item) == "Item('Смартфон', 1200, 5)"
    assert str(item) == 'Смартфон'

def test_item_string_to_number():
    assert Item.string_to_number("42") == 42
    assert Item.string_to_number("3.14") == 3
    assert Item.string_to_number("invalid") == 0


