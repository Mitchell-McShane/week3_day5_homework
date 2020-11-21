import unittest

from app.models.game import *
from app.models.player import *

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("player 1", "rock")
        self.player_2 = Player("player 2", "scissors")

        self.game = Game(self.player_1, self.player_2)   

    def test_create_game(self):
        game_hands = self.player_1.hand + " vs " + self.player_2.hand
        self.assertEqual("rock vs scissors", game_hands)


    def test_game_is_a_draw(self):
        self.player_2 = Player("player 2", "rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("draw", self.game.play_game())


    def test_paper_beats_rock(self):
        self.player_1 = Player("player 1", "paper")
        self.player_2 = Player("player 2", "rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("paper", self.player_1.hand)
        self.assertEqual("rock", self.player_2.hand)
        self.assertEqual("player 1", self.game.play_game())


    def test_rock_beats_scissors(self):
        self.player_1 = Player("player 1", "rock")
        self.player_2 = Player("player 2", "scissors")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("rock", self.player_1.hand)
        self.assertEqual("scissors", self.player_2.hand)
        self.assertEqual("player 1", self.game.play_game())


    def test_scissors_beats_paper(self):
        self.player_1 = Player("player 1", "scissors")
        self.player_2 = Player("player 2", "paper")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("scissors", self.player_1.hand)
        self.assertEqual("paper", self.player_2.hand)
        self.assertEqual("player 1", self.game.play_game())

