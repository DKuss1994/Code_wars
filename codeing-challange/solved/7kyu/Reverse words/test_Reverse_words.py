import unittest
from Reverse_words import reverse_words


class MyTestCase(unittest.TestCase):
    def test_exampel(self):
        self.assertEqual(reverse_words("This is an example!"), "sihT si na !elpmaxe")
    def test_douppel_space(self):
        self.assertEqual(reverse_words("double  spaces"), "elbuod  secaps")
    def test_douppel_space_plusdpuppel_space(self):
        self.assertEqual(reverse_words("  double  spaces  "), "  elbuod  secaps  ")




if __name__ == '__main__':
    unittest.main()
