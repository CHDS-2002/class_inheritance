import os
import math

os.system('COLOR B')


class Figure:
    def __init__(self, filled: bool, __sides: list, __color: list, sides_count=0):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valied_color(r, g, b):
            self.r = r
            self.g = g
            self.b = b

    def __is_valid_sides(self, *sides):
        return bool(list(filter(lambda x: x > 0, *sides)))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides[i] = new_sides[i]


class Circle(Figure):
    def __init__(self, filled: bool, __sides: list, __color: list, __radius, sides_count=1):
        super().__init__(filled, __sides, __color, sides_count)
        self.__radius = __radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, filled: bool, __sides: list, __color: list, sides_count=3):
        super().__init__(filled, __sides, __color, sides_count)

    def get_square(self):
        p = sum(self.__sides) / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    def __init__(self, filled: bool, __sides: list, __color: list, sides_count=12):
        super().__init__(filled, __sides, __color, sides_count)
        self.__sides = [self.__sides[0] for i in range(len(self.__sides))]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

try:
    os.system('PAUSE')
except:
    os.system('CLS')
