#!/usr/bin/env python3

# Standard library imports
from flask import Flask, make_response, jsonify, request
# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import db, Consoles, Games, ConsoleGames, Genres

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

#model routes below
@app.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == 'GET':
        games = Games.query.all()
        games_dict = [game.to_dict(rules=(''))for game in games]
        response = make_response(games_dict, 200)
    else:
        response = make_response('Error games not found!', 404)
    return response

@app.route('/consoles', methods=['GET'])
def consoles():
    if request.method == 'GET':
        consoles = Consoles.query.all()
        consoles_dict = [console.to_dict(rules=(''))for console in consoles]
        response = make_response(consoles_dict, 200)
    else:
        response = make_response('Error console not found!', 404)
    return response

@app.route('/genres', methods=['GET', 'POST', 'DELETE'])
def genres():
    if request.method == 'GET':
        genres = Genres.query.all()
        genres_dict = [genre.to_dict(rules=(''))for genre in genres]
        response = make_response(genres_dict, 200)
    else:
        response = make_response('Error genres not found!', 404)
    return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)

