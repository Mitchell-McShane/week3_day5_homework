class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def play_game(self):
        if(self.player_1.hand == self.player_2.hand):
            # print("It's a draw!")
            return "draw"


        elif((self.player_1.hand == "rock" and self.player_2.hand =="paper") or (self.player_1.hand == "paper" and self.player_2.hand =="rock")):
            # print("Paper wins!")
            result = "paper"
    

        elif((self.player_1.hand == "scissors" and self.player_2.hand =="paper") or (self.player_1.hand == "paper" and self.player_2.hand =="scissors")):
            # print("Scissors wins!")
            result= "scissors"

        else:
            # print("Rock wins!")
            result= "rock"

        if result == self.player_1.hand:
            # print("Winner:", player_1.name)
            return self.player_1.name
        elif result == self.player_2.hand:
            # print("Winner:", player_2.name)
            return self.player_2.name