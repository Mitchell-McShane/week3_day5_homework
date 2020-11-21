import unittest
from app.models.player import *

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1", "Rock")

    def test_player_has_name(self):
        self.assertEqual(self.player_1.name, "Player 1")

    def test_player_has_hand(self):
        self.assertEqual(self.player_1.hand, "Rock")