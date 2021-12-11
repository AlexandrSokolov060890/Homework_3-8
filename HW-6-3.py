class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return (self._income.get('wage') + self._income.get('bonus')) * 0.87


h = Position('Lev', 'Tolstoy', 'Writer', 60000, 5000)
print(h.get_full_name())
print(h.position)
print(h.get_total_income())
