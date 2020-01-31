
season = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}
month = int(input('Введите номер месяца:  '))
for key in season.keys():
    if month in season[key]:
        print(key)
