from models.player import Player
from random import Random

# class Game():

#     def __init__(self):
#         self.player_1_win_count = 0
#         self.player_2_win_count = 0

wins=[]

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

def computer_player():
    choices = ["rock", "paper", "scissors"]
    name = "Computer"
    return Player(name, Random().choice(choices))

def win_tracker(player):
    if player == None:
        wins.append("Draw")
    else:
        wins.append(player.name)
