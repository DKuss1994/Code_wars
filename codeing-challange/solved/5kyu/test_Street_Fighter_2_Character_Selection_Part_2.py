import unittest
from Street_Fighter_2_Character_Selection_Part_2 import super_street_fighter_selection


class MyTestCase(unittest.TestCase):
    fighter = ["", "ryu"]

    def test_something(self):
        self.assertEqual(super_street_fighter_selection(), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
