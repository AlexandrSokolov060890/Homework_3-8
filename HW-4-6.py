from itertools import count, cycle

for el in count(int(input('Введите начальное число для итерации каждого пятого числа до 100: ')), 5):
    if el > 100:
        break
    else:
        print(el)

c = 0
my_list = [123, 'Help me.', True, None]
for el in cycle(my_list):
    if c > 18:
        break
    print(el)
    c += 1
