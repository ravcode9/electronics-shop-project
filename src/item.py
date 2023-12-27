import os
import csv

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
    def instantiate_from_csv(cls, filename: str) -> None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, '..', filename)

        # Проверяем существование файла
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Файл '{filename}' не найден.")

        with open(os.path.join(script_dir, '..', filename), 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                instance = cls(name, price, quantity)
                cls.all.append(instance)

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
