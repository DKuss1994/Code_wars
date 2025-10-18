import unittest
from Counting_Duplicates import duplicate_count

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(duplicate_count("AabbCC"), 3)
    def test_2(self):
        self.assertEqual(duplicate_count("123456789123456789"), 9)
    def test_3(self):
        self.assertEqual(duplicate_count("12c3c4567891b23b456789aa"), 12)
    def test_4(self):
        self.assertEqual(duplicate_count("1ab2cd9ef8ghijk5lmn7o3pqrs4tuv6wxyz"), 0)


if __name__ == '__main__':
    unittest.main()
