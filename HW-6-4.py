class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        self.direction = direction
        return f'{self.name} повернула {self.direction}'

    def show_speed(self):
        return f'{self.name} передвигается на скорости {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} передвигается на скорости {self.speed}')

        if self.speed > 60:
            return f'{self.name} превысил скорость!'
        else:
            return f'{self.name} движется на допустимой скорости.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} передвигается на скорости {self.speed}')

        if self.speed > 40:
            return f'{self.name} превысил скорость!'
        else:
            return f'{self.name} движется на допустимой скорости.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} является полицейской машиной'


kia = TownCar(70, 'Белый', 'Kia', False)
porsche = SportCar(135, 'Чёрный', 'Porsche', False)
cat = WorkCar(30, 'Желтый', 'Caterpillar', True)
uaz = PoliceCar(110, 'Голубой', 'UAZ', True)
print(kia.turn('влево'))
print(f'Когда {cat.turn("вправо")}, тогда {porsche.stop()}')
print(kia.go())
print(kia.show_speed())
print(f'{kia.name} цвета {kia.color}')
print(porsche.show_speed())
print(cat.show_speed())
print(uaz.police())
print(uaz.show_speed())
print(f'{porsche.name} является полицейской машиной? {porsche.is_police}')
print(f'{kia.name} является полицейской машиной? {kia.is_police}')
print(f'Когда {uaz.name} тормозит {porsche.name}, водитель становится {kia.color}')
