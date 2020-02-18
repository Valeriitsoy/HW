
class CompNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        x = complex(self.a, self.b)
        y = complex(other.a, other.b)
        return f'Сумма комплексных чисел z ={x + y}'

    def __mul__(self, other):
        x = complex(self.a, self.b)
        y = complex(other.a, other.b)
        return f'Произведение равно z={x * y}'


av = CompNum(1, 2)
bc = CompNum(3, 6)
print(av + bc)
print(av * bc)
