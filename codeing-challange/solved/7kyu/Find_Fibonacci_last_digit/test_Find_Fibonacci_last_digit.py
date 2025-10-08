import unittest
from Find_Fibonacci_last_digit import get_last_digit


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_last_digit(1), 1)
    def test_2(self):
        self.assertEqual(get_last_digit(21),6 )
    def test_3(self):
        self.assertEqual(get_last_digit(302),1)
    def test_3(self):
        self.assertEqual(get_last_digit(4003),7)
    def test_3(self):
        self.assertEqual(get_last_digit(50004),8)


if __name__ == '__main__':
    unittest.main()
