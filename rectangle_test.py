import unittest
import rectangle


class TestRectangle(unittest.TestCase):
    '''
    Tests for rectangle's functions.
    '''

    def test_area_positive(self):
        '''
        Testing area function with positive side lengths.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated area matches expected value
        '''
        self.assertEqual(rectangle.area(5, 10), 50)
        self.assertEqual(rectangle.area(3, 7), 21)

    def test_area_zero(self):
        '''
        Testing area function with zero side lengths (edge cases).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that area equals 0 when at least one side is 0
        '''
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_area_negative(self):
        '''
        Testing area function with negative side lengths (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError for negative inputs
        '''
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)
        with self.assertRaises(ValueError):
            rectangle.area(5, -10)

    def test_perimeter_positive(self):
        '''
        Testing perimeter function with positive side lengths.
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that calculated perimeter matches expected value
        '''
        self.assertEqual(rectangle.perimeter(5, 10), 30)
        self.assertEqual(rectangle.perimeter(3, 7), 20)

    def test_perimeter_zero(self):
        '''
        Testing perimeter function with zero side lengths (edge cases).
        ARGUMENTS:
            * None (uses hardcoded test values)
        RETURNS:
            * Asserts correct perimeter calculation when sides are 0
        '''
        self.assertEqual(rectangle.perimeter(0, 10), 20)
        self.assertEqual(rectangle.perimeter(5, 0), 10)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_negative(self):
        '''
        Testing perimeter function with negative side lengths (invalid input).
            ARGUMENTS:
                * None
            RETURNS:
                * Asserts that function raises ValueError for negative inputs
        '''
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 10)
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -10)


if __name__ == '__main__':
    unittest.main()