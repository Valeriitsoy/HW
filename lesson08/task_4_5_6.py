
class Storage:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price


class Value(Exception):
    def __init__(self, txt):
        self.txt = txt


class Equipment(Storage):
    @staticmethod
    def my_list():
        try:
            name = input('Введите название: ')
            qty = input('Введите количество: ')
            if qty.isdigit() is False:
                raise Value('Ошибка. Введите количество.')
            price = input('Введите цену: ')
            if price.isdigit() is False:
                raise Value('Ошибка. Введите цену')
            department = input('Введите отдел:  ')
            count = {'Название': name, 'количество': qty, 'цена': price, 'отдел': department}
            print(count)
        except Value as err:
            print(err)


class Printer(Equipment):
    pass


class Scanner(Equipment):
    pass


class Xerox(Equipment):
    pass


Printer.my_list()
Scanner.my_list()
Xerox.my_list()
