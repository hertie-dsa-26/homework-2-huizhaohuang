import unittest 
import math
from circle import Circle

class TestSomething(unittest.TestCase):

    def test_perimeter_1(self):         
        c = Circle(1) 
        result = c.perimeter()
        self.assertAlmostEqual(result, 1 * 2 * math.pi)  

    def test_perimeter_6(self):         
        c = Circle(6) 
        result = c.perimeter()
        self.assertAlmostEqual(result, 6 * 2 * math.pi)  
    
    def test_area_1(self):         
        c = Circle(1) 
        result = c.area()
        self.assertAlmostEqual(result, 1 ** 2 * math.pi)  

    def test_area_6(self):         
        c = Circle(6) 
        result = c.area()
        self.assertAlmostEqual(result, 6 ** 2 * math.pi)  