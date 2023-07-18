"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    def __init__(self, long, width=None):
        self.long = long
        self.width = width

    def perimeter(self):
        if not self.width:
            perim = self.long * 4
        else:
            perim = self.long * 2 + self.width * 2

        return perim

    def plosh(self):
        if not self.width:
            return self.long ** 2
        else:
            return self.long * self.width

    def __add__(self, other):
        new_long = self.long + other.long
        new_width = self.width + other.width
        return Rectangle(new_long, new_width)

    def __sub__(self, other):
        if self.long - other.long < 0 or self.width - other.width < 0:
            raise ValueError
        new_long = self.long - other.long
        new_width = self.width - other.width
        return Rectangle(new_long, new_width)

    def __eq__(self, other):
        return other.plosh() == self.plosh()

    def __gt__(self, other):
        return self.plosh() > other.plosh()


"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""

sq_1 = Rectangle(10, 6)
sq_2 = Rectangle(2, 1)
sq_3 = sq_1 + sq_2
sq_4 = sq_1 - sq_2

print(sq_3.perimeter())
print(sq_4.perimeter())

# sq_5 = sq_2 - sq_1

print(sq_1 > sq_2)
print(sq_1 < sq_2)
print(sq_1 == sq_2)
print(sq_1 != sq_2)
print(sq_1 >= sq_2)

"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""
