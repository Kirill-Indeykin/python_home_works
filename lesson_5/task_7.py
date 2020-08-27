"""Задача 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json

profit = {}
profit_1 = {}
profit_2 = 0
average_profit = 0
i = 0
with open('text_for_task_7.txt', 'r') as file:
    for line in file:
        name, type_of_ownership, proceeds, costs = line.split()
        profit[name] = int(proceeds) - int(costs)
        if profit.setdefault(name) >= 0:
            profit_2 = profit_2 + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = profit_2 / i
        print(f'Средняя прибыль равна: {average_profit:.2f}\n')
    else:
        print(f'Средняя прибыль отсутствует, работа всех фирм в убыток!\n')
    profit_1 = {'Средняя прибыль': round(average_profit)}
    profit.update(profit_1)
    print(f'Прибыль по компаниям, равна: {profit}\n')

with open('text_for_task_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Файл с расширением json содержит:\n {js_str}')
