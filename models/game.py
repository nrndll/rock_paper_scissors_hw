from models.player import Player
from random import Random

class Game():

    def __init__(self, player_1, player_2):
        self.player_1=player_1
        self.player_2=player_2 
        # self.wins=[]

# wins=[]

    def judication(self):
        if self.player_1.choice == self.player_2.choice:
            return None
        elif self.player_1.choice == "rock" and self.player_2.choice == "paper":
            return self.player_2
        elif self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_1
        elif self.player_1.choice == "paper" and self.player_2.choice == "scissors":
            return self.player_2
        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_1
        elif self.player_1.choice == "scissors" and self.player_2.choice == "rock":
            return self.player_2
        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_1
        else: 
            return None


    def computer_player(self):
        choices = ["rock", "paper", "scissors"]
        name = "Computer"
        # return Player(name, Random().choice(choices))
        self.player_2 = Player(name, Random().choice(choices))
        return



    # def win_tracker(self, player):
    #     if player == None:
    #         self.wins.append("Draw")
    #     else:
    #         self.wins.append(player.name)
