import unittest
import triangle


class TestTriangle(unittest.TestCase):
    '''
    Tests for triangle's functions.
    '''

    def test_area_positive(self):
        '''
        Testing area function with positive base and height.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated area matches expected value
        '''
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(6, 3.5), 10.5)

    def test_area_zero(self):
        '''
        Testing area function with zero base or height (edge cases).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that area equals 0 when base or height is 0
        '''
        self.assertEqual(triangle.area(0, 10), 0)
        self.assertEqual(triangle.area(10, 0), 0)
        self.assertEqual(triangle.area(0, 0), 0)

    def test_area_negative(self):
        '''
        Testing area function with negative base or height (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError for negative inputs
        '''
        with self.assertRaises(ValueError):
            triangle.area(-10, 5)
        with self.assertRaises(ValueError):
            triangle.area(10, -5)

    def test_perimeter_positive(self):
        '''
        Testing perimeter function with positive side lengths.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated perimeter matches expected value
        '''
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(2.5, 3.5, 4.5), 10.5)

    def test_perimeter_zero(self):
        '''
        Testing perimeter function with zero side lengths (edge cases).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts correct perimeter calculation when sides are 0
        '''
        self.assertEqual(triangle.perimeter(0, 4, 5), 9)
        self.assertEqual(triangle.perimeter(3, 0, 5), 8)
        self.assertEqual(triangle.perimeter(3, 4, 0), 7)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_negative(self):
        '''
        Testing perimeter function with negative side lengths (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError for negative inputs
        '''
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, -5)


if __name__ == '__main__':
    unittest.main()