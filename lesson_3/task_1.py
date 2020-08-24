"""Задача 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def my_div(arg_1: float, arg_2: float) -> float:

    """
    Функция деления дывух чисел. Сообщение об ошибке деления на ноль.
    :param arg_1: делимое - float.
    :param arg_2: делитель (не 0) - float.
    :return: результат деления - float.
    """
    if arg_2 == 0:
        print('Ошибка ввода. Деление на ноль!')
    else:
        return arg_1 / arg_2


print(my_div(4, 2))
