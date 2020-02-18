
class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        dividend = int(input('Делимое: '))
        divider = int(input('Делитель: '))
        if divider == 0:
            raise Zero('Делить на ноль нельзя')
        print(dividend / divider)
    except Zero as err:
        print(err)


division()
