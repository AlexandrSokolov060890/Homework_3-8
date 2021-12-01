def div():
    try:
        up = int(input('Введите первое число: '))
        down = int(input('Введите второе число: '))
        return (up / down)
    except ZeroDivisionError:
        return 'На ноль нельзя...'
print(div())
