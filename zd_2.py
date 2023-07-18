"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
📌 list-архивы также являются свойствами экземпляра
"""

class Archive:
    _archive = []
    _instance = None


    def __new__(cls, name, age):
        instance = super().__new__(cls)
        if cls._instance:
            cls._archive.append(cls._instance)
        cls._instance = instance
        instance.archive = cls._archive

        return cls._instance

        #cls.archive_dict[cls.instance] = super().__new__(cls, name, number)
        #instance = super().__new__(cls, name, number)

        #instance.numvalue = num_value
        #instance.strvalue = str_value
        #instance.count += 1
        #instance.old_instace = cls.instance if cls.instance.count_ == instance.count_ - 1



    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def __str__(self) -> str:
        return f'Игрок по имени {self.name} ({self.age} лет). До него были созданы игроки: {[pl.name for pl in self.archive]}'


    def __repr__(self) -> str:
        return f'{self.name} {self.age}'

arch_1 = Archive('kfbskd', 1)
arch_2 = Archive('sddwq', 2)
arch_3 = Archive('dffdfsefrfsddwq', 2341)

print(arch_1)
print(arch_1.archive)
print(arch_2)
print(arch_2.archive)

#Задание №4
#Доработаем класс Архив из задачи 2.
#Добавьте методы представления экземпляра для программиста
#и для пользователя.