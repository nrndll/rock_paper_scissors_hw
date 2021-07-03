from flask import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/play")
def play_computer():
    return render_template("play.html")

@app.route("/<player_1_choice>")
def first_choice(player_1_choice):
    player_1 = Player("Player 1", player_1_choice)
    return render_template("player_choices.html", player_1=player_1)

@app.route("/<player_1_choice>/<player_2_choice>")
def second_choice(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()
    result = Game.judication(player_1, player_2)
    # Game.victory(game, result)
    return render_template("result.html", result=result, player_1=player_1, player_2=player_2, game=game)

