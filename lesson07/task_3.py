
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Слияние клетки теперь {self.quantity + other.quantity} ячеек'

    def __sub__(self, other):
        subtraction = self.quantity - other.quantity
        return f'Ячеек в клетке осталось {subtraction}' if subtraction > 0 else 'Клетки нет'

    def __mul__(self, other):
        return f'Ячейки умножились {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Ячейки разделились {self.quantity / other.quantity}'

    def make_order(self, line):
        result = ''
        for i in range(int(self.quantity / line)):
            result += '*' * line + '\n'
        result += '*' * (self.quantity % line)
        return result


cell = Cell(12)
cell2 = Cell(3)
print(cell.__add__(cell2))
print(cell + cell2)
print(cell - cell2)
print(cell * cell2)
print(cell / cell2)
print(cell.make_order(3))
