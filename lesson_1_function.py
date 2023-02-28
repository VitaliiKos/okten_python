"""
function
1) створити функцію яка виводить ліст
2) створити функцію яка приймає три числа та виводить та повертає найбільше.
3) створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
4 створити функцію яка повертає найбільше число з ліста
5) створити функцію яка повертає найменьше число з ліста
6) створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
7) створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
"""


# 1)
def simple_list():
    print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# 2)
def max_number(a, b, c):
    print('Task_2: max number is', max(a, b, c))
    if b < a > c:
        return a
    elif b > c:
        return b
    return c


# 3)
def max_min_number(*args):
    result = args[0]
    print('Task_3: max number is', max(args))
    for number in args:
        if number < result:
            result = number
    return result


# 4)
def max_from_list(list_number):
    result = list_number[0]

    for item in list_number:
        if item > result:
            result = item
    return result


# 5)
def min_from_list(list_number):
    return min(list_number)


# 6)
def list_sum(list_number):
    result = 0
    for i in list_number:
        result += i
    return result


# 7)
def average(list_number):
    return sum(list_number) / len(list_number)


print('Task_1: ')
simple_list()
print('-' * 20)

print('Task_2: max number is', max_number(4, 7, 9))
print('-' * 20)

print('Task_3: min number is', max_min_number(6, 5, 9))
print('-' * 20)

print('Task_4: max number is', max_from_list([6, 5, 1]))
print('-' * 20)

print('Task_5: min number is', min_from_list([3, 5, 8]))
print('-' * 20)

print('Task_6: sum is', list_sum([3, 5, 8]))
print('-' * 20)

print('Task_7: average value is', average([6, 2, 7]))
print('-' * 20)
