"""Задача 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# Для выполнение данной Задачи 2 используем файл из Задачи 1.
# можно использовать другой файл, но тогда нужен путь к файлу.
# from pathlib import Path
# file_name = Path(__file__).parent.joinpath('test.txt')

open_my_file = open('test.txt', 'r')

el = open_my_file.readlines()

print('-' * 70 + f'\nКоличество строк в файле - {len(el)}\n' + '-' * 70)

for i in range(len(el)):
    print(f'Количество символов в {i + 1}-ой строке: {len(el[i])}')

print('-' * 70 )
j = 0
for el in el:
    print(f'Количество слов в {j + 1}-ой строке: {len(el.split())}')
    j += 1
print('-' * 70)

open_my_file.close()
