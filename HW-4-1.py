from sys import argv
script_name, time, rate, premium = argv
print("Выработка в часах: ", time)
print("Ставка в час: ", rate)
print("Премия: ", premium)
rez = (float(time) * float(rate)) + int(premium)
print(f'Заработная плата: {rez}')

# если без скрипта:
# def wage():
#     try:
#         time = int(input('Введите выработку работника в часах: '))
#         rate = float(input('Введите ставку работника в час: '))
#         premium = float(input('Введите размер премии работника: '))
#         rez = (time * rate) + premium
#         print(f'Заработная плата работника составляет: {rez}')
#     except:
#         return print('Это не число.')
# wage()
