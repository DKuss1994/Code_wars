import unittest
from Basic_Mathematical_Operation import basic_op

class MyTestCase(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(basic_op("+",5,5), 10)
    def test_minus(self):
        self.assertEqual(basic_op("-",5,5), 0)
    def test_mal(self):
        self.assertEqual(basic_op("*",5,5), 25)
    def test_teilen(self):
        self.assertEqual(basic_op("/",5,5), 1)


if __name__ == '__main__':
    unittest.main()
