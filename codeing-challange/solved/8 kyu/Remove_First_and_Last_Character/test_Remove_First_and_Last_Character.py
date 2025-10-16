import unittest
from Remove_First_and_Last_Character import remove_char

class MyTestCase(unittest.TestCase):
    def test_hallo(self):
        self.assertEqual(remove_char("Hallo"), "all")
    def test_ab(self):
        self.assertEqual(remove_char("ab"), "")


if __name__ == '__main__':
    unittest.main()
