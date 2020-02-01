def my_func():
    result = []
    stop = 0
    while stop != 1:
        my_list = list(input('Введите числа через пробел:  ').split())
        try:
            for i in my_list:
                if i == '/':
                    my_list.remove('/')
                    digit = map(int, my_list)
                    sum_list = sum(digit)
                    result.append(sum_list)
                    stop += 1
                    print(sum(result), '\n', '-------END-------')
                    break
            else:
                digit_1 = map(int, my_list)
                sum_list_1 = sum(digit_1)
                result.append(sum_list_1)
                print(sum(result))
        except ValueError:
            print('Ошибка! Введите числа через пробел или </> для выхода')


my_func()
