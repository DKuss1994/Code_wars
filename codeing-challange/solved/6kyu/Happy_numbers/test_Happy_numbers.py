import unittest
from Happy_numbers import is_happy

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_happy(7), True)
    def test_something(self):
        self.assertEqual(is_happy(16), False)


if __name__ == '__main__':
    unittest.main()
