"""Задача 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

# Для выполнение данной Задачи 3 используем файл из Задачи 1.
# можно использовать другой файл, но тогда нужен путь к файлу.
# from pathlib import Path
# file_name = Path(__file__).parent.joinpath('test.txt')

from statistics import mean

with open("test.txt") as open_my_file:
    average_income = []
    for el in open_my_file:
        surname, salary = el.split()
        salary = int(salary)
        if salary < 20_000:
            print('-' * 70 + f'\n{surname} - зарплата менее 20000.')
        average_income.append(salary)
print('-' * 70 + f'\nСредняя величина дохода сотрудников: {mean(average_income)}.\n' + '-' * 70)
