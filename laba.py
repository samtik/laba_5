import math

class Color_shape():
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

    def choose_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def repr(self):
        return [self.height,self.width, self.square, self.r, self.g,self.b]

    def name(self):
        return self.type()


class RectangLe(Color_shape):
    def __init__(self, H, W, r, g, b):
        self.height = H
        self.width = W
        self.square = 0
        self.r = r
        self.g = g
        self.b = b

    def S(self):
        self.square = self.width * self.height

    def type(self):
        return 'Прямоугольник'

class Circle(Color_shape):
     def __init__(self, R, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.R = R
        self.square = 0

     def S(self):
        self.square = math.pi * (self.R ** 2)

     def type(self):
         return 'Круг'

class Square(RectangLe):
     def __init__(self, H, r, g, b):
        self.height = H
        self.width = H
        self.square = 0
        self.r = r
        self.g = g
        self.b = b

     def type(self):
         return 'Квадрат'


class Point():
     def __init__(self):
        self.x = 0
        self.y = 0

     def get(self):
         return self.x, self.y

     def set(self, x, y):
        self.x = x
        self.y = y

class Figure():
     def _init__(self, r, x, y):
        '''
        self.H = H
        self.W = W
        '''
        self.r = r
        self.x = x
        self.y = y


     def is_in(self,n):
        '''
        if n.get()[0] > self.x and n.get()[0] < (self.x + self.W):
            if n.get()[1] > self.y and n.get()[1] < (self.y + self.H):
                return 'True'
        '''
        if ((n.get()[0] - self.x) ** 2 + (n.get()[1] - self.y) ** 2) ** 0.5 < n:
            return 'True'
        return 'False'


n = Point()
n.set(20, 20)
F = Figure(100, 100, -10000, -10000)
print(F.is_in(n))
