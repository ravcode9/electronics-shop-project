# src/keyboard.py
from src.item import Item

class LanguageMixin:
    supported_languages = ['EN', 'RU']

    def __init__(self, initial_language='EN', name=None, price=None, quantity=None):
        super().__init__(name=name, price=price, quantity=quantity)
        self._language = initial_language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value in self.supported_languages:
            self._language = value
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        current_index = self.supported_languages.index(self._language)
        next_index = (current_index + 1) % len(self.supported_languages)
        self._language = self.supported_languages[next_index]

class Keyboard(LanguageMixin, Item):
    def __init__(self, name, price, quantity, initial_language='EN'):
        super().__init__(initial_language=initial_language, name=name, price=price, quantity=quantity)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"
