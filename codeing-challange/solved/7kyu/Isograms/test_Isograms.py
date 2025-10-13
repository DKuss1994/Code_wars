import unittest
from Isograms import is_isogram


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)  # add assertion here
    def test_false(self):
        self.assertEqual(is_isogram("aba"), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
