from itertools import count, cycle

for i in count(10):
    if i > 20:
        break
    else:
        print(i)


result = 0
for el in cycle('PYTHON'):
    if result > 20:
        break
    print(el)
    result += 1
