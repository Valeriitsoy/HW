
with open('qwerty.txt') as f:
    lin = f.readlines()
    lines = 0
    for index, value in enumerate(lin):
        lines = index
        lines += 1
        words = len(value.split())
        print(f'Строка {index + 1} содержит {words} слов(а).')
print('Сумма строк:', lines)
