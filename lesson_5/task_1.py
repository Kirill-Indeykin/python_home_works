""" Задача 1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

create_my_file = open('test.txt', 'w')
input_line = input('Введите текст и нажмите Enter для записи строки в файл.'
                   '\n[Ввод пустой строки - для завершение работы]:\n>>> ')
while input_line:
    create_my_file.writelines(input_line + '\n')
    input_line = input('>>> ')
    if not input_line:
        print('Завершение работы.')
        break
create_my_file.close()


"""Второй вариант решения задачи (с with)
input_line = input('Введите текст и нажмите Enter для записи строки в файл.'
                   '\n[Ввод пустой строки - для завершение работы]:\n>>> ')
with open(r 'test.txt', 'w') as create_my_file:
    while True:
        create_my_file.write(input_line + '\n')
        input_line = input('>>> ')
        if not input_line:
            print('Завершение работы.')
            break
"""