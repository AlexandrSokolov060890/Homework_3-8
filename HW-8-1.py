class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if day >= 29 and month == 2:
                    return f'Это февраль!'
                if day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
                    return f'В этом месяце 30 дней.'
                if 2021 >= year >= 0:
                    return f'Всё впорядке.'
                else:
                    return f'Этот год ещё не наступил.'
            else:
                return f'Неверный месяц.'
        else:
            return f'Неправильный день.'

    def __str__(self):
        return f'Сегодня: {Data.extract(self.day_month_year)}'


today = Data('6 - 6 - 1799')
print(today)
print(Data.extract('3 - 10 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(3, 9, 2022))
print(Data.valid(31, 4, 2021))
print(Data.valid(29, 2, 2017))
print(today.valid(11, 13, 2015))
