import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * math.pi * 2

    def area(self):
        return self.radius ** 2 * math.pi
    