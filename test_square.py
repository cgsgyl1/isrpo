
Яна Левина <ya2006lev@gmail.com>
14:06 (1 час назад)
кому: мне

import unittest
import square


class TestSquare(unittest.TestCase):
    '''
    Tests for square's functions.
    '''

    def test_area_positive(self):
        '''
        Testing area function with positive side length.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated area matches expected value
        '''
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(2.5), 6.25)

    def test_area_zero(self):
        '''
        Testing area function with zero side length (edge case).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that area with side 0 equals 0
        '''
        self.assertEqual(square.area(0), 0)

    def test_area_negative(self):
        '''
        Testing area function with negative side length (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError
        '''
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_perimeter_positive(self):
        '''
        Testing perimeter function with positive side length.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated perimeter matches expected value
        '''
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_zero(self):
        '''
        Testing perimeter function with zero side length (edge case).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that perimeter with side 0 equals 0
        '''
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_negative(self):
        '''
        Testing perimeter function with negative side length (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError
        '''
        with self.assertRaises(ValueError):
            square.perimeter(-3)


if __name__ == '__main__':
    unittest.main()