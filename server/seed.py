#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Games, Genres, Consoles

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!


# games = []

# games.append(Games(title= 'Dark Tide', release_yr=2022))
# games.append(Games(title='God of War', release_yr=2018))

# db.session.add_all(games)
# db.session .commit()

genres = []

genres.append(Genres(name='RPG'))
genres.append(Genres(name='Fighter'))

db.session.add_all(genres)
db.session.commit()

# consoles = []

# consoles.append(Consoles(name='Xbox'))
# consoles.append(Consoles(name='PC'))

# db.session.add_all(consoles)
# db.session.commit()

