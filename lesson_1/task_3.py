"""Задание 3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

# Решение:

# 1. Ввод числа и проверка, что пользователь ввел - число.
while True:
    try:
        var_input_n = int(input("Введите число: "))
        break
    except ValueError:
        print("Вы невнимательны, необходимо ввести целое число. Попробуйте еще раз!")

# 2. Объединяем введенное число с самим собой.
var_input_nn = int(str(var_input_n) + str(abs(var_input_n)))

# 3. Объединяем введенное число с числом, полученным при предудущем объединении (п.2).
var_input_m = int(str(var_input_nn) + str(abs(var_input_n)))

# 4. Складывам все полученные объединением значения и затем ввыодим, если введенное значение положительное.
if var_input_n < 0:
    var_sum = var_input_n + var_input_nn + var_input_m
    print("Считаем: " + str(var_input_n) + str(var_input_nn) + str(var_input_m) + " = " + str(var_sum))
# 4.1. Складывам все полученные объединением значения и затем ввыодим, если введенное значение отрицательное.
else:
    var_sum = var_input_n + var_input_nn + var_input_m
    print("Считаем: " + str(var_input_n) + "+" + str(var_input_nn) + "+" + str(var_input_m) + " = " + str(var_sum))

