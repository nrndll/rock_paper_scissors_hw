from flask import render_template, request
from app import app
from models.player import Player
from models.game import judication

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<player_1_choice>")
def first_choice(player_1_choice):
    player_1 = Player("Player 1", player_1_choice)
    return render_template("player_choices.html", player_1=player_1)

@app.route("/<player_1_choice>/<player_2_choice>")
def second_choice(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    result = judication(player_1, player_2)
    return render_template("result.html", result=result, player_1=player_1, player_2=player_2)

# @app.route("/rock")
# def rock():
#     return render_template("rock.html")

# @app.route("/paper")
# def paper():
#     return render_template("paper.html")

# @app.route("/scissors")
# def scissors():
#     return render_template("scissors.html")
