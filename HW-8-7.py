class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.x = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна:')
        return f'y = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно:')
        return f'y = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'x = {self.a} + {self.b} * i'


x_1 = ComplexNumber(5, -4)
x_2 = ComplexNumber(-6, 1)
print(f'x1: {x_1}')
print(f'x2: {x_2}')
print(x_1 + x_2)
print(x_1 * x_2)