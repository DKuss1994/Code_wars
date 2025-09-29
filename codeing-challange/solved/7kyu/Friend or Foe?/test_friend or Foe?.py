import unittest
from friend_or_foe import friend


class TestFriendorFoe(unittest.TestCase):

    def test_cases_1(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
    def test_case_2(self):
        self.assertEqual(friend(["Kevin", "Kieran", "Melli", ]), [])




if __name__ == '__main__':
    unittest.main()

