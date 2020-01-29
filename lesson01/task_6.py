A = int(input('Ввести начальную дистанцию: '))

B = int(input('Ввести желаемую дистанцию: '))

days = 1
while A <= B:
    print(f'{days}-й день:', A)
    A = round(A + A * 0.1, 2)
    days += 1
else:
    print(f'на {days} день спортсмен достиг результата — не менее {B} км')
