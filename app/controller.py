from flask import render_template
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template('base.html', title='Home')

@app.route('/<hand1>/<hand2>')
def play_game(hand1, hand2):
    player_1 = Player("Mitch", hand1)
    player_2 = Player("Computer", hand2)
    current_game = Game(player_1, player_2)
    winner = current_game.check_winner()