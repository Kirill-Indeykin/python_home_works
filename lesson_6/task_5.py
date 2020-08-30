"""Задача 6. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return f'{self.title} - Запуск отрисовки.'


class Pen(Stationary):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        return f'Пишем - {self.title}.'


class Pencil(Stationary):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        return f'Рисуем - {self.title}.'


class Handle(Stationary):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        return f'Выделяем текст - {self.title}.'


test = Stationary('Проверка')
print(test.draw() + '\n')

pen = Pen('ручкой')
print(pen.draw())

pencil = Pencil('карандашем')
print(pencil.draw())

handle = Handle('маркером')
print(handle.draw())
