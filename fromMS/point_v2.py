import math

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_pos(self):
        return (self.x, self.y)

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'


point1 = Point()  # Uses the default values x=0 and y=0
point2 = Point(3, 4)
point3 = Point(1, 1)

assert point1.get_x() == 0
assert point2.get_x() == 3
assert point3.get_x() == 1

assert point1.get_y() == 0
assert point2.get_y() == 4
assert point3.get_y() == 1

assert point1.get_pos() == (0, 0)
assert point2.get_pos() == (3, 4)
assert point3.get_pos() == (1, 1)

assert point1.norm() == 0.0
assert point2.norm() == 5.0
assert point3.norm() == math.sqrt(2)

assert str(point1) == "Point(0, 0)"
assert str(point2) == "Point(3, 4)"
assert str(point3) == "Point(1, 1)"

point1 = Point()
point2 = Point()

point1.set_x(3)
assert point1.get_x() == 3

point2.set_x(0)
assert point2.get_x() == 0

point1.set_y(4)
assert point1.get_y() == 4

point2.set_y(0)
assert point2.get_y() == 0