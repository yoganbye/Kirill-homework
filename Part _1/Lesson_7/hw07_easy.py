# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C

        def len_line(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

        self.ab = len_line(self.a, self.b)
        self.bc = len_line(self.b, self.c)
        self.ca = len_line(self.c, self.a)

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def area (self):
        semi_perimeter = self.perimeter() / 2      
        return math.sqrt(semi_perimeter * (semi_perimeter - self.ab) * \
            (semi_perimeter - self.bc) * (semi_perimeter - self.ca))

    def height(self):
        return self.area() / (2 * self.ab) 


treugolnik = Triangle((7,3), (4,8), (6,7))

print(treugolnik.__dict__)
print('Периметр', treugolnik.perimeter())
print('Площадь', treugolnik.area())
print('Высота', treugolnik.height())




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Trapezoid:
    'Равнобедренная трапеция — это трапеция у котрой боковые стороны равны.'

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def len_line(self):
        self.ab = self.math_len_line(self.a, self.b)
        self.bc = self.math_len_line(self.b, self.c)
        self.cd = self.math_len_line(self.c, self.d)
        self.da = self.math_len_line(self.d, self.a)

        self.diagonal_ac = self.math_len_line(self.a, self.c)
        self.diagonal_bd = self.math_len_line(self.b, self.d)
        return {'ab' : self.ab, 'bc' :self.bc, 'cd': self.cd, 'da' : self.da}

    @staticmethod
    def math_len_line(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def perimetr(self):
        return self.ab + self.bc + self.cd + self.da

    def area(self):
        result = self.triangle_area(self.ab, self.bc, self.diagonal_ac) + \
            self.triangle_area(self.da, self.cd, self.diagonal_bd)
        return result
        
    @staticmethod
    def triangle_area(len1, len2, len3):
        semi_perimeter = (len1 + len2 + len3) / 2      
        return math.sqrt(semi_perimeter * (semi_perimeter - len1) * \
            (semi_perimeter - len2) * (semi_perimeter - len3))

    def isTrapeze(self):
        return True if self.diagonal_ac == self.diagonal_bd else False


trapez1 = Trapezoid((8,2), (6,3), (7,4), (9,9))
print(Trapezoid.__doc__)
print("Координаты точек", trapez1.__dict__)
print('Длины сторон', trapez1.len_line())
print('Периметр', trapez1.perimetr())
print('Площадь', trapez1.area())
print('Трапеция равнобедренная:', trapez1.isTrapeze())
