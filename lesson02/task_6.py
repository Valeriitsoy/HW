number = int(input('Введите номер товара:  '))
my_list = []
name_1 = []
price_1 = []
quantity_1 = []
unit_1 = []
i = 3
while number <= i:
    name = input('Введите название:  ')
    price = int(input('Введите цену:  '))
    quantity = int(input('Введите количество:  '))
    unit = input('Введите единцу измерения:  ')
    my_tuple = (number, {
        'название': name,
        'цена': price,
        'количество': quantity,
        'ед.': unit
    })
    my_list.append(my_tuple)
    number += 1

    name_1.append(name)
    price_1.append(price)
    quantity_1.append(quantity)
    unit_1.append(unit)
    unit_1 = list(set(unit_1))

    my_dict = {
        'название': name_1,
        'цена': price_1,
        'количество': quantity_1,
        'ед.': unit_1
    }
else:
    print(my_list)
    print(my_dict)
