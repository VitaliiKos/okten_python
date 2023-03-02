"""
3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""


def sum_of_digits_of_a_number(number: str) -> str:
    result = [value + '0' * (len(number) - index - 1) for index, value in enumerate(number) if value != '0']

    return ",".join(result)


print(sum_of_digits_of_a_number(input('Insert your number:')))
