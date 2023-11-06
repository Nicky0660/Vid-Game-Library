"""empty message

Revision ID: c2913cd7f78c
Revises: 
Create Date: 2023-11-06 13:09:50.309931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2913cd7f78c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consoles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('release_yr', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], name=op.f('fk_games_genre_id_genres')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('console_games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('console_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['console_id'], ['consoles.id'], name=op.f('fk_console_games_console_id_consoles')),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_console_games_game_id_games')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('console_games')
    op.drop_table('games')
    op.drop_table('genres')
    op.drop_table('consoles')
    # ### end Alembic commands ###