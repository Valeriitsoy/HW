
my_list = input('введите данные:  ')

sp = my_list.split()
x = 1
for i in sp:
    print(f'{x}.', i[:10])
    x += 1
print('end')
