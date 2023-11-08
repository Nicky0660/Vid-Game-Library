#!/usr/bin/env python3

# Standard library imports
from flask import Flask, make_response, jsonify, request
# Remote library imports
from flask import request
from flask_restful import Resource
from flask_migrate import Migrate

# Local imports
from config import app, api
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
        games_dict = [game.to_dict(rules=('-genre.games',))for game in games]
        response = make_response(games_dict, 200)
    elif request.method == 'POST':
        form_data = request.get_json()
        print(form_data)
        try:
            new_game = Games(
                title = form_data['title'],
                release_yr = form_data['release_yr'],
                genre_id = form_data['genre_id'],
                img = form_data['img']
                )
            db.session.add(new_game)
            db.session.commit()
            print(new_game)
            console_ids = form_data['console_ids']

            for id in console_ids:
                new_console_game = ConsoleGames(game_id = new_game.id, console_id = id)

                db.session.add(new_console_game)
                db.session.commit()
            

            response = make_response(new_game.to_dict(), 201)
        except ValueError:
            response =make_response(
                {'Game must title, release_yr,genre,and console'},
                400
            )
    else:
        response = make_response('Error games not found!', 404)
    return response

@app.route('/games/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def games_by_id(id):
    game = Games.query.filter(Games.id == id).first()
    print(game)
    if game:
        if request.method == 'GET':
            response = make_response(game.to_dict(rules=('-genre.games',)), 200)
        elif request.method == 'DELETE':
            print(game)
            db.session.delete(game)
            db.session.commit()
            response = make_response({}, 204)
            print(response)
            return response
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(game, attr, form_data.get(attr))
                db.session.commit()
                response = make_response(game.to_dict(), 202)
            except ValueError:
                response = make_response(
                    {"game must have title and release year!"}, 400)
    else:
        response = make_response({"error": ("Game not found")}, 404)
        return response
    return response

@app.route('/consoles', methods=['GET'])
def consoles():
    if request.method == 'GET':
        consoles = Consoles.query.all()
        consoles_dict = [console.to_dict(rules=('-console_games', ))for console in consoles]
        response = make_response(consoles_dict, 200)
    else:
        response = make_response('Error console not found!', 404)
    return response

@app.route('/genres', methods=['GET', 'POST'])
def genres():
    if request.method == 'GET':
        genres = Genres.query.all()
        genres_dict = [genre.to_dict(rules=('-games',))for genre in genres]
        response = make_response(genres_dict, 200)
    elif request.method == 'POST':
        form_data = request.get_json()
        new_genre = Genres(name = form_data['name']) 
        db.session.add(new_genre)
        db.session.commit()
        response = make_response(new_genre.to_dict(), 201)
    
    else:
        response = make_response('Error genres not found!', 404)
    return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)

