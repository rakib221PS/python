class Point:
    x, y = None, None
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def get_pos(self):
        return(self.x, self.y)

    def show(self):
        return "Point({}, {})".format(self.x, self.y)

    def __str__(self):
        return "Point("+str(self.x)+", "+str(self.y)+")"

point = Point(3,4)
print(point.get_pos())
assert point.__str__() == "Point(3, 4)"
print(point.x)