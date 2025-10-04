import unittest
from Duplicate_Encoder import duplicate_encode

class MyTestCase(unittest.TestCase):
    def test_all_other(self):
        self.assertEqual(duplicate_encode("din"), "(((")
    def test_all_same(self):
        self.assertEqual(duplicate_encode("ddd"), ")))")
    def test_3(self):
        self.assertEqual(duplicate_encode("adbd"), "()()")
    def test_4(self):
        self.assertEqual(duplicate_encode("(( @"), "))((")
    def test_4(self):
        self.assertEqual(duplicate_encode("Success"), ")())())")


if __name__ == '__main__':
    unittest.main()
