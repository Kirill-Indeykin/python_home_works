"""Задача 3.  Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_function(arg_1: float, arg_2: float, arg_3: float) -> float:
    """
    Функция суммы двух наибольших аргументов.
    :param arg_1: первый аргумент, число - float.
    :param arg_2: второй аргумент, число - float.
    :param arg_3: третий аргумент, число - float.
    :return: Результат, число - float.
    """

    if arg_1 < arg_2 and arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_2 < arg_1 and arg_2 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


print(my_function(1, 2, 3))
