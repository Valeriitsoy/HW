
a = input('ввести значение: ')
new_a = list(a)

x = 0
for i in range(int(len(new_a) / 2)):
    new_a[x], new_a[x + 1] = new_a[x + 1], new_a[x]
    x += 2

print(new_a)

