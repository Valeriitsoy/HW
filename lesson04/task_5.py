from functools import reduce

numbers = [el for el in range(100, 1001) if el % 2 == 0]


def my_f(pr_i, i):
    return pr_i + i


print(numbers)
print(reduce(my_f, numbers))

