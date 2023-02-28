"""
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
#################################################################################
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
#################################################################################
"""
# 1)
st = 'as 23 fdfdg544'
result_task_1 = []
for i in st:
    if i.isdigit():
        result_task_1.append(i)

print('Task_1: ', ','.join(result_task_1))
print('-' * 20)

# 2)
st2 = 'as 23 fdfdg544 34'

result_task_2 = []
temporary_variable = ''
for j in st2:
    if j.isdigit():
        temporary_variable += j
    else:
        if len(temporary_variable):
            result_task_2.append(temporary_variable)
            temporary_variable = ''
if len(temporary_variable):
    result_task_2.append(temporary_variable)

print('Task_2: ', ','.join(result_task_2))
print('-' * 20)
