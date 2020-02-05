from itertools import count
num = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_n = [el for el in num if num.count(el) == 1]

print(new_n)