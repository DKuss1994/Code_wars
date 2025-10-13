import unittest
from Friday_the_13th_Part_1 import kill_count


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(kill_count([["Tiffany", 4],["Jack", 6],["Megan", 7],["Tyler", 3]],6), ["Tiffany", "Tyler"])  # add assertion here


if __name__ == '__main__':
    unittest.main()
