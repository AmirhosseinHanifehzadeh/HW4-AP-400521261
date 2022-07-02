import Gemo

print('Learn Geometry')

while True:
    print("""
    What do you want to do?
    (1) Add new shape
    (2) Show all shapes
    (3) Show shape with the largest perimeter
    (4) Show shape with the largest area
    (5) Show formulas
    (0) Exit program""")
    n = int(input())    
    if n == 1:
        print("""
        (1) Triangle
        (2) Circle
        (3) Equilateraltriangle
        (4) Rectangle
        (5) square
        (6) Regular pantagon
        """)
        m = int(input())
        if m == 1:
            shape_list = Gemo.ShapeList()
            first_side = int(input('first side: '))
            second_side = int(input('second side: '))
            third_side = int(input('third side: '))
            shape_list.add_shape(Gemo.Triangle(first_side, second_side, third_side)) 
        elif m == 2:
            radius = int(input('radius: '))
            shape_list.add_shape(Gemo.Circle(radius))
        elif m == 3:
            side = int(input('side: '))
            shape_list.add_shape(Gemo.EquilateralTriangle(side))
        elif m == 4:
            lenght = int(input('lenght: '))
            width = int(input('width: '))
            shape_list.add_shape(Gemo.Rectangle(lenght, width))
        elif m == 5:
            side = int(input('side: '))
            shape_list.add_shape(Gemo.Square(side))
        elif m == 6:
            side = int(input('side: '))
            shape_list.add_shape(Gemo.RegularPantagon(side))
        
    elif n == 2:
        pass
    elif n == 3:
        pass
    elif n == 4:
        pass
    elif n == 5:
        print("""
        (1) Triangle
        (2) Circle
        (3) Equilateraltriangle
        (4) Rectangle
        (5) square
        (6) Regular pantagon
        """)
        m = int(input())
        if m == 1:
            print('Permeter' + Gemo.Triangle.formula[0])
            print('Erea:' + Gemo.Triangle.formula[1])
        elif m == 2:
            print('Permeter' + Gemo.Circle.formula[0])
            print('Erea:' + Gemo.Circle.formula[1])
        elif m == 3:
            print('Permeter' + Gemo.EquilateralTriangle.formula[0])
            print('Erea:' + Gemo.EquilateralTriangle.formula[1])
        elif m == 4:
            print('Permeter' + Gemo.Rectangle.formula[0])
            print('Erea:' + Gemo.Rectangle.formula[1])
        elif m == 5:
            print('Permeter' + Gemo.Square.formula[0])
            print('Erea:' + Gemo.Square.formula[1])
        elif m == 6:
            print('Permeter' + Gemo.RegularPantagon.formula[0])
            print('Erea:' + Gemo.RegularPantagon.formula[1])


    elif n == 0:
        break

# gemo files codes 
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
