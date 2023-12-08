import prompt
from brain_games.cli import welcome_user


GAME_ROUNDS = 3


def run_games(game):
    name_gamer = welcome_user()
    print(game.DESCRIPTION)

