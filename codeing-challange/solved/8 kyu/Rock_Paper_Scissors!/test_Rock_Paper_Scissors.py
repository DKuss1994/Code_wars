import unittest
from Rock_Paper_Scissors import rps


class MyTestCase(unittest.TestCase):
    def test_player_2_win(self):
        self.assertEqual(rps("rock","paper"), "Player 2 won!")
    def test_player_1_win(self):
        self.assertEqual(rps("paper", "rock"), "Player 1 won!")
    def test_drwa(self):
        self.assertEqual(rps("paper", "paper"), "Draw!")


if __name__ == '__main__':
    unittest.main()
