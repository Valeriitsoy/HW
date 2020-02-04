

def fac(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield i
    print(factorial)


for el in fac(10):
    print(el)
