import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player1", "Rock")
        self.player_2 = Player("Player2", "Scissors")

        self.game = Game(self.player_1, self.player_2)

    def test_create_game(self):
        game_hands = self.player_1.hand + " vs " + self.player_2.hand
        self.assertEqual("Rock vs Scissors", game_hands)

    def test_game_draw(self):
        self.player_2 = Player("Computer", "Rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual(None, self.game.play_game(self.player_1, self.player_2))

    def test_game_rock_beats_scissors(self):
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("Rock", self.player_1.hand)
        self.assertEqual("Scissors", self.player_2.hand)
        self.assertEqual(None, self.game.play_game(self.player_1, self.player_2))

