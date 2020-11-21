from flask import render_template, request, redirect
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def base():
    return render_template('base.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<hand_1>/<hand_2>')
def play_the_game(hand_1, hand_2):
    player_1 = Player("Player 1", hand_1)
    player_2 = Player("Player 2", hand_2)
    game = Game(player_1, player_2)
    winner = game.play_game()
    return render_template('result.html', winner = winner)

@app.route('/play_game')
def play_game():
    return render_template('play_game.html')
