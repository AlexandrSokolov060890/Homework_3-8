from itertools import count
from math import factorial
numb = int(input('Введите число: '))


def fact(numb):
    for el in count(1):
        yield factorial(el)


x = 0
for el in fact(numb):
    if x < numb:
        print(el)
        x += 1
    else:
        break
