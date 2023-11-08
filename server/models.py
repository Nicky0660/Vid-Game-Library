from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)


# Models go here!
#Main models are games, genres, consolegames, consoles. May add in user_games and users in the future.

class Games(db.Model, SerializerMixin):
    __tablename__='games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_yr = db.Column(db.Integer)
    img = db.Column(db.String)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    serialize_rules = ('-console_games.game', '-genres.game')

    genre = db.relationship('Genres', back_populates='games', lazy = 'subquery')
    console_games = db.relationship('ConsoleGames', back_populates='game', cascade='all,delete-orphan')

    @validates('title')
    def validates_title(self, key, title):
        if type (title) == str:
            return title
        else:
            raise ValueError('Title must be a String')
    @validates('release_yr')
    def validates_release_yr(self, key, release_yr):
        if type (release_yr) == int and len(str(release_yr)) == 4:
            return release_yr
        else:
            raise ValueError('release_yr must be a Integer')
   
    def __repr__(self):
        return f'<Games {self.id}: {self.title}>'

class Genres(db.Model, SerializerMixin):
    __tablename__='genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    serialize_rules = ('-games.genre',)

    games = db.relationship('Games', back_populates='genre')

class ConsoleGames(db.Model, SerializerMixin):
    __tablename__='console_games'
    id = db.Column(db.Integer, primary_key=True)
    serialize_rules = ('-console.console_games', '-game.console_games')

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'))

    game = db.relationship('Games', back_populates='console_games')
    console = db.relationship('Consoles', back_populates='console_games', lazy = 'subquery')


class Consoles(db.Model, SerializerMixin):
    __tablename__='consoles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    img = db.Column(db.String)
    serialize_rules = ('-console_games.console', )

    console_games = db.relationship('ConsoleGames', back_populates='console', cascade = 'all, delete-orphan')

    @validates('name')
    def validates_name(self, key, name):
        if name : 
            return name
        else: 
            raise ValueError('Console must have name')



#optional stretch goal models
# class UserGames(db.Model, SerializerMixin):
#     __tablename__='user_games'
#     game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
#     console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class User(db.Model, SerializerMixin):
#     __tablename__='users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
