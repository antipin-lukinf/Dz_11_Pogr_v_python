"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import datetime


class My_string(str):
    """Строка документации для класса"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

first_string = My_string('Im', 'write')
print(first_string)
print(first_string.name)
print(first_string.date)

new_e = My_string('lsdfjslkjs,', 1)
help(My_string)