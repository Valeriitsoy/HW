
my_list = [7, 5, 3, 3, 2]

number = int(input('Введите число: '))

max_number = max(my_list)
min_number = min(my_list)
if number < min_number:
    my_list.append(number)
    print(my_list)
elif number > max_number:
    my_list.insert(0, number)
    print(my_list)
elif number in my_list:
    my_list.insert(my_list.index(number), number)
    print(my_list)
elif number > min_number:
    my_list.append(number)
    my_list.sort(reverse=True)
    print(my_list)

print('end')
