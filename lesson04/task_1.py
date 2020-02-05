from sys import argv

script_name, hours_param, payment_param, bonus_param = argv

salary = int(hours_param) * int(payment_param) + int(bonus_param)

print('Долг по ЗП:', salary)
