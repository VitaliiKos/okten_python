from pprint import pprint


def notebook_2() -> tuple:
    todo_list2: list[dict] = []

    def add_todo(todo: dict) -> None:
        nonlocal todo_list2
        todo_list2.append(todo)

    def get_todos() -> list[dict]:
        return todo_list2

    return add_todo, get_todos


add_todo2, get_all2 = notebook_2()

add_todo2({'1': 'to do something 1'})
add_todo2({'2': 'to do something 2'})
add_todo2({'3': 'to do something 3'})
add_todo2({'4': 'to do something 4'})
add_todo2({'5': 'to do something 5'})
add_todo2({'6': 'to do something 6'})
add_todo2({'7': 'to do something 7'})

pprint(get_all2())
