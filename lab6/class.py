class Point:

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def get_pos(self):
        return(self.x, self.y)

    def show(self):
        return "Point({}, {})".format(self.x, self.y)

point = Point()
point.set_x(3)
point.set_y(4)
print(point.get_pos())
assert point.show() == "Point(3, 4)"
