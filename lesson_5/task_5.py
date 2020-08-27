"""Задача 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

set_of_numbers = [str(el for el in range(0, 101) if el % 2 == 0)]

with open('text_for_task_5.txt', 'w') as create_my_file:
    i = 1
    while i < 10:
        num_list = [str(randint(0, 10))]
        create_my_file.write(' '.join(num_list) + ' ')
        i += 1

with open('text_for_task_5.txt') as reading_my_file:
    new_list = [int(el) for el in reading_my_file.read().split()]

print()
print('-' * 50 + f'\nСумма чисел = {sum(new_list)}\n' + '_' * 50)
