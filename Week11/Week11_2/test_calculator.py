import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_root(self):
        self.assertAlmostEqual(root(27, 3), 3)
        with self.assertRaises(ValueError):
            root(10, 0)

    def test_sine(self):
        self.assertAlmostEqual(sine(90), 1, places=5)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1, places=5)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1, places=5)

if __name__ == '__main__':
    unittest.main()
