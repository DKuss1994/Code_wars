import unittest
from find_next_square import find_next_square


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(find_next_square(121), 144)  # add assertion here
    def test_2_sqr(self):
        self.assertEqual(find_next_square(9),16)
    def test_sqr_not_perfect(self):
        self.assertEqual(find_next_square(8),-1)



if __name__ == '__main__':
    unittest.main()
