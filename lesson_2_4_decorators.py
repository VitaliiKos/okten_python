"""
4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
та буде виводити це значення після виконання функцій
"""
from typing import Callable


def decor(func: Callable) -> Callable:
    count = 0

    def inner() -> None:
        nonlocal count
        count += 1
        print('Count:', count)
        func()
        print('_' * 50)

    return inner


@decor
def func1() -> None:
    print('func1')


@decor
def func2() -> None:
    print('func2')


func1()
func1()
func2()
func1()
