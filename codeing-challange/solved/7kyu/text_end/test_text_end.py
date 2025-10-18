import unittest
from text_end import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("Hello","lo"), True)  # add assertion here
    def test_something(self):
        self.assertEqual(solution("Hello","la"), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
