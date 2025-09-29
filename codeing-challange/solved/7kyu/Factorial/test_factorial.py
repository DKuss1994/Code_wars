import unittest
from main import factorial


class TestFactorial(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)

    def test_case_upper_12(self):
        with self.assertRaises(ValueError):
            factorial(13)

    def test_case_under_0(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == '__main__':
    unittest.main()
