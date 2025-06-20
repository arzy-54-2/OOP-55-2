# Инкапсуляция

import random
class BankAccount:

    def __init__(self, user_name, balance, pin_code):
        self.user_name = user_name
        # protected
        self._balance = balance
        # private
        self.__pin_code = pin_code

    def get_balance(self):
        return self._balance

class Test(BankAccount):
    pass

john = Test("John", 1000, 123321)

# print(john.user_name)

from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        # ...
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Gaf gaf")

    def move(self):
        print("step")

class Cat(Animal):

    def make_sound(self):
        print("myu myu")

    def move(self):
        print("step")

gufi = Dog()
