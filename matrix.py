"""
 Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
"""
import random


class Matrix2D:
    def __init__(self):
        '''
        Создание матрицы.
        '''
        self.matrix = []
        self.rows = 0
        self.columns = 0
        self.name = 'Unnamed'

    def __str__(self):
        return self.matrix

    def generate(self, rows, columns, verbose=False):
        '''
         Возвращает список списков, содержащих сумму индексов матрицы .
        int, int -> [[(int + int), ...], ...]
        '''
        self.rows = rows
        self.columns = columns
        self.matrix = [[(row + col + random.randint(1, 10)) for col in range(columns)] for row in range(rows)]

        return self.matrix

    def printme(self, verbose=False):
        '''
        Вывод матрицы построчно.
        '''
        if verbose:
            print(f'{self.rows}  {self.columns} matrix')
        for row in self.matrix:
            print(row)

    def __add__(self, other):
        new_rows = self.rows + other.rows
        new_columns = self.columns + other.columns


m_1 = Matrix2D()
m_2 = Matrix2D()
m_1.generate(4, 5, True)
m_2.generate(4, 5, True)
m_1.printme()
print('------------------')
m_2.printme()
print('------------------')
m = m_1 + m_2
print(m)
