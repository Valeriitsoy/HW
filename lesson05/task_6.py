
with open('t_6.txt') as f:
    result = []
    names = []
    hours = []
    for line in f:
        key, value, value1, value2 = line.split()
        names.append(key)
        key1 = [value.split('('), value1.split('('), value2.split('(')]
        for i in key1:
            i.pop()
            f = [int(x) for x in i]
            result.extend(f)
a = sum(result[0:3])
hours.append(a)
b = sum(result[3:5])
hours.append(b)
c = result[5]
hours.append(c)
print(dict(zip(names, hours)))
