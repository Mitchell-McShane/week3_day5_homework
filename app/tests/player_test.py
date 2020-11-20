import unittest
from app.models.player import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player1", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Player1", self.player_1.name)

    def test_player_has_hand(self):
        self.assertEqual("Rock", self.player_1.hand)