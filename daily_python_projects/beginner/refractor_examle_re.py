# Lets write a simpel code of distance between two point and refactor that code with class
#

from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return  f'Point {self.x} and {self.y}'

    def __abs__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def distance(self,p):
        diff = self - p
        distance = sqrt(diff.x **2 * diff.y ** 2)
        return  distance

if __name__ == "__main__":
    x = Point(1, 0)
    y = Point(5, 3)

    print(f'Distance between {x} and {y} is {x.distance(y)}')

