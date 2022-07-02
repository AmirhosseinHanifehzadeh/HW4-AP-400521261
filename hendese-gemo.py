from abc import ABC, abstractmethod
from math import pi, sqrt

class Shape(ABC):
    @abstractmethod
    def get_erea(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Circle(Shape):
    formula = ['perimeter: 2*pi * radius', 'Erea: pi * radius ** 2 ']
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if type(val) != float:
            return TypeError('radius should be float!')
        self._radius = val


    def get_erea(self):
        return f"Erea: {self.radius ** 2 * pi}"

    def get_perimeter(self):
        return f"Perimeter: {self.radius * pi * 2}"

    def __str__(self):
        return f"Circle: radius={self.radius}"


class Triangle(Shape):
    formula = ['perimeter: a + b + c', 'erea: sqrt(s * (s - self.firstSide) * (s - self.secSide) * (s - self.thirdSide)) [s = (a + b + c) / 2]']
    def __init__(self, a, b, c):
        self.firstSide = a
        self.secSide = b
        self.thirdSide = c

    @property
    def firstSide(self):
        return self._firstSide
    
    @firstSide.setter
    def firstSide(self, val):
        if type(val) != float:
            raise TypeError('your first side should be float')
        self._firstSide = val

    @property
    def secSide(self):
        return self._secSide
    
    @secSide.setter
    def secSide(self, val):
        if type(val) != float:
            raise TypeError('your second side should be float')
        self._secSide = val

    @property
    def thirdSide(self):
        return self._thirdSide
    
    @thirdSide.setter
    def thirdSide(self, val):
        if type(val) != float:
            raise TypeError('your third side should be float')
        self._thirdSide = val
    
    def get_erea(self):
        s = (self.firstSide + self.secSide + self.thirdSide) / 2
        return f"Erea: {sqrt(s * (s - self.firstSide) * (s - self.secSide) * (s - self.thirdSide))}"

    def get_perimeter(self):
        return f"Perimeter: {self.firstSide + self.secSide + self.thirdSide}"

    def __str__(self):
        return f"triangle: firstside={self.firstSide} secondSide={self.secSide} thirdSide={self.thridSide}"

    
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a,a,a)
  
    def __str__(self):
        return f"trianlge: triangleside={self.firstSide}"

class Rectangle(Shape):
    formula = ['Perimeter: 2(lenght  + widht)' ,'Erea: lenght * widht']
    def __init__(self, a, b):
        self.lenght = a
        self.widht = b

    @property
    def lenght(self):
        return self._lenght
    @lenght.setter
    def lenght(self, val):
        if type(val) != float:
            raise TypeError('type of lenght should be float!')
        self._lenght = val

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val):
        if type(val) != float:
            raise TypeError('type of width should be float!')
        self._width = val

    def get_erea(self):
        return f"Erea: {self.widht * self.lenght}"
    
    def get_perimeter(self):
        return f"Perimeter: {2 * (self.widht + self.lenght)}"
    
    def __str__(self):
        return f"Rectangle: lenght={self.lenght} width={self.widht}"

class Square(Rectangle):
    formula = ['perimeter: 4(side)', 'Erea: side ** 2']
    def __init__(self, a):
        super().__init__(a, a)

    def get_erea(self):
        return super().get_erea()

    def get_perimeter(self):
        return super().get_perimeter()

    def __str__(self):
        return super().__str__()


class RegularPantagon(Shape):
    formula = ['Perimeter: side * 5', 'Erea: ((sqrt(5 * (5 + 2 * sqrt(5)))) / 4) * self.side ** 2']
    def __init__(self, a):
        self.side = a

    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, val):
        if type(val) != float:
            raise TypeError('type of side should be float')
        self._side = val

    def get_erea(self):
        return f"Erea: {((sqrt(5 * (5 + 2 * sqrt(5)))) / 4) * self.side ** 2}"

    def get_perimeter(self):
        return f"Perimeter: {self.side * 5}"

    def __str__(self):
        return f"Pantagon: side={self.side}"


class ShapeList:
    shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            ShapeList.shapes.append(shape)
        else:
            raise TypeError
    @staticmethod
    def get_largest_shape_by_perimeter(self):
        perimeter_list = []

        for shape in ShapeList.shapes:
            perimeter_list.append(shape.get_perimeter())
        return ShapeList.shapes[perimeter_list.index(max(perimeter_list))]
    @staticmethod
    def get_largest_shape_by_erea():
        erea_list = []

        for shape in ShapeList.shapes:
            erea_list.append(shape.get_erea())
        return ShapeList.shapes[erea_list.index(max(erea_list))]
