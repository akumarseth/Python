import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def tst_area(self):
        #Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 1)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value error are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        #make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area,3_5j)
        self.assertRaises(TypeError, circle_area,True)
        self.assertRaises(TypeError, circle_area,"radius")
