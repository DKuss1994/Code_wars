import unittest
from Street_Fighter_2_Character_Selection_Part_2 import super_street_fighter_selection


class MyTestCase(unittest.TestCase):

    def test_something(self):
        fighters = [
            ["", "Ryu", "E.Honda", "Blanka", "Guile", ""],
            ["Balrog", "Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat"],
            ["Vega", "T.Hawk", "Fei Long", "Deejay", "Cammy", "M.Bison"]
        ]
        position = (0, 1)  # start on Ryu
        moves = ["left", "left", "down", "right"]
        expected = ["Guile", "Blanka", "Zangief", "Dhalsim"]
        self.assertEqual(super_street_fighter_selection(fighters,position,moves), expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
