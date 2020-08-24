"""Задача 5. Реализовать формирование списка, используя функцию range()
и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


def my_reduce(function, sequence):

    func_it = iter(sequence)
    result = next(func_it)
    for el in func_it:
        result = function(result, el)
    return result


print('-' * 1000 + f'\nСписок четных значений\n{[el for el in range(99, 1001) if el % 2 == 0]}')

print('-' * 1000 + f'\nРезультат перемножения всех элементов списка\n'
                   f'{reduce(lambda el_1, el_2: el_1 * el_2, [el for el in range(99, 1001) if el % 2 == 0])}\n'
      + '-' * 1000)
print(f'Результат перемножения всех элементов списка (my_reduce)\n'
      f'{my_reduce(lambda el_1, el_2: el_1 * el_2, [el for el in range(99, 1001) if el % 2 == 0])}\n'
      + '-' * 1000)
