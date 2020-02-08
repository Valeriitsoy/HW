
with open('salary.txt') as f:
    workers_dict = {}
    workers = 0
    result = []
    for line in f:
        key, value = line.split()
        workers_dict[key] = value
        workers += 1
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
        result.append(float(value))
print('Средняя ЗП:', round(sum(result) / workers, 2))
