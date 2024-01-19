import os
import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value[:10] if len(value) > 10 else value

    def calculate_total_price(self) -> float:
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str = 'item.csv') -> None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, filename)

        try:
            with open(csv_path, 'r') as file:
                reader = csv.DictReader(file)
                required_columns = {'name', 'price', 'quantity'}
                if not required_columns.issubset(reader.fieldnames):
                    raise InstantiateCSVError(f"Файл {filename} поврежден.")

                for row in reader:
                    name = row['name']

                    # Проверяем, что значение в колонке 'price' присутствует и не None
                    if 'price' not in row or row['price'] is None or row['price'].strip() == '':
                        raise InstantiateCSVError(f"Отсутствует цена для товара {name}.")

                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    instance = cls(name, price, quantity)
                    cls.all.append(instance)

        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {filename}.")
        except csv.Error:
            raise InstantiateCSVError(f"Файл {filename} поврежден.")

    @staticmethod
    def string_to_number(value: str) -> int:
        try:
            return int(float(value))
        except ValueError:
            return 0



    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить Item с объектами других классов.")
