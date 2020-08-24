""" Задача 2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры, как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def my_function_user_info_data(name: str,
                               surname: str,
                               birth_year: str,
                               city_of_resident: str,
                               e_mail: str,
                               telephone_number: str) -> str:
    """
    Функция описывающая данные пользователя.
    :param name: Имя пользователя - str.
    :param surname: Фамилия пользователя - str.
    :param birth_year: Год рождение - str.
    :param city_of_resident: Место рождения - str.
    :param e_mail: e-mail пользователя - str.
    :param telephone_number: номер телефона - str.
    :return: Выводит параметры в одну строку - str.
    """
    return ' '.join([name, surname, birth_year, city_of_resident, e_mail, telephone_number])


print(my_function_user_info_data(name='Ivan',
                                 surname='Ivanov',
                                 birth_year='2000',
                                 city_of_resident='Moscow',
                                 e_mail='iv.iv@mail.ru',
                                 telephone_number='84952001010'))
