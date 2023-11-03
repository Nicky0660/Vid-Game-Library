from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
#Main models are games, genres, consolegames, consoles. May add in user_games and users in the future.

class Games(db.Model, SerializerMixin):
    __tablename__='games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_yr = db.Column(db.Timestamp)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))


class Genres(db.Model, SerializerMixin):
    __tablename__='genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class ConsoleGames(db.Model, SerializerMixin):
    __tablename__='console_games'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'))


class Consoles(db.Model, SerializerMixin):
    __tablename__='consoles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

#optional stretch goal models
class UserGames(db.Model, SerializerMixin):
    __tablename__='user_games'
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Users(db.Model, SerializerMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
