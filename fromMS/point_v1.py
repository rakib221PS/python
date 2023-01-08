import math

class Point:
    
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
    
    def show(self):
        return f'Point({self.x}, {self.y})'




point1 = Point()
point1.set_x(3)
point1.set_y(4)

point2 = Point()
point2.set_x(0)
point2.set_y(0)

point3 = Point()
point3.set_x(1)
point3.set_y(1)

assert point1.get_x() == 3
assert point2.get_x() == 0
assert point3.get_x() == 1

assert point1.get_y() == 4
assert point2.get_y() == 0
assert point3.get_y() == 1

assert point1.get_pos() == (3, 4)
assert point2.get_pos() == (0, 0)
assert point3.get_pos() == (1, 1)

assert point1.norm() == 5.0
assert point2.norm() == 0.0
assert point3.norm() == math.sqrt(2)

assert point1.show() == "Point(3, 4)"
assert point2.show() == "Point(0, 0)"
assert point3.show() == "Point(1, 1)"