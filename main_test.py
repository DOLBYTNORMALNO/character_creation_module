from random import randint

class Character:
    def __init__(self, name):
        self.name = name
    base_atc = 5
    base_def = 10
    base_stm = 80
    atc_rng = (1, 3)
    def_rng = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def attack(self):
        attack_value = base_atc + randint(*self.atc_rng)
        return (f'{self.name} нанес противнику урон, равный '
                f'{attack_value}')

    def defence(self):
        defence_value = base_def + randint(*self.def_rng)
        return (f'{self.name} блокировал {defence_value} урона.')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    ...



class Mage(Character):
    ...



class Healer(Character):
    ...

