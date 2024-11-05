import unittest
from game import play_game

class TestGame(unittest.TestCase):
    def test_play_game_win(self):
        self.assertEqual(play_game(15), "You win!")
    
    def test_play_game_lose(self):
        self.assertEqual(play_game(5), "You lose!")
    
    def test_play_game_edge_case(self):
        self.assertEqual(play_game(10), "You lose!")

if __name__ == "__main__":
    unittest.main()
