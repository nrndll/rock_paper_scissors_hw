from flask import render_template, request
from app import app
from models.player import Player
from models.game import judication

@app.route("/")
def index():
    return render_template("index.html")