"""
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  a знайти мін число
  b видалити усі дублікати
  c замінити кожне 4-те значення на 'X'
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
3) вывести табличку множення за допомогою цикла while
4) переробити це завдання під меню
"""

list_number = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# 1.a)
def min_from_list(arr):
    result = arr[0]
    print('Task_1: min value is', min(arr))
    for i in arr:
        if i < result:
            result = i
    return result


# 1.b)

def change_item(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr


# 1.c
def change_every_fourth(arr, step):
    for i in range(step - 1, len(arr), step):
        arr[i] = 'X'
    return arr


# 2)
def square(n):
    if not isinstance(n, int) or int(n) <= 0:
        print('Wrong number')
    else:
        n = int(n)
        if n == 1:
            print('*')
        else:
            print('*' * n)
            for i in range(n - 2):
                print(f'*{" " * (n - 2)}*')
            print('*' * n)


# 3)


def multiplication_table(y):
    n = 1
    while n <= y:
        for i in range(1, y + 1):
            print(str(n * i).center(3), end=' ')
        n += 1
        print(end='\n')
    return 'Finish'


# 4) переробити це завдання під меню
def menu():
    while True:
        print('1. знайти мін число.')
        print('2. видалити усі дублікати.')
        print('3. замінити кожне 4-те значення на "X".')
        print('4. вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції.')
        print('5. вывести табличку множення за допомогою цикла while.')
        print('6. Вихід')

        menu_number = input('Зробіть свій вибір:')
        if not menu_number.isdigit() or 0 >= int(menu_number) > 6:
            print('------------------------------------------------')
            print('Wrong number!')
            print('------------------------------------------------')
        else:
            if menu_number == '1':
                print('min value is', min_from_list(list_number))
            elif menu_number == '2':
                print('New arr is', change_item(list_number))
            elif menu_number == '3':
                print('new arr is', change_every_fourth(list_number[:], 4))
            elif menu_number == '4':
                square(input('Write a number:'))
            elif menu_number == '5':
                print(multiplication_table(10))
            elif menu_number == '6':
                break
            else:
                print('------------------------------------------------')
                print("Wrong number!")
                print('------------------------------------------------')
        print('--------------- Chose task ----------------------------')


print('Task_1.a: min value is', min_from_list(list_number))
print('-' * 20)

print('Task_1.b: new arr is', change_item(list_number))
print('-' * 20)

print('Task_1.c: new arr is', change_every_fourth(list_number[:], 4))
print('-' * 20)

print('Task_2:')
square(input('Write a number:'))
print('-' * 20)

print('Task_3:')
print(multiplication_table(10))
print('-' * 20)

menu()
