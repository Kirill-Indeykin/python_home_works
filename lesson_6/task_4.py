"""Задача 4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    # Свойства машины
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        """
        Параметры машины:
        :param speed: - скорость (float).
        :param color: - цвет (str).
        :param name: - марка (str).
        :param is_police: - тип (bool).
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'"{self.name}" - движение.'

    def stop(self):
        return f'"{self.name}" - остановилась.'

    def turn_right(self):
        return f'"{self.name}" - совершила поворот на право.'

    def turn_left(self):
        return f'"{self.name}" - совершила поворот на лево.'

    def show_speed(self):
        return f'Текущая скорость "{self.name}" = {self.speed} км/ч.'


class TownCar(Car):
    # Свойства городской машины
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        """
        Параметры машины:
        :param speed: - скорость (float).
        :param color: - цвет (str).
        :param name: - марка (str).
        :param is_police: - тип (bool).
        """
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость "{self.name}" = {self.speed} км/ч.')

        if self.speed > 60:
            return f'Превышение скорости "{self.name}" на: {abs(60 - self.speed)} км/ч.'
        else:
            return f'Движение по городу "{self.name}" без нарушений скоростного режима.'


class SportCar(Car):
    # Свойства спортивной машины
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        """
        Параметры машины:
        :param speed: - скорость (float).
        :param color: - цвет (str).
        :param name: - марка (str).
        :param is_police: - тип (bool).
        """
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    # Свойства рабочей машины
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        """
        Параметры машины:
        :param speed: - скорость (float).
        :param color: - цвет (str).
        :param name: - марка (str).
        :param is_police: - тип (bool).
        """
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость "{self.name}" = {self.speed} км/ч.')

        if self.speed > 60:
            return f'Превышение скорости "{self.name}" на: {abs(60 - self.speed)} км/ч.'
        else:
            return f'Движение по городу "{self.name}" без нарушений скоростного режима.'


class PoliceCar(Car):
    # Свойства полицейской машины
    def __init__(self, speed, color, name, is_police):
        """
        Параметры машины:
        :param speed: - скорость (float).
        :param color: - цвет (str).
        :param name: - марка (str).
        :param is_police: - тип (bool).
        """
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Полицейская машина - "{self.name}"'
        else:
            return f'Машина "{self.name}" гражданская.'


# Параметры спортивной машины:
ferrari = SportCar(200, 'Желтый', 'Ferrari', False)
# Параметры городской машины:
lada = TownCar(50, 'Красная', 'Lada', False)
# Параметры рабочей машины:
gazel = WorkCar(70, 'Серая', 'Gazel', False)
# Параметры полицейской машины
ford = PoliceCar(110, 'Голубая',  'Ford', True)

# Проверка:
print('\n' + ferrari.turn_left())
print(f'{ferrari.show_speed()}')
print(f'Цвет машины марки: "{ferrari.name}" - {ferrari.color}.')
print(f'Машина марки: "{ferrari.name}" полицейская? - {ferrari.is_police}')

print('\n' + lada.turn_right())
print(f'{lada.show_speed()}')
print(f'Цвет машины марки: "{lada.name}" - {lada.color}.')
print(f'Машина марки: "{lada.name}" полицейская? - {lada.is_police}')

print('\n' + gazel.turn_left())
print(f'{gazel.show_speed()}')
print(f'Цвет машины марки: "{gazel.name}" - {gazel.color}.')
print(f'Машина марки: "{gazel.name}" полицейская? - {gazel.is_police}')

print('\n' + ford.turn_right())
print(f'{ford.show_speed()}')
print(f'Цвет машины марки: "{ford.name}" - {ford.color}.')
print(f'Машина марки: "{ford.name}" полицейская? - {ford.is_police}')
