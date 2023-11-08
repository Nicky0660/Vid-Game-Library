#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app  # Make sure 'app' is properly imported
from models import db, Games, Genres, Consoles, ConsoleGames

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Nuking the database...")
        
        # Delete all existing records from the tables
        db.session.query(Games).delete()
        db.session.query(Genres).delete()
        db.session.query(Consoles).delete()
        db.session.query(ConsoleGames).delete()
                
        print("Starting seed...")
        
        # Create and seed the Games
        print('Picking Games ...')
        games = [
            Games(title='DarkTide', release_yr=2022, genre_id=7, img = 'https://cdn.mobygames.com/covers/11169388-warhammer-40000-darktide-windows-apps-front-cover.jpg' ),
            Games(title='God of War', release_yr=2005, genre_id=7, img = 'https://e.snmc.io/lk/l/x/68b4cfef747e6876310b305d30568cc2/10596713'),
            Games(title='GoldenEye 007', release_yr=1997, genre_id=3, img = 'https://images.nintendolife.com/0becf36f5e461/goldeneye-007-cover.cover_large.jpg'),
            Games(title='Super Smash Bros', release_yr=1999, genre_id=4, img ='https://upload.wikimedia.org/wikipedia/en/4/42/Supersmashbox.jpg'),
            Games(title='Legend of Zelda', release_yr=1986, genre_id=7, img ='https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png'),
            Games(title='Super Mario 64', release_yr=1996, genre_id=7, img= 'https://m.media-amazon.com/images/M/MV5BNjQzZmQzNWMtZTVmOS00NjU4LTlmNjktOTM2MDQwMjgxMmY0XkEyXkFqcGdeQXVyMTA3NjAwMDc4._V1_.jpg'),
            Games(title='Splitgate', release_yr=2019, genre_id=3, img='https://howlongtobeat.com/games/66142_Splitgate_Arena_Warfare.jpg'),
            Games(title='Tekken', release_yr=1994, genre_id=4, img ='https://m.media-amazon.com/images/M/MV5BMzJiMDYwMTAtZmJiZS00NGZiLTkzYzgtZGMxM2Q4YjJiNTAzXkEyXkFqcGdeQXVyMTA0MTM5NjI2._V1_.jpg'),
            Games(title='SSX Tricky', release_yr=2001, genre_id=1, img = 'https://media.retroachievements.org/Images/056697.png'),
            Games(title='1080 Snowboarding', release_yr=1998, genre_id=1, img = 'https://upload.wikimedia.org/wikipedia/en/0/04/1080snowboardingbox.jpg'),
            
            # Games(title='Wave Race', release_yr=1992, genre_id=5),
            # Games(title='Forza', release_yr=2005, genre_id=5),
            # Games(title='Gran Tourismo', release_yr=1997, genre_id=5),
            # Games(title='Halo', release_yr=2001, genre_id=3),
            # Games(title='Contra', release_yr=1987, genre_id=3),
            # Games(title='Call of Duty', release_yr=2003, genre_id=3),
            # Games(title='Skyrim', release_yr=2011, genre_id=7),
            # Games(title='Mega Man', release_yr=1987, genre_id=2),
            # Games(title='Metroid', release_yr=1988, genre_id=2),
            # Games(title='Tetris', release_yr=1985, genre_id=2),
            # Games(title='Left 4 Dead', release_yr=2008, genre_id=3),
            # Games(title='Risk of Rain 2', release_yr=2019, genre_id=1),            
            # Games(title='Monster Hunter World', release_yr=2018, genre_id=7),
            # Games(title='Rocket League', release_yr=2015, genre_id=9),
            # Games(title='Elden Ring', release_yr=2022, genre_id=7),
            # Games(title='CyberPunk2077', release_yr=2020, genre_id=7),
            # Games(title='Onimusha', release_yr=2001, genre_id=7),
            # Games(title='Mortal Kombat', release_yr=1992, genre_id=4),
            # Games(title='Crysis', release_yr=2007, genre_id=3),
            # Games(title='Portal', release_yr=2007, genre_id=8),
            # Games(title='Grand Theft Auto', release_yr=1997, genre_id=1),
            # Games(title='Spider-Man', release_yr=2000, genre_id=1),
            # Games(title='Twisted Metal', release_yr=1995, genre_id=1),
            # Games(title='Amped: Freestyle Snowboarding', release_yr=2002, genre_id=1),
            # Games(title='Minecraft', release_yr=2009, genre_id=8),
            # Games(title='The Last of Us', release_yr=2013, genre_id=7),
            # Games(title='Resident Evil', release_yr=1996, genre_id=1),
            # Games(title='Street Fighter II', release_yr=1992, genre_id=4),
            # Games(title="Assassin's Creed", release_yr=2007, genre_id=7),
            # Games(title='Tony Hawk Pro Skater', release_yr=1999, genre_id=1),
            # Games(title='Mario Kart', release_yr=1992, genre_id=5),
            # Games(title='Donkey Kong', release_yr=1981, genre_id=2),
            # Games(title='Alter Echo', release_yr=2003, genre_id=7),
            # Games(title='eXcite Bike', release_yr=1984, genre_id=5),
            # Games(title='Spyro', release_yr=1998, genre_id=1),
            # Games(title='Sonic', release_yr=1991, genre_id=1),
            # Games(title='Apex Legends', release_yr=2019, genre_id=3),
            # Games(title='Final Fantasy', release_yr=1987, genre_id=7),
            # Games(title='DOOM 64', release_yr=1997, genre_id=7),
            # Games(title='Castlevania Symphony of the Night', release_yr=1997, genre_id=1),

        ]
        
        db.session.add_all(games)
        db.session.commit()

        # Create and seed the Genres
        print('Deciding Genres ...')
        genres = [
            Genres(name='Action'),
            Genres(name='Platform'),
            Genres(name='Shooter'),
            Genres(name='Fighter'),
            Genres(name='Race'),
            Genres(name='Rhythm'),
            Genres(name='RPG'),
            Genres(name='Puzzle'),
            Genres(name='Sports')            
        ]

        db.session.add_all(genres)
        db.session.commit()

        # Create and seed the Consoles
        print('Selecting Consoles ...')
        consoles = [
            Consoles(name='Xbox', img = ('https://assetsio.reedpopcdn.com/-1620825867462.jpg?width=1200&height=900&fit=crop&quality=100&format=png&enable=upscale&auto=webp')),
            Consoles(name='Nintendo', img = 'https://bleedingcool.com/wp-content/uploads/2019/07/nintendo-logo-large-red-white-1200x900.jpg'),
            Consoles(name='Playstation', img = 'https://i2-prod.dailystar.co.uk/incoming/article15542870.ece/ALTERNATES/s1200b/923899'),
            Consoles(name='PC', img = 'https://totalmayhemgames.com/wp-content/uploads/2020/09/PC-Game_-2020-Black-300x300.png'),
            Consoles(name= 'All', img = 'https://yt3.googleusercontent.com/ytc/APkrFKaCabvNmIWM1VHuLHc8_aQru-yNcc6JM3oWQUWQNA=s900-c-k-c0x00ffffff-no-rj')
        ]
        

        db.session.add_all(consoles)
        db.session.commit()

        # Create and seed ConsoleGames
        consolegames = [
            ConsoleGames(game_id = 1, console_id = 1), 
            ConsoleGames(game_id = 1, console_id = 3),
            ConsoleGames(game_id = 1, console_id = 4),
            ConsoleGames(game_id = 2, console_id=3),
            ConsoleGames(game_id = 2, console_id=4),                      
            ConsoleGames(game_id = 3, console_id=2),
            ConsoleGames(game_id = 4, console_id=2),
            ConsoleGames(game_id = 5, console_id=2),
            ConsoleGames(game_id = 6, console_id=2),
            ConsoleGames(game_id = 7, console_id=1),
            ConsoleGames(game_id = 7, console_id=3),
            ConsoleGames(game_id = 7, console_id=4),
            ConsoleGames(game_id = 8, console_id=1),
            ConsoleGames(game_id = 8, console_id=3),
            ConsoleGames(game_id = 8, console_id=4),
            ConsoleGames(game_id = 9, console_id=1),
            ConsoleGames(game_id = 9, console_id=3),
            ConsoleGames(game_id = 9, console_id=4),
            ConsoleGames(game_id = 10, console_id=2)



            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1),
            # ConsoleGames(game_id = 1, console_id=1)
        ]
        db.session.add_all(consolegames)
        db.session.commit()

        print('Seeds grown ... ')
        print('')
        print('Game on!')

        
