class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани для пошива  \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани для пошива пальто {self.square_coat}'


class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_jacket = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для пошива костюма {self.square_jacket}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(coat.get_sq_full)
print(jacket.get_square_coat())
print(jacket)
print(jacket.get_sq_full)
print(jacket.get_square_jacket())