from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value

    def __repr__(self) -> str:
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"
