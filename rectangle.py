# 1. Створити клас Rectangle:
#       - він має приймати дві сторони x,y
#       - описати поведінку на арифметични методи:
#           + сумма площин двох екземплярів ксласу
#           - різниця площин двох екземплярів ксласу
#           == площин на рівність
#           != площин на не рівність
#           >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    perimeter = 0

    def __init__(self, x: int, y: int) -> None:
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f'{self.__dict__}'

    def area(self) -> int:
        return (self.x + self.y) * 2

    def __add__(self, other) -> int:
        return self.area() + other.area()

    def __sub__(self, other) -> int:
        return self.area() - other.area()

    def __eq__(self, other) -> bool:
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        return self.area() != other.area()

    def __lt__(self, other) -> bool:
        return self.area() < other.area()

    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    def __len__(self) -> int:
        return (self.x + self.y) * 2


item1 = Rectangle(5, 6)
item2 = Rectangle(6, 8)

print(item2 + item1)
print(item2 - item1)
print(item2 == item1)
print(item2 != item1)
print(item2 > item1)
print(item2 < item1)
print(len(item1))
print(len(item2))
