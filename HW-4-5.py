from functools import reduce
list = [el for el in range(100, 1001) if el % 2 ==0]
print(list)
def func(i, n):
    return i * n
print(reduce(func, list))
