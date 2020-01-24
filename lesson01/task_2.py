
sec = int(input('Введите секунды:  '))

sec = sec % (24 * 3600)                # граница 24 часа
h = sec // 3600
sec %= 3600
minutes = sec // 60
sec %= 60

print(f'{h}:{minutes}:{sec}')
