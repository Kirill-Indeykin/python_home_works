"""Задача 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Создадим списки времен года
seasons_list = ['Зимний', 'Весенний', 'Летний', 'Осенний']
seasons_dict = {1: 'Зимний', 2: 'Весенний', 3: 'Летний', 4: 'Осенний'}

# Запрос на ввод месяца года, проверка и вывод
while True:
    try:
        month_input: str = input('Введите числом месяц года: ')
        month_input: int = int(month_input)
        if month_input // 3 == 0 or month_input == 12:
            print('-' * 50 + '\nВведен ' + str(month_input) + '-ый месяц - ' + seasons_list[0])
            print('Введен ' + str(month_input) + '-ый месяц - ' + seasons_dict.get(1))
        elif month_input // 3 == 1:
            print('-' * 50 + '\nВведен ' + str(month_input) + '-ый месяц - ' + seasons_list[1])
            print('Введен ' + str(month_input) + '-ый месяц - ' + seasons_dict.get(2))
        elif month_input // 3 == 2:
            print('-' * 50 + '\nВведен ' + str(month_input) + '-ый месяц - ' + seasons_list[2])
            print('Введен ' + str(month_input) + '-ый месяц - ' + seasons_dict.get(3))
        elif month_input // 3 == 3:
            print('-' * 50 + '\nВведен ' + str(month_input) + '-ый месяц - ' + seasons_list[3])
            print('Введен ' + str(month_input) + '-ый месяц - ' + seasons_dict.get(4))
        else:
            print('Увы, такого месяца не существует. Попробуйте еще раз.\n' + '-' * 70)
            continue
        break
    except ValueError:
        print('Необходимо ввести целое, положительное число. Попробуйте еще раз.\n' + '-' * 70)
