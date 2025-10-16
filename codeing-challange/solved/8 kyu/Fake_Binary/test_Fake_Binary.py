import unittest
from Fake_Binary import fake_bin

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fake_bin("45385593107843568"), "01011110001100111")  # add assertion here


if __name__ == '__main__':
    unittest.main()
