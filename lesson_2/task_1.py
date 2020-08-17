"""Задача 1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

# Определим элементы из которых буде состоять наш список
# 1 class - int
a_1 = 1
# 2 class - float
a_2 = 0.1
# 3 class - complex
a_3 = complex(1, 2)
# 4 class - str
b_1 = 'Hello'
# 5 class - list
c_1 = [1, 2, 3]
# 6 class - tuple
c_2 = (1, 2, 'World')
# 7 class - set
d_1 = set('Hello World')
# 8 class - frozenset
d_2 = frozenset('Hello World')
# 9 class - dict
e_1 = {'key_1': 1, 'key_2': 2, 'key_3': 3}
# 10 class - bool
f_1 = True
# 11 class bytes
g_1 = b'hello'
# 12 class bytearray
g_2 = bytearray(b'hello')
# 13 class NoneType
h_1 = None

# Создадим наш список из элементов описанных ранее
my_list = [a_1, a_2, a_3, b_1, c_1, c_2, d_1, d_2, e_1, f_1, g_1, g_2, h_1]

# В цикле определим класс каждого объекта нашего списка и выведем
print('Список содержит следующие классы: \n' + '-' * 35)
for idx, itm in enumerate(my_list, 1):
    print(idx, '- элемент: ' + str(type(itm)) + '\n' + '-' * 35)
