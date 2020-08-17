"""Задача 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# Проверка вводимых пользователем данных;
while True:
    try:
        list_size: str = input('Введите количество элементов списка: ')
        list_size: int = int(list_size)
        if list_size < 1:
            print('Увы, но список не может состоять из: ' + str(list_size) + ' элементов')
            print('Необходимо ввести целое, положительное число. Попробуйте еще раз.')
            continue
        else:
            print('-' * 50 + '\nОтлично, список будет состоять из: ' + str(list_size) + ' элементов')
        break
    except ValueError:
        print('Необходимо ввести целое, положительное число. Попробуйте еще раз.')

# Создаем пустой список
my_list = []

# Заполняем список элементами
i = 0
while i < list_size:
    my_list.append(input('Введите ' + str(i+1) + ' элемент списка: '))
    i += 1
print('\nПолученный список:\n' + '-' * 30 + '\n' + str(my_list) + '\n' + '=' * 30)

# Меняем местами элементы списка 1-2, 3-4, n-(n+1)
j = 0
while j < list_size - 1:  # индекс списка с начинается с 0, поэтому вычитаем 1
    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    j += 2
print('\nПреобразованный список:\n' + '-' * 30 + '\n' + str(my_list) + '\n' + '=' * 30)




