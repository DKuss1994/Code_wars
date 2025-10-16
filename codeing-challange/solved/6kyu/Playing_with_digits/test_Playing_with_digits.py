import unittest
from Playing_with_digits import dig_pow

class MyTestCase(unittest.TestCase):
    def test_create(self):
        print(dig_pow(180,2))
    def test_1(self):
        self.assertEqual(dig_pow(89,1), 1)
    def test_2(self):
        self.assertEqual(dig_pow(150,2),-1)
    def test_3(self):
        self.assertEqual(dig_pow(180,2),-1)

if __name__ == '__main__':
    unittest.main()
