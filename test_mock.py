# test_calculator.py

import unittest
from calculator import add  # Importing the function we want to test

class TestCalculator(unittest.TestCase):  # Creating a test class

    def test_add(self):
        result = add(2, 3)  # Using our add function
        self.assertEqual(result, 5)  # Checking if result is 5

        # # Let's add more checks
        # self.assertEqual(add(0, 0), 0)  # 0 + 0 should be 0
        # self.assertEqual(add(-1, 2), 0)  # -1 + 1 should be 0

if __name__ == '__main__':
    unittest.main()  # Run all tests when the file is executed
