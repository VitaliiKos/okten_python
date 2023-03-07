# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
from typing import Callable


class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, size_of_hand: int) -> None:
        super().__init__(name, age)
        self.size_of_hand = size_of_hand
        Cinderella.__count += 1

    @classmethod
    def get_counter(cls) -> None:
        print(f'Кількість учасниць: {cls.__count}')

    def __str__(self) -> str:
        return f'Власниця туфельки {self.name}. Їй {self.age} роки. Розмір ноги {self.size_of_hand}!'

    def __repr__(self) -> str:
        return self.__str__()


class Prince(Human):

    def __init__(self, name: str, age: int, size_of_shoes: int) -> None:
        super().__init__(name, age)
        self.size_of_shoes = size_of_shoes

    def find_girl(self, princes_lis: list[Cinderella]) -> Callable | str:
        winner = [girl for girl in princes_lis if girl.size_of_hand == self.size_of_shoes]
        return winner if winner else 'Серед претендентів немає переможниці. Продовжуємо пошук...'


prince = Prince('Макс', 22, 34)
cinderella1 = Cinderella('Kira', 33, 34)
cinderella2 = Cinderella('Іра', 31, 33)
cinderella3 = Cinderella('Віра', 37, 36)
cinderella4 = Cinderella('Надя', 37, 38)
cinderella5 = Cinderella('Катя', 37, 37)

print(prince.find_girl([cinderella1, cinderella2, cinderella3, cinderella4, cinderella5]))
Cinderella.get_counter()
