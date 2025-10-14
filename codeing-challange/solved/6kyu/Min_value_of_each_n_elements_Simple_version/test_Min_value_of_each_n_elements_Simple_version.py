import unittest
from Min_value_of_each_n_elements_Simple_version import min_value


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min_value([1, 2, 3, 10, -5], 2), [1, 2, 3, -5])

    def test_2(self):
        self.assertEqual(min_value([1, 2, 3, 10, -5], 3), [1, 2, -5])

    def test_3(self):
        self.assertEqual(min_value([1, 2, 3, 10, -5], 4), [1, -5])
    def test_4(self):
        self.assertEqual(min_value([1, 2, 3, 10, -5], 5), [-5])


if __name__ == '__main__':
    unittest.main()
