from itertools import count
with open('t_5.txt', 'w') as f:
    for el in count(1):
        if el > 5:
            break
        else:
            num = str(el)
            f.write(num)
            f.write(' ')
with open('t_5.txt') as f:
    for line in f:
        value = line.split()
        num = map(int, value)
        sum_num = sum(num)
        print(sum_num)

