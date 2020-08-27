"""Задача 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from pathlib import Path

file_name = Path(__file__).parent.joinpath('text_for_task_4.txt')

template = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
list_for_new_file = []
with open('text_for_task_4.txt', 'r') as open_my_file:
    for el in open_my_file:
        el = el.split(' ', 1)
        list_for_new_file.append(template[el[0]] + ' ' + el[1])

with open('ext_for_task_4_new.txt', 'w') as my_file_new:
    my_file_new.writelines(list_for_new_file)
