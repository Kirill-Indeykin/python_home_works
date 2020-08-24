"""Задача 1. Реализовать скрипт, в котором должна быть
предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def salary(hours: float, rate: float, bonus: float) -> float:
    """
    Функция расчета заработной платы сотрудника, по формуле (выработка в часах * ставка в час) + премия.
    :param hours: выработка в часах - float.
    :param rate: ставка в час - float.
    :param bonus: премия - float.
    :return: заработная плата - float.
    """
    return hours * rate + bonus


_, hours, rate, bonus = argv

try:
    hours = float(hours)
    rate = float(rate)
    bonus = float(bonus)
    result = salary(hours, rate, bonus)
    print(f'Зароботная плата сотрудника: {result} у.е.')
except ValueError:
    print('Ошибка ввода данных.')
