with open('text.txt', 'w') as f:
    while True:
        text = input('Введите данные:  ')
        if text == '':
            break
        f.write(text + '\n')
print('END')
