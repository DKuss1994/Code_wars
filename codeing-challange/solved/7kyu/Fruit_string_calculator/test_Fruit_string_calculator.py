import unittest
from Fruit_string_calculator import calculate

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calculate("Panda has 48 apples and loses 4"), 44)
    def test_1(self):
        self.assertEqual(calculate("Jerry has 34 apples and gains 6"), 40)
    def test_2(self):
        self.assertEqual(calculate("Hanna has 40 apples and gains 20"), 60)


if __name__ == '__main__':
    unittest.main()
