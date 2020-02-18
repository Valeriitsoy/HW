from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('.')

    @classmethod
    def digit(cls, data):
        try:
            day, month, year = map(int, data.split('.'))
            print(f'{type(day), day,type(month), month,type(year), year}')
        except ValueError:
            print('Wrong data')

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('.')
            date(int(year), int(month), int(day))
            print('Ok')
        except ValueError:
            print('Wrong date')


Data.digit('10.11.2020')
Data.valid("21.01.2012")

