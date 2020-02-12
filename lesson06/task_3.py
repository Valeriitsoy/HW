
dict_income = {'wage': 2000, 'bonus': 500}


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum(dict_income.values())


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income


a = Position('Gerald', 'zRivii', 'Witcher')
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
