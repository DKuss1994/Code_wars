import unittest
from Green_Glass_Door import step_through_with


class MyTestCase(unittest.TestCase):
    def test_moon(self):
        self.assertEqual(step_through_with("moon"), True)  # add assertion here
    def test_sun(self):
        self.assertEqual(step_through_with("sun"), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
