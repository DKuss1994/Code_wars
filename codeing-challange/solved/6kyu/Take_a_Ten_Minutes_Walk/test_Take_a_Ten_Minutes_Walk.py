import unittest
from Take_a_Ten_Minutes_Walk import is_valid_walk


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True)
    def test_2(self):
        self.assertEqual(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']),
                         False)

    def test_3(self):
        self.assertEqual(is_valid_walk(['n', 'n', 'e', 's', 'n', 'w', 'e', 'w', 'n', 's']), False)


if __name__ == '__main__':
    unittest.main()
