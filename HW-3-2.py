name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = input('Введите ваш год рождения: ')
city = input('Введите ваш город обитания: ')
mail = input('Введите вашу почту: ')
phone = input('Введите ваш телефон: ')
def user(name, surname, year, city, mail, phone):
    return ' '.join([name, surname, year, city, mail, phone])
print(user(name, surname, year, city, mail, phone))
