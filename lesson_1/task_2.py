"""Задание 2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

# Решение:

# 1. Ввод времени в секундах и проверка, что пользователь ввел - число. - нагуглил =)
while True:
    try:
        time_input_sec = int(input("Введите время в секундах: "))
        break
    except ValueError:
        print("Введите время в секундах - целым числом. Попробуйте еще раз!")

# 2. Вычисляем часы. И добавляем 0, если значение меньше 10.
time_hour = (abs(time_input_sec) // 3600) % 24
if time_hour < 10:
    time_hour = str("0" + str(time_hour))
else:
    time_hour = str(time_hour)

# 3. Вычисляем минуты. И добавляем 0, если значение меньше 10.
time_min = (abs(time_input_sec) // 60) % 60
if time_min < 10:
    time_min = str("0" + str(time_min))
else:
    time_hour = str(time_hour)

# 4. Вычисляем секунды. И добавляем 0, если значение меньше 10.
time_sec = abs(time_input_sec) % 60
if time_sec < 10:
    time_sec = str("0" + str(time_sec))
else:
    time_hour = str(time_hour)

# 5. Выводим время в формате чч:мм:сс.
if time_input_sec < 0:
    print("Введенное время в секундах, равно прошедшим: " + str(time_hour) + "чч:" + str(time_min) + "мм:" + str(time_sec) + "сс")
else:
    print("Введенное время в секундах, равно: " + str(time_hour) + "чч:" + str(time_min) + "мм:" + str(time_sec) + "сс")
