

def my_func(x, y, z):
    numbers = (x, y, z)
    sp = list(numbers)
    sp.remove(min(numbers))
    return sum(sp)


print(my_func(3, 2, 1))
