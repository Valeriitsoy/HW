receipt = int(input('Введите выручку: '))
costs = int(input('Введите затраты: '))
workers = int(input('Введите количество сотрудников: '))

if receipt > costs:
    profit = receipt - costs
    print('Ваша прибыль:', profit, '$')
    print('Рентабельность:', round((profit / receipt) * 100, 2), '%')
    print('Прибыль на одного сотрудника:', round(profit/workers, 2), '$')
else:
    print('Ваш убыток:', receipt - costs, '$')


