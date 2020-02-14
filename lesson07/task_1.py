
class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        for line in self.my_matrix:
            for i in line:
                print(f'| {i:3}', end='')
            print('|')
        return '-----------'

    def __add__(self, other):
        for x in range(len(self.my_matrix)):
            for y in range(len(other.my_matrix[x])):
                self.my_matrix[x][y] = self.my_matrix[x][y] + other.my_matrix[x][y]
        return Matrix.__str__(self)


matrix = Matrix([[31, 22], [37, 43], [51, 86]])
second_matix = Matrix([[44, 32], [10, 9], [43, 89]])
print(matrix.__add__(second_matix))
