import math


class Figure:
    sides_count = 0

    def __init__(self, sides, *color):
        self.set_color(*color)
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            return r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def __is_valid_side(self, *else_side):
        return len(else_side) == self.sides_count and all(isinstance(side, int) and side > 0 for side in else_side)

    def set_sides(self, *else_side):
        if self.__is_valid_side(*else_side):
            self.__sides = list(else_side)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__((radius,), *color)
        if self.get_sides()[0] > 0:
            self.__radius = self.get_sides()[0] / 2 / math.pi
        else:
            self.__radius = 0

    def get_square(self):
        return self.__radius ** 2 * math.pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(sides, *color)
        self.square = None

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        if all(isinstance(side, (int, float)) and side > 0 for side in (a, b, c)):
            return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__([side] * 12, *color)
        self.__sides = [side] * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((125, 222, 135), (10, 20, 50))

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

# Проверка площади (треугольника):
print(triangle1.get_square())
