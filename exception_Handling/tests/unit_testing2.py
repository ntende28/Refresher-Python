# unit_testing2.py
# Importing unittest framework
import unittest

'''
Method 								Equivalent
assertEqual(condition, exp, error) 	Evaluates if a condition evaluates to expected 
									output (exp), if not returns error

assertIn(variable, container) 		Checks if variable exists in container

assertTrue(bool) 					Evaluates if the condition(bool) evaluates to true

assertLess(value1, value2)			checks that the first argument is less than the second one

assertAlmostEqual(val1, val2)		checks that their difference, when rounded to 7 decimal 
									places, is 0. In other words, if they are almost equal.
'''

# Function that gets tested
def times_ten(number):
    return number * 100

# Test class
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')

    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')

# Run the tests
unittest.main()
