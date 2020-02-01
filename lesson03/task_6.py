def int_func(word):
    return word.capitalize()


print(int_func('text'))


print(list(map(int_func, input('Введите набор слов на латинце в нижнем регситре:  ').split())))


