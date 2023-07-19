"""
 Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
"""


class Matrix(object):
    """Класс Матрица"""
    def __init__(self, list2D):
        self.list2D = list2D
        self.dim_R = len(self.list2D)
        self.dim_C = len(self.list2D[0])

    def __repr__(self):
        res = ''
        for x in self.list2D:
            s = ''
            for y in x:
                s += str(y) + '    '
            res += s.strip() + '\n'
        return res.strip()

    def __add__(self, other):
        """Метод складывания матриц"""
        if self.dim_R == other.dim_R and self.dim_C == other.dim_C:
            result = []
            res = []
            for x in range(self.dim_R):
                for y in range(self.dim_C):
                    sum = self.list2D[x][y] + other.list2D[x][y]
                    res.append(sum)
                result.append(res)
                res = []
            return Matrix(result)
        else:
            return 'Размерности не совпадают'

    def __sub__(self, other):
        """Метод вычитания матриц"""
        if self.dim_R == other.dim_R and self.dim_C == other.dim_C:
            res = []
            result = []
            for x in range(self.dim_R):
                for y in range(self.dim_C):
                    sub = self.list2D[x][y] - other.list2D[x][y]
                    res.append(sub)
                result.append(res)
                res = []
            return Matrix(result)
        else:
            return 'Размерности не совпадают'

    def __mul__(self, other):
        """Метод умножения матриц"""
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.list2D]
            return Matrix(result)
        elif self.dim_C != other.dim_R:
            return 'Нельзя перемножить матрицы таких размерностей'
        else:
            a = range(self.dim_C)
            b = range(self.dim_R)
            c = range(other.dim_C)
            result = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)


m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
m2 = Matrix([[3, 1, 3], [5, 2, 8], [6, 8, 4]])
print(m1)
print('------------------')
print(m2)
print('------------------')
print(m1 == m2)
print('------------------')
print(m1 + m2)
print('------------------')
print(m1 * m2)

help(Matrix)
