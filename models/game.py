from models.player import Player

class Game():

    # def __init__(self):
    #     self.player_1_victory_count = 0
    #     self.player_2_victory_count = 0


    def judication(player_1, player_2):
        if player_1.choice == player_2.choice:
            return None
        elif player_1.choice == "rock" and player_2.choice == "paper":
            return player_2
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            return player_1
        elif player_1.choice == "paper" and player_2.choice == "scissors":
            return player_2
        elif player_1.choice == "paper" and player_2.choice == "rock":
            return player_1
        elif player_1.choice == "scissors" and player_2.choice == "rock":
            return player_2
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return player_1

    # def victory(self, judication_result):
    #     if judication_result == None:
    #         return
    #     if judication_result == "player_1":
    #         self.player_1_victory_count += 1
    #     else:
    #         self.player_2_victory_count += 1
