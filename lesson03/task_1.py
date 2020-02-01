def div():
    div_number = int(input('Введите делимое:  '))
    number = int(input('Введите делитель:  '))
    try:
        return div_number / number

    except ZeroDivisionError:
        print('Делить на ноль нельзя')


print(div())




