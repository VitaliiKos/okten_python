# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются 
# від класу Printable
# 3) Створити клас Main в якому буде:
#   - змінна класу printable_list яка буде зберігати книжки та журнали
#   - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку 
#   чи то що передають є
#       класом Book або Magazine инакше ігрнорувати додавання
#   - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
#   - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def print(self) -> None:
        pass


class Book(Printable):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def print(self) -> None:
        print(f'Name: {self.name}')


class Magazine(Printable):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def print(self) -> None:
        print(f'Name: {self.name}')


class Main:
    printable_list: list[Book, Magazine] = []

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def add(cls, obj: Book | Magazine) -> None:
        print(obj in cls.printable_list)
        if isinstance(obj, (Book, Magazine)):
            cls.printable_list.append(obj)

    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()

    @classmethod
    def show_all_books(cls) -> None:
        for book in cls.printable_list:
            if isinstance(book, Magazine):
                book.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
Main.add('Book3')

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
