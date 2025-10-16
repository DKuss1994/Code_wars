import unittest
from Beginner_Lost_Without_a_Map import maps
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(maps([1, 2, 3]), [2, 4, 6])  # add assertion here


if __name__ == '__main__':
    unittest.main()
