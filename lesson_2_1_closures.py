"""
1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
"""
from pprint import pprint


def notebook_1():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        return todo_list

    return [add_todo, get_all]


todo_add1, get_all1 = notebook_1()

todo_add1({'Sunday': 'sleep'})
todo_add1({'Monday': 'go work'})
pprint(get_all1())
todo_add1({'Tuesday': 'came from wor'})
todo_add1({'Wednesday': 'study'})
todo_add1({'Thursday': 'go shopping'})
pprint(get_all1())
todo_add1({'Friday': 'go work'})
todo_add1({'Saturday': 'go to English lessons'})
pprint(get_all1())

