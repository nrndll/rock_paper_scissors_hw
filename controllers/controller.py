from flask import render_template, request
from app import app
from models.player import Player
from models.game import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/play")
def play_computer():
    return render_template("play.html")

@app.route("/play", methods=["POST"])
def challenger_entry():
    challenger_name = request.form["player_name"]
    challenger_choice = request.form["player_choose"]
    challenger = Player(challenger_name, challenger_choice)
    computer = computer_player()
    result = judication(challenger, computer)
    win_tracker(result)
    return render_template("result.html", result=result, player_1=challenger, player_2=computer)

@app.route("/<player_1_choice>")
def first_choice(player_1_choice):
    player_1 = Player("Player 1", player_1_choice)
    return render_template("player_choices.html", player_1=player_1)

@app.route("/<player_1_choice>/<player_2_choice>")
def second_choice(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    result = judication(player_1, player_2)
    win_tracker(result)
    return render_template("result.html", result=result, player_1=player_1, player_2=player_2, wins=wins)

@app.route("/game_history")
def game_history():
    return render_template("game_history.html", wins=wins)            
