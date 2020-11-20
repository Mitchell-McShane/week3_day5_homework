from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('base.html', title='Home')

@app.route('/<hand1>/<hand2>')
def play_game(hand1, hand2):
    player_1 = Player("Player 1", hand1)
    player_2 = Player("player 2", hand2)
    current_game = Game(player_1, player_2)
    winner = current_game.get_winner()