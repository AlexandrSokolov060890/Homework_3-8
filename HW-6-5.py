class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас в руках {self.title}. Пишем ручкой.'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас в руках {self.title}. Рисуем карандашом.'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'У вас в руках {self.title}. Раскрашиваем маркером.'


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
