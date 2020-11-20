class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result = ''

    def play_game(self, player_1, player_2):

        if (self.player_1.hand == self.player_2.hand):
            self.result = "The game is a tie"

        elif(self.player_1.hand == "rock" and self.player_2.hand == "scissors") or \
            (self.player_1.hand == "scissors" and self.player_2.hand == "paper") or \
            (self.player_1.hand == "paper" and self.player_2.hand == "rock"):
            self.result = f"{self.player_1.name} has won!"

        else:
            self.result = f"{self.player_2.name} has won!"
