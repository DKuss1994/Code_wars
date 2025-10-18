import unittest
from Street_Fighter_2_Character_Selection import street_fighter_selection


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(street_fighter_selection([["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
                   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]], (0, 0), ["left"] * 8),
                         ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega',
                          'Balrog'])


if __name__ == '__main__':
    unittest.main()
