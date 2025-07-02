# Наследование
# Полиморфизм
from email.policy import default


# Родительский класс/ Супер класс
class Hero:

    def __init__(self, name, hp, lvl=None):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def action(self):
        print(f"{self.name} action!!")

# Дочерний класс/Класс наследник
class WarriorHero(Hero):

    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st

    def action(self):
        print(f"WarriorHero method!!!")

hero_1 = WarriorHero("Hero 1", 11, 100)

hero_1.action()

# CamelCase
# snake_case


