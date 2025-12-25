import unittest
import math
import circle


class TestCircle(unittest.TestCase):
    '''
    Tests for circle's functions.
    '''

    def test_area_positive(self):
        '''
        Testing area function with positive radius values.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated area matches expected value
        '''
        self.assertAlmostEqual(circle.area(5), math.pi * 25)
        self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5 * 2.5)

    def test_area_zero(self):
        '''
        Testing area function with zero radius (edge case).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that area with radius 0 equals 0
        '''
        self.assertEqual(circle.area(0), 0)

    def test_area_negative(self):
        '''
        Testing area function with negative radius (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError
        '''
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_perimeter_positive(self):
        '''
        Testing perimeter function with positive radius values.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated perimeter matches expected value
        '''
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)

    def test_perimeter_zero(self):
        '''
        Testing perimeter function with zero radius (edge case).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that perimeter with radius 0 equals 0
        '''
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_negative(self):
        '''
        Testing perimeter function with negative radius (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError
        '''
        with self.assertRaises(ValueError):
            circle.perimeter(-3)


if __name__ == '__main__':
    unittest.main()