
class DigitErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def digit():
    my_list = []
    while True:
        a = input('Введите число:  ')
        try:
            if a == 'stop':
                break
            elif a.isdigit() is True:
                my_list.append(a)
            elif a.isdigit() is False:
                raise DigitErr('ОШИБКА!!!Введите число')
        except DigitErr as err:
            print(err)

    print(my_list)


digit()
